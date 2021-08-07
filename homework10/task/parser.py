import time
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import requests
import json


class Parser:
    @staticmethod
    def dollar_price():
        url = "https://www.banki.ru/products/currency/usd/"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "lxml")
        return float(soup.find("div", class_="currency-table__large-text").text.replace(",", "."))

    def __init__(self):
        self.url = "https://markets.businessinsider.com/index/components/s&p_500?p="
        self.main_url = self.url.split("index")[0]
        self.dollar_price = Parser.dollar_price()
#
#
    async def gather_links_and_gains(self):
        links = []
        gains = []
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(self.get_link_gain(session, str(page))) for page in range(1, 12)]
            await asyncio.gather(*tasks)
            for task in tasks:
                links.extend(task.result()[0])
                gains.extend(task.result()[1])
        return links, gains


    async def get_link_gain(self, session, page):
        async with session.get(self.url + page) as response:
            response_text = await response.text()
            soup = BeautifulSoup(response_text, "lxml")
            hrefs_from_page = soup.find_all(class_="table__td table__td--big")
            links = [self.main_url + item.find("a").get("href") for item in hrefs_from_page]
            all_tr = soup.find(class_="table__tbody").find_all("tr")
            gains = [tr.find_all('td')[7].text.split()[1] for tr in all_tr]
        return links, gains

    async def gather_main_company_info(self, links):
        codes, prices, PEs, weeks = [], [], [], []
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(self.get_info(session, url)) for url in links]
            await asyncio.gather(*tasks)
            for task in tasks:
                codes.append(task.result()[0])
                prices.append(task.result()[1])
                PEs.append(task.result()[2])
                weeks.append(task.result()[3])
        return codes, prices, PEs, weeks

    async def get_info(self, session, url):
        async with session.get(url) as response:
            response_text = await response.text()
            soup = BeautifulSoup(response_text, "lxml")
            code = self.get_code(soup)
            price = self.get_MarketCap(soup)
            PE = self.get_PE(soup)
            week52 = self.get_52week_info(soup)
        return code, price, PE, week52


    def get_code(self, soup):
        return soup.find(class_="price-section__category").find("span").text.split()[1]


    def get_MarketCap(self, soup):
        table_with_data = soup.find_all(class_="snapshot__data-item")
        for data in table_with_data:
            element = data.text.strip().split("\n")
            if element[1].strip() == "Market Cap":
                return float(element[0].split()[0].strip().replace(',', '')) * self.usd_to_rub

    def get_PE(self, soup):
        table_with_data = soup.find_all(class_="snapshot__data-item")
        for data in table_with_data:
            element = data.text.strip().split("\n")
            if element[1].strip() == "P/E Ratio":
                return float(element[0].strip().replace(',',''))
        return 0


    def get_52week_info(self, soup):
        try:
            low_info = soup.find_all(class_="snapshot__data-item snapshot__data-item--small")
            low = float(low_info[1].text.split()[0].replace(',', ''))
            high_info = soup.find_all(class_="snapshot__data-item snapshot__data-item--small snapshot__data-item--right")
            high = float(high_info[1].text.split()[0].replace(',', ''))
            return round(high - low, 3)
        except IndexError:
            return 0

    def parse(self):
        loop = asyncio.get_event_loop()
        company_info = []
        links, gains = loop.run_until_complete(a.gather_links_and_gains())
        codes, prices, PEs, weeks =loop.run_until_complete(self.gather_codes(links))
        for index in range(len(codes)):
            company_info.append(
                            {
                                "Company code": codes[index],
                                "Company price": prices[index],
                                "P/E Ratio": PEs[index],
                                "Years growth": gains[index],
                                "Week52 difference": weeks[index]

                            }
                        )
        with open("companies_info.json", "a", encoding="utf-8") as file:
            json.dump(company_info, file, indent=4, ensure_ascii=False)

a = Parser()
loop = asyncio.get_event_loop()
t1 = time.time()
links, gains = loop.run_until_complete(a.gather_links_and_gains())
print(time.time() - t1)
t1 = time.time()
print(a.parse())
print(time.time() - t1)


