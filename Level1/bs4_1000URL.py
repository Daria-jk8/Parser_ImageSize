from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd
import time

# Execution time: 2 minutes and 8.44 seconds
filename = "Parser_1000_driver.csv"


df = pd.read_csv(filename)

op = webdriver.ChromeOptions()
op.add_argument("--headless")
driver = webdriver.Chrome(options=op)

sizestitle = []
sizes = []
start_time = time.time()

for index, row in df.iterrows():
    url = row["image_url"]

    # Get the HTML source of the page
    driver.get(url)
    html_page = driver.page_source

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_page, "html.parser")

    # Extract data from the title element
    title_element = soup.title
    title_text = title_element.string if title_element else "No title found"

    # Use regular expression to find dimensions in the title text
    dimensions_match = re.search(r"\((\d+×\d+)\)", title_text)
    dimensions = dimensions_match.group(1) if dimensions_match else "N/A"
    sizestitle.append(dimensions)

    # Print the combined information
    print(f"URL {index + 1}: {title_text} Dimensions: {dimensions}")

    pic = soup.find("img")
    # Iterate through img elements and print width and height
    # for pic in soup.find_all("img"):
    if pic:
        width = pic.get("width")
        height = pic.get("height", "N/A")

    size = f"{width} х {height}"
    sizes.append(size)

    # print(pic["width"], "х", pic["height"])
    # print(f"The image width is {width} pixels")
    # print(f"The image height is {height} pixels")

df["SIZE"] = sizes
df["SIZEtitle"] = sizestitle

df.to_csv(filename, index=False)

driver.quit()

end_time = time.time()
elapsed_time = end_time - start_time

minutes, seconds = divmod(elapsed_time, 60)
print(f"Execution time: {int(minutes)} min and {round(seconds, 2)} sec")
