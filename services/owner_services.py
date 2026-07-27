from repository.owner_repository import OwnerRepositoy
owner_repo = OwnerRepositoy()


class OwnerService:

    def get_no_hostels(self, owner_id):
        return owner_repo.get_hostels_count(owner_id)
    

    def delete_listing(self, listing_name):

        return owner_repo.delete_listing(listing_name)


    def get_owner_properties(self,owner_id):
        print("Onwer Service --->> entered")
        return owner_repo.get_owner_listings(owner_id)


