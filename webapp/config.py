import os


class BaseConfig:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Application threads. A common general assumption is using 2 per available
    # processor cores.
    THREADS_PER_PAGE = 8

    # Admins
    ADMINS = frozenset(['me@jhh3.net'])

    # Session
    SESSION_TYPE = 'filesystem'


class DevelopmentConfig(BaseConfig):
    NAME = "dev"

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    # Use a secure, unique and absolutely secret key for signing the data.
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "supersecret"


class AWSProductionConfig(BaseConfig):
    NAME = "prod"

    # CSRF
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = os.environ.get('CSRF_SESSION_KEY')

    # Secret key for signing cookies
    SECRET_KEY = os.environ.get('SECRET_KEY')
