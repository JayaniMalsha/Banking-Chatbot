from flask import Flask, request, jsonify, render_template
import sqlite3
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

app = Flask(__name__)

# Setup database in memory
conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_type TEXT NOT NULL
    )
''')
cursor.executemany('INSERT INTO accounts (account_type) VALUES (?)',
                   [('Savings Account',), ('Current Account',), ('Fixed Deposit Account',)])
cursor.execute('''
    CREATE TABLE IF NOT EXISTS learning (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL
    )
''')
conn.commit()

def get_response(user_input):
    user_input_lower = user_input.lower()

    if 'hello' in user_input_lower or 'hi' in user_input_lower:
        return "Hello! How can I assist you with your banking needs today?"
    elif 'how are you' in user_input_lower:
        return "I'm doing great, thank you! How can I assist you today?"
    elif 'good morning' in user_input_lower:
        return "Good morning! How may I assist you today?"
    elif 'account' in user_input_lower:
        cursor.execute('SELECT account_type FROM accounts')
        accounts = cursor.fetchall()
        return "We offer Savings, Current, and Fixed Deposit accounts."
    elif 'loan' in user_input_lower:
        return "We provide Home Loans, Personal Loans, and Vehicle Loans."
    elif 'thank' in user_input_lower:
        return "You're welcome!"
    else:
        cursor.execute('INSERT INTO learning (question) VALUES (?)', (user_input,))
        conn.commit()
        return "I'm sorry, could you rephrase that?"



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_response', methods=['POST'])
def chatbot_reply():
    user_input = request.form.get('user_input')
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
