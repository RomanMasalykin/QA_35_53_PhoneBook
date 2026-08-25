import uuid
from models.user import User
from pages.registration_page import RegistrationPage


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)

    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        f"roman_test_{random_suffix}@gmail.com"
        "Password123$"
    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "User already exist" in registration_page.get_alert_text()
    registration_page.accept_alert()


def test_registration_wrong_email(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        f"roman_test_gmail.com"
        "Password123$"
    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "User already exist" in registration_page.get_alert_text()
    registration_page.accept_alert()


def test_registration_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        f"roman_test_@gmail.com"
        "d123$"
    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_exists_user(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        f"roman_test_@gmail.com"
        "Password123$"
    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "User already exist" in registration_page.get_alert_text()
    registration_page.accept_alert()

































