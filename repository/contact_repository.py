from DB.db import DBConnection


class ContactRepository:

    def __init__(self):
        self.connection = DBConnection().get_connection()

    def save_contact_message(self, contact):
        try:
            cursor = self.connection.cursor()

            sql = """
                INSERT INTO contact_messages
                (name, email,  subject, message)
                VALUES (%s, %s,  %s, %s)
                RETURNING message_id
            """

            cursor.execute(sql, (
                contact.name,
                contact.email,
                contact.subject,
                contact.message
            ))

            message_id = cursor.fetchone()[0]

            self.connection.commit()
            cursor.close()

            return message_id

        except Exception as e:
            print("Contact Repository Error:", e)
            self.connection.rollback()
            return None