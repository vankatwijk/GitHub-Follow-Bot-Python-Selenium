from selenium import webdriver
from time import sleep
from random import randint
from secrets import *


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

    def followersRatio(self):
        #number of follers to following , if this user does not follow many users back there is no point in following
        #here we will determin if this is a good person to follow from the above list
        temp = []

        for follower in self.followers:
            self.driver.get(follower)
            sleep(randint(8, 14))

            print('--------------------------------------')
            try:
                #get the number of followers
                numFollowers = self.driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[4]/div[2]/div/div/a[1]/span')
                numFollowing = self.driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[4]/div[2]/div/div/a[2]/span')
                print('Followers : ' + numFollowers[0].text)
                print('Following : ' + numFollowing[0].text)

                #convert to number and check if half the follers is less than the following
                halfFollowers = int(numFollowers[0].text) / 2

                if numFollowing > halfFollowers:
                    print(follower)
                    print('follower ratio good')
                    isActive = self.activeOnGithub(follower)
                    print(isActive)
                    if isActive == True:
                        print('User is Active')
                        self.followThisUser(follower)
                        temp.append(follower)



            except:
                print("can't get the total amount of followers")
    
        list_set = set(temp)
        self.followersRatio = (list(list_set))


    def activeOnGithub(self,follower):
        #check if the users from the ratio are active on github ifnot then there is really no point in following
        sleep(randint(4, 14))

        try:
            #get the number of followers
            numberOfPinned = len(self.driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li[1]'))
            numberOfActivities = len(self.driver.find_elements_by_class_name('profile-rollup-wrapper'))
            print(numberOfPinned)
            print(numberOfActivities)

            #if number of pinned projects 1 or more
            if numberOfPinned >= 1:
                #if activites for the month greater than 1
                if numberOfActivities  >= 1:
                    return True
            

            print('User is not Active')
            return False

        except:
            print("can't get activities and pinned projects")
            return False

    def followThisUser(self,follower):
        #click the follow button if this is a good match
        sleep(randint(4, 14))

        try:
            print("Following......")
            follow_button = self.driver.find_element_by_xpath('//input[@value="Follow"]')
            # follow_button = self.driver.find_elements_by_xpath("//input[@aria-label='Follow this person']")
            inputParent = follow_button.find_element_by_xpath('..')
            inputParent.submit()
            
            # checking if you already follow does not work
            # print('Follow button : '+inputParent.get_attribute('hidden') )
            # if inputParent.get_attribute('hidden') == None:
            #     print('Submit clicked !')
            #     inputParent.submit()

            # else:
            #     print('you are already folloing them')

            return True

        except:
            print("can't click follow button")
            return False

        

my_bot = GithubBot(gituser,gitpw,gitCopyFollowers)
my_bot.copy_followers()
my_bot.followersRatio()
