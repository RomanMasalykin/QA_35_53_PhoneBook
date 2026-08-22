from pages.registration_page import RegistrationPage
import uuid

random_suffix = uuid.uuid4().hex[:8]

VALID_EMAIL = f"masalykin{random_suffix}123@gmail.com"
VALID_PASSWORD = "Roman1234$"
INVALID_EMAIL = "masalykiiin@gmal.com"
INVALID_PASSWORD = "rom124$"

def test_registration_success(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_form()
    registration_page.fill_email(VALID_EMAIL)
    registration_page.fill_password(VALID_PASSWORD)
    registration_page.submit_registration()

    assert registration_page.is_registered() is True

def test_registration_wrong_email(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_form()
    registration_page.fill_email(INVALID_EMAIL)
    registration_page.fill_password(VALID_PASSWORD)
    registration_page.submit_registration()

    assert "User already exist" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_form()
    registration_page.fill_email(VALID_EMAIL)
    registration_page.fill_password(VALID_PASSWORD)
    registration_page.submit_registration()

    assert "User already exist" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_exists_user(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_form()
    registration_page.fill_email(VALID_EMAIL)
    registration_page.fill_password(VALID_PASSWORD)
    registration_page.submit_registration()

    assert registration_page.get_alert_text() == "User already exist"

























