import uuid

from mongoengine import Document, fields


class Provider(Document):

    provider_id = fields.StringField(required=True, default=str(uuid.uuid4()))
    name = fields.StringField(required=True)
    email = fields.EmailField(required=True)
    phone_number = fields.StringField(required=True)
    language = fields.StringField(required=True)
    currency = fields.StringField(required=True)
