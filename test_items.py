import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket"))
    )
    buttons=browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    print(len(buttons))
    assert len(buttons)>0, 'Кнопка не найдена'