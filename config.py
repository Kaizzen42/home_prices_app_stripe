import os

class Config:
    # Basic Flask Settings
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    DEBUG = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False
    
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}