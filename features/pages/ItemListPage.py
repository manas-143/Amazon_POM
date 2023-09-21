"""created a Item list class to sorting the items based on ratings"""


class ItemLists:
    RATINGS = "xpath =//li[@id='p_72/1318476031']"

    def __init__(self, page):
        self.page = page

    def click(self):
        self.page.locator(self.RATINGS).click()
