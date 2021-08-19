import asyncio
import json
from collections import defaultdict
from typing import Callable, Dict, List, Tuple

import aiohttp
from bs4 import BeautifulSoup


class Parser:
    async def dollar_convert(url: str) -> float:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                """Function get information about currency dollar price in rub"""
                text = await response.text()
        return float(
            BeautifulSoup(text, "lxml")
            .find("div", class_="currency-table__large-text")
            .text.replace(",", ".")
        )

    @staticmethod
    async def fetch_all(function: Callable, urls: List) -> List:
        """Method that creates tasks and return results of tasks"""
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(function(session, url)) for url in urls]
            await asyncio.gather(*tasks)
            return tasks

    @staticmethod
    async def get_soup(session, url) -> BeautifulSoup:
        """Method that get url and return soup object"""
        async with session.get(url) as response:
            response_text = await response.text()
            return BeautifulSoup(response_text, "lxml")

    def __init__(self) -> None:
        self.url = "https://markets.businessinsider.com/index/components/s&p_500?p="
        self.main_url = self.url.split("index")[0]
        self.pages = [self.url + str(page) for page in range(1, 12)]

    async def get_links_and_year_growth(
        self, session: aiohttp.ClientSession, page: str
    ) -> Tuple:
        """Method, that parses information about companies links and their gains"""
        soup = await Parser.get_soup(session, page)
        hrefs_tags_from_page = soup.find_all(class_="table__td table__td--big")
        companies_urls = [
            self.main_url + item.find("a").get("href") for item in hrefs_tags_from_page
        ]
        all_tr_tags = soup.find(class_="table__tbody").find_all("tr")
        year_growths = [tr.find_all("td")[7].text.split()[1] for tr in all_tr_tags]
        return companies_urls, year_growths

    async def gather_links_and_year_growth_dollar_price(self) -> Tuple[List, List]:
        """Method that creates tasks and return tuple of all companies links and their years gains"""
        self.dollar_price = await Parser.dollar_convert(
            "https://www.banki.ru/products/currency/usd/"
        )
        links, gains = [], []
        tasks = await Parser.fetch_all(self.get_links_and_year_growth, self.pages)
        for task in tasks:
            links.extend(task.result()[0])
            gains.extend(task.result()[1])
        return links, gains

    async def get_main_company_info(
        self, session: aiohttp.ClientSession, url: str
    ) -> Tuple:
        """Method that parses all info about company from company's page"""
        soup = await Parser.get_soup(session, url)
        code = Parser.get_code(soup)
        MarketCapPrice_and_PEratio = self.get_MarketCap_and_PE(soup)
        price = MarketCapPrice_and_PEratio["Market Cap"]
        PE = MarketCapPrice_and_PEratio["P/E Ratio"]
        week52 = Parser.get_52week_info(soup)
        return code, price, PE, week52

    async def gather_main_company_info(self, links: List[str]) -> Tuple:
        """Method that creates tasks and return tuple of company code, total price, PE_ratio and 52 week difference"""
        codes, prices, PE, weeks = [], [], [], []
        tasks = await Parser.fetch_all(self.get_main_company_info, links)
        for task in tasks:
            codes.append(task.result()[0])
            prices.append(task.result()[1])
            PE.append(task.result()[2])
            weeks.append(task.result()[3])
        return codes, prices, PE, weeks

    @staticmethod
    def get_code(soup: BeautifulSoup) -> str:
        """Method that parses company's code"""
        return soup.find(class_="price-section__category").find("span").text.split()[1]

    def get_MarketCap_and_PE(self, soup: BeautifulSoup) -> Dict:
        """Method that parses company's total price in rub"""
        table_with_data = soup.find_all(class_="snapshot__data-item")
        MarketCap_and_PEratio_dict = defaultdict(float)
        for data in table_with_data:
            element = data.text.strip().split("\n")
            if element[-1].strip() == "Market Cap":
                MarketCap_and_PEratio_dict["Market Cap"] = round(
                    float(element[0].split()[0].strip().replace(",", ""))
                    * self.dollar_price,
                    3,
                )
            elif element[-1].strip() == "P/E Ratio":
                MarketCap_and_PEratio_dict["P/E Ratio"] = float(
                    element[0].strip().replace(",", "")
                )
        return MarketCap_and_PEratio_dict

    @staticmethod
    def get_52week_info(soup: BeautifulSoup) -> float:
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

    def parse(self) -> None:
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
            self.gather_links_and_year_growth_dollar_price()
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

    @staticmethod
    def create_json_file(name: str, data: List) -> None:
        """Method that creates json file"""
        with open(f"{name}.json", "a") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def open_and_read_companies_info_file(companies_info_file: str):
        """Function that loads data from json file"""
        with open(companies_info_file) as file:
            return json.load(file)

    def __init__(self, companies_info_file="companies_info.json"):
        self.companies_info = StockAnalyzer.open_and_read_companies_info_file(
            companies_info_file
        )

    def top10_prices(self) -> None:
        """Method that creates json file with top 10 companies the highest total price"""
        top10prices = sorted(
            self.companies_info, key=lambda k: k["Company price"], reverse=True
        )[:10]
        for element in top10prices:
            element["Company price"] = str(element["Company price"]) + " B"
        StockAnalyzer.create_json_file("Top_10_Most_expensive", top10prices)

    def top10_PE(self) -> None:
        """Method that creates json file with top 10  companies the fewest total price"""
        top10PE = (
            element for element in self.companies_info if element["P/E Ratio"] != 0
        )
        top10PE = sorted(top10PE, key=lambda k: k["P/E Ratio"], reverse=False)[:10]
        StockAnalyzer.create_json_file("Top_10_fewest_PE_ratio", top10PE)

    def top10_growth(self) -> None:
        """Method that creates json file with top 10 companies the highest year growth of stoks prices"""
        top10growth = sorted(
            self.companies_info,
            key=lambda k: float(k["Years growth"].replace("%", "")),
            reverse=True,
        )[:10]
        StockAnalyzer.create_json_file("Top_10_the_most_growth_per_year", top10growth)

    def top10_52weeks_difference(self) -> None:
        """Method that creates json file with top 10 companies the highest 52 weeks difference"""
        top10_52weeks_difference = sorted(
            self.companies_info, key=lambda k: k["Week52 difference"], reverse=True
        )[:10]
        StockAnalyzer.create_json_file(
            "Top_10_Most_difference_52_weeks", top10_52weeks_difference
        )

    def analyze(self) -> None:
        """Method that creates all top10 json files"""
        self.top10_PE()
        self.top10_growth()
        self.top10_prices()
        self.top10_52weeks_difference()
