import os
from flask import Flask, render_template
from flask.ext.session import Session

# ---------------------------------------------------------------------------
# Define the WSGI application object.
# ---------------------------------------------------------------------------
app = Flask(__name__)
sess = Session()

# ---------------------------------------------------------------------------
# Configuration.
# ---------------------------------------------------------------------------
if os.environ.get('AWS_ENV') == 'prod':
    app.config.from_object('config.AWSProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

sess.init_app(app)

# ---------------------------------------------------------------------------
# Enable logging in production.
# ---------------------------------------------------------------------------
if os.environ.get('AWS_ENV') == 'prod':
    import logging
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler('jhh3.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    file_handler.setLevel(logging.DEBUG)
    format_str = "%(asctime)s - %(levelname)s: (%(filename)s:%(lineno)s) %(message)s "
    file_formatter = logging.Formatter(format_str)
    file_handler.setFormatter(file_formatter)

    app.logger.addHandler(file_handler)

# ---------------------------------------------------------------------------
# Import the modules using the blueprint handler variables and register
# blueprints.
# ---------------------------------------------------------------------------
from app.main_module.controllers import mod as main_mod

app.register_blueprint(main_mod)

# ---------------------------------------------------------------------------
# HTTP error handling
# ---------------------------------------------------------------------------


@app.errorhandler(404)
def not_found(error):
    app.logger.warning(error)
    return render_template('error_module/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    app.logger.exception(error)
    return render_template('error_module/500.html'), 500
