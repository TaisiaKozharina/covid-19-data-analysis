from snowflake.snowpark.session import Session
import sys
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

connection_params = {
    'user': os.getenv("SF_USER"),
    'password': os.getenv("SF_PASSWORD"),
    'account': os.getenv("SF_ACCOUNT"),
    'warehouse': os.getenv("SF_WAREHOUSE"),
    'database': os.getenv("SF_DATABASE"),
    # 'schema': 'some_schema'
}

def snowflake_connector():
    try:
        session = Session.builder.configs(connection_params).create()
        print("connection successful!")
    except:
        raise ValueError("error while connecting with db")
    return session

#define a session
session = snowflake_connector()

snowpark_df = session.table("COVID19_RECORDS")

print(type(snowpark_df)) # snowflake.snowpark.table.Table
print(f"Size of the table object: {(sys.getsizeof(snowpark_df)/1e6)} MB")