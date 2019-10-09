from flask_marshmallow import Schema


class UserSerializers(Schema):

    class Meta:
        fields = [
            'id',
            'username',
            'email',
        ]
