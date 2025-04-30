from functools import wraps
from typing import Any, Callable, TypeVar

from flask import current_app, jsonify, request
from jsonschema import ValidationError, validate
from werkzeug.exceptions import BadRequest


F = TypeVar("F", bound=Callable[..., Any])


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        # リクエストのコンテンツタイプがjsonかどうかをチェックします。
        ctype = request.headers.get("Content-Type")
        method_ = request.headers.get("X-HTTP-Method-Override", request.method)
        if method_.lower() == request.method.lower() and ctype and "json" in ctype:
            try:
                # bodyメッセージがそもそもあるかどうかをチェックします。
                request.json
            except BadRequest:
                msg = "This is an invalid json"
                return jsonify({"error": msg}), 400
            return f(*args, **kw)

    return wrapper


def validate_schema(schema_name: str) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # 先程、定義したjsonファイルの通りにjsonのbodyメッセージ送られているかどうかをチェックします。
                validate(request.json, current_app.config[schema_name])
            except ValidationError as e:
                return jsonify({"error": e.message}), 400
            return func(*args, **kwargs)
        return wrapper  # type: ignore
    return decorator
