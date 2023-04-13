from base_page import BasePage
from search_locators import SearchLocators


class Main(BasePage):

    def click_on_button(self, locator_for_button):
        return self.find_element(locator_for_button, time=2).click()

    def find_response_window(self):
        return self.find_element(SearchLocators.RESPONSE_WINDOW)

    def find_request_window(self):
        return self.find_element(SearchLocators.REQUEST_WINDOW)

    def find_response_code(self):
        return self.find_element(SearchLocators.RESPONSE_CODE)
