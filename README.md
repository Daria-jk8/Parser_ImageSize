## Level1_Web Scraping with AIOHTTP and Python
[source] [Parser_ImageSize](https://docs.google.com/spreadsheets/d/1QX2IhFyYmGDFMvovw2WFz3wAT4piAZ_8hi5Lzp7LjV0/edit#gid=1902149593)

![L1](https://github.com/Daria-jk8/Parser_ImageSize/assets/92945302/f30e1703-a5fa-41fc-984d-32ac6145be2e)

```
Level1/  
│   ├─ requirements.txt
|   ├─ Parser_ImageSize - feed.csv
|   |    
│   ├─ IMGdriver_q200.py                                                                # selenium
│   ├─ Parser_200_driver.csv               
│   ├─ IMGdriver_q1000.py                                                               # selenium
│   ├─ Parser_1000_driver.csv
|   ├─ IMGasyncio_q200.py           #(-) doesn't work                                   asyncio&aiohttp&webdriver  
|   ├─ Parser_200a.csv   
|   ├─ IMGasyncio_q1000.py          #(-) doesn't work_size not found                    asyncio&aiohttp&webdriver   
|   ├─ Parser_1000_asyncio.csv
|   ├─ bs4_200URL.py                # Parser_200a.csv -- 11.81 seconds                  BeautifulSoup&webdriver
|   ├─ bs4_1000URL.py               # Parser_1000_driver.csv -- 2 min and 8.44 seconds  BeautifulSoup&webdriver
|   ├─ bs4_46888URLdriver.py        # Parser_Image_driver_ALL.csv -- URL 9535: stop     BeautifulSoup&webdriver
|   ├─ bs4_200URLasyncio.py         #(-) doesn't work Parser_200_asyncio.csv            asyncio&aiohttp&BeautifulSoup
|   
|- README.md

```

## SUMMARY

- get the image size: Parser_200a.csv, Parser_1000_driver.csv, 

<u>PROS</u>
- [x] досліджено методи отримання Dimensions(блок <head>) та Size(width х height) (блок<body>): selenium, asyncio&aiohttp, BeautifulSoup&webdriver, asyncio&aiohttp&BeautifulSoup
- [x] отримані дані по картинкам до 9534;
- [x] встановлено час виконання методів при 200/1000 шт картинок. 

<u>CONS</u>

- [ ] не реалізовано метод asyncio&aiohttp, error: encoding="ISO-8859-1"| decode("utf-8", errors="replace")
- [ ] не відправлено дані в google sheet.


GitHub Repository [Parser_ImageSize](https://github.com/Daria-jk8/Parser_ImageSize)

Google Sheet [Parser_ImageSize](https://docs.google.com/spreadsheets/d/1QX2IhFyYmGDFMvovw2WFz3wAT4piAZ_8hi5Lzp7LjV0/edit#gid=1902149593)


  
