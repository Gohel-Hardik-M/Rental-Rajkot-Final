from DB.db import DBConnection

from models.view_listing_model import ViewListing


class AdminRepository:


    
    def __init__(self):

        self.connection = DBConnection().get_connection()


    def delete_listing(self, listing_id):


        cursor = self.connection.cursor()

        sql = """
            DELETE FROM listings
            WHERE listing_id = %s
        """

        cursor.execute(sql, (listing_id,))
        self.connection.commit()

        cursor.close()

        return True


    

    def get_all_listings(self):

       cursor = self.connection.cursor()

       sql = """
      SELECT
    l.listing_id,
    l.owner_id,
    u.phone,
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
INNER JOIN users u
ON l.owner_id = u.user_id

ORDER BY l.created_at DESC;
    """

       cursor.execute(sql)

       rows = cursor.fetchall()

       listings = []

       for row in rows:
        print(row)
        print(len(row))

       for row in rows:

        listing = ViewListing(
    
 listing_id=row[0],
    owner_id=row[1],
    owner_phone=row[2],

    property_name=row[3],
    property_type=row[4],
    area=row[5],
    full_address=row[6],
    university=row[7],
    gender_preference=row[8],
    description=row[9],
    facilities=row[10],
    monthly_rent=row[11],
    security_deposit=row[12],
    other_charges=row[13]
    
        )

        listings.append(listing)

       cursor.close()

       return listings

    def get_dashboard_counts(self):

        cursor = self.connection.cursor()

        sql = """
        SELECT

            (SELECT COUNT(*)
             FROM users
             WHERE user_type = 'OWNER') AS total_owners,

            (SELECT COUNT(*)
             FROM listings
             WHERE property_type = 'hostel') AS total_hostels,

            (SELECT COUNT(*)
             FROM listings
             WHERE property_type = 'room') AS total_rooms;
        """

        cursor.execute(sql)

        row = cursor.fetchone()

        cursor.close()

        return {
            "owners": row[0],
            "hostels": row[1],
            "rooms": row[2]
        }