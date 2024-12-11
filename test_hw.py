import time

from selene import browser, have, be, by, command
import pytest
from selenium import webdriver


def test_form(browser_manager):
    # browser.element('#firstName').type('Kseniya')
    # browser.element('#lastName').type('Goryaeva')
    # browser.element('#userEmail').type('Goryaeva@mail.ru')
    # browser.element('#gender-radio-2').click() # не работает
    browser.element('#userNumber').type('89101234567')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select option').element_by(have.text(['1995'])).click()
    # browser.element('.react-datepicker__month-select').click() # выбор селекта месяца
    # browser.element('.react-datepicker__navigation--previous').double_click()
    # browser.element('.react-datepicker__navigation--previous').double_click()

    # browser.element('.react-datepicker__month-select>value')[7].click() # вторая попытка выбора селекта месяца и в нем значения 7

    # browser.element('.react-datepicker__year-select>value')[1995].click()
    # browser.element('#subjectsContainer').type('Студент') # не работает
    # browser.element('#hobbies-checkbox-1').perform(command.js.click)
    # browser.element('#currentAddress').type('Нижний Новгород')
    # browser.execute_script("window.scrollBy(0,6000)")
    browser.element('.css-yk16xz-control .css-19bqh2r').click()
    browser.element('#react-select-3-option-1').click()


    print('hi')















