from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

Chrome_Driver_Path = "C:\Development\chromedriver.exe"
Twitter_Email = "dafadarts@gmail.com"
Twitter_Password = 8877190290


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get("https://www.speedtest.net/")

    def get_internet_speed(self):
        self.internet_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                '2]/div[3]/div[1]/a/span[4]')
        self.internet_speed.click()
        time.sleep(62)
        self.download_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                                '1]/div[2]/div/div[2]/span')
        self.upload_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div['
                                                              '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                              '3]/div/div[2]/span')
        print(self.download_speed.text)
        print(self.upload_speed.text)
        self.d_speed = self.download_speed.text
        self.u_speed = self.upload_speed.text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(6)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                  '2]/form/div/div[ '
                                                  '1]/label/div/div[2]/div/input')
        email.send_keys('dafadarts@gmail.com')
        time.sleep(3)
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                     '2]/form/div/div[ '
                                                     '2]/label/div/div[2]/div/input')
        password.send_keys(8877190290)
        time.sleep(5)
        password.send_keys(Keys.ENTER)
        print(self.d_speed)
        print(self.u_speed)
        time.sleep(10)
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                  '2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                  '1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div['
                                                  '2]/div/div/div/div')
        tweet.send_keys(f"Hey, @airtelindia why my internet speed is (download speed: {self.d_speed}MB/s, "
                        f"upload speed: {self.u_speed})MB/s is slow?")
        time.sleep(5)
        post = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                 '2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div['
                                                 '3]/div/span/span')
        post.click()
        self.driver.quit()



bot = InternetSpeedTwitterBot(Chrome_Driver_Path)
bot.get_internet_speed()
bot.tweet_at_provider()
