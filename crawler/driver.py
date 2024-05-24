# Setting up Selenium WebDriver for Chrome

# Importing necessary modules
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# Configuring Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Initializing WebDriver with Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

# Maximizing the browser window
driver.maximize_window()
