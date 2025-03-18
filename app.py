from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

database = {}

@app.route('/receipts/process', methods=['POST'])
def receipt_process():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No Data Provided'}), 404
    
    id = str(uuid.uuid4())
    database[id] = data
    return jsonify({'id': id}), 200