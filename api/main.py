import snowflake.connector
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import os

# Load environment variables from .env file
load_dotenv()

connection_params = {
    'user': os.getenv("SF_USER"),
    'password': os.getenv("SF_PASSWORD"),
    'account': os.getenv("SF_ACCOUNT"),
    'warehouse': os.getenv("SF_WAREHOUSE"),
    'database': os.getenv("SF_DATABASE_OPER"),
    'schema': 'PUBLIC'
}


app = Flask(__name__)

@app.route('/get_table_data', methods=['GET'])
def get_data_from_table():

    #Opening connection
    con = snowflake.connector.connect(**connection_params)
    cursor = con.cursor()

    table_name = request.args.get('table')

    query = f"""
    SELECT *
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME = '{table_name}'
      AND TABLE_SCHEMA = 'PUBLIC'
    """
    cursor = con.cursor()
    cursor.execute(query)

    # Check if any rows were returned
    table_exists = cursor.rowcount > 0

    if table_exists:
        query = f"SELECT * from {table_name} limit 10"
        cursor.execute(query)

        data = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        response = {'data': [dict(zip(column_names, row)) for row in data], 'comment': "OK"}

    else:
        response={'data': [], "comment": "NO SUCH TABLE"}

    con.close()
    return jsonify(response)



@app.route('/get_demographic_data', methods=['GET'])
def get_demographic_data():

    #Opening connection
    con = snowflake.connector.connect(**connection_params)
    cursor = con.cursor()

    query = ""
    cursor = con.cursor()
    cursor.execute(query)

    query = f"SELECT * from EXPOSURE_COUNTRY_INFO limit"
    cursor.execute(query)

    data = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]

    response = {'data': [dict(zip(column_names, row)) for row in data], 'comment': "OK"}



    con.close()

    return jsonify(response)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)


#Closing connection
cursor.close()
con.close()