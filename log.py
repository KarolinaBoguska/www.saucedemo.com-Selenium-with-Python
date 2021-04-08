from time import sleep
from selenium import webdriver
import unittest

# from selenium.driver.common.keys import Keys
# from selenium.driver.common.by import By
# from driver_manager.chrome import ChromeDriverManager
# driver = driver.Chrome()
#driver = webdriver.Chrome(executable_path=r"C:\Users\karol\PycharmProjects\Drivers\chromedriver.exe")

class TestCase(unittest.TestCase):
    # logowanie prawidłowy login i hasło
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("https://www.saucedemo.com/")
    def test_login(self):
        login = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input")
        login.send_keys("standard_user")
        self.driver.implicitly_wait(5)
        password = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input")
        password.send_keys("secret_sauce")
        self.driver.implicitly_wait(5)
        log = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/input")
        log.click()
        title = self.driver.title
        print(title)
        assert title == "Swag Labs"
        self.driver.implicitly_wait(5)
        self.driver.close()
    def test_logout(self):
        login = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input")
        login.send_keys("standard_user")
        self.driver.implicitly_wait(5)
        password = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input")
        password.send_keys("secret_sauce")
        self.driver.implicitly_wait(5)
        log = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/input")
        log.click()
        title = self.driver.title
        print(title)
        assert title == "Swag Labs"
        self.driver.implicitly_wait(5)
        menu = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button")
        menu.click()
        logout = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]")
        logout.click()
        if self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/input[1]"):
            print("Element exist")
        self.driver.close()
    def test_faild_login(self):
        # logowanie nieprawidłowy login i hasło
        login = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input")
        login.send_keys("standard_use")
        self.driver.implicitly_wait(5)
        password = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input")
        password.send_keys("secret_sauce")
        self.driver.implicitly_wait(5)
        log = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/input")
        log.click()
        self.driver.implicitly_wait(5)
        error1 = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        print(error1)
        assert error1 == "Epic sadface: Username and password do not match any user in this service", "Username and password do not match any user in this service"
        self.driver.quit()
    def test_empty_login(self):
    # log with empty login and password
        log = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/input")
        log.click()
        self.driver.implicitly_wait(5)
        error2 = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
        print(error2)
        assert error2 == "Epic sadface: Username is required", "Username is required"
        self.driver.quit()



