from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

#SQL engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

#SQL session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base for models
Base = declarative_base()

