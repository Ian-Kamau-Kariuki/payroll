class Config:


    SECRET_KEY='56509b5ec2cf56fa6c7c71d54cdd698c'

# inherit properties of class config
class Development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@127.0.0.1:5432/june_payroll_system'
    DEBUG =True


class Production(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@127.0.0.1:5432/june_payroll_system'
    DEBUG = False