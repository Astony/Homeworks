import asyncio
import json

import aiohttp
import requests
from bs4 import BeautifulSoup


class Parser:
    @staticmethod
    def dollar_convert(url):
        """Method that parse information about dollar price on today"""
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "lxml")
        return float(
            soup.find("div", class_="currency-table__large-text").text.replace(",", ".")
        )

    def __init__(self):
        self.url = "https://markets.businessinsider.com/index/components/s&p_500?p="
        self.main_url = self.url.split("index")[0]
        self.dollar_price = Parser.dollar_convert(
            "https://www.banki.ru/products/currency/usd/"
        )
        self.pages = list(range(1, 12))

    async def gather_links_and_year_growth(self):
        """Method that creates tasks and return tuple of all companies links and their years gains"""
        links = []
        gains = []
        async with aiohttp.ClientSession() as session:
            tasks = [
                asyncio.create_task(self.get_links_and_year_growth(session, str(page)))
                for page in self.pages
            ]
            await asyncio.gather(*tasks)
            for task in tasks:
                links.extend(task.result()[0])
                gains.extend(task.result()[1])
        return links, gains

    async def get_links_and_year_growth(self, session, page):
        """Method, that parses information about companies links and their gains"""
        async with session.get(self.url + page) as response:
            response_text = await response.text()
            soup = BeautifulSoup(response_text, "lxml")
            hrefs_from_page = soup.find_all(class_="table__td table__td--big")
            companies_links = [
                self.main_url + item.find("a").get("href") for item in hrefs_from_page
            ]
            all_tr = soup.find(class_="table__tbody").find_all("tr")
            year_growths = [tr.find_all("td")[7].text.split()[1] for tr in all_tr]
        return companies_links, year_growths

    async def gather_main_company_info(self, links):
        """Method that creates tasks and return tuple of company code, total price, PE_ratio and 52 week difference"""
        codes, prices, PEs, weeks = [], [], [], []
        async with aiohttp.ClientSession() as session:
            tasks = [
                asyncio.create_task(self.get_main_company_info(session, url))
                for url in links
            ]
            await asyncio.gather(*tasks)
            for task in tasks:
                codes.append(task.result()[0])
                prices.append(task.result()[1])
                PEs.append(task.result()[2])
                weeks.append(task.result()[3])
        return codes, prices, PEs, weeks

    async def get_main_company_info(self, session, url):
        """Method that parses all info about company from company's page"""

        async with session.get(url) as response:
            response_text = await response.text()
            soup = BeautifulSoup(response_text, "lxml")
            code = Parser.get_code(soup)
            price = self.get_MarketCap(soup)
            PE = Parser.get_PE(soup)
            week52 = Parser.get_52week_info(soup)
        return code, price, PE, week52

    @staticmethod
    def get_code(soup):
        """Method that parses company's code"""
        return soup.find(class_="price-section__category").find("span").text.split()[1]

    def get_MarketCap(self, soup):
        """Method that parses company's total price in rub"""
        table_with_data = soup.find_all(class_="snapshot__data-item")
        for data in table_with_data:
            element = data.text.strip().split("\n")
            if element[-1].strip() == "Market Cap":
                return round(
                    float(element[0].split()[0].strip().replace(",", ""))
                    * self.dollar_price,
                    3,
                )

    @staticmethod
    def get_PE(soup):
        """Method that parses company's PE ratio"""
        table_with_data = soup.find_all(class_="snapshot__data-item")
        for data in table_with_data:
            element = data.text.strip().split("\n")
            if element[-1].strip() == "P/E Ratio":
                return float(element[0].strip().replace(",", ""))
        return 0

    @staticmethod
    def get_52week_info(soup):
        """Method that parses company's 52 weeks difference"""
        try:
            low_info = soup.find_all(
                class_="snapshot__data-item snapshot__data-item--small"
            )
            low = float(low_info[0].text.split()[0].replace(",", ""))
            high_info = soup.find_all(
                class_="snapshot__data-item snapshot__data-item--small snapshot__data-item--right"
            )
            high = float(high_info[0].text.split()[0].replace(",", ""))
            return round(high - low, 3)
        except IndexError:
            return 0

    def parse(self):
        """Method that writes info about all companies in json file"""
        loop = asyncio.get_event_loop()
        company_info = []
        parameters = [
            "Company code",
            "Company price",
            "P/E Ratio",
            "Years growth",
            "Week52 difference",
        ]
        links, year_growths = loop.run_until_complete(
            self.gather_links_and_year_growth()
        )
        codes, prices, PEs, weeks = loop.run_until_complete(
            self.gather_main_company_info(links)
        )
        for index in range(len(codes)):
            values = (
                codes[index],
                prices[index],
                PEs[index],
                year_growths[index],
                weeks[index],
            )
            company_info.append(dict(zip(parameters, values)))
        with open("companies_info.json", "a", encoding="utf-8") as file:
            json.dump(company_info, file, indent=4, ensure_ascii=False)


class StockAnalyzer:
    """Class that analyzes info about different companies"""

    def __init__(self, companies_info_file="companies_info.json"):
        with open(companies_info_file) as file:
            self.companies_info = json.load(file)

    @staticmethod
    def create_json_file(name, data):
        """Method that creates json file"""
        with open(f"{name}.json", "a") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def top10_prices(self):
        """Method that creates json file with top 10 companies the highest total price"""
        top10prices = sorted(
            self.companies_info, key=lambda k: k["Company price"], reverse=True
        )[:10]
        for element in top10prices:
            element["Company price"] = str(element["Company price"]) + " B"
        StockAnalyzer.create_json_file("Top_10_Most_expensive", top10prices)

    def top10_PE(self):
        """Method that creates json file with top 10 companies the fewest total price"""
        top10PE = (
            element for element in self.companies_info if element["P/E Ratio"] != 0
        )
        top10PE = sorted(top10PE, key=lambda k: k["P/E Ratio"], reverse=False)[:10]
        StockAnalyzer.create_json_file("Top_10_fewest_PE_ratio", top10PE)

    def top10_growth(self):
        """Method that creates json file with top 10 companies the highest year growth of stoks prices"""
        top10growth = sorted(
            self.companies_info,
            key=lambda k: float(k["Years growth"].replace("%", "")),
            reverse=True,
        )[:10]
        StockAnalyzer.create_json_file("Top_10_the_most_growth_per_year", top10growth)

    def top10_52weeks_difference(self):
        """Method that creates json file with top 10 companies the highest 52 weeks difference"""
        top10_52weeks_difference = sorted(
            self.companies_info, key=lambda k: k["Week52 difference"], reverse=True
        )[:10]
        StockAnalyzer.create_json_file(
            "Top_10_Most_difference_52_weeks", top10_52weeks_difference
        )

    def analyze(self):
        """Method that creates all top10 json files"""
        func_list = [
            self.top10_PE,
            self.top10_growth,
            self.top10_prices,
            self.top10_52weeks_difference,
        ]
        for func in func_list:
            func()
