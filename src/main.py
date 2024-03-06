def main(driver):
    driver.get("https://www.geeksforgeeks.org/how-to-get-title-of-a-webpage-using-selenium-in-python/")
    print(driver.title)