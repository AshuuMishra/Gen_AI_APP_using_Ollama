import os 
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#langsmith Tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_TRACING_V2"]='true'
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')

#prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You're a helpful assistant.Please respond to the question asked")
        ("user","Question:{question}")
    ]
    
)


#stremlit framework
st.title('Langchain Demo with LLama2')
input_text=st.text_input("what question you have in mind ?")

llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:

  st.write(chain.invoke({'question':input_text}))
