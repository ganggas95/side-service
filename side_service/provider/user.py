from side_service.provider import Provider
from side_service.serializers.user_serializers import UserSerializers
from side_service.validators.user_validators import NewUserInputs
from side_service.validators.user_validators import UpdateUserInputs
from side_service.models.user import Users


class UserProvider(Provider):
    user_serializers = UserSerializers(many=True)
    user_serializer = UserSerializers()

    @staticmethod
    def get_all():
        return Users.all()
    
    @staticmethod
    def get_by_username(username):
        return Users.by_username(username)

    @staticmethod
    def create_new(payload):
        inputs = NewUserInputs(payload)
        if not inputs.validate():
            return None, inputs.errors
        payload = payload.get_json(force=True)
        user = Users(payload['username'],
                     payload['email'],
                     payload['password'])
        if not user.is_exist:
            user.save()
            return user, None
        return None, "Users is exist"

    @staticmethod
    def update_user(username, payload):
        inputs = UpdateUserInputs(payload)
        if not inputs.validate():
            return None, inputs.errors
        payload = payload.get_json(force=True)
        user = Users.by_username(username)
        user.from_payload(payload)
        user.update()
        return user, None
