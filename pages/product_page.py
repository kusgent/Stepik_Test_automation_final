from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_link.click()

    def should_be_message_about_add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ABOUT_ADDITION), "Message about addition product is not presented"
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDITION).text
        assert message == name, "Added another product"

    def should_be_message_with_basket_cost(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_WITH_BASKET_COST), "Message with basket cost is not presented"
        cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_BASKET_COST).text
        assert message == cost, "Basket cost is calculated incorrectly"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.MESSAGE_ABOUT_ADDITION), "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDITION), "Success message is not disappeared"
