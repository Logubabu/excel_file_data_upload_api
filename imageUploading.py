import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

cpath = r"D:\chromedriver.exe"
driver = webdriver.Chrome(cpath)
wait = WebDriverWait(driver, 20)
# chrome_options = Options()
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "http://localhost:1337/admin/content-manager/collectionType/api::party-wing.party-wing?page=1&pageSize=10&plugins[i18n][locale]=en"
)
time.sleep(5)
input_1 = driver.find_element(
    by=By.XPATH,
    value=
    "/html/body/div[1]/div[2]/div/main/div[1]/form/div[2]/div[1]/div/div/div/input",
)
input_2 = driver.find_element(
    by=By.XPATH,
    value=
    "/html/body/div[1]/div[2]/div/main/div[1]/form/div[2]/div[2]/div/div/div/input",
)
input_1.send_keys("loganathan@thepenindia.com")
input_2.send_keys("Logu8799")
time.sleep(5)
log_button = driver.find_element(
    by=By.XPATH,
    value="/html/body/div[1]/div[2]/div/main/div[1]/form/div[2]/button").click(
    )
time.sleep(5)

id = 294
driver.get(
    f"http://localhost:1337/admin/content-manager/collectionType/api::party-wing.party-wing/{id}?plugins[i18n][locale]=en"
)
time.sleep(5)
# input_3 = driver.find_element(
#     by=By.ID,
#     value="Name",
# )
# input_3.send_keys("loganathan@thepenindia.com")
# time.sleep(5)
img_path = "D:\PEN INDIA\automation\image upload\6.jpg.jpg"
img_button = driver.find_element(
    by=By.XPATH,
    value='//*[@id="carouselinput-14"]/div/section/div/div/button',
    # /html/body/div[11]/div/div/div/div/div[2]/div[1]/div[2]/button[2]
).click()

time.sleep(5)
# ok =  driver.find_element_by_xpath('//*[@id="discount-marketing-modal"]/footer/button')
# ActionChains(driver).move_to_element(img_button).pause(1).click(
#     img_button).perform()
# x=driver.find_element_by_xpath('//*[@id="discount-marketing-modal"]/header/button/svg').click()
add_button = driver.find_element(
    by=By.XPATH,
    value='/html/body/div[11]/div/div/div/div/div[2]/div[1]/div[2]/button[2]',
).click()
time.sleep(5)

# browse_button = driver.find_element(
#     by=By.XPATH,
#     value=
#     # '//*[@id="tabgroup-61-0-tabpanel"]/form/div[1]/label/div/div/div/input',
#     '//*[@id="tabgroup-61-0-tabpanel"]/form/div[1]/label/div/div/div/div[3]'
# ).click()
# input_3 = wait.until(
#     EC.presence_of_element_located(
#         (By.XPATH, '//*[@id="carouselinput-14"]/div/section/div/div/button'
#          ))).send_keys(img_path)
# input_3 = driver.find_element(
#     by=By.ID,
#     value="Description",
# )
# input_3.send_keys("loganathan@thepenindia.com")
time.sleep(5)
save_button = driver.find_element(
    by=By.XPATH,
    value=
    "/html/body/div[1]/div[2]/div/div/div/div/form/main/div[1]/div/div[2]/div[2]/button[2]",
).click()
time.sleep(5)
dropdown = driver.find_element(
    by=By.XPATH,
    value=
    "/html/body/div[1]/div[2]/div/div/div/div/form/main/div[2]/div/div[2]/div/div/aside[2]/div[2]/div[2]/div[1]/div/div/div/button",
).click()
time.sleep(5)
button = driver.find_element(
    by=By.XPATH,
    value=
    '//*[@id="main-content"]/div[2]/div/div[2]/div/div/aside[2]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div',
)
