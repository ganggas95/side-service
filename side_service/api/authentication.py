from flask import request
from flask_injector import inject
from flask_jwt_extended import jwt_refresh_token_required
from side_service.provider import login_provider


@inject
def login(login_provider: login_provider.LoginProvider) -> dict:
    login_result, errors = login_provider.login_user(request)
    status = 200 if login_result else 403
    msg = "Login successfully" if login_result else "Login failed"
    return login_provider.create_response(
        status=status,
        data=login_result,
        msg=msg,
        errors=errors
    )


@inject
@jwt_refresh_token_required
def refresh_token(login_provider: login_provider.LoginProvider) -> dict:
    refresh_result = login_provider.refresh_token()
    status = 200
    if refresh_result is None:
        status = 403
    return login_provider.create_response(
        status=status,
        data=refresh_result,
        errors=login_provider.error_refresh if refresh_result is None else None,
    )
