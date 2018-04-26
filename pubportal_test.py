import selenium
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://qa-aws.pubportal.dev.defymedia.com")
username = driver.find_element_by_name('identity')
username.send_keys("jliu")
password = driver.find_element_by_name('credential')
password.send_keys('Defy@123')

login_button = driver.find_element_by_xpath('//button')
login_button.click()


