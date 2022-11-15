from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/home', methods=['POST'])
def home():
    data = request.files['file']
    print(type(data))
    return jsonify({"status":"ok"})

app.run()