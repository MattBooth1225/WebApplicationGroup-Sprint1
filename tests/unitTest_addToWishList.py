import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import warnings


# DESC:   Unit test file to determine if a Product can be successfully added to the user's Wish List

class AddProduct(unittest.TestCase):

    # set up the test class - assign the driver to Chrome
    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.simplefilter('ignore', ResourceWarning)  # ignore resource warning if it occurs

    # Test if a product was successfully added to the user's wishlist
    # Product is added to Wish List successfully if its name can be located on the screen
    def test_ll(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")

        # find the username and password input boxes and login - Wish List is only available to authenticated users
        user = "instructor"  # must be a valid username for the application
        pwd = "maverick1"  # must be the password for a valid user
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

        # go to 'All Products' page
        driver.get("http://127.0.0.1:8000/store/all-products")
        time.sleep(3)

        # if a product already exists, click on it & add to wish list
        if driver.find_element(By.XPATH, '//*[@id="product_container"]/div/a'):
            # click on the test product
            driver.find_element(By.XPATH, '//*[@id="product_container"]/div/a').click()
            time.sleep(3)

            # click on 'Add to Wish List' button
            driver.find_element(By.XPATH, '//*[@id="prod_detail_container"]/div/form[2]/input[3]').click()
            time.sleep(3)

        # input product information if it does not exist
        else:
            # go to admin page
            driver.get("http://127.0.0.1:8000/admin")
            time.sleep(3)

            # find 'Products' model and click 'Add'
            driver.find_element(By.XPATH, '//*[@id="content-main"]/div[3]/table/tbody/tr[8]/td[1]/a').click()
            time.sleep(3)

            # input product information
            select = Select(driver.find_element(By.ID, 'id_category'))
            select.select_by_visible_text('Music')
            elem = driver.find_element(By.ID, 'id_name')
            elem.send_keys('test_product')
            elem = driver.find_element(By.ID, 'id_price')
            elem.send_keys('19.99')
            select = Select(driver.find_element(By.ID, 'id_image'))
            select.select_by_visible_text('test_image')
            elem = driver.find_element(By.ID, 'id_desc')
            elem.send_keys('test product description')

            # click 'Save'
            driver.find_element(By.XPATH, '//*[@id="product_form"]/div/div/input[1]').click()
            time.sleep(3)

            # go back to site's 'All Products' page
            driver.get("http://127.0.0.1:8000/store/all-products")
            time.sleep(3)

            # click on the test product
            driver.find_element(By.XPATH, '//*[@id="product_container"]/div/a').click()
            time.sleep(3)

            # click on 'Add to Wish List' button
            driver.find_element(By.XPATH, '//*[@id="prod_detail_container"]/div/form[2]/input[3]').click()
            time.sleep(3)

        try:
            # verify that the Product's name is visible on the screen
            elem = driver.find_element(By.XPATH, '//*[text()="test_product"]')
            print("Test passed - Product added to Wish List successfully ")
            assert True
        except NoSuchElementException:
            self.fail("Product was not added to Wish List - test failed")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
