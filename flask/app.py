from flask import Flask, render_template, redirect, url_for
from models import db, Move, Game
from forms import ResultForm
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///results.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  

db.init_app(app)


with app.app_context():
    db.create_all()

def check_winner(game_id):
    moves = Move.query.filter_by(game_id=game_id).all()
    board = [''] * 9
    for move in moves:
        board[move.position - 1] = move.player
    
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != '':
            return board[combo[0]]  # Победитель: 'X' или 'O'
    
    if '' not in board:
        return 'draw'  # Ничья
    
    return None  # Игра продолжается

@app.route('/')
def index():
    games = Game.query.all()
    return render_template('index.html', games=games)

@app.route('/new_game')
def new_game():
    game = Game()
    db.session.add(game)
    db.session.commit()
    return redirect(url_for('game', game_id=game.id))

@app.route('/game/<int:game_id>')
def game(game_id):
    game = Game.query.get_or_404(game_id)
    moves = {move.position: move.player for move in game.moves}
    return render_template('game.html', game=game, moves=moves)

@app.route('/make_move/<int:game_id>', methods=['POST'])
def make_move(game_id):
    game = Game.query.get_or_404(game_id)
    if game.status != 'in_progress':
        return redirect(url_for('game', game_id=game_id))
    
    position = int(request.form['position'])
    player = request.form['player']
    
    move = Move(game_id=game_id, player=player, position=position)
    db.session.add(move)
    db.session.commit()
    
    winner = check_winner(game_id)
    if winner:
        game.status = 'won' if winner != 'draw' else 'draw'
        game.winner = winner if winner != 'draw' else None
        db.session.commit()
    
    return redirect(url_for('game', game_id=game_id))

if __name__ == '__main__':
    app.run(debug=True)
