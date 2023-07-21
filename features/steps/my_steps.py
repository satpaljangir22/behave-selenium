from behave import *


@given('User is on google search page')
def step_impl(context):
    page_url = context.driver.current_url
    assert page_url in "https://www.google.com/"


@then('verify google search page title')
def step_impl(context):
    title = context.driver.title
    assert title in "Google"


@given('User is on facebook login page')
def step_impl(context):
    context.driver.get("https://www.facebook.com/")
    page_url = context.driver.current_url
    assert page_url in "https://www.facebook.com/"


@then('verify facebook login page title')
def step_impl(context):
    title = context.driver.title
    assert title == "Facebook login page"
