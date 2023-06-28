import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def test_basket_button_langs(browser):

    browser.get('https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

    time.sleep(5)

    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary')))

    assert button is not None, 'Кнопка не найдена'