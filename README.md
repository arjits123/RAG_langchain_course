## Building a Production-Ready RAG Chatbot with FastAPI and LangChain

### Following approach is taken for creating FastAPI

main.py: This is the entry point of our FastAPI application. It defines the API routes and orchestrates the different components of our system.

chroma_utils.py: Contains utilities for interacting with the Chroma vector store, including functions for indexing documents and performing similarity searches.

db_utils.py: Handles database operations, including storing and retrieving chat history and document metadata.

langchain_utils.py: Encapsulates the LangChain-specific logic, such as creating the RAG chain and configuring the language model.

pydantic_models.py: Defines Pydantic models for request and response validation, ensuring type safety and clear API contracts.

requirements.txt: Lists all the Python packages required for the project.