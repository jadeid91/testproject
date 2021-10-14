import config as app_config

# if I import config, it will take me to labor.config
# import config


def hello():
    print(app_config.MAIN_TABLE_ID)
