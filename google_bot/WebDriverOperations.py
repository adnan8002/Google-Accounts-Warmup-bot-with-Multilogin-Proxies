from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import random
from time import sleep


def human_clicker_click(driver_arg, xpath):
    element = WebDriverWait(driver_arg, 30).until(
    EC.presence_of_element_located((By.XPATH, xpath)))
    element.click()
def human_clicker_js3(driver_arg, xpath,index):
    element = WebDriverWait(driver_arg, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)))
    driver_arg.execute_script("arguments[0].click();", element[index])
def human_clicker_js_single_el(driver_arg, xpath):
    element = WebDriverWait(driver_arg, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)))
    randomIndex = random.randrange(len(element))
    driver_arg.execute_script("arguments[0].click();", element[randomIndex])
def human_typer(driver_arg, xpath, text: str):
    element = WebDriverWait(driver_arg, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    for s in text:
        element.send_keys(s)
        sleep(random.uniform(0.07, 0.7))
def human_clicker_js(driver_arg, xpath):
    element = WebDriverWait(driver_arg, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    driver_arg.execute_script("arguments[0].click();", element)

def random_wait(lower_limit, uper_limit):
        time_wait = random.randint(lower_limit, uper_limit)
        sleep(time_wait)

def send_keys_interval(el, string):
    for char in string:
        el.send_keys(char)
        rand_wait = random.uniform(0.03, 0.08)
        sleep(rand_wait)
    
        
