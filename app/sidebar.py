import streamlit as st
from api_utils import upload_document, list_documents, delete_documents


def display_sidebar():

    # Model selection
    model_options = ['gpt-3.5-turbo', 'gpt-4o']
    st.sidebar.selectbox('Select model', options = model_options, key = 'model')

    # File uploader
    st.sidebar.header('Upload the document')
    uploaded_file = st.sidebar.file_uploader('Choose a file', type=['pdf', 'docx','html'])
    if uploaded_file is not None:
        button = st.sidebar.button('Upload')
        if button:
            with st.spinner('Uploading...'):
                upload_response = upload_document(uploaded_file)
                if upload_response:
                    st.sidebar.success(f'File {uploaded_file.name} uploaded successfully with ID {upload_response['file_id']}.')
                    st.session_state.documents = list_documents() # refresh the list after upload
    
    # List documents 
    st.sidebar.header('Uploaded Documents ')
    if st.sidebar.button('List documents'):
        with st.spinner('Refreshing...'):
            st.session_state_documents = list_documents()

    #Initialise the document list if not present
    if "documents" not in st.session_state:
        st.session_state.documents = list_documents()

    
    documents = st.session_state.documents
    if documents:
        for doc in documents:
            st.sidebar.text(f"{doc['filename']} (ID: {doc['id']}, Uploaded: {doc['uploaded_timestamp']})")

            #Delete the document
            selected_file_id = st.sidebar.selectbox("select the document to delete", options = [doc['id']for doc in documents],
                                    format_func = lambda x : next(doc['filename'] for doc in documents if doc['id'] == x))
            
            if st.sidebar.button('Delete selected document'):
                with st.spinner('Deleting...'):
                    delete_response = delete_documents(selected_file_id)
                    if delete_response:
                        st.sidebar.success(f"Document with ID {selected_file_id} deleted successfully")
                        st.session_state.documents = list_documents()
                    else:
                        st.sidebar.error(f"Failed to delete the document with ID {selected_file_id} ")





