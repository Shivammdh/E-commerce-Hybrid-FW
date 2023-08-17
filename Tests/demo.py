import time
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Change this to your preferred browser driver.

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_case_1(self):
        try:
            driver=self.driver
            # alert = Alert(driver)
            driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
            driver.find_element(By.NAME, "confirmati").click()
            alt = driver.switch_to.alert
            print(alt.text)
            alt.dismiss()
            time.sleep(3)
        except Exception as e:
            self.fail(f"Test case 1 failed with exception: {e}")

    def test_case_2(self):
        try:
            driver=self.driver
            driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

            driver.find_element(By.NAME, "prompt").click()
            alt = driver.switch_to.alert
            print(alt.text)
            alt.send_keys("Hi i am inside alert..")

            time.sleep(5)
            alt.accept()
            time.sleep(3)
        except Exception as e:
            self.fail(f"Test case 2 failed with exception: {e}")



    def test_case_3(self):
        try:
            driver=self.driver
            driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

            driver.find_element(By.NAME, "alert").click()
            alt = driver.switch_to.alert
            print(alt.text)
            alt.accept()
            time.sleep(3)
        except Exception as e:
            self.fail(f"Test case 3 failed with exception: {e}")

if __name__ == "__main__":
    # Create the test suite and add test cases to it
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_case_1"))
    suite.addTest(MyTestCase("test_case_2"))
    suite.addTest(MyTestCase("test_case_3"))

    # Run the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    # Check if any test case failed, and if so, stop further execution
    if not result.wasSuccessful():
        raise SystemExit(1)
