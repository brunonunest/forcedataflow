from langchain_openai import OpenAI

# Accessing the OPENAI KEY
import env

API_KEY = env.OPENAI_API_KEY

# Simple LLM call Using LangChain
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", openai_api_key=API_KEY)
question = "Which language is used to create chatgpt ?"
print(question, llm(question))