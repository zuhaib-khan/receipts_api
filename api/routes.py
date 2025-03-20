from flask import request, jsonify, Blueprint, current_app
import uuid
from api.validation import ReceiptSchema
import math
from api.helpers import day_check, time_check, alpha_numeric_counter

routes = Blueprint('routes', __name__)

database = {}

@routes.route('/receipts/process', methods=['POST'])
def receipt_process():
    
    data = request.get_json()

    validator = ReceiptSchema()
    validation_errors = validator.validate(data)
    if validation_errors:
        
        current_app.logger.warning(validation_errors)
        return jsonify({"descrption":  "The receipt is invalid."}), 400    
    
    retailer_name = data.get('retailer')
    retailer_name_length = alpha_numeric_counter(retailer_name)

    items = data.get('items')
    
    purchase_date = data.get('purchaseDate')
    purchase_time = data.get('purchaseTime')
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


@routes.route('/receipts/<id>/points', methods=['GET'])
def receipt_points(id):
    
    if id not in database:
        return jsonify({"description": "No receipt found for that ID."}), 404
     
    return jsonify({'points': database[id]}), 200