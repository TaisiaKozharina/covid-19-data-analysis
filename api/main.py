import snowflake.connector
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_caching import Cache
from pymongo import MongoClient
import os
from bson.json_util import dumps


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


cache_config = {
    "DEBUG": True,          
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(cache_config)
cache = Cache(app)

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
@cache.cached(timeout=3000)
def get_demographic_data():

    #Opening connection
    con = snowflake.connector.connect(**connection_params)
    cursor = con.cursor()

    query = "USE ROLE ACCOUNTADMIN"
    cursor.execute(query)


    query = f"SELECT * from EXPOSURE_COUNTRY_INFO"
    cursor.execute(query)

    data = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]

    response = {'data': [dict(zip(column_names, row)) for row in data], 'comment': "OK"}

    con.close()

    return jsonify(response)


@app.route('/get_vaccination_data', methods=['GET'])
@cache.cached(timeout=3000)
def get_vaccination_data():

    #Opening connection
    con = snowflake.connector.connect(**connection_params)
    cursor = con.cursor()

    query = "USE ROLE ACCOUNTADMIN"
    cursor.execute(query)

    query = f'''select o.date, o.total_vaccinations as "TOTAL_VACCINATED", o.daily_vaccinations as "DAILY_VACCINATED",
                o.people_fully_vaccinated as "FULLY_VACCINATED", o.country_region, o.iso3166_1, o.country_region
                from OWID_VACCINATIONS o'''
    cursor.execute(query)

    data = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]

    response = {'data': [dict(zip(column_names, row)) for row in data], 'comment': "OK"}

    con.close()

    return jsonify(response)


@app.route('/post_comment', methods=['POST'])
def post_comment():
    data = request.json

    client = MongoClient()
    db = client['covid19_meta']
    collection = db['exposure_comments']

    inserted_id = collection.insert_one(data).inserted_id
    print("Inserted data to MongoDB. Inserted ID: ", inserted_id)
    
    response_data = {"inserted_id": str(inserted_id)}
    return jsonify(response_data)



@app.route('/get_comment', methods=['GET'])
def get_comment():

    country = request.args.get('country')

    client = MongoClient()
    db = client['covid19_meta']
    collection = db['exposure_comments']


    result = list(collection.find({"country": country}))
    print(result)

    return dumps(result)




if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
