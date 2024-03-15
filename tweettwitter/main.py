
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "minhtam71.work@gmail.com"
TWITTER_PASSWORD ="Madelynn05"
SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/?logout=1704946543315"
TWITTER_USERNAME = 'Minhtam71work'
class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options = chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_URL)
        time.sleep(3)
        start_button = self.driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_button.click()
        time.sleep(100)
        self.up = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        up_down = [self.up,self.down]
        return up_down
    def tweet_at_provider(self,text):
        self.driver.get(TWITTER_URL)
        time.sleep(5)

        #-------SIGN IN ------------
        sign_in_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in_button.click()
        time.sleep(5)

        #-----FILL IN MAIL ---------
        mail_fill = self.driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        mail_fill.send_keys(TWITTER_EMAIL,Keys.ENTER)



        #---FILL IN USERNAME ---------
        time.sleep(5)
        username_fill = self.driver.find_element(by=By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username_fill.send_keys(TWITTER_USERNAME,Keys.ENTER)

        #----FILL IN PASSWORD ----------
        time.sleep(5)
        pw_fill = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pw_fill.send_keys(TWITTER_PASSWORD,Keys.ENTER)
        log_in_button = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        log_in_button.click()

        post_text = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        post_text.send_keys(text)
        post_button = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        post_button.click()

bot = InternetSpeedTwitterBot()
up = bot.get_internet_speed()[0]
down = bot.get_internet_speed()[1]
print(up)
print(down)
#bot.tweet_at_provider()
