# import time
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

sev = Service()
driver = webdriver.Chrome(options=options, service=sev)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
# o use for first window and 1 use for second window
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
