from playwright.sync_api import Page,expect

def test_form(page:Page):
    page.goto("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    # page.get_by_placeholder("First Name").fill("playwright")
    #id
    page.locator("#name").fill("user name")

    #class
    # page.locator(".form-control").fill("user name")

    # page.get_by_placeholder("name@example.com").fill("user@gmail.com")
    page.locator('//*[@id="email"]').fill("user@gmail.com")

    page.locator("#gender").click()



    # page.get_by_placeholder("Enter Mobile Number").fill("96876542310")
    page.locator("#mobile").fill("987654321")

    page.locator(".dob").fill("05-03-2000")
    page.get_by_placeholder("Enter Subject").fill("Maths")
    page.get_by_placeholder("Currend Address").fill("Ahmedabad")
    page.pause()