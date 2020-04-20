# тест авторизации
import unittest
from selenium import webdriver


# Решение если у пользователя кастомное расположение Google Chrome
# options = webdriver.ChromeOptions()
# chrome_driver_binary = "/usr/local/bin/chromedriver"
# options.binary_location = "/Applications/Chrome.app/Contents/MacOS/Google Chrome"
# driver = webdriver.Chrome(chrome_driver_binary, options=options)

# class Authorization():
#     def happy_authorization(self, a):
driver = webdriver.Chrome()

driver.get("https://dev.adapty.io/login")

email_field = driver.find_element_by_name("email")
password_field = driver.find_element_by_name("password")
login_button = driver.find_element_by_xpath(
    "//*[@id='root']/div/div/div/div/div[2]/div/div/form/div[5]/div/div/span/button")

email_field.send_keys('mxm.mishin@gmail.com')
password_field.send_keys('hakunamatata')
login_button.click()

print('current_url= ', driver.current_url)
# assert "https://dev.adapty.io/dashboard" in driver.current_url

driver.quit()
