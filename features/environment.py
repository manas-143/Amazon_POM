from utilities import Configreader
from playwright.sync_api import *

start = sync_playwright().start()


def before_scenario(context, scenario):
    browser_name = Configreader.read_configuration("basic info", "browser")
    if browser_name == "chrome":
        browser = start.chromium.launch(headless=False, slow_mo=3000)
        context.tab = browser.new_context()
        context.page = context.tab.new_page()
        context.page.goto(Configreader.read_configuration("basic info", "url"))

    elif browser_name == "firefox":
        browser = start.firefox.launch(headless=False, slow_mo=5000)
        context.tab = browser.new_context()
        context.page = context.tab.new_page()
        context.page.goto(Configreader.read_configuration("basic info", "url"))


def after_scenario(context, scenario):
    context.page.close()
