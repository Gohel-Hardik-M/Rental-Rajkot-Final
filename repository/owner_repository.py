from DB.db import DBConnection

from models.listing import Listing


class OwnerRepositoy:


    
    def __init__(self):

        self.connection = DBConnection().get_connection()


    def get_hostels_count(self,owner_id):
       cursor = self.connection.cursor()

       cursor.execute("""SELECT COUNT(*) 
                         FROM listings
                         WHERE property_type = 'hostel' AND owner_id = %s;""",(owner_id,))
       hostels = cursor.fetchone()
       return hostels

    def get_listing_id_by_property_name(self, property_name):
         print("----->>>> get_listing_id_by_property_name --->> Called......")
         cursor = self.connection.cursor()
         sql = """
        SELECT listing_id
FROM listings
WHERE property_name LIKE %s
LIMIT 1;

    """

         cursor.execute(sql, (f"%{property_name}%",))
         row = cursor.fetchone()

         cursor.close()

         if row:
           return row[0]   # listing_id
         else:
            print("No listing found for property_name:", property_name)
            return None



    def delete_listing(self, listing_name):

        listing_id = self.get_listing_id_by_property_name(listing_name)


        cursor = self.connection.cursor()

        sql = """
            DELETE FROM listings
            WHERE listing_id = %s
        """

        cursor.execute(sql, (listing_id,))
        self.connection.commit()

        cursor.close()

        return True


    

    def get_owner_listings(self,owner_id):
       print("----->>>> get_owner_listings --->> Called......")

       cursor = self.connection.cursor()

       sql = """
      SELECT
    l.owner_id,
    l.property_name,
    l.property_type,
    l.area,
    l.full_address,
    l.nearest_college,
    l.gender_preference,
    l.description,
    l.facilities,
    l.monthly_rent,
    l.security_deposit,
    l.other_charges

FROM listings l
WHERE owner_id = %s
ORDER BY l.created_at DESC;
    """

       cursor.execute(sql,(owner_id,))

       rows = cursor.fetchall()

       listings = []

       for row in rows:

        listing = Listing(
    owner_id=row[0],
    property_name=row[1],
    property_type=row[2],
    area=row[3],
    full_address=row[4],
    university=row[5],
    gender_preference=row[6],
    description=row[7],
    facilities=row[8],
    monthly_rent=row[9],
    security_deposit=row[10],
    other_charges=row[11]
    
        )

        listings.append(listing)
        print("listings.append(listing) --->> Done")

       cursor.close()


       if(listings):
          print("Listing is Added")
       else:
          print("-------Listing EMPTY----")

       return listings
