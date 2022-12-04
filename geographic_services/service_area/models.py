import uuid

from mongoengine import Document, fields


class ServiceArea(Document):

    service_area_id = fields.StringField(
        required=True, default=str(uuid.uuid4())
    )
    name = fields.StringField(required=True)
    price = fields.DecimalField(required=True)
    geographic_area = fields.PolygonField(required=True)
    provider_name = fields.StringField(required=True)
