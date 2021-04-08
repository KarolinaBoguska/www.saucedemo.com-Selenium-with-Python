from time import sleep
from selenium import webdriver
import unittest

class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        # create your card and show card
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
        # reset app state
        menu = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button")
        menu.click()
        self.driver.implicitly_wait(5)
        reset = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[4]")
        reset.click()
        close_menu = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/button")
        close_menu.click()
        self.driver.implicitly_wait(5)
        add1 = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        add1.click()
        add2 = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button")
        add2.click()
        add3 = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button")
        add3.click()
        cart = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        cart.click()
        self.driver.implicitly_wait(5)
    def test_remove_from_cart(self):
        cart = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/div[3]/a/span").text
        print(cart)
        assert cart == "3"
        remove = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button")
        remove.click()
        cart = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/div[3]/a/span").text
        print(cart)
        assert cart == "2"
        self.driver.close()
    def test_continue_shopping(self):
        continue_shopping = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/button[1]")
        continue_shopping.click()
        product_page = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/span").text
        print(product_page)
        assert product_page == "PRODUCTS"
        self.driver.close()
    def test_checkout_shopping(self):
        checkout = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/button[2]")
        checkout.click()
        your_card = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/span").text
        print(your_card)
        assert your_card == "CHECKOUT: YOUR INFORMATION"
        self.driver.close()


