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
        checkout = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/button[2]")
        checkout.click()
        information = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/span").text
        print(information)
        assert information == "CHECKOUT: YOUR INFORMATION"
    def test_empty_card_information(self):
        contin = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/input")
        contin.click()
        error = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3").text
        print(error)
        assert error == "Error: First Name is required"
        self.driver.close()
    def test_finish_shopping(self):
        first_name = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input")
        first_name.send_keys("Karolina")
        last_name = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input")
        last_name.send_keys("Nowak")
        postal_code = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input")
        postal_code.send_keys("18400")
        contin = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/input")
        contin.click()
        overview = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/span").text
        print(overview)
        assert overview == ("CHECKOUT: OVERVIEW")
        summary = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/div[5]").text
        print(summary)
        assert summary == ("Item total: $55.97")
        finish = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/div[8]/button[2]")
        finish.click()
        completed = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/span").text
        print(completed)
        assert completed == ("CHECKOUT: COMPLETE!")
        self.driver.close()


