from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestRegistration(unittest.TestCase):

    def test_link_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element('xpath', '//input[@placeholder="Input your first name"]').send_keys('Victor')
        browser.find_element('xpath', '//input[@placeholder="Input your last name"]').send_keys('Victorov')
        browser.find_element('xpath', '//input[@placeholder="Input your email"]').send_keys("Victor@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст и сохраняем текст элемента
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_link_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element('xpath', '//input[@placeholder="Input your first name"]').send_keys('Victor')
        browser.find_element('xpath', '//input[@placeholder="Input your last name"]').send_keys('Victorov')
        browser.find_element('xpath', '//input[@placeholder="Input your email"]').send_keys("Victor@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст и сохраняем текст элемента
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
