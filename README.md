# Banking-Chatbot

# 🏦 Banking Assistant Chatbot

This is a **simple banking assistant chatbot** web application built using **Flask** for the backend and **NLTK** for natural language processing. It simulates basic conversations with customers, answering banking-related questions, and learning from unrecognized queries.

---

## 🔧 Technologies Used

| **Component**  | **Description** |
|----------------|-----------------|
| **Flask**      | Web framework used to create the chat interface and API endpoints. |
| **NLTK**       | Python library for text processing, used here to tokenize user input. |
| **SQLite**     | Temporary in-memory database used to store account types and log unknown queries. |
| **HTML**       | Frontend interface (`index.html`) where users interact with the bot. |

---

## 🔄 How It Works

### 1. 📦 Database Setup

Two SQLite tables are created:

- **`accounts`**: Stores predefined banking account types (e.g., "Savings", "Current", "Fixed Deposit").
- **`learning`**: Logs unrecognized user queries to enhance future responses.

---

### 2. 🧠 Tokenization

User input is split into tokens (words) using NLTK:

```python
tokens = word_tokenize(user_input.lower())
This allows the bot to identify keywords such as "hello", "account", and "loan".
```

### 3. 🤖 Response Logic

The `get_response()` function handles the logic:

#### Greeting & Known Inputs:
- **"hello"** → Bot greets the user.
- **"how are you"** → Bot responds positively.
- **"loan"** → Bot provides loan information.
- **"account"** → Bot fetches and lists all available accounts.
- **"thank"** → Bot expresses appreciation.

#### Fallback & Learning:
If the input isn’t recognized, the query is saved to the `learning` table.

The bot responds with: **"I'm sorry, could you rephrase that?"**

---

### 4. 🌐 Web Interface

- **`index()`**: Serves the main HTML page where users chat with the bot.
- **`chatbot_reply()`**: Handles AJAX requests, receives user input, and returns the bot’s response in JSON format.

---

## 🧪 Sample Interactions

| **User Says**                               | **Bot Responds**                                                      |
|---------------------------------------------|----------------------------------------------------------------------|
| hello                                      | "Hello! How can I assist you with your banking needs today?"           |
| what types of accounts do you offer        | "We offer Savings, Current, and Fixed Deposit accounts."              |
| tell me about loan                         | "We provide Home Loans, Personal Loans, and Vehicle Loans."           |
| thank you                                   | "You're welcome!"                                                     |
| can I apply online                         | "I'm sorry, could you rephrase that?"                                 |

---

## 🔄 Learning Mechanism

Unrecognized queries are saved in the `learning` table.

These queries can be reviewed later, and you can manually enhance the bot by handling these unrecognized queries.

---

## ✅ Strengths of the Project

- **Lightweight**: Easy to set up and run.
- **Modular**: The response logic is simple and can be easily expanded.
- **Logs Unknown Queries**: Unrecognized inputs are stored for future enhancement.
- **Real-Time Responses**: Flask provides quick, interactive feedback to users.

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JayaniMalsha/Banking-Chatbot.git
cd Banking-Chatbot
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv chatbot_env
chatbot_env\Scripts\activate    # Windows
# OR
source chatbot_env/bin/activate # macOS/Linux
```

### 3. Install the Required Packages

```bash
pip install flask nltk
```

### 4. Download NLTK Tokenizer Data

```bash
# In a Python shell
import nltk
nltk.download('punkt')
```

### 5. Run the Jupyter notebook

```bash
jupyter notebook
```
Open BankingAssistantChatbot_Valid.ipynb

### 6. Run the Application

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser to interact with the chatbot.

---

## 🛠️ Future Enhancements

- **Persistent Database**: Use a file-based SQLite database instead of in-memory storage.
- **User Authentication**: Add login and session tracking features for personalized responses.
- **Machine Learning Integration**: Integrate NLP models to classify user intent and improve understanding.
- **Admin Panel**: Implement an admin interface to review and label unrecognized queries for training.
