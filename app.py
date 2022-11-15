from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/home', methods=['POST'])
def home():
    data = request.files['file']
    return jsonify({"status":"ok"})

if __name__ == "__main__":
    app.run()
