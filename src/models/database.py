from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('sqlite:///yourdatabase.db')
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def add_user(username, email, password, is_admin=False):
    with Session() as session:
        new_user = User(username=username, email=email, password=password, is_admin=is_admin)
        session.add(new_user)
        session.commit()
        
def get_user_by_username(username):
    with Session() as session:
        user = session.query(User).filter_by(username=username).first()
        return user