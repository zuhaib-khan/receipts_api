from marshmallow import Schema, fields

class ItemSchema(Schema):
    shortDescription = fields.Str(required=True)
    price = fields.Str(required=True)

class ReceiptSchema(Schema):
    retailer = fields.Str(required=True)
    purchaseDate = fields.Date(required=True)
    purchaseTime = fields.Time(required=True)
    items = fields.List(fields.Nested(ItemSchema), required=True)
    total = fields.Str(required=True)

    