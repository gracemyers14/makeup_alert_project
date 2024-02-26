from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Correctly initialize the WebDriver for Chrome on a single line
# Initialize the WebDriver for Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the Sephora product page
driver.get('https://www.sephora.com/product/summer-fridays-lip-butter-balm-P455936?skuId=2745289&icid2=products%20grid:p455936:product')

# Wait for the page to load and JavaScript to execute
driver.implicitly_wait(10)

try:
    # Try to find the "Out of Stock" indicator by its data attribute
    availability_indicator = driver.find_element(By.CSS_SELECTOR, 
'span[data-at="product_flag_label"]')
    if availability_indicator:
        print("Product is out of stock.")
    else:
        print("Product might be available!")
except Exception as e:
    # If the element is not found, print the exception and assume the 
    #product might be available
    print(e)
    print("Product might be available!")

# Close the browser window
driver.quit()

