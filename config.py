import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "477fcd746521ea30f2940d8c0934bc950dd89b9f88f9b37300233fc7352b4637fc0dff5f6f3070904279e5a9fa963075b11a88825d66fc3e978de5b00123d2a3",
    )
    REDIS_USERNAME = os.getenv("REDIS_USERNAME", "")
    REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")
    REDIS_PORT = os.getenv("REDIS_PORT", "6379")
    REDIS_CONN = "redis://{}:{}@{}:{}".format(
        REDIS_USERNAME, REDIS_PASSWORD, REDIS_HOST, REDIS_PORT
    )


class Production(Config):
    DEBUG = False


class Staging(Config):
    DEVELOPMENT = True
    DEBUG = True


class Development(Config):
    DEVELOPMENT = True
    DEBUG = True


class Test(Config):
    TESTING = True


config_map = {
    "TEST": Test,
    "DEVELOPMENT": Development,
    "STAGING": Staging,
    "PRODUCTION": Production,
}


def current_config(env=None):
    if env:
        return config_map[env]
    else:
        return config_map[os.getenv("ENVIRONMENT", "DEVELOPMENT").upper()]
