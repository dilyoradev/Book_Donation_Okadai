# Book Donation Website for Okayama University Students

A **Book Donation platform** for Okayama University students to donate, request, and manage books within their community. Users can share books they no longer need, request books from others, and interact through comments.

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.1.2-orange)](https://flask.palletsprojects.com/)
[![Issues](https://img.shields.io/github/issues/dilyoradev/Book_Donation_Okadai)](https://github.com/dilyoradev/Book_Donation_Okadai/issues)

## ✨ Features

* **User Authentication** – Signup & login required to donate or request books.
* **Book Donation** – Upload and manage books you want to donate.
* **Request Books** – Browse and request available books.
* **Donation & Request List** – Track all your donated and requested books.
* **Comments** – Leave comments on books for communication.
* **Meetup Arrangement** – Donors and requesters can coordinate time & place for exchanges.
  
---

## 📌 Screenshots

* **Homepage**
  ![Homepage](app/static/docs/screenshots/homepage_demo.png)

* **Book Donation Form**
  ![Donate Form](app/static/docs/screenshots/donate_page_demo.png)

---

## 🖥️ Tech Stack

* **Frontend:** HTML, CSS, Jinja2 templates
* **Backend:** Python, Flask
* **Database:** SQLAlchemy
* **Dependencies:**

```text
blinker==1.9.0
click==8.2.1
Flask==3.1.2
Flask-SQLAlchemy==3.1.1
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
SQLAlchemy==2.0.43
typing_extensions==4.15.0
Werkzeug==3.1.3
```

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/dilyoradev/Book_Donation_Okadai.git
cd Book_Donation_Okadai/backend
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
flask run
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 🛠️ Usage

1. **Signup/Login** – Only registered users can donate or request books.
2. **Donate a Book** – Upload book details including title, author, and description.
3. **Request a Book** – Browse donations and send requests for books you need.
4. **Comment** – Leave feedback or coordinate with donors.
5. **Manage Lists** – Keep track of your donated and requested books.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a pull request

---

## 🔗 Repository

[Book Donation Okadai GitHub](https://github.com/dilyoradev/Book_Donation_Okadai.git)
