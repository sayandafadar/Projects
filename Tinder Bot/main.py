from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/app/recs")
time.sleep(5)
login_with_tinder = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div['
                                                 '1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_with_tinder.click()
time.sleep(3)
try:
    facebook_sign_in_option_in_tinder = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div['
                                                                     '1]/div/div[3]/span/div[2]/button/span[2]')
    facebook_sign_in_option_in_tinder.click()
except:
    more_option = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/button')
    more_option.click()
    facebook_sign_in_option_in_tinder = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div['
                                                                     '1]/div/div[3]/span/div[2]/button/span[2]')
    facebook_sign_in_option_in_tinder.click()


# google_sign_in = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div['
#                                               '1]/div/button/span[2]')
# google_sign_in.click()
time.sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

facebook_email = driver.find_element_by_xpath('//*[@id="email"]')
facebook_email.send_keys('gepsumorki@nedoz.com')

facebook_password = driver.find_element_by_xpath('//*[@id="pass"]')
time.sleep(5)
facebook_password.send_keys('8877190290')
time.sleep(2)
facebook_password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(2)
# location_allow = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
# location_allow.click()

time.sleep(5)
# notification = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
# notification.click()


# cookie = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button/span')
# cookie.click()

time.sleep(9)
while True:
    time.sleep(3)
    nope = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div['
                                        '2]/div[ '
                                        '2]/button/span')
    nope.click()
