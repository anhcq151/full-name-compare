import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '3d180d1f57dbb4411248d186e81627c707ae0d614f7dccbd'