from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser

# create an engine
config = configparser.ConfigParser()
config.read('config.ini')
host_name = config['POSTGRES']['postgres_db_server']
port = int(config['POSTGRES']['postgres_db_port'])
db_name = config['POSTGRES']['postgres_db_name']
username = config['POSTGRES']['postgres_db_user']
password = config['POSTGRES']['postgres_db_password']

url = 'postgresql://{}:{}@{}:{}/{}'.format(username, password, host_name, port, db_name)

engine = create_engine(url)
if not engine.dialect.has_table(engine, 'services'):
    metadata = MetaData()
    services = Table('services', metadata,
        Column('id', Integer, Sequence('servicesid_seq'),metadata, primary_key=True),
        Column('service_name', String(60), nullable=False)
    )
    services.create(engine)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

Base = declarative_base()