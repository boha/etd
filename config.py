import os
import ConfigParser

DIRNAME = os.path.abspath(os.path.dirname(__file__))

config = ConfigParser.ConfigParser()
config.read(os.path.join('etd.ini'))


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "asd252rg242tqwf5y6h4wefefa"


# dev
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "%s://%s:%s@%s/earntheday" % (
        config.get('development', 'db_engine'),
        config.get('development', 'db_username'),
        config.get('development', 'db_password'),
        config.get('development', 'db_host')
    )


# prod
class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "%s://%s:%s@%s/earntheday" % (
        config.get('production', 'db_engine'),
        config.get('production', 'db_username'),
        config.get('production', 'db_password'),
        config.get('production', 'db_host')
    )

settings = DevelopmentConfig