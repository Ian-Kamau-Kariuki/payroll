class Config:


    SECRET_KEY='56509b5ec2cf56fa6c7c71d54cdd698c'

# inherit properties of class config
class Development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@127.0.0.1:5432/june_payroll_system'
    DEBUG =True


class Production(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI ='postgres://usptufuhuictjb:5f38304e99d83d22d6fc01ea580ae340ebac82bc681413a80fd52680a2a68dc5@ec2-174-129-29-101.compute-1.amazonaws.com:5432/ddneuur53ilu9d'
    DEBUG = False