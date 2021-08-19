import json
import os

import pytest

from homework10.task.parser import StockAnalyzer

all_names_of_created_jsons = [
    "Top_10_Most_expensive",
    "Top_10_fewest_PE_ratio",
    "Top_10_the_most_growth_per_year",
    "Top_10_Most_difference_52_weeks",
]


@pytest.fixture
def Analyzer_instance(text):
    """Fixture that creates json file, starts test of analyzer class and deletes all files after tests"""
    with open("test_json_file.json", "a") as file:
        json.dump(text, file, indent=4, ensure_ascii=False)
    analyzer = StockAnalyzer("test_json_file.json")
    yield analyzer
    os.remove("test_json_file.json")
    for name in all_names_of_created_jsons:
        if os.path.exists(name + ".json"):
            os.remove(name + ".json")
