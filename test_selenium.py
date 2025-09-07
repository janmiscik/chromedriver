from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# spustenie Chrome s automatickým stiahnutím ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# otvorenie Google
driver.get("https://www.google.com")

# vypíš aktuálny titulok stránky
print("Titulok stránky:", driver.title)

# zatvor Chrome
driver.quit()
