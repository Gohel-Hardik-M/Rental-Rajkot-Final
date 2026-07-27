from  repository.user_repository import UserRepository
from models.user import User

userrepo = UserRepository()

class UserService:

    def __init__(self):

        self.repository = UserRepository()

    def register_owner(self,    full_name,    email,    phone,    password,    confirm_password):
        if password != confirm_password:
            return False

        user = User(    full_name,    email,    phone,    password,    "OWNER" )

        try:
           if(userrepo.register_user(user)):
               return True
           else:
               return False
        except Exception as e:
           print("Execption occured ",e)

        return True
    



        # Login
    def login(

            self,

            email,

            password

    ):

        user = userrepo.get_user_by_email(email)

        if user is None:

            return False, "Email not registered.", None

        if user.password != password:

            return False, "Incorrect Password.", None

        return True, "Login Successful.", user