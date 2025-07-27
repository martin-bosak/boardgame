from flask import Flask, render_template
from game.game import Game

app = Flask(__name__)

# Create a game instance
game = Game()
game.add_player("Player 1")
game.add_player("Player 2")
game.start_game()

@app.route('/')
def index():
    return render_template('index.html', game=game)

if __name__ == '__main__':
    app.run(debug=True) 