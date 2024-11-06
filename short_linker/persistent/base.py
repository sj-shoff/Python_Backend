from sqlalchemy import  MetaData
from sqlalchemy.orm import declarative_base

Base = declarative_base()
Base.metadata = MetaData(schema = "public")
