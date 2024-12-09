from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


options = webdriver.ChromeOptions()
#options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument("--user-agent=	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36")

options.page_load_strategy = 'eager'
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 12, poll_frequency=1)

#функция для вычисления значения, которое необходимо отправить в ответную форму
def calc(value):
  return str(math.log(abs(12*math.sin(int(value)))))


driver.get("https://suninjuly.github.io/explicit_wait2.html")

PRICE_LOCATOR = ('xpath', '//h5[@id="price"]')
# ждём, когда появится цена $100 и бронируем, кликая на кнопку book
wait.until(EC.text_to_be_present_in_element(PRICE_LOCATOR, "$100"))
driver.find_element('xpath', '//button[@id="book"]').click()

x = int(driver.find_element('xpath', '//span[@id="input_value"]').text)
driver.find_element('xpath', '//input[@id="answer"]').send_keys(calc(x))
driver.find_element('xpath', '//button[text()="Submit"]').click()


# перехватываем и печатаем alert, так как там необходимое значение для выполнения задания:)
print(driver.switch_to.alert.text)