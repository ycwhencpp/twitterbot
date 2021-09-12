from selenium import webdriver
from selenium.webdriver.common.keys import keys
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
    

