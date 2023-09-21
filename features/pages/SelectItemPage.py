"""select item class is used for selecting the desire number of items according to the user"""


class SelectItem:
    ITEM_LISTS = "xpath=//span[@class='a-size-medium a-color-base a-text-normal']"
    ITEM_AMT = "xpath=//span[@id='tp_price_block_total_price_ww']/descendant::span[@class='a-price-whole']"
    ADD_TO_CART = "xpath=//*[@id='add-to-cart-button']"

    def __init__(self, page):
        self.page1 = None
        self.page = page

    def item_select(self, number):
        all_items = self.page.locator(self.ITEM_LISTS)
        amount = []

        for i in range(int(number)):
            with self.page.expect_popup() as page1_info:
                all_items.nth(i).click()  # click on each laptop
            self.page1 = page1_info.value  # going to the next tab
            amt = self.page1.locator(self.ITEM_AMT).inner_text()  # locator for amount
            amount.append(float(amt.replace(",", "")))  # storing each laptop value in float
            self.page1.locator(self.ADD_TO_CART).click()  # adding the laptop to cart
            self.page1.close()  # closing the new tab
        return amount  # returning the amount to base page
