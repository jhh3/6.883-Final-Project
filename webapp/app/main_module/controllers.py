from flask import render_template, Blueprint, jsonify, request, session
from mind_reading_machine.mind_reader import MindReader
from seer.seer import SEER
from experts.experts import ExpertsCombo

# ---------------------------------------------------------------------------
# Define Blueprint.
# ---------------------------------------------------------------------------
mod = Blueprint('main', __name__, template_folder='../templates/main_module')

# ---------------------------------------------------------------------------
# Page views.
# ---------------------------------------------------------------------------


def reset_bot():
    bot = session.get('bot', 'Shannon')
    if bot == 'Shannon':
        session['penny_bot'] = MindReader()
    elif bot == 'Hagelbarger':
        session['penny_bot'] = SEER()
    elif bot == 'Expert':
        session['penny_bot'] = ExpertsCombo([MindReader(), SEER()])


# ---------------------------------------------------------------------------
# Page views.
# ---------------------------------------------------------------------------


@mod.route('/')
def index():
    return render_template("main_module/index.html")


@mod.route('/play')
def play_game():
    return render_template("main_module/play.html")


@mod.route('/game-over', methods=['POST'])
def game_over():
    reset_bot()
    return "", 200


@mod.route('/change-bot', methods=['POST'])
def change_bot():
    session['bot'] = request.form.get('bot', 'Shannon')
    reset_bot()
    return "", 200


@mod.route('/take-turn', methods=['GET'])
def take_turn():
    # Map right arrow key (39) to a 1
    action = int('39' == request.args.get('action'))
    # Get bot
    bot = session.get('penny_bot', False)
    if not bot:
        bot = session['penny_bot'] = MindReader()
    prev_computer_score = bot.computer_score
    bot.take_turn(action)
    result = {'computer_score': bot.computer_score,
              'player_score': bot.player_score,
              'won': prev_computer_score < bot.computer_score}
    return jsonify(**result)
