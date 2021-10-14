import app.config as app_config


def hello():
    app_config.MAIN_TABLE_ID = 3
    print("hello")
