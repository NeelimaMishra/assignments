# Part 1: frontend automation testing
# This library contains utilities and tagname class

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import constants as const


class Utilities:
    """
    This class contains utilities methods
    """
    def __init__(self, driver):
        driver.implicitly_wait(30)
    
    def click_element(self, element):
        element.click()
    
    def enter_text(self, element, text):
        element.send_keys(text)
    
    def find_elements(self, driver, find_by, criteria):
        if find_by == 'id':
            return driver.find_element_by_id(criteria)

        elif find_by == 'xpath':
            return driver.find_element_by_xpath(criteria)

class TagName(Utilities):
    def __init__(self, driver):
        Utilities.__init__(self, driver)

    def get_tag_with_highest_question_count(self, driver):
        import pdb; pdb.set_trace()
        element_list = driver.find_elements_by_xpath(const.element_list)
        question_count = None
        for element in element_list:
            question_text = element.text
            count = int(question_text.split(' ')[0])

            if (question_count is None) or (count > question_count):
                question_count = count
                tag_name = element.find_element_by_xpath(const.tag_name).text
        return tag_name, question_count
