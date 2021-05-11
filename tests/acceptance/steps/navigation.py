from behave import *
from selenium import webdriver
import sys
sys.path.append("tests/acceptance/page_model")
from page_model.home_page import HomePage
from page_model.blog_page import BlogPage
from page_model.new_post_page import NewPostPage


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


@given('I am on the new post page')
def step_impl(context):
    context.driver = webdriver.Chrome('/Users/allyboy08/Downloads/chromedriver_win32/chromedriver')
    page = NewPostPage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url
    
    
@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url