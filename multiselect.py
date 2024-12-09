from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys


options = webdriver.ChromeOptions()
#options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument("--user-agent=	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36")

options.page_load_strategy = 'eager'
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://suninjuly.github.io/selects1.html")

num1 = driver.find_element('xpath', '//span[@id="num1"]').text
num2 = driver.find_element('xpath', '//span[@id="num2"]').text
button = driver.find_element('xpath', '//button[text()="Submit"]')

sm = int(num1) + int(num2)

dropdown = Select(driver.find_element("xpath", '//select[@id="dropdown"]'))
dropdown.select_by_visible_text(f'{sm}') #выбираем нужное значение на основе текста в мультиселективном выборе
button.click()

time.sleep(5)

