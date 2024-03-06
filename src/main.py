from .workers.cracked_dev_api import CrackedDevApi
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
def main(driver:WebDriver):
    crackedDevJobs= CrackedDevApi.get_cracked_dev_jobs(pageNo=1, pageSize=12);
    # for i in range(len(crackedDevJobs)):
    driver.get(crackedDevJobs[0]["apply_url"])
    time.sleep(2)
    url_to_job=(driver.find_element(by=By.XPATH,value= "/html/body/div[2]/section/div[2]/div/div/aside/div[1]/div/div[3]/a").get_attribute("href"))
    driver.get(url=url_to_job)
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 200)")
    while(True):
        a=0;
    