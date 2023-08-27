import snowflake.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

connection_params = {
    'user': os.getenv("SF_USER"),
    'password': os.getenv("SF_PASSWORD"),
    'account': os.getenv("SF_ACCOUNT"),
    'warehouse': os.getenv("SF_WAREHOUSE"),
    'database': os.getenv("SF_DATABASE_OPER"),
    # 'schema': 'some_schema'
}

# TODO: Change database!!!!


#Opening connection
con = snowflake.connector.connect(**connection_params)

cursor = con.cursor()

query = "SELECT * from MOBILITY_DATA LIMIT 10"
cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)


#Closing connection
cursor.close()
con.close()