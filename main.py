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
    'database': os.getenv("SF_DATABASE"),
    # 'schema': 'some_schema'
}


#Opening connection
con = snowflake.connector.connect(**connection_params)

cursor = con.cursor()

query = "SELECT COUNTRY_REGION, SUM(CASES) AS Cases FROM ECDC_GLOBAL GROUP BY COUNTRY_REGION"
cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)


#Closing connection
cursor.close()
con.close()