from DB.db import DBConnection
from models.listing_job import Job


class JobRepository:

    def __init__(self):

        self.connection = DBConnection().get_connection()


    def get_all_jobs(self):

        print("===== JOB REPO : GET ALL JOBS =====")

        try:

            cursor = self.connection.cursor()

            sql = """
            SELECT
                j.job_id,
                j.category_id,
                jc.category_name,
                j.company_name,
                j.title,
                j.area,
                j.experience_min,
                j.experience_max,
                j.salary_min,
                j.description,
                j.skills,
                j.posted_date,
                j.apply_link,
                j.status,
                j.is_featured,
                j.created_at,
                j.updated_at

            FROM jobs j

            JOIN job_categories jc
                ON j.category_id = jc.category_id

            WHERE j.status = 'ACTIVE'

            ORDER BY
                j.is_featured DESC,
                j.posted_date DESC,
                j.job_id DESC
            """

            cursor.execute(sql)

            rows = cursor.fetchall()

            cursor.close()

            jobs = []

            for row in rows:

                job = Job(
                    job_id=row[0],
                    category_id=row[1],
                    category_name=row[2],
                    company_name=row[3],
                    title=row[4],
                    area=row[5],
                    experience_min=row[6],
                    experience_max=row[7],
                    salary_min=row[8],
                    description=row[9],
                    skills=row[10],
                    posted_date=row[11],
                    apply_link=row[12],
                    status=row[13],
                    is_featured=row[14],
                    created_at=row[15],
                    updated_at=row[16]
                )

                jobs.append(job)

            return jobs

        except Exception as e:

            print("Exception Occurred :", e)

            return []


    def get_job_by_id(self, job_id):

        print("===== JOB REPO : GET JOB BY ID =====")

        try:

            cursor = self.connection.cursor()

            sql = """
            SELECT
                j.job_id,
                j.category_id,
                jc.category_name,
                j.company_name,
                j.title,
                j.area,
                j.experience_min,
                j.experience_max,
                j.salary_min,
                j.description,
                j.skills,
                j.posted_date,
                j.apply_link,
                j.status,
                j.is_featured,
                j.created_at,
                j.updated_at

            FROM jobs j

            JOIN job_categories jc
                ON j.category_id = jc.category_id

            WHERE
                j.job_id = %s
                AND j.status = 'ACTIVE'
            """

            cursor.execute(sql, (job_id,))

            row = cursor.fetchone()

            cursor.close()

            if row is None:
                return None

            job = Job(
                job_id=row[0],
                category_id=row[1],
                category_name=row[2],
                company_name=row[3],
                title=row[4],
                area=row[5],
                experience_min=row[6],
                experience_max=row[7],
                salary_min=row[8],
                description=row[9],
                skills=row[10],
                posted_date=row[11],
                apply_link=row[12],
                status=row[13],
                is_featured=row[14],
                created_at=row[15],
                updated_at=row[16]
            )

            return job

        except Exception as e:

            print("Exception Occurred :", e)

            return None

    def add_category(self, category_name):

           print("===== ADD CATEGORY REPO =====")

           try:

                   cursor = self.connection.cursor()

                   sql = """
        INSERT INTO job_categories
        (
            category_name
        )
        VALUES
        (
            %s
        )
        RETURNING category_id
        """

                   cursor.execute(
                               sql,
                        (
                                category_name,
                                     )
                               )

                   category_id = cursor.fetchone()[0]

                   self.connection.commit()

                   cursor.close()

                   return category_id

           except Exception as e:

                     print("Exception Occurred :", e)

                     self.connection.rollback()
 
                     return None

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