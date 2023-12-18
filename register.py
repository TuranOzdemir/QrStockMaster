from database_service import * 
from register_ui import *


class RegisterLogic:
    def __init__(self, db):
        self.db = db
        self.db_manager = DatabaseManager(db)
    def register(self, user:User):
        user_id = self.db_manager.add_user(user)
        if user_id:
            return True
        else:
            return False
