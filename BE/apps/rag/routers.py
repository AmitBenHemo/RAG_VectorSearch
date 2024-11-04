from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
 
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain_community.llms import openai
from config import settings
from .models import QueryModel
from pymongo import MongoClient

router = APIRouter()

@router.post("/", response_description="Ask a question")
async def create_query(request: Request, query: QueryModel = Body(...)):
    query = jsonable_encoder(query)

    client = MongoClient(settings.DB_URI)
    collection = client[settings.DB_NAME][query["organization"]]

    print("collection", collection)


    embeddings = OpenAIEmbeddings(openai_api_key=settings.OPEN_AI_KEY)

# 
    vectorStore = MongoDBAtlasVectorSearch(collection, embeddings)


    docs = vectorStore.similarity_search(query=query["prompt"], K=3)
    as_output = docs[0].page_content


    llm = openai.OpenAI(openai_api_key= settings.OPEN_AI_KEY, temperature=0, model=query["model"])

    # Manually create the prompt by combining the context with the user's question
    prompt = f"Context: {as_output}\n\nQuestion: {query['prompt']}\n\nAnswer:"

    
    # Call the LLM with the formatted prompt
    retriever_output = llm(prompt)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=retriever_output)
