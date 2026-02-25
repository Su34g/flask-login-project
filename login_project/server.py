from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Read database URL from environment variable
conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
cur = conn.cursor()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cur.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )
        conn.commit()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
