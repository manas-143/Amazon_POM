"""created a class home page to perform all the tasks in amazon homepage such as searching of product"""


class HomePage:
    SEARCH_BOX = "xpath=//*[@id='twotabsearchtextbox']"
    SEARCH_BTN = "xpath=//*[@id='nav-search-submit-button']"

    def __init__(self, page):
        self.page = page

    def send_input(self, search_item):
        self.page.locator(self.SEARCH_BOX).fill(search_item)

    def click(self):
        self.page.locator(self.SEARCH_BTN).click()
