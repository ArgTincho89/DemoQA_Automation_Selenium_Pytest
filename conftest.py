import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from utilities.test_data import TestData


@pytest.fixture(params=["chrome",  # "firefox", "edge"
                        ])
def initialize_driver(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("--headless")
        download_directory = "C:\\Users\\marti\\Downloads\\DemoQADownloads"
        prefs = {"download.default_directory": download_directory}
        chrome_options.add_experimental_option("prefs", prefs)
        
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
        #firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
    elif request.param == "edge":
         edge_options = EdgeOptions()
         edge_options.add_argument("--start-maximized") 
         #edge_options.add_argument("--headless")
         driver = webdriver.Edge(options=edge_options)

    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.url)

    # Checking recurrent Gateway error
    try:
        # Searching for the Gateway error message
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > center:nth-child(1) > h1")))
        print("Gateway error detected, refreshing...")
        driver.refresh()
        # Waiting for the page to load correctly
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > header > a > img")))
    except:
        pass

    yield driver
    print("Close Driver")
    driver.close()





"""@pytest.fixture(params=["chrome",  # "firefox", "edge"
                        ])
def initialize_driver(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        #chrome_options.add_argument("--headless")
        download_directory = "C:\\Users\\marti\\Downloads\\DemoQADownloads"
        prefs = {"download.default_directory": download_directory}
        chrome_options.add_experimental_option("prefs", prefs) 
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
        #firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
    elif request.param == "edge":
         edge_options = EdgeOptions()
         edge_options.add_argument("--start-maximized") 
         #edge_options.add_argument("--headless")
         driver = webdriver.Edge(options=edge_options)
    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.url)
    yield driver
    print("Close Driver")
    driver.close()"""



