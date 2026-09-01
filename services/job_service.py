from repository.job_repository import JobRepository
from models.job import Job


jobrepo = JobRepository()


class JobService:

    def __init__(self):

        self.repository = JobRepository()

    # ==========================================
    # GET ALL JOB CATEGORIES
    # ==========================================

    def get_all_categories(self):

        try:

            return self.repository.get_all_categories()

        except Exception as e:

            print("Exception Occurred :", e)

            return []

    # ==========================================
    # CREATE JOB
    # ==========================================

    def create_job(
        self,
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
    ):

        job = Job(

            category_id=category_id,

            company_name=company_name,

            title=title,

            area=area,

            experience_min=experience_min,

            experience_max=experience_max,

            salary_min=salary_min,

            description=description,

            skills=skills,

            apply_link=apply_link,

            is_featured=is_featured

        )

        try:

            return self.repository.create_job(job)

        except Exception as e:

            print("Exception Occurred :", e)

            return None