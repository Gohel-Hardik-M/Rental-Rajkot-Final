class Job:

    def __init__(
        self,
        job_id,
        category_id,
        category_name,
        company_name,
        title,
        area,
        experience_min,
        experience_max,
        salary_min,
        description,
        skills,
        posted_date,
        apply_link,
        status,
        is_featured,
        created_at,
        updated_at
    ):

        self.job_id = job_id
        self.category_id = category_id
        self.category_name = category_name

        self.company_name = company_name
        self.title = title
        self.area = area

        self.experience_min = experience_min
        self.experience_max = experience_max

        self.salary_min = salary_min

        self.description = description
        self.skills = skills

        self.posted_date = posted_date
        self.apply_link = apply_link

        self.status = status
        self.is_featured = is_featured

        self.created_at = created_at
        self.updated_at = updated_at