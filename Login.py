from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

url = "http://gold2cashexchange.co.in/Signin.html"
sobj = Service("C:\\Selenium\\Drivers\\chromedriver-win64\\chromedriver.exe")

@Given("launch the chrome browser and load the application")
def launch_application(context):
    global driver
    driver = webdriver.Chrome(service=sobj)
    driver.get(url)
    time.sleep(3)

@When("enter the username, password and click login button")
def login_check(context):
    driver.find_element(By.NAME, "username").send_keys("Abirashmi")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("Abirashmi")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/div/button[1]").click()
    time.sleep(2)

@Then("verify the result")
def verify_result(context):
    result = driver.find_element(By.ID, "info").text
    print(result)
    driver.close()
