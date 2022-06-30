from connection import Session  
from models import User

class Commands:
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, user_id, username):
        new_user = User(id=user_id, name=username)
        self.session.add(new_user)
    
    def user_exists(self, user_id):
        if self.session.query(User).get(user_id):
            return True
        return False

    def commit(self):
        self.session.commit()
    

