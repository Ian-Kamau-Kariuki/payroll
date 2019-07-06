class Config:


    SECRET_KEY='56509b5ec2cf56fa6c7c71d54cdd698c'

# inherit properties of class config
class Development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@127.0.0.1:5432/june_payroll_system'
    DEBUG =True


class Production(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgres://qglepwvjxcrxzr:9b860f71b592ab4c40fd61473eac46794382b29b3239355331cd75af8ac2eca4@ec2-23-21-160-38.compute-1.amazonaws.com:5432/d3av0ii8aftl43'
    DEBUG = False