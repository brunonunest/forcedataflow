from langchain_core.prompts import ChatPromptTemplate
import os
os.environ['OPENAI_API_KEY'] = env.OPENAI_API_KEY

from langchain_core.prompts import ChatPromptTemplate

template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

# Question: {question}
# SQL Query:"""
prompt = ChatPromptTemplate.from_template(template)
# ans = prompt.format(schema='my schema', question="how many tables we have on this db?")
# print(ans)


from langchain_community.utilities import SQLDatabase

db_uri = 'mysql+mysqlconnector://rfamro@mysql-rfam-public.ebi.ac.uk:4497/Rfam'
db = SQLDatabase.from_uri(db_uri)
# res = db.run('SELECT * FROM family LIMIT 1')
# print(res)
def get_schema(_):
    schema = db.get_table_info()
    return schema
# print(get_schema(db=db))

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

sql_chain = (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt
    | llm.bind(stop="\nSQL Result:")
    | StrOutputParser()
)

# qs = sql_chain.invoke({'question': 'select 1 family data'})
# print(qs)
