# import time
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

sev = Service()
driver = webdriver.Chrome(options=options, service=sev)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/loginpagePractise/')
driver.find_element(By.XPATH, "//a[@target='_blank']").click()

nextwindow = driver.window_handles
driver.switch_to.window(nextwindow[1])

t1 = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
t2 = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
driver.close()
driver.switch_to.window(nextwindow[0])
driver.find_element(By.ID, 'username').send_keys(t2)
driver.find_element(By.ID, "password").send_keys('learning')
driver.find_element(By.XPATH, "//input[@value='admin']").click()
driver.find_element(By.XPATH, "//select[@data-style='btn-info']").click()
driver.find_element(By.XPATH, "//option[@value='stud']").click()
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
