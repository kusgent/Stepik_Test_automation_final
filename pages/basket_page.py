from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Text about empty basket is not presented"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCTS_IN_BASKET), "Products in basket is presented, but should not be"
