import os
import time

from selene import browser, be, have, command


def test_demo_qa_form(browser_setup):
    browser.open("/automation-practice-form")


    # Ввод данных: Имя, Фамилия, Email, Пол, Мобильный телефон
    browser.element('#firstName').type('Frog')
    browser.element('#lastName').type('Green')
    browser.element('#userEmail').type('greenfrog@frog.com')
    browser.element('[for=gender-radio-3]').click()
    browser.element('#userNumber').type('1234567890')

    # Выбор Даты рождения 24.04.2024
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element('[value="2024"]').click()
    browser.element('.react-datepicker__month-select').element('[value="3"]').click()
    browser.element('.react-datepicker__day--024').click()

    # Выбор Предмета через нажатие Enter
    browser.element('#subjectsInput').type('Arts').press_enter()

    # Выбор Предмета через клик в подсказке (выбирается второй элемент - History)
    browser.element('#subjectsInput').type('hi')
    browser.element('#react-select-2-option-1').click()

    # Выбор Хобби
    browser.element('[for=hobbies-checkbox-3]').click()

    # Загрузка Изображения
    browser.element('#uploadPicture').send_keys(os.path.abspath('cute_frog.jpg'))

    # Ввод Адреса проживания
    browser.element('#currentAddress').type('North Forest, Great Swamp, Reed #1')

    # Выбор Штата и Города
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()

    # Скролл до кнопки, чтобы она стала видима
    # Подтверждение данных
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    # Проверка результата
    browser.element('.table-responsive').all('tr').should(
        have.exact_texts(
            'Label Values',
            'Student Name Frog Green',
            'Student Email greenfrog@frog.com',
            'Gender Other',
            'Mobile 1234567890',
            'Date of Birth 24 April,2024',
            'Subjects Arts, History',
            'Hobbies Music',
            'Picture cute_frog.jpg',
            'Address North Forest, Great Swamp, Reed #1',
            'State and City Haryana Karnal',
        )
    )