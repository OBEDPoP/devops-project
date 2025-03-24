# JSON Expression Evaluator

## Overview
This is a Flask-based web application that evaluates mathematical expressions provided in JSON format. Users can input a JSON array containing values and operators, and the application will compute the result dynamically.

## Features
- Accepts JSON input with numbers (`val`) and operators (`opr`).
- Evaluates the mathematical expression securely.
- Provides real-time results.
- Web-based interface using HTML, JavaScript, and jQuery.

## Prerequisites
Ensure you have Python installed along with Flask. You can install Flask using:
```sh
pip install flask
```

## Installation & Setup
1. Clone the repository or copy the script.
2. Create a `templates` folder and add `index.html` inside it.
3. Run the Flask app:
   ```sh
   python app.py
   ```
4. Open a browser and navigate to:
   ```
   http://<your-ip>:5000
   ```
   Replace `<your-ip>` with your system's IP address.

## JSON Input Format
The input should be structured as an array of objects, where:
- `val` represents a numeric value.
- `opr` represents an operator (`+`, `-`, `*`, `/`, `**`, etc.).

### Example JSON Input
```json
[
  {"val": 25},
  {"opr": "*"},
  {"val": 2},
  {"opr": "**"},
  {"val": 3}
]
```

### Expected Output
```sh
250000
```

## API Endpoints
### `GET /`
Loads the web interface.

### `POST /evaluate`
Accepts JSON input and returns the evaluated result.

#### Request Example:
```json
{
  "expression": [
    {"val": 5},
    {"opr": "*"},
    {"val": 10}
  ]
}
```

#### Response Example:
```json
{
  "result": 50
}
```

## Security Considerations
- The application currently uses `eval()` to compute expressions, which can be a security risk if the input is not validated properly.
- In a production environment, implement strict validation to prevent code injection.

## License
This project is open-source and free to use. Modify it as needed!

## Contributing
Feel free to submit pull requests or suggestions to improve this application.


