from enum import Enum

from pages.registration_page import RegistrationPage


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3


class Hobby(Enum):
    SPORTS = 1
    READING = 2
    MUSIC = 3


def test_demo_qa_form(browser_setup):
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_first_name('Frog')
    registration_page.fill_last_name('Green')
    registration_page.fill_email('greenfrog@frog.com')
    registration_page.choose_gender(Gender.OTHER)
    registration_page.fill_mobile('1234567890')
    registration_page.fill_date_of_birth('2024-04-24')
    registration_page.fill_subjects("Arts")
    registration_page.choose_hobby(Hobby.MUSIC)
    registration_page.upload_picture('test_demo_qa/resources/cute_frog.jpg')
    registration_page.fill_current_address('North Forest, Great Swamp, Reed #1')
    registration_page.select_state('Haryana')
    registration_page.select_city('Karnal')
    registration_page.submit_form()
    registration_page.should_have_elements('Frog Green',
                                           'greenfrog@frog.com',
                                           'Other',
                                           '1234567890',
                                           '24 April,2024',
                                           'Arts',
                                           'Music',
                                           'cute_frog.jpg',
                                           'North Forest, Great Swamp, Reed #1',
                                           'Haryana Karnal'
                                           )
