import random
import time
from faker import Faker
from models.contact import Contact
from pages.add_contact_page import ContactPage


def test_add_contact_success_all_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    random_suffix = random.randint(1, 1000000)

    contact = Contact(
        "Anna",
        "Test",
        f"05012{random_suffix}",
        f"anna_test_{random_suffix}@gmail.com",
        "LA",
        "QA lesson contact"
    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    time.sleep(2)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)