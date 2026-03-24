# Wilkens Ave Renaissance Coalition - Flask App

This is the Flask application for the Wilkens Ave Renaissance Coalition website, including a join/contact form that stores submissions in a CSV file.

## Requirements

- Python 3.12 (or the version specified in `.python-version`)
- pip

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/DHBjorndalen/Wilkens-Ave_Renaissance.git
cd Wilkens-Ave_Renaissance
Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
Install dependencies
pip install -r requirements.txt
Set environment variables

Create a .env file in the project root with:

SECRET_KEY="your_secret_key_here"

Submissions are saved in submissions.csv in the project root.
Deployment Notes
Ensure the host environment has the correct Python version and reads .env.
For production, use a WSGI server like Gunicorn or uWSGI.