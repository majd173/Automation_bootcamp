from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_click_me_btn():
    driver = webdriver.Chrome()
    driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')
    time.sleep(1.5)
    click_me = driver.find_element(By.XPATH, '//*[@id="button1"]')
    time.sleep(1.5)
    click_me.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.quit()


def test_insert_name_email():
    driver = webdriver.Chrome()
    driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')
    time.sleep(1)
    name = driver.find_element(By.XPATH, '//*[@id="et_pb_contact_name_0"]')
    time.sleep(1)
    name.send_keys('majd', Keys.RETURN)
    email = driver.find_element(By.XPATH, '//*[@id="et_pb_contact_email_0"]')
    email.send_keys('majdb173@gmail.com', Keys.RETURN)
    time.sleep(1)
    click_btn = driver.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[2]/form/div/button')
    click_btn.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.quit()


def test_gender_checkbox(gender):
    driver = webdriver.Chrome()
    driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')
    time.sleep(3)
    select_gender = driver.find_element(By.XPATH, f'//input[@value="{gender}"]')
    time.sleep(3)
    selected = select_gender.is_selected()
    if selected:
        print(f"{gender} checkbox is selected")
    else:
        select_gender.click()
        print(f"{gender} checkbox is selected")

    driver.quit()


def select_from_tab():
    driver = webdriver.Chrome()
    driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')
    time.sleep(1)
    select_gender = driver.find_element(By.XPATH, '//ul[@id="menu-main-menu"]//a[contains(text(),"Selenium C#")]')
    time.sleep(1)
    select_gender.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.quit()


def test_solve_quiz(quiz_num, box):
    driver = webdriver.Chrome()
    driver.get('https://ultimateqa.com/complicated-page/')
    time.sleep(1)
    locate_quiz = driver.find_element(By.XPATH, f'// div[ @ id = "et_pb_contact_form_{quiz_num}"]//span')
    locate_box = driver.find_element(By.XPATH, f'//input[@name = "et_pb_contact_captcha_{box}"]')
    parts = locate_quiz.text.split()
    solution = int(parts[0]) + int(parts[2])
    locate_box.send_keys(Keys.RETURN, solution)
    print(parts[0], parts[1], parts[2], "=", solution)

    driver.quit()











# test_click_me_btn()
# test_insert_name_email()
# test_gender_checkbox('male')
# test_gender_checkbox('female')
# test_gender_checkbox('other')
# select_from_tab()
test_solve_quiz("0", "0")



