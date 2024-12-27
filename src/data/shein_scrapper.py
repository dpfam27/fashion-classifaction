import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from tqdm import tqdm

class SheinScraper:
    def __init__(self):
        # Basic setup
        options = webdriver.ChromeOptions()
        # Remove headless mode to allow manual captcha solving
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-notifications')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        
        self.driver = webdriver.Chrome(options=options)
        self.base_url = "https://us.shein.com"
        
    def wait_for_captcha(self):
        """Wait for user to solve captcha"""
        print("\n*** CAPTCHA detected! ***")
        print("Please solve the captcha in the browser window.")
        print("After solving, press Enter to continue...")
        input()
        time.sleep(3)  # Wait a bit after captcha solution
        
    def test_scrape(self):
        """Test basic scraping functionality"""
        try:
            # Try to access the main page
            print("Accessing SHEIN homepage...")
            self.driver.get(self.base_url)
            time.sleep(5)
            
            if "challenge" in self.driver.current_url:
                self.wait_for_captcha()
            
            print(f"Current URL: {self.driver.current_url}")
            print(f"Page Title: {self.driver.title}")
            
            # Try to access a category page
            category_url = f"{self.base_url}/women-dresses-c-1727.html"
            print(f"\nAccessing category page: {category_url}")
            self.driver.get(category_url)
            time.sleep(5)
            
            if "challenge" in self.driver.current_url:
                self.wait_for_captcha()
            
            print(f"Current URL: {self.driver.current_url}")
            print(f"Page Title: {self.driver.title}")
            
            # Try to find products
            print("\nLooking for products...")
            selectors = [
                'div[class*="product-item"]',
                'div[class*="S-product-item"]',
                'div.goods-item',
                'div[class*="goods-item"]',
                'div[class*="S-product-item__wrapper"]',
                'div[data-cat-id]',  # New selector
                'a[href*="/detail/"]'  # New selector for product links
            ]
            
            for selector in selectors:
                print(f"\nTrying selector: {selector}")
                try:
                    # Wait for elements to be present
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    
                    items = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if items:
                        print(f"Found {len(items)} items with selector: {selector}")
                        
                        # Try to extract data from first item
                        first_item = items[0]
                        print("\nFirst item HTML:")
                        print(first_item.get_attribute('outerHTML'))
                        
                        # Try to find specific elements
                        try:
                            title = first_item.find_element(By.CSS_SELECTOR, '[class*="name"]')
                            print(f"\nFound title: {title.text}")
                        except:
                            print("Could not find title")
                            
                        try:
                            price = first_item.find_element(By.CSS_SELECTOR, '[class*="price"]')
                            print(f"Found price: {price.text}")
                        except:
                            print("Could not find price")
                            
                        try:
                            image = first_item.find_element(By.TAG_NAME, 'img')
                            print(f"Found image URL: {image.get_attribute('src')}")
                        except:
                            print("Could not find image")
                        
                        break
                except Exception as e:
                    print(f"Error with selector {selector}: {str(e)}")
            
            # Save page source for analysis
            with open("shein_page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            print("\nSaved page source to shein_page_source.html")
            
        except Exception as e:
            print(f"Error during test: {str(e)}")
            import traceback
            print(traceback.format_exc())
        finally:
            input("Press Enter to close the browser...")
            self.driver.quit()

if __name__ == "__main__":
    scraper = SheinScraper()
    scraper.test_scrape()