from flask import Flask
import psycopg2
import os
import random
import string
import logging

app = Flask(__name__)
conn = psycopg2.connect(os.environ["DATABASE_URL"])
conn.autocommit = True

# Ensure table exists
with conn.cursor() as cur:
    logging.info("Ensuring mytable exists in the database.")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS mytable (
            id SERIAL PRIMARY KEY,
            value VARCHAR(64)
        );
    """)

def get_str():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

@app.route('/', methods=['GET'])
def handle():
    logging.info("Handling request to insert a new record.")
    with conn.cursor() as cur:
        cur.execute("INSERT INTO mytable(value) VALUES (NULL) RETURNING id;")
        id_ = cur.fetchone()[0]
        s = get_str()
        cur.execute("UPDATE mytable SET value = %s WHERE id = %s;", (s, id_))
    return f"Inserted id={id_} with value={s}\n"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("asdfasdf")
    app.run(host="0.0.0.0", port=80)
