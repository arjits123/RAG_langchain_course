import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"

def upload_document(file):

    try:
        files = {'file': (file.name, file, file.type)}
        response = requests.post('{BASE_URL}/upload-doc', files = files)

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
        response = requests.post('{BASE_URL}/list-docs')

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to list the docuements. Error {response.status_code} - {response.text}")
            return None

    except Exception as e:
        st.error(f"An error occured while listing the docs: {str(e)}")
        return None

def delete_documents():

    try:
        response = requests.post('{BASE_URL}/list-docs')

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to list the docuements. Error {response.status_code} - {response.text}")
            return None

    except Exception as e:
        st.error(f"An error occured while listing the docs: {str(e)}")
        return None
    
def chat(file):

    try:
        response = requests.post('{BASE_URL}/list-docs')

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to upload the file. Error {response.status_code} - {response.text}")
            return None

    except Exception as e:
        st.error(f"An error occured while uploading the file: {str(e)}")
        return None
