from flask import request
from flask_injector import inject
from flask_jwt_extended import jwt_required
from side_service.provider import user_provider


@inject
@jwt_required
def search(user_provider: user_provider.UserProvider) -> dict:
    serializers = user_provider.user_serializers.dump(user_provider.get_all())
    return user_provider.create_response(
        status=200,
        data=serializers,
        msg="Success get data users"
    )


@inject
@jwt_required
def create_user(user_provider: user_provider.UserProvider) -> dict:
    user, errors = user_provider.create_new(request)
    return user_provider.create_response(
            status=201 if errors is None else 400,
            data=user_provider.user_serializer.dump(user),
            errors=errors,
        )


@inject
@jwt_required
def detail_user(user_provider: user_provider.UserProvider, username: str) -> dict:
    user = user_provider.get_by_username(username)
    return user_provider.create_response(
        status=200 if user else 404,
        data=user_provider.user_serializer.dump(user),
        errors=None if user else "Data not found"
    )


@inject
@jwt_required
def update_user(user_provider: user_provider.UserProvider, username: str) -> dict:
    user, errors = user_provider.update_user(username, request)
    return user_provider.create_response(
        status=200 if errors is None else 400,
        data=user_provider.user_serializer.dump(user),
        errors=errors
    )


@inject
@jwt_required
def delete_user(user_provider: user_provider.UserProvider, username: int) -> dict:
    success = user_provider.delete_user(username)
    msg = "Failed to remove user" if not success else "Success remove user"
    status = 400 if not success else 200
    return user_provider.create_response(
            status=status,
            data=username,
            msg=msg
        )


@inject
@jwt_required
def update_profile(user_provider: user_provider.UserProvider) -> dict:
    pass


@inject
@jwt_required
def update_password(user_provider: user_provider.UserProvider) -> dict:
    pass
