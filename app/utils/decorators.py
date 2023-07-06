from functools import wraps

import pydantic

from app.utils.exceptions import NotFoundException


def handle_not_found(func):
    @wraps(func)
    async def wrapper(*args, **kwarg):
        try:
            return await func(*args, **kwarg)
        except pydantic.error_wrappers.ValidationError:
            raise NotFoundException

    return wrapper
