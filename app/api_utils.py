import requests
import streamlit as st
import json

def get_api_response (question, session_id, model) :
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    data = {
        'question': question,
        'model': model
    }

    if session_id:
        data['session_id'] = session_id

    try:
        response = requests.post("http://127.0.0.1:8000/chat", headers=headers, json=data)
        
        if response.status_code == 200:
            # data = response.json()
            # print(data)
            return response.json()
        else:
            st.error(f"API request failed with status code {response.status_code}: {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None


# Upload the document using requests
def upload_document(file):
    try:
        files = {'file': (file.name, file, file.type)}
        response = requests.post('http://127.0.0.1:8000/upload-doc', files = files)

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to upload the file. Error {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occured while uploading the file: {str(e)}")
        return None
    
def list_documents():
    try:
        response = requests.get('http://127.0.0.1:8000/list-docs')

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to list the documents. Error {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occured while listing the docs: {str(e)}")
        return None

def delete_documents(file_id):

    """
    Content Type Specification:
    This header tells the server that the body of the request will be in JSON format. 
    It's crucial because it informs the server how to interpret the data being sent in the request body.

    Accept Header:
    This header indicates to the server that the client (your application) expects a JSON response. 
    It's a way of telling the server what format of data you're prepared to handle in the response.
    """
    headers ={
        'accept':'application/json',
        'Content-type': 'application/json'
    }
    data = {'file_id': file_id}
    try:
        response = requests.post('http://127.0.0.1:8000/delete-doc', headers = headers, json = data)

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to delete the document. Error {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occured while deleting the docs: {str(e)}")
        return None
    

