from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema


new_user_schema = {
    'type': 'object',
    'required': ['username', 'email', 'password', 'conf_password'],
    'properties': {
        'username': {'type': 'string', 'minLength': 4, 'pattern': "^[a-zA-Z0-9]+([_]?[a-zA-Z0-9])*$"},
        'email': {'type': 'string', 'minLength': 6, 'format': 'email'},
        'password': {'type': 'string', 'minLength': 6},
        'conf_password': {'type': 'string', 'minLength': 6},
    }
}

update_user_schema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string', 'minLength': 4, 'pattern': '^[a-zA-Z0-9]+([_]?[a-zA-Z0-9])*$'},
        'email': {'type': 'string', 'minLength': 6},
    }
}

update_password_schema = {
    'type': 'object',
    'required': ['old_password', 'password', 'conf_password'],
    'properties':  {
        'old_password': {
            'type': 'string',
            'minLength': 6,
        },
        'password': {
            'type': 'string',
            'minLength': 6,
        },
        'conf_password': {
            'type': 'string',
            'minLength': 6,
        },
    }
}


class NewUserInputs(Inputs):
    json = [JsonSchema(schema=new_user_schema)]


class UpdateUserInputs(Inputs):
    json = [JsonSchema(schema=update_user_schema)]


class UpdatePasswordInputs(Inputs):
    json = [JsonSchema(schema=update_password_schema)]
