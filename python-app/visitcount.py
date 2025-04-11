from flask import Flask, session

app = Flask(__name__)
app.secret_key = "session_secret_key"  # Required for session management
app.config['SESSION_PERMANENT'] = False  # Keep session active for the session duration


def increment_visit_count(route):
    """Helper function to increment visit count for a specific route"""
    if "visits" not in session:
        session["visits"] = {"home": 0, "test": 0, "prod": 0}
    session["visits"][route] += 1
    session.modified = True  # Ensure session data is saved



@app.route('/')
def home():
    increment_visit_count("home")
    return f"Welcome to the Home Page! You have visited this page {session['visits']['home']} times."

@app.route('/test')
def test():
    increment_visit_count("test")
    return f"This is the Test Environment. You have visited this page {session['visits']['test']} times."

@app.route('/prod')
def prod():
    increment_visit_count("prod")
    return f"This is the Production Environment. You have visited this page {session['visits']['prod']} times."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=("cert.pem", "key.pem"))
