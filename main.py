from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from fp.fp import FreeProxy
import time

PROXY = FreeProxy().get()

service = Service(executable_path="chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY[6:])

driver = webdriver.Chrome(
    service=service,
    options=options
    )

driver.get('chrome://settings/clearBrowserData')
driver.delete_all_cookies()
driver.get("https://www.instagram.com/")

def login(username, password):
    username_field = driver.find_element(by=By.NAME, value="username")
    username_field.send_keys(username)

    pass_field = driver.find_element(by=By.NAME, value="password")
    pass_field.send_keys(password)

    login_button = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
    login_button.click()

def close_dialog():
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div").click()

    time.sleep(3)
    driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()

def search():
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]").click()

    time.sleep(3)
    search_field = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
    search_field.send_keys("_cruz_rider_" + "\ue007")

    time.sleep(3)
    result_div = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div")
    links = result_div.find_element(by=By.TAG_NAME, value="a").get_attribute('href')

    driver.get(links)

    time.sleep(3)
    follow_button = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[2]/div/div/div[2]/div/div/button")
    follow_button.click()

time.sleep(3)
login("rider.of.cruz.0902@gmail.com", "Hello@RM8")

time.sleep(5)
close_dialog()

time.sleep(3)
search()

time.sleep(10)
driver.quit()