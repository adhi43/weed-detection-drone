"""
Image Scraping Utility (Research Use Only)

Downloads images from Google Images using Selenium.
Used for dataset exploration and background image collection.

NOTE:
- For research and experimentation only
- Do not use scraped images for commercial redistribution
"""

import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from io import BytesIO


def download_images(search_query, num_images=50, download_path="downloaded_images"):
    os.makedirs(download_path, exist_ok=True)

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(f"https://www.google.com/search?q={search_query}&tbm=isch")
    time.sleep(3)

    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    images = driver.find_elements(By.CSS_SELECTOR, "img")
    count = 0

    for img in images:
        if count >= num_images:
            break
        try:
            img_url = img.get_attribute("src")
            if img_url and img_url.startswith("http"):
                response = requests.get(img_url, timeout=10)
                image = Image.open(BytesIO(response.content))
                image.save(os.path.join(download_path, f"{search_query}_{count}.jpg"))
                count += 1
        except Exception:
            continue

    driver.quit()
    print(f"Downloaded {count} images.")
download_images("parthenium", num_images=100)
download_images("lantana", num_images=100)

