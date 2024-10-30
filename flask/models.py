from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
    __tablename__ = 'games'
    
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10), nullable=False, default='in_progress')  # Возможные значения: 'in_progress', 'won', 'draw'
    winner = db.Column(db.String(1), nullable=True)  # 'X', 'O' или None
    moves = db.relationship('Move', backref='game', lazy=True)  # Все ходы игры


class Move(db.Model):
    __tablename__ = 'moves'
    
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    player = db.Column(db.String(1), nullable=False)  # 'X' или 'O'
    position = db.Column(db.Integer, nullable=False)  # Позиция от 1 до 9