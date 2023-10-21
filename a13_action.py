# import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

sev = Service()
driver = webdriver.Chrome(options=options, service=sev)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
action = ActionChains(driver)
# action.context_click()
# action.double_click()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

"""
The code you provided is written in Python and seems to be using the Selenium WebDriver library to perform various
actions on a web page. The `ActionChains` class in Selenium allows you to chain multiple actions together and perform
them as a sequence. Here's how to use the `ActionChains` class to perform these actions:

1. Import the necessary libraries:

```python
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

2. Create an instance of the `ActionChains` class, passing the WebDriver instance as an argument:

```python
action = ActionChains(driver)

3. Chain the actions together:

a. `context_click()`: Right-click on an element.

```python
action.context_click()

b. `double_click()`: Double-click on an element.

```python
action.double_click()

c. `drag_and_drop(source, target)`: Drag an element from a source location and drop it onto a target location.

```python
source_element = driver.find_element(By.ID, "source_element_id")
target_element = driver.find_element(By.ID, "target_element_id")
action.drag_and_drop(source_element, target_element)

d. `move_to_element(element)`: Move the mouse cursor to a specific element on the page.

```python
element_to_hover = driver.find_element(By.ID, "mousehover")
action.move_to_element(element_to_hover)

e. `context_click(element)`: Right-click on a specific element.

```python
element_to_context_click = driver.find_element(By.LINK_TEXT, "Top")
action.context_click(element_to_context_click)

f. `click()`: Click on the currently hovered element.

```python
reload_element = driver.find_element(By.LINK_TEXT, "Reload")
action.move_to_element(reload_element).click()

4. Finally, perform the actions:

```python
action.perform()

This sequence of actions will be executed in the order specified when you call `perform()`. Make sure to replace `
"source_element_id"` and `"target_element_id"` with the appropriate element identifiers from your web page.

Remember to set up your Selenium WebDriver instance (`driver`) and navigate to the desired webpage before executing 
these actions.
"""