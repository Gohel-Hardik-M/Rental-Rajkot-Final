from fastapi import APIRouter, Form, requests, Request
from fastapi.responses import FileResponse, RedirectResponse
from services.user_services import UserService
from starlette.middleware.sessions import SessionMiddleware




from services.listing_services import ListingService

from services.owner_services import OwnerService

owner_service = OwnerService()

listing_service = ListingService()


from services.admin_service import AdminService

admin_service= AdminService()

from config.template_config import templates
users = UserService()

router = APIRouter()


@router.get("/")
def index():
    return FileResponse("templates/index.html")





@router.get("/robots.txt", include_in_schema=False)
def robots():
    return FileResponse("static/robots.txt")

@router.get("/sitemap.xml", include_in_schema=False)
def sitemap():
    return FileResponse("static/sitemap.xml")

from fastapi.responses import Response

@router.get("/sitemap2.xml", include_in_schema=False)
def sitemap2():
    with open("static/sitemap2.xml", "r") as f:
        return Response(content=f.read(), media_type="application/xml")


@router.get("/about")
def about():
    return FileResponse("templates/about.html")













@router.get("/listing/{listing_id}/whatsapp")
def whatsapp_click(
        listing_id: int
):

    listing_service.increase_whatsapp_click(listing_id)

    listing = listing_service.get_listing_by_id(listing_id)

    whatsapp_url = (
        f"https://wa.me/{listing.phone_number}"
        f"?text=Hello, I'm interested in {listing.property_name}."
    )

    return RedirectResponse(url=whatsapp_url)




@router.get("/listing/{listing_id}/call")
def phone_click(
        listing_id: int
):

    listing_service.increase_phone_click(listing_id)

    listing = listing_service.get_listing_by_id(listing_id)

    return RedirectResponse(
        url=f"tel:{listing.phone_number}"
    )



@router.get("/admin/delete-listing/{listing_id}")
def delete_listing(request: Request, listing_id: int):

    # Login check
    if "user_id" not in request.session:
        return RedirectResponse("/", status_code=303)
    
    # Admin check
    if request.session.get("user_type") != "admin":
        return RedirectResponse("/", status_code=303)

    admin_service.delete_listing(listing_id)

    return RedirectResponse(
        url="/admin/dashboard",
        status_code=303
    )

@router.get("/admin/dashboard")
def admin_dashboard(request : Request):
    if "user_id" not in request.session:
        return RedirectResponse(url="/", status_code=303)


      # Check admin role
    if request.session.get("user_type") != "admin":
        return RedirectResponse(url="/owner/dashboard", status_code=303)

    dashboard = admin_service.get_dashboard_counts()
    properties = admin_service.get_all_properties()

    return templates.TemplateResponse(
        request=request,
        name="admin-dashboard.html",
        context={
            "user_name": request.session.get("user_name"),
            "user_email": request.session.get("user_email"),
            "dashboard": dashboard,
            "properties": properties
        }
    )




@router.get("/admin/listings")
def admin_listings(request : Request):
    if "user_id" not in request.session:
        return RedirectResponse(url="/", status_code=303)

    return FileResponse("templates/admin-listings.html")


@router.get("/admin/owners")
def admin_owners(request : Request):
    if "user_id" not in request.session:
        return RedirectResponse(url="/", status_code=303)

    return FileResponse("templates/admin-owners.html")


@router.get("/admin/verify-listings")
def verify(request : Request):
    if "user_id" not in request.session:
        return RedirectResponse(url="/", status_code=303)

    return FileResponse("templates/admin-verify-listings.html")


@router.get("/owner/login")
def owner_login(request : Request):
    return templates.TemplateResponse(
    request=request,
    name="owner-login.html",
    context={}
    )   








@router.post("/owner/login_action")
def owner_login_action(

        request: Request,

        email: str = Form(...),

        password: str = Form(...)

):

    success, message, user = users.login(

        email,

        password

    )

    if not success:

        return templates.TemplateResponse(
    request=request,
    name="owner-login.html",
    context={
        "message": "Invalid Email or Password"
    }
    )

    request.session["user_id"] = user.id

    request.session["user_name"] = user.full_name

    request.session["user_email"] = user.email

    request.session["user_type"] = user.user_type

    if request.session["user_type"] == "admin":
           return RedirectResponse(
         url="/admin/dashboard",
         status_code=303
           )

        


    return RedirectResponse(
    url="/owner/dashboard",
    status_code=303
)



