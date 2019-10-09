from side_service.utils.response import create_response


class Provider:
    @staticmethod
    def create_response(status=200, data=None, msg="", errors={}, meta=None):
        return create_response(status=status, data=data, msg=msg, errors=errors, meta=meta)
