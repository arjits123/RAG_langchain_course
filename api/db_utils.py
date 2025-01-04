import sqlite3
from datetime import datetime

"""
--------------------------CREATING DATABASE AND CONNECTION ----------------------------------------
"""

DB_name = 'rag_app.db'

#Creating database and connecting to it
def get_db_connection():
    conn = sqlite3.connect(DB_name)
    conn.row_factory = sqlite3.Row # if row_factory not selected fetched rows are returned as tuples
    return conn

"""
--------------------------CREATING DATABASE TABLES -------------------------------------------------
"""
#Creating table
def create_application_logs_table():
    conn = get_db_connection()
    conn.execute(
        '''
            CREATE TABLE IF NOT EXISTS application_logs
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                user_query TEXT,
                llm_response TEXT,
                model TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        '''
    )
    conn.close()

# keeping the track of the uploaded docuemnts
def create_document_store():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS document_store
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     filename TEXT,
                     upload_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.close()

"""
--------------------------INSERTING RECORDS IN THE TABLE AND MANAGEING CHAT LOGS----------------------------------------
"""

#Insterting the records in the application_logs table
def insert_into_table(session_id, user_query, llm_response, model):
    conn = get_db_connection()
    conn.execute('INSERT INTO application_logs (session_id, user_query, llm_response, model) VALUES (?, ?, ?, ?)',
                 (session_id, user_query, llm_response, model))
    conn.commit()
    conn.close()

#Get the chat history
def get_chat_history(session_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT user_query, llm_response FROM application_logs WHERE session_id = ? ORDER BY created_at', (session_id,))
    messages = []
    for row in cursor.fetchall():
        messages.extend([
            {"role": "human", "content": row['user_query']},
            {"role": "ai", "content": row['llm_response']}
        ])
    conn.close()
    return messages

"""
-------------------------- MANAGING THE DOCUMENT RECORDS ------------------------------------------------------
"""
# Function for inserting the docuemnt in the document_store table in DB
def insert_document_record(filename):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO document_store (filename) VALUES (?)', (filename,))
    file_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return file_id

# Function for deleting the docuemnt in the document_store table in DB
def delete_document_record(file_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM document_store WHERE id = ?', (file_id,))
    conn.commit()
    conn.close()
    return True

# Function for getting the docuemnt in the document_store table in DB
def get_all_documents():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, filename, upload_timestamp FROM document_store ORDER BY upload_timestamp DESC')
    documents = cursor.fetchall()
    # print(documents)
    conn.close()
    return [dict(doc) for doc in documents]

#Initialise the databases tables
create_application_logs_table()
create_document_store()


"""
This ensures that our tables are created when the application starts, if they don't already exist.
By centralizing our database operations in db_utils.py, we maintain a clean separation of concerns. 
Our main application logic doesn't need to worry about the details of database interactions, 
making the code more modular and easier to maintain.

In a production environment, you might consider using an ORM (Object-Relational Mapping) library like SQLAlchemy for 
more complex database operations and better scalability. However, for our current needs, this straightforward SQLite 
implementation serves well.
"""