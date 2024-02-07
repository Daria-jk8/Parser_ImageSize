from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd
import time

# Execution time: 2 minutes and 8.44 seconds
# filename = "Parser_1000_driver.csv"

# 46888 images
# Execution time:
filename = "Parser_Image_driver_ALL.csv"

df = pd.read_csv(filename)

op = webdriver.ChromeOptions()
op.add_argument("--disable-gpu")
op.add_argument("--headless")
driver = webdriver.Chrome(options=op)

sizestitle = []
sizes = []
start_time = time.time()

# Set the counter and interval
counter = 0
print_interval = 1000  # Змінив print_interval на 1000

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

    # Increment the counter
    counter += 1

    # Check if it's time to print the elapsed time
    if counter % print_interval == 0:
        current_time = time.time()
        elapsed_time = current_time - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        print(
            f"Processed {counter} URLs. Elapsed time: {int(minutes)} min and {round(seconds, 2)} sec"
        )

        # Save data to CSV file
        temp_df = pd.DataFrame({"SIZE": sizes, "SIZEtitle": sizestitle})
        temp_filename = f"Parser_Image_driver_{counter}.csv"
        temp_df.to_csv(temp_filename, index=False)
        print(f"Data saved to {temp_filename}")

        # Clear lists for the next iteration
        sizestitle.clear()
        sizes.clear()

# Print the final elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
print(f"Total execution time: {int(minutes)} min and {round(seconds, 2)} sec")

# Save remaining data to CSV file
remaining_df = pd.DataFrame({"SIZE": sizes, "SIZEtitle": sizestitle})
remaining_filename = f"Parser_Image_driver_remaining.csv"
remaining_df.to_csv(remaining_filename, index=False)
print(f"Remaining data saved to {remaining_filename}")

driver.quit()

# URL 9535:
# 2nd
# start_5:34
# 5000_5:42(8m)
# 6000_5:48(6m)_14m
# 7000_5:57(9m)_23m
# 8000_6:09(12m)_35m
# 9000_6:26(17m)_52m
# 9535_6:37(17m)_63m

# 3rd_start 6:42
# 1000_6:43
# 2000_6:44
# 3000_6:46
# 4000_6:47
# 5000_6:50(8m)
# 6000_6:57
# Processed 6000 URLs. Elapsed time: 14 min and 39.67 sec
# Processed 7000 URLs. Elapsed time: 23 min and 38.83 sec
# Processed 8000 URLs. Elapsed time: 35 min and 19.38 sec

# 4th 7:26
# Processed 1000 URLs. 0 min and 56.8 sec
# Processed 2000 URLs. 1 min and 55.17 sec
# Processed 3000 URLs. 3 min and 5.28 sec
# Processed 4000 URLs. 4 min and 10.99 sec
# Processed 5000 URLs. 8 min and 00.00 sec
# Processed 6000 URLs. 14 min and 18.15 sec
# Processed 7000 URLs. 22 min and 59.04 sec
# Processed 8000 URLs. 34 min and 55.96 sec
# Processed 9000 URLs. 48 min and 28.29 sec
# Processed 9534 URLs. 58 min and 0 seconds.
# finish 8:24
