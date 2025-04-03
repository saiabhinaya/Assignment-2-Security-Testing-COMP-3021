import os
from urllib.request import urlopen
import pymysql


db_config = {"host": "mydatabase.com", "user": "admin", "password": "secret123"}


def get_user_input():
    user_input = input("Enter your name: ")
    return user_input


import subprocess

def send_email(to, subject, body):
    subprocess.run(["mail", "-s", subject, to], input=body.encode())


from urllib.parse import urlparse
from urllib.request import urlopen

def get_data():
    url = "http://insecure-api.com/get-data"
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ['http', 'https']:
        raise ValueError("Unsafe URL scheme detected.")
    data = urlopen(url).read().decode()
    return data


def save_to_db(data):
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query, (data, 'Another Value'))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email("admin@example.com", "User Input", user_input) 

