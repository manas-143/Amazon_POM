from behave import *

from features.pages.HomePage import HomePage  # imported home page module to perform actions in homepage
from features.pages.ItemListPage import ItemLists  # imported Item list page module to perform item sorting
from features.pages.SelectItemPage import SelectItem  # imported select item page module to select the items
from features.pages.CheckOutPage import CheckOut  # imported check out page module to compare the value


amount = []  # to store the price of each item


@given(u'User is on the amazon website search for "{search_query}"')
def step_impl(context, search_query):
    home_page = HomePage(context.page)
    home_page.send_input(search_query)  # item that user wants to search for
    home_page.click()


@when(u'User filter by ratings')
def filtering_the_items(context):
    item_list = ItemLists(context.page)
    item_list.click()


@when(u'add top "{number}" laptops to the cart')
def adding_multiple_items(context, number):
    num = int(number)  # total number that user wants to buy
    global amount
    select_item = SelectItem(context.page)
    x = select_item.item_select(num)
    amount = x


@then(u'the total amount in the cart should match the laptop prices')
def price_compare(context):
    check_out = CheckOut(context.page)
    cart_amt = check_out.price_compare()
    laptop_amt = sum(amount)
    assert laptop_amt == cart_amt, "Amount not matching"  # comparing the price
    print("Test case passed")

