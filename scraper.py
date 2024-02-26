import requests
from bs4 import BeautifulSoup

# URL of the product page you want to monitor
url = 'https://www.sephora.com/product/summer-fridays-lip-butter-balm-P455936?skuId=2745289&icid2=products%20grid:p455936:product'

# Headers to simulate a real browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

def check_availability():
    print("Checking availability...")
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Look for the "Out of Stock" span by its "data-at" attribute
        availability_indicator = soup.find('span', attrs={'data-at': 'product_flag_label'})
        print(availability_indicator)

        # Check if the indicator is found and its text includes "Out of Stock"
        if availability_indicator and "Out of Stock" in availability_indicator.text:
            print("Product is out of stock.")
        else:
            print("Product might be available!")
    else:
        print(f"Failed to fetch the webpage, status code: {response.status_code}")

if __name__ == "__main__":
    check_availability()
