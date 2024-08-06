import streamlit as st
import requests
import time
import os
from dotenv import load_dotenv
dotenv_path = os.path.realpath(filename="../frontend.env")
load_dotenv(dotenv_path)
# print(dotenv_path)

API_URL = os.getenv("API_URL")
API_URL_DELETE = os.getenv("API_URL_DELETE")

def get_response_from_api(prompt):
    try:
        # print(prompt)
        response = requests.post(API_URL, json={"query": prompt})
        # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()
        res = response.json()
        return str(res["response"])
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None
    except Exception as e:
        st.error(f'An error occured as you mentioned here ```{e}```')

def delete_api():
    try:
        response = requests.delete(API_URL_DELETE)
        # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()
        res = response.json()
        return str(res["response"])
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None
    except Exception as e:
        st.error(f'An error occured as you mentioned here ```{e}```')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for PDF upload
with st.sidebar:
    st.header("Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    st.header("Clear Book Data Base")
    delete = st.button("Clear")
    if delete:
        delete_res = delete_api()
        st.success(delete_res)
        st.toast('You refresh the Data base, buddy!', icon='😍')

    
    if uploaded_file is not None:
        # Prepare the file for upload
        files = {"file": (f"{uploaded_file.name}.pdf", uploaded_file.getvalue(), "application/pdf")}
        
        # Send the file to the FastAPI backend
        response = requests.post("http://localhost:8000/api/uploadfile/", files=files)
        
        if response.status_code == 200:
            st.success("PDF uploaded successfully!")
            st.json(response.json())
        else:
            st.error("Failed to upload PDF")

    

# Main chat interface
st.title("Book Reader friend")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is your question?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get bot response
    with st.spinner('Thinking...'):
        response = get_response_from_api(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for char in response:
            full_response += char
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.005)  # Adjust typing speed here
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})