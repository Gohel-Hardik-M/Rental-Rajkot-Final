from DB.db import DBConnection
from models.user import User

class UserRepository:

    def __init__(self):
        self.connection = DBConnection().get_connection()

    def register_user(self, user):

        print("===== REPO =====")


        try:
            cursor = self.connection.cursor()

            sql = """
            INSERT INTO users
            (
                full_name,
                email,
                phone,
                password,
                user_type
            )
            VALUES
            (%s,%s,%s,%s,%s)
            """

            cursor.execute(
                sql,
                (
                    user.full_name,
                    user.email,
                    user.phone,
                    user.password,
                    user.user_type
                )
            )

            self.connection.commit()
            cursor.close()
            return True

        except Exception as e:
            return False
            print(e)

    


     # Login
    def get_user_by_email(self, email):

        cursor = self.connection.cursor()

        cursor.execute(

            "SELECT * FROM get_user_by_email(%s)",

            (email,)

        )

        row = cursor.fetchone()

        cursor.close()

        if row is None:

            return None

        user = User(

            row[1],
            row[2],
            row[3],
            row[4],
            row[5]

        )

        user.id = row[0]

        return user