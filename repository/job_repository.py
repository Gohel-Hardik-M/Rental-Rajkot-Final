from DB.db import DBConnection


class JobRepository:

    def __init__(self):

        self.connection = DBConnection().get_connection()

    # ==========================================
    # GET ALL JOB CATEGORIES
    # ==========================================

    def get_all_categories(self):

        print("===== JOB CATEGORY REPO =====")

        try:

            cursor = self.connection.cursor()

            sql = """
            SELECT
                category_id,
                category_name
            FROM job_categories
            ORDER BY category_id
            """

            cursor.execute(sql)

            categories = cursor.fetchall()

            cursor.close()

            return categories

        except Exception as e:

            print("Exception Occurred :", e)

            return []

    # ==========================================
    # CREATE JOB
    # ==========================================

    def create_job(self, job):

        print("===== JOB REPO =====")

        try:

            cursor = self.connection.cursor()

            sql = """
            INSERT INTO jobs
            (
                category_id,
                company_name,
                title,
                area,
                experience_min,
                experience_max,
                salary_min,
                description,
                skills,
                apply_link,
                is_featured
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
            RETURNING job_id
            """

            cursor.execute(
                sql,
                (
                    job.category_id,
                    job.company_name,
                    job.title,
                    job.area,
                    job.experience_min,
                    job.experience_max,
                    job.salary_min,
                    job.description,
                    job.skills,
                    job.apply_link,
                    job.is_featured
                )
            )

            job_id = cursor.fetchone()[0]

            self.connection.commit()

            cursor.close()

            return job_id

        except Exception as e:

            print("Exception Occurred :", e)

            self.connection.rollback()

            return None