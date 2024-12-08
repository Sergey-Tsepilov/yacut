from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):  # type: ignore
    """Модель для хранения информации о ссылках."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(2048), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        """Возвращает данные модели в виде словаря."""
        return dict(
            url=self.original,
            short_link=url_for(
                'opinion_view', short=self.short, _external=True),
        )

    def from_dict(self, data):
        """Заполняет данные модели из словаря."""
        self.original = data['url']
        self.short = data['custom_id']
