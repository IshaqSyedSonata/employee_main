import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = 'mysql+pymysql://root:@localhost/test'

my_sql_engine = create_engine(database_url)


local_session  = sessionmaker(autocommit=False, autoflush=False, bind=my_sql_engine)
Base = declarative_base()