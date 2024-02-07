import pandas as pd
from selenium import webdriver
import time
import re

# Execution time: 19 minutes and 0.8 seconds

filename = "Parser_1000_driver.csv"

df = pd.read_csv(filename)

df["SIZE"] = ""

op = webdriver.ChromeOptions()
op.add_argument("--headless")
driver = webdriver.Chrome(options=op)

start_time = time.time()

for index, row in df.iterrows():
    image_url = row["image_url"]

    try:
        driver.get(image_url)
        time.sleep(1)

        size_regex = re.compile(r"\((\d+×\d+)\)")
        match = size_regex.search(driver.title)

        if match:
            size = match.group(1)
            df.at[index, "SIZE"] = size
        else:
            df.at[index, "SIZE"] = None

    except Exception as e:
        print(f"Failed to process URL {index}. Error: {e}")

driver.quit()

end_time = time.time()
elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)

df.to_csv(filename, index=False)

print(f"Size data saved to {filename}")
print(f"Execution time: {int(minutes)} minutes and {round(seconds, 2)} seconds")
