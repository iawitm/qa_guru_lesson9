import os
from datetime import datetime

from selene import browser, command, have


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def choose_gender(self, enum_value):
        browser.element(f'[for=gender-radio-{str(enum_value.value)}]').click()

    def fill_mobile(self, mobile):
        browser.element('#userNumber').type(mobile)

    def fill_date_of_birth(self, birthday):
        birthday = datetime.strptime(birthday, "%Y-%m-%d")
        year = str(birthday.year)
        month = str(birthday.month - 1)
        day = "0" + str(birthday.day)

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').element(f'[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').element(f'[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--{day}').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def choose_hobby(self, enum_value):
        browser.element(f'[for=hobbies-checkbox-{str(enum_value.value)}]').click()

    def upload_picture(self, file_path):
        browser.element('#uploadPicture').send_keys(os.path.abspath(str(file_path)))

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def select_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def submit_form(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_have_elements(self, student_name, student_email, gender, mobile, date_of_birth, subjects, hobbies,
                             picture, address, state_and_city):
        browser.element('.table-responsive').all('tr').should(
            have.exact_texts(
                'Label Values',
                'Student Name ' + student_name,
                'Student Email ' + student_email,
                'Gender ' + gender,
                'Mobile ' + mobile,
                'Date of Birth ' + date_of_birth,
                'Subjects ' + subjects,
                'Hobbies ' + hobbies,
                'Picture ' + picture,
                'Address ' + address,
                'State and City ' + state_and_city
            )
        )
