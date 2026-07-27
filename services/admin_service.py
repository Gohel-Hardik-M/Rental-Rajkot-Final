from repository.admin_repository import AdminRepository
admin_repo = AdminRepository()


class AdminService:

    def delete_listing(self, listing_id):

        return admin_repo.delete_listing(listing_id)

    def get_dashboard_counts(self):

        return admin_repo.get_dashboard_counts()

    def get_all_properties(self):
        return admin_repo.get_all_listings()


