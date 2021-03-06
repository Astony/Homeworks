import json

import aiohttp
import pytest
from asynctest import CoroutineMock, patch

from homework10.task.parser import Parser, StockAnalyzer


class MockParser(Parser):
    """Mock Parser class"""

    def __init__(self):
        self.url = "https://fake.com"
        self.dollar_price = 1
        self.main_url = ""


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.get")
async def test_dollar_price_func(mock_get):
    """Test that Parser method parses information about dollar price correct"""
    with open("homework10/tests/dollar_price_file.html", "r", encoding="utf-8") as file:
        html_text = file.read()
    mock_get.return_value.__aenter__.return_value.text = CoroutineMock(
        side_effect=[html_text]
    )
    result = await MockParser.dollar_convert("some_url")
    assert result == 30


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.get")
async def test_get_links_and_growths_func(mock_get):
    """Test that Parser method parses links and year growths correct"""
    with open("homework10/tests/page1info.html", "r", encoding="utf-8") as file:
        html_text = file.read()
    parser = MockParser()
    mock_get.return_value.__aenter__.return_value.text = CoroutineMock(
        side_effect=[html_text]
    )
    async with aiohttp.ClientSession() as session:
        result = await parser.get_links_and_year_growth(session=session, page="a")
        assert result == (["link"], ["value"])


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.get")
async def test_get_main_company_info(mock_get):
    """Test that Parser method parses info from companies page correct"""
    with open(
        "homework10/tests/testing_company_page.html", "r", encoding="utf-8"
    ) as file:
        html_text = file.read()
    parser = MockParser()
    mock_get.return_value.__aenter__.return_value.text = CoroutineMock(
        side_effect=[html_text]
    )
    async with aiohttp.ClientSession() as session:
        result = await parser.get_main_company_info(session=session, url=parser.url)
        assert result == ("company_code", 666.0, 777.0, 888.0)


@pytest.mark.parametrize(
    "text", [[{"Company price": 6}, {"Company price": 9}, {"Company price": 1}]]
)
def test_top10_prices_method_of_Analyzer_class(Analyzer_instance):
    Analyzer_instance.top10_prices()
    with open("Top_10_Most_expensive.json") as json_file:
        sorted_companies = json.load(json_file)
    assert sorted_companies == [
        {"Company price": "9 B"},
        {"Company price": "6 B"},
        {"Company price": "1 B"},
    ]


@pytest.mark.parametrize(
    "text", [[{"P/E Ratio": 6}, {"P/E Ratio": 9}, {"P/E Ratio": 1}]]
)
def test_top10_PE_ratio_method_of_Analyzer_class(Analyzer_instance):
    Analyzer_instance.top10_PE()
    with open("Top_10_fewest_PE_ratio.json") as file:
        sorted_companies = json.load(file)
    assert sorted_companies == [{"P/E Ratio": 1}, {"P/E Ratio": 6}, {"P/E Ratio": 9}]


@pytest.mark.parametrize(
    "text", [[{"Years growth": "6%"}, {"Years growth": "9%"}, {"Years growth": "1%"}]]
)
def test_top10_growth_method_of_Analyzer_class(Analyzer_instance):
    Analyzer_instance.top10_growth()
    with open("Top_10_the_most_growth_per_year.json") as file:
        sorted_companies = json.load(file)
    assert sorted_companies == [
        {"Years growth": "9%"},
        {"Years growth": "6%"},
        {"Years growth": "1%"},
    ]


@pytest.mark.parametrize(
    "text",
    [[{"Week52 difference": 6}, {"Week52 difference": 9}, {"Week52 difference": 1}]],
)
def test_top10_52weeks_difference_method_of_Analyzer_class(Analyzer_instance):
    Analyzer_instance.top10_52weeks_difference()
    with open("Top_10_Most_difference_52_weeks.json") as file:
        sorted_companies = json.load(file)
    assert sorted_companies == [
        {"Week52 difference": 9},
        {"Week52 difference": 6},
        {"Week52 difference": 1},
    ]
