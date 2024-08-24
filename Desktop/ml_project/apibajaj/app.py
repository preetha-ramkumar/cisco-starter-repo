from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        data = request.json.get("data", [])

        # Separate numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        # Determine the highest alphabet
        highest_alphabet = sorted(alphabets, key=lambda x: x.upper())[-1:] if alphabets else []

        # Response
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with your user_id format
            "email": "john@xyz.com",  # Replace with the user's email
            "roll_number": "ABCD123",  # Replace with the roll number
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }

        return jsonify(response)

    elif request.method == 'GET':
        # Hardcoded response for GET request
        response = {
            "operation_code": 1
        }
        return jsonify(response), 200

if __name__ == "__main__":
    app.run()
