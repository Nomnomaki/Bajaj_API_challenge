from flask import Flask, jsonify, request 

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.get_json()
        arr = data.get("data", [])

        even = [x for x in arr if x.isdigit() and int(x) % 2 == 0]
        odd = [x for x in arr if x.isdigit() and int(x) % 2 != 0]
        alpha = [x.upper() for x in arr if x.isalpha()]
        special= [x for x in arr if not x.isalnum()]
        summ = str(sum(int(x) for x in arr if x.isdigit()))

        concat = ""
        letters = "".join([x for x in arr if x.isalpha()])
        temp= letters[::-1]
        for i, ch in enumerate(temp):
            concat += ch.upper() if i % 2 == 0 else ch.lower()

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
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
