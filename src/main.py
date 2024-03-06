from .workers.cracked_dev_api import CrackedDevApi
def main(driver):
    # driver.get("https://www.geeksforgeeks.org/how-to-get-title-of-a-webpage-using-selenium-in-python/")
    # print(driver.title)
    CrackedDevApi.get_cracked_dev_jobs(pageNo=1, pageSize=12);