from behave import *
from selenium import webdriver
from tests.acceptance.page_model.home_page import HomePage


use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('/Users/allyboy08/Downloads/chromedriver_win32/chromedriver')
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome('/Users/allyboy08/Downloads/chromedriver_win32/chromedriver')
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url
    
    
@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.driver.current_url == expected_url