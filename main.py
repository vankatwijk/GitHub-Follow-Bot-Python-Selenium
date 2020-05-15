from selenium import webdriver
from time import sleep
from secrets import pw


class GithubBot:
    def __init__(self, username, pw, copyfollowers):
        self.username = username
        self.copyfollowers = copyfollowers

        # START LOGIN PROCESS
        self.driver = webdriver.Chrome("/chromedriver")
        self.driver.get("https://github.com/login")
        # wait for the page to load the DOM
        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="login_field"]')\
            .send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="password"]')\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]')\
            .click()
        # wait for the page to load the DOM
        sleep(4)
        # END LOGIN PROCESS

    def copy_followers(self):
        #go to profile
        



my_bot = GithubBot(gituser,gitpw,gitCopyFollowers)