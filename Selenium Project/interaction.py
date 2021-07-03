from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Manokamna")
first_name.send_keys(Keys.ENTER)

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Sayan Dafadar")
last_name.send_keys(Keys.ENTER)






































email = driver.find_element_by_name("email")
email.send_keys("dafadarts@gmail.com")
email.send_keys(Keys.ENTER)