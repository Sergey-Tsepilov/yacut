from http import HTTPStatus

from flask import jsonify, render_template

from . import app, db


class CustomAPIError(Exception):
    """Кастомное исключение для API с поддержкой статуса ошибки."""
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        """Возвращает словарь с сообщением об ошибке."""
        return {'message': self.message}


@app.errorhandler(CustomAPIError)
def api_error_handler(error):
    """Обработчик кастомных ошибок API."""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):
    """Обработчик ошибки 404."""
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error):
    """Обработчик ошибки 500."""
    db.session.rollback()
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR
