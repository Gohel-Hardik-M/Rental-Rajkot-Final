class Job:

    def __init__(
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

        self.category_id = category_id
        self.company_name = company_name
        self.title = title
        self.area = area
        self.experience_min = experience_min
        self.experience_max = experience_max
        self.salary_min = salary_min
        self.description = description
        self.skills = skills
        self.apply_link = apply_link
        self.is_featured = is_featured