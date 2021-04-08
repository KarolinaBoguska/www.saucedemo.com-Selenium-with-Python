from time import sleep
from selenium import webdriver
import unittest

class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(5)
        login = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input")
        login.send_keys("standard_user")
        self.driver.implicitly_wait(5)
        password = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input")
        password.send_keys("secret_sauce")
        self.driver.implicitly_wait(5)
        log = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/input")
        log.click()
        self.driver.implicitly_wait(5)
    def test_add(self):
        add = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        add.click()
        self.driver.implicitly_wait(5)
        cart = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/div[3]/a/span").text
        print(cart)
        assert cart == "1"
        self.driver.close()
    def test_add_and_remove(self):
        add = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        add.click()
        remove = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        remove.click()
        self.driver.implicitly_wait(5)
        add = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button").text
        print(add)
        assert add == "ADD TO CART"
        self.driver.close()
    def test_watch_products(self):
        bike_light = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[2]/div[1]/a/img")
        bike_light.click()
        self.driver.implicitly_wait(5)
        price = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[2]/div[3]").text
        print(price)
        assert price == "$9.99"
        self.driver.close()