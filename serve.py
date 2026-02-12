'''from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain_groq import ChatGroq
import os
from langserve import add_routes ## Used for adding API routes for a given chain
from dotenv import load_dotenv
load_dotenv()

## groq_api_key=os.getenv("GROQ_API_KEY")
## model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

parser=StrOutputParser()

##create chain
chain=prompt_template|model|parser



## App definition
app=FastAPI(title="Langchain Server",
            version="1.0",
            description="A simple API server using Langchain runnable interfaces")

## Adding chain routes
add_routes(                ### Actual API route will be /chain/translate
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn     ## Running the app using uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)'''


