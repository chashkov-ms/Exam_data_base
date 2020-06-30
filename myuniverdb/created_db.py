from sqlalchemy import create_engine
from models import Base

DB_NAME = r'univer_network.db'

engine = create_engine(r'sqlite:///%s'% DB_NAME, echo=False)

Base.metadata.create_all(engine)
