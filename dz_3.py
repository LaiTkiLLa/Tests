from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")

driver = webdriver.Chrome(
    executable_path="C:\\Program Files\\Selenium\\chromedriver.exe",
    options = options
)
def auth_ya(login, user_password):
    try:
        driver.get('https://passport.yandex.ru/auth/')
        time.sleep(3)

        email = driver.find_element_by_id('passp-field-login')
        email.clear()
        email.send_keys(login)
        time.sleep(1)
        email.send_keys(Keys.ENTER)

        password = driver.find_element_by_id("passp-field-passwd")
        password.clear()
        password.send_keys(user_password)
        time.sleep(1)
        password.send_keys(Keys.ENTER)

    except Exception as ex:
        print(ex)
    # finally:
    #     driver.close()
    #     driver.quit()

auth_ya()
