from flask import flash, redirect, render_template

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import check_short, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Обрабатывает главную страницу: создание короткой ссылки."""
    form = URLForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if custom_id:
            if URLMap.query.filter_by(short=custom_id).first():
                flash('Предложенный вариант короткой ссылки уже существует.')
                return render_template('main.html', form=form)
            elif not check_short(custom_id):
                flash('Указано недопустимое имя для короткой ссылки')
                return render_template('main.html', form=form)
        else:
            custom_id = get_unique_short_id()
        url = URLMap(original=form.original_link.data, short=custom_id)
        db.session.add(url)
        db.session.commit()
        return render_template('main.html', form=form, url=url)
    return render_template('main.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def opinion_view(short):
    """Перенаправляет пользователя на оригинальный URL по короткой ссылке."""
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)
