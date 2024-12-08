from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .error_handlers import CustomAPIError
from .models import URLMap
from .utils import check_short, get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    """Создает короткую ссылку из переданного URL."""
    data = request.get_json(silent=True)
    if data is None:
        raise CustomAPIError('Отсутствует тело запроса')
    elif 'url' not in data:
        raise CustomAPIError('"url" является обязательным полем!')
    if data.get('custom_id'):
        if len(data['custom_id']) > 16 or not check_short(data['custom_id']):
            raise CustomAPIError(
                'Указано недопустимое имя для короткой ссылки')
        elif URLMap.query.filter_by(
            short=data['custom_id']
        ).first() is not None:
            raise CustomAPIError(
                'Предложенный вариант короткой ссылки уже существует.')
    else:
        data['custom_id'] = get_unique_short_id()
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    """Возвращает оригинальный URL по короткому идентификатору."""
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise CustomAPIError('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original}), HTTPStatus.OK
