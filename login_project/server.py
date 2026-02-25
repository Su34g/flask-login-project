from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    database="login_db",
    user="postgres",
    password="suyog",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)