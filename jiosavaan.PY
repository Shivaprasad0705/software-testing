from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time


chromedriver_path = r'c:\Users\Shivaprasad p\Downloads\chromedriver_py-126.0.6478.126\chromedriver_py-126.0.6478.126\chromedriver_py\chromedriver_win64.exe'

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.jiosaavn.com/')

driver.maximize_window()

wait = WebDriverWait(driver, 5)
time.sleep(5)



search_box_xpath = '//*[@id="search"]/div[1]/div[1]/input[1]'
search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
search_box.click()
time.sleep(5)

search_icon_xpath = '//*[@id="search"]/div[1]/div[1]'
search_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, search_icon_xpath)))
search_icon.click()
time.sleep(5)


search_box.send_keys("Tum Se")
search_box.send_keys(Keys.RETURN)
time.sleep(5)

wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search"]/div[1]/div[1]/input[1]')))
button.click()
time.sleep(5)

TumSe_xpath='//*[@id="search"]/div[2]/div/div[1]/div[1]/article/div[1]/figure/figcaption/h4/a'
first_result = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, TumSe_xpath)))
first_result.click()
time.sleep(5)



play_button_xpath = '//*[@id="root"]/div[2]/div[1]/div/main/div[2]/figure/figcaption/div/p[1]/a'
play_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, play_button_xpath)))
play_button.click()

time.sleep(5)

home_button_xpath = '//*[@id="sidebar_library"]/li[1]/a/strong'
home_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, home_button_xpath)))
home_button.click()

time.sleep(3)

playlist_xpath='//*[@id="telugu"]'
plus_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, playlist_xpath))
)
plus_button.click()

time.sleep(3)

search_icon_xpath = '//*[@id="search"]/div[1]/div[1]'
search_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, search_icon_xpath)))
search_icon.click()


search_box.send_keys("arya 2")
search_box.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search"]/div[1]/div[1]/input[1]')))
button.click()

arya2_xpath='//*[@id="search"]/div[2]/div/div[1]/div[1]/article/div[1]/figure/figcaption/h4/a'
first_result = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, arya2_xpath)))
first_result.click()

time.sleep(3)

play_button_xpath = '//*[@id="root"]/div[2]/div[1]/div/main/figure/figcaption/div/p[3]/span'
play_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, play_button_xpath)))
play_button.click()
add_to_library_xpath='//*[@id="root"]/div[2]/aside[3]/div/div[2]/div/div/nav/ul/li[3]/a'
add_to_library = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, add_to_library_xpath)))
add_to_library.click()

time.sleep(3)
