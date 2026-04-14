swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Decision Journal API",
        "description": "RESTful API for capturing and reviewing decisions.",
        "version": "1.0.0",
    },
    "basePath": "/",
    "schemes": ["http", "https"],
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/",
}
