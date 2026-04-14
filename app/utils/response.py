def api_response(success: bool, message: str, data=None, status_code: int = 200):
    payload = {
        "success": success,
        "message": message,
        "data": data or {},
    }
    return payload, status_code