@router.get("/owner/register")
def owner_register(request: Request):
        return templates.TemplateResponse(
        request=request,
        name="owner-register.html",
        context={}
    )


@router.post('/owner/register_action')
def owner_register_action(      request: Request,full_name: str = Form(...), email: str = Form(...),  phone: str = Form(...),  password: str = Form(...), confirm_password: str = Form(...)):
    success = users.register_owner( full_name,email, phone,password,confirm_password )

    if success:

        return RedirectResponse(url="/owner/login", status_code=303 )

    return templates.TemplateResponse(
    request=request,
    name="owner-register.html",
    context={
        "message": "Email Already Exists"
    }
)




@router.get("/owner/delete-listing/{listing_name}")
def delete_listing(request: Request, listing_name: str):

    # Login check
    if "user_id" not in request.session:
        return RedirectResponse("/", status_code=303)
    
    # Admin check
    if request.session.get("user_type") != "OWNER":
        return RedirectResponse("/", status_code=303)

    owner_service.delete_listing(listing_name)

    return RedirectResponse(
        url="/owner/my-listings",
        status_code=303
    )




@router.get("/owner/dashboard")
def owner_dashboard(request : Request):
    print("===============================")
    print("Owner Dashborad")
    print("================================")
    print(request.session)

    hostels = owner_service.get_no_hostels(request.session.get("user_id"))
    return templates.TemplateResponse(
        request=request,
        name="owner-dashboard.html",
        context={
            "user_name": request.session.get("user_name"),
            "user_email": request.session.get("user_email"),
            "hostels": hostels
        }
    )



@router.get("/owner/my-listings")
def owner_listings(request : Request):
    if "user_id" not in request.session:
        return RedirectResponse(url="/", status_code=303)


        
    owner_id = request.session.get("user_id")
    my_listings = owner_service.get_owner_properties(owner_id)
    if(my_listings):
            print("LISTINGS REACHED HERE--------------------------------------")
    else:
            print("GOT EMPTY MY LSUTINGSSSSSS")
    return templates.TemplateResponse(
                request=request,
                name="owner-my-listings.html",
                context={
                  "owner_listings" :my_listings
                }
            )



@router.get("/owner/inquiries")
def owner_inquiries(request : Request):
    if "user_id" not in request.session:
        return RedirectResponse(url="/", status_code=303)

    return FileResponse("templates/owner-inquiries.html")


@router.get("/tenant/login")
def tenant_login():
    return FileResponse("templates/tenant-login.html")


@router.get("/tenant/register")
def tenant_register():
    return FileResponse("templates/tenant-register.html")


@router.get("/tenant/dashboard")
def tenant_dashboard(request : Request):
    if "user_id" not in request.session:
        return RedirectResponse(url="/", status_code=303)

    return FileResponse("templates/tenant-dashboard.html")




@router.get("/listing/{listing_id}/details")
def get_listing_details(request: Request, listing_id: int):

    listing = listing_service.get_listing_details_by_id(listing_id)

    if listing is None:
        return RedirectResponse(url='/listings',status_code=302)

    return templates.TemplateResponse(
       name= "listing-details.html",
       request= request,
       context= {
            "request": request,
            "listing": listing
        }
    )

@router.get("/listings")
def listings(request: Request,
                 property_type: str = "",
                 area: str = "",
                 university: str = "",
                 gender: str = ""):

    listings = listing_service.filter_listings(

        property_type,
        area,
        university,
        gender

    )
    areas = listing_service.get_all_areas()

    universities = listing_service.get_all_universities() 


    return templates.TemplateResponse(
        request=request,
        name="listings.html",
        context={
            "listings": listings,
            "areas" : areas,
            "universities":universities,
        }
    )







@router.get("/logout")
def logout(request: Request):

    request.session.clear()

    return RedirectResponse(
        url="/",
        status_code=303
    )



