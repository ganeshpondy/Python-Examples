# https://blog.teclado.com/first-rest-api-flask-postgresql-python/
import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request
from datetime import datetime, timezone

CREATE_USERS_TABLE = (
    "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT);"
)
CREATE_items_price_TABLE = """CREATE TABLE IF NOT EXISTS items_price (user_id INTEGER, item TEXT, price INTEGER,
                        date TIMESTAMP, FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE);"""

INSERT_USERS_RETURN_ID = "INSERT INTO users (name) VALUES (%s) RETURNING id;"

INSERT_ITEM = (
    "INSERT INTO items_price (user_id, item, price, date) VALUES (%s, %s, %s, %s);"
)

GLOBAL_NUMBER_OF_DAYS = (
    """SELECT COUNT(DISTINCT DATE(date)) AS days FROM items_price;"""
)
GLOBAL_AVG = """SELECT AVG(price) as average FROM items_price;"""


# To Read .env file
load_dotenv()  # loads variables  from .env file into environment

app = Flask(__name__)
url = os.getenv("DATABASE_URL")  # gets variables  from environment
connection = psycopg2.connect(url)

# @app.get("/")
# def home():
#     return "Hello World!! and Happy Coding!!!!"

@app.post("/api/user")
def create_user():
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cursor: #insert data into Database or get table details
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(INSERT_USERS_RETURN_ID, (name,)) # to pass tupal
            user_id = cursor.fetchone()[0]
    return {"id": user_id, "message": f"user {name} created."}, 201

@app.post("/api/item")
def add_item():
    data = request.get_json()
    item = data["item"]
    user_id = data["user_id"]
    price = data["price"]
    try:
        date = datetime.strptime(data["date"], "%m-%d-%Y %H:%M:%S") # add data and time details
    except KeyError:
        date = datetime.now(timezone.utc)
    with connection:    # Connecting DB
        with connection.cursor() as cursor:
            cursor.execute(CREATE_items_price_TABLE)
            cursor.execute(INSERT_ITEM, (user_id, item, price, date))
    return {"message": "Item added."}, 201

@app.get("/api/average")
def get_global_avg():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GLOBAL_AVG)
            average = cursor.fetchone()[0]
            # cursor.execute(GLOBAL_NUMBER_OF_DAYS)
            # days = cursor.fetchone()[0]
    # return {"average": round(average, 2), "days": days}
    return {"average Price": round(average, 2)}
