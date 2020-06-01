from selenium import webdriver
from time import sleep
from random import randint
from secrets import gituser
from secrets import gitpw
from secrets import gitCopyFollowers


class GithubBot:
    def __init__(self, username, pw, copyfollowers):
        self.username = username
        self.copyfollowers = copyfollowers

        # START LOGIN PROCESS
        self.driver = webdriver.Chrome("/home/hkatwijk/repo/GitHub-Follow-Bot/chromedriver")
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
        sleep(randint(4, 12))
        # END LOGIN PROCESS

    def copy_followers(self):
        #here we go to our target and make a list of all there followers
        #go to profile
        self.driver.get("https://github.com/{}?tab=followers".format(self.copyfollowers))
        sleep(randint(3, 10))

        #get all the followers from the first page
        users = self.driver.find_elements_by_xpath("//a[@data-hovercard-type='user']")
        temp = []

        for follower in users:
            temp.append(follower.get_attribute("href"))

        list_set = set(temp) 
        self.followers = (list(list_set))
        print(self.followers)

    def match_followers(self):
        #here we will determin if this is a good person to follow from the above list

        for follower in self.followers:
            self.driver.get(follower)
            sleep(randint(4, 10))

            try:
                #get the number of followers
                numFollowers = self.driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[4]/div[2]/div/div/a[1]/span')
                numFollowing = self.driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[4]/div[2]/div/div/a[2]/span')
                print(numFollowers[0].text)
                print(numFollowing[0].text)

                #convert to number and check if half the follers is less than the following
                halfFollowers = int(numFollowers[0].text) / 2

                if numFollowing > halfFollowers:
                    print(follower)
                    print('lets follow')

            except:
                print("can't get the total amount of followers")


my_bot = GithubBot(gituser,gitpw,gitCopyFollowers)
my_bot.copy_followers()
my_bot.match_followers()
