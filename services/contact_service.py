from repository.contact_repository import ContactRepository
from models.contact_message import ContactMessage


class ContactService:

    def __init__(self):
        self.repository = ContactRepository()

    def save_contact_message(
        self,
        name,
        email,
        subject,
        message
    ):
        contact = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        try:
            return self.repository.save_contact_message(contact)

        except Exception as e:
            print("Contact Service Error:", e)
            return None