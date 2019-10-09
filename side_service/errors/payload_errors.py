from side_service.utils.response import create_response


def validation_error(e):
    error = dict()
    for err in e.errors:
        error[err.path[0]] = err.message
    return create_response(
        status=400,
        msg=e.message,
        errors=error
    )
