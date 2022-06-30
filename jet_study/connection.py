from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from config import db_username, db_password, \
                    db_name, db_host

engine = create_engine(
    f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}/{db_name}"
    )
Session = sessionmaker(bind=engine)
