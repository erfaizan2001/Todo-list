host = "localhost"
username="root"
password = "root"



class Config:
    SQLALCHEMY_DATABASE_URI = f'mysql://{username}:{password}@{host}/todo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
