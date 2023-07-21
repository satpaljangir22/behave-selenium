from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def launch_browser(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless=new")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


def terminate_browser(context):
    context.driver.quit()
