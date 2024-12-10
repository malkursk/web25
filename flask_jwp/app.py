from flask import Flask, g, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from functools import wraps
import jwt
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Должно быть строкой

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
        ]
        db.session.bulk_save_objects(users)

        # Добавление начальных данных в таблицу msg_types
        msg_types = [
            MsgType(type='proverb', description='пословицы'),
            MsgType(type='wise', description='мудрые фразы'),
            MsgType(type='joke', description='юмор')
        ]
        db.session.bulk_save_objects(msg_types)

        # Добавление начальных данных в таблицу messages
        admin = User.query.filter_by(login='admin').first()
        user = User.query.filter_by(login='user').first()
        msg_type_joke = MsgType.query.filter_by(type='joke').first()
        msg_type_proverb = MsgType.query.filter_by(type='proverb').first()
        msg_type_wise = MsgType.query.filter_by(type='wise').first()

        messages = [
            # Шутки
            Message(text='Что сказал слепой, войдя в бар? Всем привет, кого не видел!', user_id=admin.id, msg_type_id=msg_type_joke.id),
            Message(text='Папа Карло приделал Буратино колесо вместо одной ноги и пошло–поехало…', user_id=user.id, msg_type_id=msg_type_joke.id),
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


# Декоратор для проверки токена доступа
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization').split()[1]
        if not token:
            return jsonify({'error': 'Token is missing'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            g.user_id = data['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 403

        return f(*args, **kwargs)

    return decorated

# Маршрут для входа и получения токена
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    login = data.get('login')
    password = data.get('password')

    if not login or not password:
        return jsonify({'error': 'Missing login or password'}), 400

    user = User.query.filter_by(login=login, password=password).first()

    if user:
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.now() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm='HS256')

        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Маршрут для создания нового сообщения (с токеном)
@app.route('/messages', methods=['POST'])
@token_required
def create_message():
    data = request.json
    text = data.get('text')
    msg_type_id = data.get('msg_type_id')

    if not text or not msg_type_id:
        return jsonify({'error': 'Missing required fields'}), 400

    message = Message(text=text, user_id=g.user_id, msg_type_id=msg_type_id)
    db.session.add(message)
    db.session.commit()
    return jsonify({'message': 'Message created successfully'}), 201

# Маршрут для редактирования сообщения (с токеном)
@app.route('/messages/<int:message_id>', methods=['PUT'])
@token_required
def edit_message(message_id):
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({'error': 'Missing text field'}), 400

    message = Message.query.filter_by(id=message_id, user_id=g.user_id).first()
    if not message:
        return jsonify({'error': 'Message not found or not authorized'}), 404

    message.text = text
    db.session.commit()
    return jsonify({'message': 'Message updated successfully'}), 200

# Маршрут для удаления сообщения (с токеном)
@app.route('/messages/<int:message_id>', methods=['DELETE'])
@token_required
def delete_message(message_id):
    message = Message.query.filter_by(id=message_id, user_id=g.user_id).first()
    if not message:
        return jsonify({'error': 'Message not found or not authorized'}), 404

    db.session.delete(message)
    db.session.commit()
    return jsonify({'message': 'Message deleted successfully'}), 200

# Маршрут для получения случайного сообщения (без токена)
@app.route('/messages/random', methods=['GET'])
def get_random_message():
    message = Message.query.order_by(func.random()).first()
    if message:
        return jsonify({
            'id': message.id,
            'text': message.text,
            'user_id': message.user_id,
            'msg_type_id': message.msg_type_id,
            'created_at': message.created_at
        }), 200
    else:
        return jsonify({'error': 'No messages found'}), 404
    

if __name__ == '__main__':
    app.run(debug=True)
