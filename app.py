from flask import Flask, jsonify, request
import uuid
from datetime import datetime, time
import math

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

@app.route('/receipts/<id>/points', methods=['GET'])
def receipt_points(id):
    requested = id
    if id not in database:
        return jsonify({'error': 'Wrong Key'}), 400
     
    data = database[id]
    retailer_name_length = len(data.get('retailer'))
     
    items = data.get('items')
    purchase_date = data.get('purchaseDate')
    purchase_day = purchase_date[8:10]
    purchase_day = int(purchase_date[8:10])
    purchase_time = data.get('purchaseTime') 
     
    total = float(data.get('total'))
 
    total_points = retailer_name_length
     #checking if total is a round dollar amount
    if total % 1 == 0:
        total_points += 50
     #Checking if the total is a multiple of 0.25
    if (total * 100) % 25 == 0:
        total_points += 25
     #For every second item, adding 5 points  
    item_points = (len(items) // 2) * 5
    total_points += item_points
     #Checking if thr desciption is a multiple of 3
    for item in items:
        item_descrption = item['shortDescription'].strip()
        length = len(item_descrption)
        if length % 3 == 0:
            price = float(item.get('price', '0.00'))
            total_points += math.ceil(price * 0.2)
     #Checking if the purchase day is odd        
    if purchase_day % 2 != 0:
        total_points += 6
          
     #Checking if the time is in between 2pm and 4pm
    is_in_between = time_check(purchase_time)
    if is_in_between:
        total_points += 10
         
    return jsonify({'points':total_points}), 200
         
       
def time_check(time_stamp):
 
    given_time_stamp = datetime.strptime(time_stamp, '%H:%M').time()
    start_time = time(14,0)
    end_time = time(16,0)
 
    in_between = start_time < given_time_stamp < end_time
    return in_between
 
if __name__ == '__main__':
    app.run()
     
    app.run(debug=True)
