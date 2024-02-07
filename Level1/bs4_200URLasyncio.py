import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

filename = "Parser_200_asyncio.csv"

df = pd.read_csv(filename)


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text(encoding="ISO-8859-1")


async def process_url(index, row):
    url = row["image_url"]

    html_page = await fetch_data(url)
    soup = BeautifulSoup(html_page, "html.parser")

    # Extract data from title element (improved regex)
    title_element = soup.title
    print(title_element)
    title_text = title_element.string if title_element else "No title found"
    dimensions_match = re.search(r"(\d+)\s*×\s*(\d+)", title_text)
    dimensions_from_title = (
        dimensions_match.groups() if dimensions_match else ("N/A", "N/A")
    )

    # Find and handle multiple images if needed
    sizes = []
    for pic in soup.find_all("img"):
        width = pic.get("width") or "N/A"
        height = pic.get("height") or "N/A"
        size = f"{width} × {height}"
        sizes.append(size)

    # Combine and append results
    sizes.extend(dimensions_from_title)
    print(
        f"URL {index + 1}: {title_text} Dimensions (title, image): {', '.join(sizes)}"
    )

    # Update DataFrame (assuming `df` and relevant columns exist)
    df.loc[index, "SIZEtitle"] = dimensions_from_title[0]  # Title width
    df.loc[index, "SIZE"] = sizes[0]  # Image width or first image's width

    # Add more columns for other sizes/dimensions as needed


start_time = time.time()


async def main():
    tasks = [process_url(index, row) for index, row in df.iterrows()]
    await asyncio.gather(*tasks)


sizestitle = []
sizes = []
# Create an event loop
asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())

# Add the 'SIZE' and 'SIZEtitle' columns to the DataFrame
df["SIZE"] = sizes
df["SIZEtitle"] = sizestitle

# Save the updated DataFrame to the same CSV file
df.to_csv(filename, index=False)

end_time = time.time()
elapsed_time = end_time - start_time

minutes, seconds = divmod(elapsed_time, 60)
print(f"Execution time: {int(minutes)} minutes and {round(seconds, 2)} seconds")
