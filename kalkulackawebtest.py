import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class KalkulackaWebTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_scitani(self):
        self.driver.get("http://127.0.0.1:8000/")

        cislo1 = self.driver.find_element(By.ID, "cislo1")
        cislo1.clear()
        cislo1.send_keys("25")

        cislo2 = self.driver.find_element(By.ID, "cislo2")
        cislo2.clear()
        cislo2.send_keys("13")

        operace = Select(self.driver.find_element(By.ID, 'operace'))
        operace.select_by_value('+')

        self.driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()

        vysledek = self.driver.find_element(By.ID,'vysledek')
        self.assertEqual(vysledek.text,"38")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
