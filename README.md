## Building a Production-Ready RAG Chatbot with FastAPI and LangChain

### Following approach is taken for creating FastAPI

main.py: This is the entry point of our FastAPI application. It defines the API routes and orchestrates the different components of our system.

chroma_utils.py: Contains utilities for interacting with the Chroma vector store, including functions for indexing documents and performing similarity searches.

db_utils.py: Handles database operations, including storing and retrieving chat history and document metadata.

langchain_utils.py: Encapsulates the LangChain-specific logic, such as creating the RAG chain and configuring the language model.

pydantic_models.py: Defines Pydantic models for request and response validation, ensuring type safety and clear API contracts.

requirements.txt: Lists all the Python packages required for the project.



The requests.post() method in Python accepts several parameters:
url: The URL to which the POST request is sent12.
data: A dictionary, list of tuples, bytes, or file object to send in the body of the request125.
json: A JSON object to send in the body of the request12.
files: A dictionary of files to send to the specified URL1.
headers: A dictionary of HTTP headers to send to the specified URL13.
allow_redirects: A Boolean to enable/disable redirection (default is True)1.
auth: A tuple to enable a certain HTTP authentication (default is None)1.
cert: A string or tuple specifying a cert file or key (default is None)1.
cookies: A dictionary of cookies to send to the specified URL (default is None)1.
proxies: A dictionary of the protocol to the proxy URL (default is None)1.
stream: A Boolean indicating if the response should be immediately downloaded (False) or streamed (True) (default is False)1.
timeout: A number or tuple indicating how many seconds to wait for the client to make a connection and/or send a response (default is None)1.
verify: A Boolean or string indicating whether to verify the server's TLS certificate