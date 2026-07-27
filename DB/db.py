import psycopg

import os
from dotenv import load_dotenv
load_dotenv()


class DBConnection:

    __instance = None

    def __new__(cls):

        if cls.__instance is None:

            cls.__instance = super(DBConnection, cls).__new__(cls)

            cls.__instance.connection = psycopg.connect(
             os.getenv("DB")

            )

            print("✅ PostgreSQL Connected Successfully")

        return cls.__instance

    def get_connection(self):
        print("===== DB =====")

        return self.connection

    def get_cursor(self):

        return self.connection.cursor()

    def commit(self):

        self.connection.commit()

    def rollback(self):

        self.connection.rollback()

    def close(self):

        if self.connection:
            self.connection.close()