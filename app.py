import streamlit as st
import openai
import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI

openai.api_key = os.environ["OPENAI_API_KEY"]

st.set_page_config(page_title="GPT Content Generator", page_icon=":robot_face:", layout="wide", initial_sidebar_state="expanded")

st.title(":robot_face: GPT Content Generator")

st.sidebar.title("Upload your text file")
# file = st.sidebar.file_uploader("Upload your text file", type=["csv"])
# df1 = pd.read_excel('Lyzr Reco - Sales DB.xlsx', sheet_name='Fields to Map')
# df2 = pd.read_excel('Lyzr Reco - Sales DB.xlsx', sheet_name='Lyzr Reco Database')
# df3 = pd.read_excel('Lyzr Reco - Sales DB.xlsx', sheet_name='Draft')
# dataset = pd.read_csv('Superstore.csv')

st.write("### Give instructions to the model:")
prompt = st.text_area("_", label_visibility="hidden", height=200)

if st.button("Generate"):
    with st.spinner("Generating..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
            "role": "system", "content": f"{prompt}"
            }],
            temperature=0,
            # top_p=0,
            # frequency_penalty=0,
            # presence_penalty=0,
        )
        # response = create_csv_agent(ChatOpenAI(temperature=0), 'Superstore.csv', verbose=True)
        st.write(response["choices"][0]["message"]["content"])