# COVID-19 Data Integration, Analysis, and Visualization Platform

## Project Goal:
To develop a web-based interactive dashboard with useful information and infographics based on Covid-19 data

## Project Structure:
- Snowflake DB - main data storage
- Python API (using Flask) for data query
- Python Dashboard (using Dash) - frontend
- Preprocessing plan to showcase data pre-processing procedure

## Package installation:
- `pip install snowflake-connector-python`
- `pip install snowflake-snowpark-python`
- `pip install python-dotenv`
- `pip3 install requests`
- `pip3 install dash-bootstrap-components`
- `pip3 install Flask-Caching`
- `pip3 install pymongo`

  Note: Snowpark API requires Python 3.8+

  ### To run the project:
1. `git clone or download zip`
2. `cd api`
3. create .env file to store database connection details:
SF_USER=<...USERNAME>
SF_PASSWORD=<...PASSWORD>  
SF_ACCOUNT=<...ACCOUNT>  
SF_WAREHOUSE=<...WAREHOUSE>  
SF_DATABASE=<...DATABASE1> #original DB from which Views and Tables were created (needed for preprocessing. Can skip this  
SF_DATABASE_OPER=<...DATABASE2> # operational database, where actual data to be queried is stored 
6. `python3 main.py`
7. `cd ../src`
8. `python3 app.py`
9. go to `http://127.0.0.1:8050/`