#========================================================LISTINGS========================================================================================================================
#=================================================================================================================================================================================================




# ----------------------------------------
# Open Add Listing Page
# ----------------------------------------

@router.get("/owner/add-listing")
def owner_add_listing(request: Request):

    if "user_id" not in request.session:
        return RedirectResponse(url="/", status_code=303)


    return templates.TemplateResponse(
        request=request,
        name="owner-add-listing.html",
        context={
            "session": request.session
        }
    )


# ----------------------------------------
# Save New Listing
# ----------------------------------------

@router.post("/owner/add-listing")
def save_listing(

        request: Request,

         property_type: str = Form(...),

    # Basic Details
    property_name: str = Form(...),
    area: str = Form(...),
    address: str = Form(...),
    nearest_college: str = Form(...),
    gender_preference: str = Form(...),
    description: str = Form(...),

    # Facilities (Checkboxes)
    facilities: list[str] = Form([]),

    # Pricing
    monthly_rent: int = Form(...),
    deposit_amount: int = Form(...),
    other_charges:  str = Form(...)

):
    if "user_id" not in request.session:
        return RedirectResponse(url="/", status_code=303)


    owner_id = request.session["user_id"]

    success = listing_service.create_listing(

        owner_id=owner_id,

        property_name=property_name,

        property_type=property_type,

        area=area,

        full_address=address,

        university=nearest_college,

        gender_preference=gender_preference,

        description=description,

        facilities=facilities,

        monthly_rent=monthly_rent,

        security_deposit=deposit_amount,

        other_charges=other_charges

    )

    if success:

        return RedirectResponse(
            url="/owner/my-listings",
            status_code=303
        )

    return templates.TemplateResponse(
        request=request,
        name="owner-add-listing.html",
        context={
            "session": request.session,
            "message": "Unable to save listing."
        }
    )
  


# ----------------------------------------
# My Listings
# ----------------------------------------

# @router.get("/owner/my-listings")
# def my_listings(request: Request):

#     owner_id = request.session["user_id"]

#     listings = listing_service.get_owner_listings(owner_id)

#     return templates.TemplateResponse(
#         request=request,
#         name="owner-my-listings.html",
#         context={
#             "session": request.session,
#             "listings": listings
#         }
#     )


# # ----------------------------------------
# # Edit Listing Page
# # ----------------------------------------

# @router.get("/owner/edit-listing/{listing_id}")
# def edit_listing(

#         request: Request,

#         listing_id: int

# ):

#     listing = listing_service.get_listing(listing_id)

#     return templates.TemplateResponse(
#         request=request,
#         name="owner-add-listing.html",
#         context={
#             "session": request.session,
#             "listing": listing
#         }
#     )


# # ----------------------------------------
# # Update Listing
# # ----------------------------------------

# @router.post("/owner/edit-listing/{listing_id}")
# def update_listing(

#         request: Request,

#         listing_id: int,

#         property_name: str = Form(...),

#         property_type: str = Form(...),

#         area: str = Form(...),

#         full_address: str = Form(...),

#         university: str = Form(...),

#         gender_preference: str = Form(...),

#         description: str = Form(...),

#         monthly_rent: float = Form(...),

#         security_deposit: float = Form(...)

# ):

#     owner_id = request.session["user_id"]

#     success = listing_service.update_listing(

#         listing_id,

#         owner_id,

#         property_name,

#         property_type,

#         area,

#         full_address,

#         university,

#         gender_preference,

#         description,

#         monthly_rent,

#         security_deposit

#     )

#     if success:

#         return RedirectResponse(
#             url="/owner/my-listings",
#             status_code=303
#         )

#     return RedirectResponse(
#         url=f"/owner/edit-listing/{listing_id}",
#         status_code=303
#     )


# # ----------------------------------------
# # Delete Listing
# # ----------------------------------------

# @router.get("/owner/delete-listing/{listing_id}")
# def delete_listing(

#         request: Request,

#         listing_id: int

# ):

#     listing_service.delete_listing(listing_id)

#     return RedirectResponse(
#         url="/owner/my-listings",
#         status_code=303
#     )
