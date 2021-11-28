from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 > h1")
    MESSAGE_ABOUT_ADDITION = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) strong")
    PRODUCT_COST = (By.CSS_SELECTOR, ".col-sm-6 > .price_color")
    MESSAGE_WITH_BASKET_COST = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > [class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "h2.col-sm-6")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
