from langchain_community.utilities import SQLDatabase

# if you are using SQLite
# sqlite_uri = 'sqlite:///./Chinook.db' 

# if you are using MySQL
# mysql_uri = 'mysql+mysqlconnector://rfamro:none@mysql-rfam-public.ebi.ac.uk:4497/Rfam'
mysql_uri = 'mysql+mysqlconnector://rfamro@mysql-rfam-public.ebi.ac.uk:4497/Rfam'

db = SQLDatabase.from_uri(mysql_uri)
