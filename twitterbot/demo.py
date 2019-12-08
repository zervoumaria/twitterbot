from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email = bot.find_element_by_class_name("js-username-field")
        password = bot.find_element_by_class_name("js-password-field")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)

        # scroll pages
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_element_by_css_selector('[data-testid="tweet"]')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            print(links)


ed = TwitterBot('mariazervou71@gmail.com','Mz6980803057!')
ed.login()
ed.like_tweet('datascience')
