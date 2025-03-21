# Flask Applications

This repository contains two simple Flask applications:

1. **app.py** - A basic Flask application that returns a static message.
2. **visitcount.py** - A Flask application that tracks how many times a user visits each route.

---

## **1. Basic Flask App (`app.py`)**

### **Description**
The `app.py` file contains a minimal Flask application with a single endpoint (`/`) that returns a static message.

### **How to Run**
1. Install Flask if not already installed:
   ```bash
   pip install flask
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open your browser and visit:
   - **http://127.0.0.1:5000/** → Displays: `"Hello, DevOps World!"`
   - **http://127.0.0.1:5000/test** → Displays: `"Hello, you are in /test path of DevOps World!"`

---

## **2. Visit Counter App (`visitcount.py`)**

### **Description**
The `visitcount.py` file extends the Flask application by tracking the number of times a user visits three different routes:  

- `/` → Home page visit count  
- `/test` → Test environment visit count  
- `/prod` → Production environment visit count  

This is done using Flask **sessions**, which store visit counts for each user.

### **How to Run**
1. Install Flask if not already installed:
   ```bash
   pip install flask
   ```
2. Run the application:
   ```bash
   python visitcount.py
   ```
3. Open your browser and visit:
   - **http://127.0.0.1:5000/** → Tracks visits to the Home page
   - **http://127.0.0.1:5000/test** → Tracks visits to the Test page
   - **http://127.0.0.1:5000/prod** → Tracks visits to the Production page

Each visit will increment and display the updated count for that page.

---

## **Technologies Used**
- **Python** (Flask)
- **Flask Sessions** (For visit tracking)

These apps serve as simple examples of **Flask routing and session management**. 🚀


