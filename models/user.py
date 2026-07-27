class User:

    def __init__(
        self,
        full_name,
        email,
        phone,
        password,
        user_type
    ):

        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.password = password
        self.user_type = user_type