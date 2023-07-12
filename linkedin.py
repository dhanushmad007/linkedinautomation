import time
from selenium import webdriver
class Linkedin:

    def __init__(self):

        path ='/Users/dhanushdasari/Downloads/chromedriver 2'
        self.driver = webdriver.Chrome(path)
    def loadPage(self,email,password):
        self.driver.get('https://www.linkedin.com/?trk=public_profile_nav-header-logo')

        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="session_key"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="session_password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/div/form/button').click()
    def checkError(self):
        while True:
                try:
                    if self.driver.find_element_by_xpath('//*[@id="app__container"]/main/h1'):
                        continue
                except:
                    print('login succes')
                break

    def loadMessagesPage(self):
        self.driver.get('https://www.linkedin.com/messaging/thread/2-MDIyZjgzZmYtZjYwZS00MjBlLTk3MGQtMjU3ODFlM2MzZTExXzAxMw==/')
        self.driver.implicitly_wait(600)
        self.driver.find_element_by_xpath('//div[@class="msg-conversation-card__content--selectable"]').click()
        while True:
            try:

                self.driver.implicitly_wait(100)
                self.driver.find_element_by_xpath('//button[@class="block mlA mrA artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]').click()
                print('hello')
            except Exception as e:
                print(e)
                break

    def sendMessages(self,message,pathImage):
    
        x = self.driver.find_element_by_xpath("//ul[@class='list-style-none msg-conversations-container__conversations-list']")
        print(x)
        y = x.find_elements_by_tag_name('a')
        print(len(y))
        n = y[0:367]
        print(y)
        for i in y:
            if i in n:
                i.click()
                continue
            else:
                i.click()
                print('hi')
                try:
                    self.driver.implicitly_wait(0.3)
                    x = self.driver.find_element_by_xpath('//form[@class=" msg-form"]').find_elements_by_tag_name('p')[
                        0]
                    name = self.driver.find_element_by_xpath('//*[@id="thread-detail-jump-target"]').text
                    x.send_keys(f'Hello {name}! \n\n{message}')
                    time.sleep(2)
                    self.driver.find_element_by_xpath(
                        '/html/body/div[5]/div[3]/div[2]/div/div/main/div/section[2]/div[2]/form/footer/div[2]/div[1]/button').click()
                    self.driver.find_element_by_xpath(
                        '/html/body/div[5]/div[3]/div[2]/div/div/main/div/section[2]/div[2]/form/footer/div[1]/div[1]/input[3]').send_keys(
                        pathImage)
                    time.sleep(2)
                    self.driver.find_element_by_xpath(
                        '/html/body/div[5]/div[3]/div[2]/div/div/main/div/section[2]/div[2]/form/footer/div[2]/div[1]/button').click()



                except Exception as e:
                    print(e)
                    continue

email = 'Your LinkedIn email'
password = 'Password'
Image =''
message ="Enter Your Message here"
obj = Linkedin()

obj.loadPage(email,password)
obj.checkError()
obj.loadMessagesPage()
obj.sendMessages(message,Image)