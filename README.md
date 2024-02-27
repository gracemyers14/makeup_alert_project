# Makeup Alert Project

## Overview

The Makeup Alert Project is a Python-based web scraping tool designed to 
monitor the availability of specific makeup products online. When the 
desired product becomes available, the user is notified, enabling them to 
purchase the product before it sells out again. This tool is particularly 
useful for tracking high-demand items that sell out quickly.

## Installation

Before running the project, make sure you have Python installed. This project was developed using Python 3.9. Follow these steps to 
install the necessary dependencies(all done on terminal on mac):


Clone the repository
git clone https://github.com/yourusername/makeup_alert_project.git

Navigate to the project directory
cd makeup_alert_project

Install dependencies
pip install -r requirements.txt

To start the product availability monitor, run the selenium_scraper.py 
script from the command line with the necessary arguments. Here is the 
basic usage command:python selenium_scraper.py

Currently, the script is set to monitor a specific product URL hardcoded 
within the script(the Summer Fridays birthday cake-limited edition lip 
balm) Future versions will include command-line arguments to 
specify the product URL and other parameters dynamically.

Make sure you have Google Chrome and ChromeDriver installed on your 
system, as the script uses Selenium with ChromeDriver to interact with web 
pages. Ensure that the ChromeDriver version corresponds to your Google 
Chrome version.

for examples, simply run the script as mentioned 
above. The script will periodically check the product's availability and 
print "Product is out of stock" or "Product is available" based on the 
current status.
