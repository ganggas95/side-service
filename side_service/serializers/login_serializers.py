from flask_marshmallow import Schema


class LoginSerializers(Schema):

    class Meta:
        fields = [
            'token',
            'refresh_token',
        ]
