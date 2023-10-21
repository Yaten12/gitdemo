import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

sev = Service()
driver = webdriver.Chrome(options=options, service=sev)
driver.implicitly_wait(8)

expextedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

"""
1. Implicity_wait replace the time.sleep
2. in which we will not define time.sleep every because this is working as globally
3. if we are using 5 sec and process is execute in 2 sec it will not take 3 mor sec it will execute same time after 2sec
4. it is time saving and execute in every line automatically if define as globally.
5. Implicit_wait not working on List of element or two or more elements (.find_elements())
6. it is working on (find_element()) only
"""

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)

assert count > 0

for result in results:
    actualList.append(result.find_element(By.XPATH, 'h4').text)
    result.find_element(By.XPATH, "div/button").click()

print(actualList)

assert expextedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text() ='PROCEED TO CHECKOUT']").click()

# time.sleep(3)
# table locator

price1 = int(driver.find_element(By.XPATH, "(//p[contains(text(),'48')])[2]").text)
price2 = int(driver.find_element(By.XPATH, "(//p[contains(text(), '160')])[2]").text)
price3 = int(driver.find_element(By.XPATH, "(//p[contains(text(), '180')])[2]").text)
price = price3 + price1 + price2
print(price)
amount = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)

# this is checking for Total amount = add to cart item value.
assert amount == price

driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()
# time.sleep(8)

"""
Explicity_wait  
1. is using for particular element 
2. Implicity_wait works globally but Explicity_wait works on particular element.
3. its help for dynamically element we don't know how much time it will take to load the element 
   so it is taking 10 sec and if we using Implicity_wait for that so  Implicity_wait waits (10 sec) for every time
   and when i am using Explicity_wait  it will take time only that element only.
"""

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
print(driver.find_element(By.CSS_SELECTOR, '.promoInfo').text)
assert driver.find_element(By.CSS_SELECTOR, '.promoInfo').text == 'Code applied ..!'


discount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)

print(discount)
# this is checking for Total amount > to discount value.
assert amount > discount
