from playwright.sync_api import Page,expect

def test_locators(page:Page):
    page.goto("https://www.facebook.com/")
    page.pause()