from flask import render_template, Blueprint

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
