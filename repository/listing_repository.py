from DB.db import DBConnection
from models.listing import Listing
from models.view_listing_model import ViewListing


class ListingRepository:

    def __init__(self):

        self.connection = DBConnection().get_connection()

    # -----------------------------
    # Add New Listing
    # -----------------------------
    def add_listing(self, listing):

        cursor = self.connection.cursor()

        sql = """

INSERT INTO listings
(
    owner_id,
    property_name,
    property_type,
    area,
    full_address,
    nearest_college,
    gender_preference,
    description,
    facilities,
    monthly_rent,
    security_deposit,
    other_charges
)
VALUES
(
    %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s
)
"""
        

        cursor.execute(

            sql,

            (

        listing.owner_id,

        listing.property_name,

        listing.property_type,

        listing.area,

        listing.full_address,

        listing.university,

        listing.gender_preference,

        listing.description,

        listing.facilities,

        listing.monthly_rent,

        listing.security_deposit,

        listing.other_charges


            )

        )

        self.connection.commit()

        cursor.close()

        return True

    # -----------------------------
    # Get Listing By ID
    # -----------------------------






    def get_listing_by_id(self, listing_id):

        cursor = self.connection.cursor()

        sql = """
        SELECT *
        FROM listings
        WHERE listing_id = %s
        """

        cursor.execute(sql, (listing_id,))

        row = cursor.fetchone()

        cursor.close()

        return row

    # -----------------------------
    # Get All Listings of Owner
    # -----------------------------
    def get_owner_listings(self, owner_id):

        cursor = self.connection.cursor()

        sql = """
        SELECT *
        FROM listings
        WHERE owner_id = %s
        ORDER BY created_at DESC
        """

        cursor.execute(sql, (owner_id,))

        rows = cursor.fetchall()

        cursor.close()

        return rows

    # -----------------------------
    # Update Listing
    # # -----------------------------
    # def update_listing(self, listing):

    #     cursor = self.connection.cursor()

    #     sql = """
    #     UPDATE listings

    #     SET

    #         property_name = %s,

    #         property_type = %s,

    #         area = %s,

    #         full_address = %s,

    #         university = %s,

    #         gender_preference = %s,

    #         description = %s,

    #         monthly_rent = %s,

    #         security_deposit = %s,

    #         updated_at = CURRENT_TIMESTAMP

    #     WHERE listing_id = %s
    #     """

    #     cursor.execute(

    #         sql,

    #         (

    #             listing.property_name,

    #             listing.property_type,

    #             listing.area,

    #             listing.full_address,

    #             listing.university,

    #             listing.gender_preference,

    #             listing.description,

    #             listing.monthly_rent,

    #             listing.security_deposit,

    #             listing.listing_id

    #         )

    #     )

    #     self.connection.commit()

    #     cursor.close()

    #     return True

    # -----------------------------
    # Delete Listing
    # -----------------------------


    def get_listing_details_by_id(self, listing_id: int):

        sql = """
        SELECT
            listing_id,
            l.owner_id,
            u.phone,
            l.property_name,
            l.property_type,
            l.area,
            l.full_address,
            l.nearest_college,
            l.gender_preference,
           l. description,
            l.facilities,
            l.monthly_rent,
            l.security_deposit,
            l.other_charges
        FROM listings l
        JOIN users u
            ON l.owner_id = u.user_id
        WHERE l.listing_id = %s;
    """

        cursor = self.connection.cursor()

        cursor.execute(sql, (listing_id,))

        row = cursor.fetchone()

        cursor.close()
 
        if row is None:
           return None

        return ViewListing(
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









    def increase_phone_click(self, listing_id):

       cursor = self.connection.cursor()

       cursor.execute(
        "SELECT increase_phone_click(%s)",
        (listing_id,)
    )

       self.connection.commit()

       cursor.close()



    def increase_whatsapp_click(self, listing_id):

       cursor = self.connection.cursor()

       cursor.execute(
        "SELECT increase_whatsapp_click(%s)",
        (listing_id,)
    )

       self.connection.commit()

       cursor.close()






    def save_search_preference(self,
                           property_type,
                           area,
                           university,
                           gender_preference):

         cursor = self.connection.cursor()

         cursor.execute("""

        SELECT save_search_preference(
            %s,
            %s,
            %s,
            %s
        )

    """, (

        property_type,
        area,
        university,
        gender_preference

    ))

         self.connection.commit()


    def get_all_universities(self):

  
       cursor = self.connection.cursor()

       sql = """
        SELECT DISTINCT nearest_college
        FROM listings
        WHERE nearest_college IS NOT NULL
        ORDER BY nearest_college
    """

       cursor.execute(sql)

       universities = [row[0] for row in cursor.fetchall()]

       cursor.close()

       return universities
    

    def get_all_areas(self):

 
       cursor = self.connection.cursor()

       sql = """
        SELECT DISTINCT area
        FROM listings
        ORDER BY area
    """

       cursor.execute(sql)

       areas = [row[0] for row in cursor.fetchall()]

       cursor.close()

       return areas






    def filter_listings(
        self,
        property_type=None,
        area=None,
        university=None,
        gender=None
):

     if any([property_type,area, university,gender]):
        self.save_search_preference(property_type,area,university,gender)


     cursor = self.connection.cursor()

     sql = """
        SELECT
            listing_id,
            owner_id,
            u.phone,
            property_name,
            property_type,
            area,
            full_address,
            nearest_college,
            gender_preference,
            description,
            facilities,
            monthly_rent,
            security_deposit,
            other_charges
        FROM listings l
        JOIN users u
        ON l.owner_id = u.user_id
        WHERE 1=1
    """

     values = []

     if property_type:
        sql += " AND property_type = %s"
        values.append(property_type)

     if area:
        sql += " AND area = %s"
        values.append(area)

     if university:
        sql += " AND nearest_college = %s"
        values.append(university)

     if gender:
        sql += " AND gender_preference = %s"
        values.append(gender)

     sql += " ORDER BY listing_id DESC"

     cursor.execute(sql, values)

     rows = cursor.fetchall()
 
     listings = []

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