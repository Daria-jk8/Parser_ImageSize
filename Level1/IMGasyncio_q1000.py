import pandas as pd
from selenium import webdriver
import re
import asyncio
import aiohttp
import time


# URL 228: size not found
# Execution time: 0 minutes and 22.44 seconds
async def fetch_size(session, url, df, index):
    try:
        async with session.get(url) as response:
            content = await response.text(encoding="ISO-8859-1")
            size_regex = re.compile(r"\((\d+×\d+)\)")
            match = size_regex.search(content)

            if match:
                size = match.group(1)
                print(f"URL {index}: size found - {size}")

                df.at[index, "SIZE"] = size
            else:
                print(f"URL {index}: size not found")
                df.at[index, "SIZE"] = None

    except Exception as e:
        print(f"Failed to process URL {index}. Error: {e}")


async def main():
    filename = "Parser_1000_asyncio.csv"
    df = pd.read_csv(filename)

    df["SIZE"] = ""  # Create an empty column for sizes

    op = webdriver.ChromeOptions()
    op.add_argument("--headless")
    driver = webdriver.Chrome(options=op)

    # Use aiohttp ClientSession for making asynchronous requests
    async with aiohttp.ClientSession() as session:
        tasks = []

        for index, row in df.iterrows():
            image_url = row["image_url"]
            task = fetch_size(session, image_url, df, index)
            tasks.append(task)

        # Run the tasks concurrently
        await asyncio.gather(*tasks)

    driver.quit()

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    start_time = time.time()

    # Run the main coroutine
    asyncio.run(main())

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Convert time to minutes and seconds
    minutes, seconds = divmod(elapsed_time, 60)

    print(f"Execution time: {int(minutes)} minutes and {round(seconds, 2)} seconds")
