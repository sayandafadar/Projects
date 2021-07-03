from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

Twitter_Email = "dafadarts@gmail.com"
Twitter_Password = 8877190290

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://twitter.com/home")
time.sleep(6)
email = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div['
                                     '1]/label/div/div[2]/div/input')
email.send_keys('sayankr30@gmail.com')
time.sleep(3)
password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div['
                                        '2]/label/div/div[2]/div/input')
password.send_keys(8877190290)
time.sleep(5)
password.send_keys(Keys.ENTER)