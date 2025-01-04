from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from typing import List
from langchain_core.documents import Document
import os
from chroma_utils import vectorstore


retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
# retriever = vectorstore.as_retriever(search_type="similarity_score_threshold", search_kwargs={"k": 2,"score_threshold": 0.5})

output_parser = StrOutputParser()

contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# qa_prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", """
#         You are an AI assistant. You are given a context and a question. 
#         Answer the question based only on the context. 
#         If the context does not provide relevant information or if the context is blank, say: "Sorry, I don't have enough information to answer."
#         """),
#         ("system", "Context : {context}"),
#         MessagesPlaceholder(variable_name = "chat_history"),
#         ("human", "{input}")
#     ]
# )


qa_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI assistant. You are given a context and a question from user.
      Answer the user's question based only on the context."""),
    ("system", "Context: {context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

def get_rag_chain(model="gpt-3.5-turbo"):
    llm = ChatOpenAI(model = model, temperature = 0.1)
    history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)    
    return rag_chain



'''
This function creates our RAG chain:

It initializes the language model (ChatOpenAI) with the specified model name.

Creates a history-aware retriever that can understand context from previous interactions.

Sets up a question-answering chain that combines retrieved documents to generate an answer.

Finally, it creates the full RAG chain by combining the retriever and question-answering chain.
'''