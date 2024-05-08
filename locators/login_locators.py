from selenium.webdriver.common.by import By

class LoginLocators:
    ACCOUNT_LINK = ("css selector", "a#nav-link-accountList")
    EMAIL_OR_PHONE_FIELD = ("css selector", "input#ap_email")
    CONTINUE_BTN = ("css selector", "input#continue")
    PASSWORD_FILD = ("css selector", "input#ap_password")
    SIGNIN_BTN = ("css selector", "input#signInSubmit")
    NOT_NOW_LINK = ("css selector", "a#ap-account-fixup-phone-skip-link")
    LOG_IN_TEXT = ("css selector", "span#nav-link-accountList-nav-line-1")
    LOGIN_NAME = "Hello, Red"
    SIN_IN_TEXT = "Sign in"
    CONDITIONS_OF_USE = ("xpath selector", "//div[@id='legalTextRow']/a[contains(text(), 'Conditions of Use')]")
    PRIVACY_NOTICE = ("xpath selector", "//div[@id='legalTextRow']/a[contains(text(), 'Privacy Notice')]")
    NEED_HELP = ("css selector", "span.a-expander-prompt")
    SIN_OUT = ("css selector", "a#nav-item-signout")
    SIN_IN_PAGE = ("css selector", "h1.a-spacing-small")
