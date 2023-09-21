"""Checkout class is used for comparing the value of cart and total price"""
class CheckOut:
    CART_ICON = "xpath=//*[@class='nav-cart-icon nav-sprite']"
    PRICE_TAG = "xpath=//*[@id='sc-subtotal-amount-buybox']/span"

    def __init__(self, page):
        self.page = page

    def price_compare(self):
        self.page.locator(self.CART_ICON).click()  # going to cart
        final_price = self.page.locator(self.PRICE_TAG).inner_text()  # extracting the total price
        price = final_price.replace(",", "")
        cart_amt = float(price)
        return cart_amt



