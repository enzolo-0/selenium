from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    options = webdriver.ChromeOptions()
    # Options for Browsing
    options.add_argument("disable-infobars")
    options.add_argument("start-maximum")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    # options.add_argument("exclude-switches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://climate.nasa.gov/vital-signs/global-temperature/?intent=121")
    return driver


def main():
    driver = get_driver()
    # global_temp_path = "//*[@id='primary_column']/div/div[1]/div[2]/div"
    site_title_path = "//*[@id='primary_column']/header/h1"
    global_temp_values_path = "//*[@id='primary_column']/div/div[1]/div[2]"
    title = driver.find_element(By.XPATH, site_title_path)
    farenheit_values = driver.find_element(By.XPATH, global_temp_values_path)
    print(f"{title.text}: {farenheit_values.text}")
    driver.quit()


main()
