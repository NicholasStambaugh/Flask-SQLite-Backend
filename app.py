from flask import Flask, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              email TEXT NOT NULL,
              password TEXT NOT NULL)''')

conn.commit()

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/users', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    c.execute('''INSERT INTO users (name, email, password)
                 VALUES (?, ?, ?)''', (name, email, password))

    conn.commit()

    return 'User added successfully!'

@app.route('/users', methods=['GET'])
def get_users():
    c.execute('''SELECT * FROM users''')
    rows = c.fetchall()

    return str(rows)

if __name__ == '__main__':
    app.run(debug=True)
