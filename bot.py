from selenium import webdriver    # to control browser operations
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from config import username,password,hashtag #to pass login credentials


#asking user about how many page to load 
load_pages=int(input("How many pages you want to load:"))


#creating bot class
class TwitterBot:
    #intailizing username and passsword
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.is_logged_in=False
        self.bot=webdriver.Firefox()
    
    #intializing login function
    def login(self):

         
        bot=self.bot
        bot.get("https://twitter.com/login")
        time.sleep(3)
        
        #locating username and password field 
        email=bot.find_element_by_name("session[username_or_email]")
        password=bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()

        #sending username and password to those located fields 
        email.send_keys(self.username)
        time.sleep(3)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)
        self.is_logged_in = True

    
    #making bot like and retweet tweets
    def like_retweet(self,hashtag,load_pages):

        #raising exception if not logged in
        if not self.is_logged_in:
            raise Exception("You must log in first!")

        bot=self.bot

        #opening hashtag page 
        bot.get(f"https://twitter.com/search?q={hashtag}&src=typed_query&f=live")
        time.sleep(4)

        
        # scrolling  pages and liking and retweeting tweets of same hashtag 
        for i in range(load_pages):
            try:

                #liking tweet
                bot.find_element_by_xpath("//div[@data-testid='like']").click()
                time.sleep(3)

                #retweeting tweet
                retweet=bot.find_element_by_xpath("//div[@data-testid='retweet']")
                action=ActionChains(bot)
                action.click(on_element=retweet).perform()

                # retweet.click()
                # retweet.send_keys("Retweet")
                time.sleep(2)

            except:
                time.sleep(5)
            
            time.sleep(3)

            #scrollling pages to load more content
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight/1.75)')
            time.sleep(5)

         

        
bot=TwitterBot(username,password)
bot.login()
bot.like_retweet(hashtag,load_pages)
