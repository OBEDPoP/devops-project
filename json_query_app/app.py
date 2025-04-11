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
        if not data:  
            return jsonify({"error": "Empty expression"})
        result = evaluate_expression(data)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

