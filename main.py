import snowflake.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

conn_params = {
    'user': os.getenv("SF_USER"),
    'password': os.getenv("SF_PASSWORD"),
    'account': os.getenv("SF_ACCOUNT"),
    'warehouse': os.getenv("SF_WAREHOUSE"),
    'database': os.getenv("SF_DATABASE"),
    # 'schema': 'some_schema'
}


#Opening connection
conn = snowflake.connector.connect(**conn_params)

cursor = conn.cursor()
query = "SELECT COUNTRY_REGION, SUM(CASES) AS Cases FROM ECDC_GLOBAL GROUP BY COUNTRY_REGION"
cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)


#Closing connection
cursor.close()
conn.close()