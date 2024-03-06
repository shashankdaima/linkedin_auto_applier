from .workers.cracked_dev_api import CrackedDevApi

# from webdriver_manager import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def main(driver: WebDriver):
    crackedDevJobs = CrackedDevApi.get_cracked_dev_jobs(pageNo=1, pageSize=12)
    driver.get(crackedDevJobs[0]["apply_url"])
    # print(driver.title)
    driver.find_element(
        by=By.XPATH,
        value="/html/body/div[2]/section/div[2]/div/div/aside/div[1]/div/div[3]/a",
    )
    while True:
        a = 0
