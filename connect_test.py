import sqlalchemy as db

# specify database configurations
config = {
    'host': 'localhost',
    'port': 8081,
    'user': 'admin',
    'password': 'admin',
    'database': 'mydatabasename'
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

# specify connection string
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# connect to database
try:
    engine = db.create_engine(connection_str)
    connection = engine.connect()
except Exception as e:
    print(e.__cause__)
else:
    print("Connected successfully to the database engine container !")




