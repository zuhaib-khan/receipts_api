"""
Routes file for the Receipt Processor API.

This file defines the API endpoints for processing receipts and retrieving points.
"""
from flask import request, jsonify, Blueprint, current_app
import uuid
from api.validation import ReceiptSchema
# import math
# from api.helpers import day_check, time_check, alpha_numeric_counter
from api.utilities.utilities import Calulator

routes = Blueprint('routes', __name__)

database = {}

@routes.route('/receipts/process', methods=['POST'])
def receipt_process():
    """
    Process a receipt and calculate points.

    The endpoint validates the receipt data using Marshmallow, computes points based on
    various rules and returns a unique receipt ID.

    Returns:
        A JSON response containing the generated receipt ID on success,
        or an error message with status code 400 if validation fails.
    """
    data = request.get_json()

    validator = ReceiptSchema()
    validation_errors = validator.validate(data)
    if validation_errors:
        
        current_app.logger.warning(validation_errors)
        return jsonify({"descrption":  "The receipt is invalid."}), 400
    
    calculator = Calulator()
    total_points = calculator.calcluate_points(data)
        
    id = str(uuid.uuid4())
    database[id] = total_points
    
    return jsonify({'id': id}), 200


@routes.route('/receipts/<id>/points', methods=['GET'])
def receipt_points(id):
    """
    Retrieve the points awarded for a given receipt.

    Param:
        id : The unique receipt identifier.

    Returns:
        A JSON response containing the points awarded if the receipt exists,
        or an error message with status code 404 if not found.
    """
    if id not in database:
        return jsonify({"description": "No receipt found for that ID."}), 404
     
    return jsonify({'points': database[id]}), 200