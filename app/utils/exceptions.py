from fastapi import HTTPException


class NotFoundException(HTTPException):
    def __init__(self):
        super(NotFoundException, self).__init__(status_code=404, detail="موردی یافت نشد.")
