from flask import render_template, Blueprint, jsonify, request, session
from mind_reading_machine.mind_reader import MindReader

# ---------------------------------------------------------------------------
# Define Blueprint.
# ---------------------------------------------------------------------------
mod = Blueprint('main', __name__, template_folder='../templates/main_module')

# ---------------------------------------------------------------------------
# Page views.
# ---------------------------------------------------------------------------


@mod.route('/')
def index():
    return render_template("main_module/index.html")


@mod.route('/game-over', methods=['POST'])
def game_over():
    session['penny_bot'] = MindReader()
    return "", 200


@mod.route('/take-turn', methods=['GET'])
def take_turn():
    action = int('39' == request.args.get('action'))
    bot = session.get('penny_bot', False)
    if not bot:
        bot = session['penny_bot'] = MindReader()
    prev_computer_score = bot.computer_score
    print prev_computer_score
    print action
    bot.take_turn(action)
    print bot.computer_score
    result = {'computer_score': bot.computer_score,
              'player_score': bot.player_score,
              'won': prev_computer_score < bot.computer_score}
    print result
    return jsonify(**result)
