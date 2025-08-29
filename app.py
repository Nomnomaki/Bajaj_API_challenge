from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.get_json()
        if not data or "data" not in data or not isinstance(data["data"], list):
            return jsonify({
                "is_success": False,
                "error": "Data should be an array"
            }), 400

        arr = data["data"]
        even = [x for x in arr if x.isdigit() and int(x) % 2 == 0]
        odd = [x for x in arr if x.isdigit() and int(x) % 2 != 0]
        alpha = [x.upper() for x in arr if x.isalpha()]
        special = [x for x in arr if not x.isalnum()]
        summ = str(sum(int(x) for x in arr if x.isdigit()))

        letters = "".join([x for x in arr if x.isalpha()])
        temp = letters[::-1]
        concat = "".join([ch.upper() if i % 2 == 0 else ch.lower() for i, ch in enumerate(temp)])

        response = {
            "is_success": True,
            "user_id": "aniket_saxena_27082004",
            "email": "aniket.saxena2022a@vitstudent.ac.in",
            "roll_number": "22BRS1050",
            "even_numbers": even,
            "odd_numbers": odd,
            "alphabets": alpha,
            "special_characters": special,
            "sum": summ,
            "concat_string": concat
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
