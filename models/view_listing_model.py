class ViewListing:

    def __init__(
        self,
        listing_id,
        owner_id,
        owner_phone,
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

        self.listing_id = listing_id
        self.owner_id = owner_id
        self.owner_phone = owner_phone
        self.property_name = property_name
        self.property_type = property_type
        self.area = area
        self.full_address = full_address
        self.university = university
        self.gender_preference = gender_preference
        self.description = description
        self.facilities = facilities
        self.monthly_rent = monthly_rent
        self.security_deposit = security_deposit
        self.other_charges = other_charges