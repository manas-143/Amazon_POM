def send_input(page, selector, search_item):  # function for sending input to  search box
    page.locator(selector).fill(search_item)


def click(page, selector):  # click function to perform click
    page.locator(selector).click()


def title(page):
    return page.title


def get_url(page):
    return page.url


def scroll(page):
    page.keyboard.press('End')


def get_text(page, selector):
    text = page.locator(selector).text_content()
    return text
