import streamlit as st
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

st.set_page_config(page_title="GPT Content Generator", page_icon=":robot_face:", layout="wide", initial_sidebar_state="expanded")

st.title(":robot_face: GPT Content Generator")

st.sidebar.title("Upload your text file")
file = st.sidebar.file_uploader("Upload your text file", type=["txt"])

if file is not None:
    file_details = {"FileName":file.name,"FileType":file.type,"FileSize":file.size}
    # st.write(file_details)

    text = file.read().decode("utf-8")
    # st.write(text)
    st.write("### Give instructions to the model:")
    prompt = st.text_area("_", label_visibility="hidden", height=200)

    if st.button("Generate"):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
            "role": "system", "content": f"{prompt}. \n\nText file: {text}. \n\nAnswer:"
            }],
            temperature=1,
            # top_p=0,
            # frequency_penalty=0,
            # presence_penalty=0,
        )
        st.write(response["choices"][0]["message"]["content"])