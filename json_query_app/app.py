from flask import Flask, render_template, request, jsonify
import json

def evaluate_expression(data):
    try:
        expression = ""
        for item in data:
            if 'val' in item:
                expression += str(item['val'])
            elif 'opr' in item:
                expression += item['opr']
        
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.json.get('expression', [])
        result = evaluate_expression(data)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Steps to Run Locally:
# 1. Install Flask if not already installed: pip install flask
# 2. Save this script as app.py
# 3. Create a 'templates' folder in the same directory and add 'index.html' inside it.
# 4. Run the script using: python app.py
# 5. Open your browser and go to: http://<your-ip>:5000 (Replace <your-ip> with your system's IP)

