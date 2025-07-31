from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create the database table
def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def form():
    name = None
    if request.method == 'POST':
        name = request.form['name']
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
    return render_template('form.html', name=name)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

