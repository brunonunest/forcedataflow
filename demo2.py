from langchain.llms import OpenAI

# Accessing the OPENAI KEY
import env

API_KEY = env.OPENAI_API_KEY

# Creating a prompt template and running the LLM chain
from langchain import PromptTemplate, LLMChain
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", openai_api_key=API_KEY)
template = "What are the top {n} resources to learn {language} programming?"
prompt = PromptTemplate(template=template,input_variables=['n','language'])
chain = LLMChain(llm=llm,prompt=prompt)
input = {'n':3,'language':'Python'}
# print(chain.run(input))