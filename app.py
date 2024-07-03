from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'draft.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS drafts
                        (id INTEGER PRIMARY KEY, participant TEXT, drafted_member TEXT)''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    participant = request.form['participant']
    drafted_member = request.form['drafted_member']
    
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('INSERT INTO drafts (participant, drafted_member) VALUES (?, ?)', 
                     (participant, drafted_member))
    
    return render_template('submit.html')

@app.route('/results')
def results():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute('SELECT participant, drafted_member FROM drafts')
        drafts = cursor.fetchall()

    results = {}
    for participant, drafted_member in drafts:
        if participant not in results:
            results[participant] = []
        results[participant].append(drafted_member)

    return render_template('results.html', results=results)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
