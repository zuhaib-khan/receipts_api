"""
Validation file for the Receipt Processor API.

"""
from marshmallow import Schema, fields

class ItemSchema(Schema):
    """
    Schema for validating an individual item on a receipt.
    """
    shortDescription = fields.Str(required=True)
    price = fields.Str(required=True)

class ReceiptSchema(Schema):
    """
    Schema for validating a receipt.
    """
    retailer = fields.Str(required=True)
    purchaseDate = fields.Date(required=True)
    purchaseTime = fields.Time(required=True)
    items = fields.List(fields.Nested(ItemSchema), required=True)
    total = fields.Str(required=True)

    