from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Определение моделей
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.login}>'

class MsgType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'<MsgType {self.type}>'

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    msg_type_id = db.Column(db.Integer, db.ForeignKey('msg_type.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    user = db.relationship('User', backref=db.backref('messages', lazy=True))
    msg_type = db.relationship('MsgType', backref=db.backref('messages', lazy=True))

    def __repr__(self):
        return f'<Message {self.text[:20]}>'

# Функция инициализации базы данных с начальными данными
def init_db():
    db.create_all()

    if not User.query.first():
        # Добавление начальных данных в таблицу users
        users = [
            User(login='admin', password='pass'),
            User(login='user', password='pass'),
            User(login='guest', password='pass')
        ]
        db.session.bulk_save_objects(users)

        # Добавление начальных данных в таблицу msg_types
        msg_types = [
            MsgType(type='proverb', description='тут будет комментарий'),
            MsgType(type='wise', description='тут будет комментарий'),
            MsgType(type='joke', description='тут будет комментарий')
        ]
        db.session.bulk_save_objects(msg_types)

        # Добавление начальных данных в таблицу messages
        admin = User.query.filter_by(login='admin').first()
        msg_type_joke = MsgType.query.filter_by(type='joke').first()
        msg_type_proverb = MsgType.query.filter_by(type='proverb').first()
        msg_type_wise = MsgType.query.filter_by(type='wise').first()

        messages = [
            # Шутки
            Message(text='Что сказал слепой, войдя в бар? Всем привет, кого не видел!', user_id=admin.id, msg_type_id=msg_type_joke.id),
            Message(text='Папа Карло приделал Буратино колесо вместо одной ноги и пошло–поехало…', user_id=admin.id, msg_type_id=msg_type_joke.id),
            Message(text='Хороший каменщик кладет на совесть.', user_id=admin.id, msg_type_id=msg_type_joke.id),
            Message(text='Во время ссоры жена внезапно применила слезоточивый глаз', user_id=admin.id, msg_type_id=msg_type_joke.id),
            Message(text='Как называют черепашку когда она вырастает? Черепавел', user_id=admin.id, msg_type_id=msg_type_joke.id),
            Message(text='Дети анестезиолога засыпают ровно в 22:00', user_id=admin.id, msg_type_id=msg_type_joke.id),

            # Пословицы
            Message(text='Не плюй в колодец, пригодится воды напиться', user_id=admin.id, msg_type_id=msg_type_proverb.id),
            Message(text='Под лежачий камень и вода не течет', user_id=admin.id, msg_type_id=msg_type_proverb.id),
            Message(text='Дело не сдвинется с места, если ничего не предпринимать', user_id=admin.id, msg_type_id=msg_type_proverb.id),
            Message(text='Был бы лес, соловьи прилетят', user_id=admin.id, msg_type_id=msg_type_proverb.id),
            Message(text='Не беречь поросли, не видать и дерева', user_id=admin.id, msg_type_id=msg_type_proverb.id),

            # Мудрости
            Message(text='За что борются - того добиваются', user_id=admin.id, msg_type_id=msg_type_wise.id),
            Message(text='Восток ли, запад ли, а дома лучше', user_id=admin.id, msg_type_id=msg_type_wise.id),
            Message(text='Кто много начинает, очень мало осуществляет', user_id=admin.id, msg_type_id=msg_type_wise.id),
            Message(text='Совершенный поступок в советах не нуждается', user_id=admin.id, msg_type_id=msg_type_wise.id),
            Message(text='В беде сотня друзей весит очень мало', user_id=admin.id, msg_type_id=msg_type_wise.id)
        ]
        db.session.bulk_save_objects(messages)
        db.session.commit()

# Инициализация базы данных при запуске приложения
with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True)
