from selenium import webdriver    # to control browser operations
from selenium.webdriver.common.keys import Keys
import time
from config import username,password


#creating bot class
class TwitterBot:
    #intailizing username and passsword
    def __init__(self,username,password):
        self.username=username
        self.password=password
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
        password.send_keys(self.password)
        time.sleep(1)
        password.send_keys(Keys.ENTER)
        


    

bot=TwitterBot(username,password)
bot.login()
