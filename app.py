from flask import Flask, jsonify, request
import uuid
from validation import ReceiptSchema
import math
from helpers import day_check, time_check, alpha_numeric_counter

app = Flask(__name__)

database = {}

@app.route('/receipts/process', methods=['POST'])
def receipt_process():
    
    data = request.get_json()

    validator = ReceiptSchema()
    validation_errors = validator.validate(data)
    if validation_errors:
        return jsonify(validation_errors), 400
    
    
    print(data)
    
    retailer_name = data.get('retailer')
    print(retailer_name)
    print(type(retailer_name))
    retailer_name_length = alpha_numeric_counter(retailer_name)

    items = data.get('items')
    
    purchase_date = data.get('purchaseDate')
    purchase_time = data.get('purchaseTime')
    #print(type(purchase_date))
    total = float(data.get('total'))
    
    purchase_day = day_check(purchase_date)
    
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
    
    #Checking if the description is a multiple of 3
    for item in items:
        item_descrption = item['shortDescription'].strip()
        length = len(item_descrption)
        if length % 3 == 0:
            price = float(item.get('price'))
            total_points += math.ceil(price * 0.2)
            
    #Checking if the purchase day is odd        
    if purchase_day % 2 != 0:
        total_points += 6
         
    #Checking if the time is in between 2pm and 4pm
    is_in_between = time_check(purchase_time)
    if is_in_between:
        total_points += 10
        
    id = str(uuid.uuid4())
    database[id] = total_points
    
    return jsonify({'id': id}), 200


@app.route('/receipts/<id>/points', methods=['GET'])
def receipt_points(id):
    
    if id not in database:
        return jsonify({'error': 'Wrong Key'}), 404
     
    return jsonify({'points': database[id]})
         
 
if __name__ == '__main__':
    app.run()
    
