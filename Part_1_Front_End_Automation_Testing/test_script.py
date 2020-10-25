from library import TagName
import constants as const
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import allure

class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(const.driver_path)

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        
        tagname_obj = TagName(self.driver)

        #Navigate to StackOverflow (https://stackoverflow.com/)
        self.driver.get(const.url)

        #Click Log in button
        element = tagname_obj.find_elements(self.driver, 'xpath', const.login_button)
        tagname_obj.click_element(element)

        #Enter email id
        element = tagname_obj.find_elements(self.driver, 'id', 'email')
        tagname_obj.enter_text(element, const.email_id)

        #Enter password
        element = tagname_obj.find_elements(self.driver, 'id', 'password')
        tagname_obj.enter_text(element, const.password)

        #Click Submit
        element = tagname_obj.find_elements(self.driver, 'id', 'submit-button')
        tagname_obj.click_element(element)

        #Click on Tags
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, 'nav-tags')))
        element = tagname_obj.find_elements(self.driver, 'xpath', const.tags_link)
        tagname_obj.click_element(element)

        #Click on Name link
        element = tagname_obj.find_elements(self.driver, 'xpath', const.name_link)
        tagname_obj.click_element(element)

        #element_list = self.driver.find_elements_by_xpath("//a[@class='post-tag']/../..")
        #element_list = self.driver.find_elements_by_xpath("//div[@class='grid jc-space-between ai-center mb12']")

        tag_name, question_count = tagname_obj.get_tag_with_highest_question_count(self.driver) 
        print(tag_name, question_count)
            
if __name__ == '__main__':
    unittest.main()