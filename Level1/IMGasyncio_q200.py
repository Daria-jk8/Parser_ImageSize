import pandas as pd
import time
import re
import aiohttp
import asyncio


# не працює


async def fetch_url(session, image_url, index, df_input):
    try:
        async with session.get(image_url) as response:
            content = await response.read()
            title = content.decode("utf-8", errors="replace")

            # print(f"Content for URL {index}: {title}")

            size_regex = re.compile(r"\((\d+×\d+)\)")
            match = size_regex.search(title)
            if match:
                size = match.group(1)
                df_input.at[index, "SIZE"] = size
            else:
                df_input.at[index, "SIZE"] = None
            print(f"Processed URL {index}: {image_url}")

    except Exception as e:
        print(f"Failed to process URL {index}. Error: {e}")
        pass


async def main():
    filename = "Parser_200a.csv"
    df_input = pd.read_csv(filename)

    df_input["SIZE"] = ""

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_url(session, row["image_url"], index, df_input)
            for index, row in df_input.iterrows()
        ]

        start_time = asyncio.get_event_loop().time()
        await asyncio.gather(*tasks)
        end_time = asyncio.get_event_loop().time()

        print(f"Execution time: {end_time - start_time} seconds")

    df_input.to_csv(filename, index=False)
    print(f"Size data saved to {filename}")


if __name__ == "__main__":
    asyncio.run(main())
