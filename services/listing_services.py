from repository.listing_repository import ListingRepository
from models.listing import Listing


listingrepo = ListingRepository()


class ListingService:

    def __init__(self):

        self.repository = ListingRepository()

    # ----------------------------------
    # Add New Listing
    # ----------------------------------

    def get_listing_details_by_id(self, listing_id: int):

        return self.repository.get_listing_details_by_id(listing_id)



    def increase_whatsapp_click(self, listing_id):

        self.repository.increase_whatsapp_click(listing_id)



    def increase_phone_click(self, listing_id):

        self.repository.increase_phone_click(listing_id)

    def create_listing(

        self,

        owner_id,

        property_name,

        property_type,

        area,

        full_address,

        university,

        gender_preference,

        description,

        facilities,

        monthly_rent,

        security_deposit,

        other_charges

):

       listing = Listing(
 
        owner_id=owner_id,

        property_name=property_name,

        property_type=property_type,

        area=area,

        full_address=full_address,

        university=university,

        gender_preference=gender_preference,

        description=description,

        facilities=facilities,

        monthly_rent=monthly_rent,

        security_deposit=security_deposit,

        other_charges=other_charges

    )

       try:

          return listingrepo.add_listing(listing)

       except Exception as e:

         print("Exception Occurred :", e)
         return False
    # ----------------------------------
    # Get All Listings of Owner
    # ----------------------------------

    def get_owner_listings(

            self,

            owner_id

    ):

        try:

            return listingrepo.get_owner_listings(owner_id)

        except Exception as e:

            print("Exception Occurred :", e)

            return []

    # ----------------------------------
    # Get Listing By ID
    # ----------------------------------

    def get_listing(

            self,

            listing_id

    ):

        try:

            return listingrepo.get_listing_by_id(listing_id)

        except Exception as e:

            print("Exception Occurred :", e)

            return None

    # ----------------------------------
    # Update Listing
    # ----------------------------------

    def update_listing(

            self,

            listing_id,

            owner_id,

            property_name,

            property_type,

            area,

            full_address,

            university,

            gender_preference,

            description,

            monthly_rent,

            security_deposit

    ):

        listing = Listing(

            owner_id,

            property_name,

            property_type,

            area,

            full_address,

            university,

            gender_preference,

            description,

            monthly_rent,

            security_deposit,

            listing_id

        )

        try:

            if listingrepo.update_listing(listing):

                return True

            return False

        except Exception as e:

            print("Exception Occurred :", e)

            return False

    # ----------------------------------
    #  Listing
    # ----------------------------------



    def filter_listings(
        self,
        property_type=None,
        area=None,
        university=None,
        gender=None):

     return listingrepo.filter_listings(

        property_type,
        area,
        university,
        gender
    )


    def get_girls_hostels(self,property_type=None,area=None,university=None):
        return listingrepo.filter_listings(property_type,area,university,"Girls Only")


    

    def get_boys_hostels(self,property_type=None,area=None,university=None):
        return listingrepo.filter_listings(property_type,area,university,"Boys Only")

    def get_boys_pg(self,area=None,university=None):
        return listingrepo.filter_listings("pg",area,university,"Boys Only")

    def get_rooms(self,area=None,university=None,gender=None):
        return listingrepo.filter_listings("room",area,university,gender)




    def get_girls_hostels_near_150_feet_ring_road(self,property_type=None,area=None,university=None):

       return listingrepo.filter_listings(property_type,area,university,"Girls Only")

    def get_boys_hostels_near_university_road(self,property_type=None,area=None,university=None):
    
           return listingrepo.filter_listings(property_type,area,university,"Boys Only")


    
    def get_boys_hostels_near_marwadi_university(self,property_type=None,area=None,university=None):
    
           return listingrepo.filter_listings(property_type,area,university,"Boys Only")

    def get_girls_hostels_near_marwadi_university(self,property_type=None,area=None,university=None):
    
           return listingrepo.filter_listings(property_type,area,university,"Girls Only")

    
    def get_girls_pg_near_marwadi_university(self,property_type=None,area=None,university=None):
    
           return listingrepo.filter_listings(property_type,area,university,"Girls Only")

        
    def get_boys_pg_near_marwadi_university(self,property_type=None,area=None,university=None):
    
           return listingrepo.filter_listings(property_type,area,university,"Boys Only")


    def get_boys_hostel_near_atmiya_university(self,property_type=None,area=None,university=None):
    
           return listingrepo.filter_listings(property_type,area,university,"Boys Only")


    def get_boys_pg_near_atmiya_university(self,property_type=None,area=None,university=None):
    
           return listingrepo.filter_listings(property_type,area,university,"Boys Only")


    def get_girls_hostels_near_atmiya_university(self,property_type=None,area=None,university=None):
    
           return listingrepo.filter_listings(property_type,area,university,"Girls Only")

    def get_girls_pg_near_atmiya_university(self,property_type=None,area=None,university=None):
    
           return listingrepo.filter_listings(property_type,area,university,"Girls Only")
    
    
    
    
    
    
        

    



    def get_all_areas(self):

      return listingrepo.get_all_areas()


    def get_all_universities(self):

       return listingrepo.get_all_universities()

    

    

    def get_all_listings(self):

        return listingrepo.get_all_listings()



    def delete_listing(

            self,

            listing_id

    ):

        try:

            if listingrepo.delete_listing(listing_id):

                return True

            return False

        except Exception as e:

            print("Exception Occurred :", e)

            return False