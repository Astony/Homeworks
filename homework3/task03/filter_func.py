from typing import ClassVar, Dict, List, Tuple


class Filter:
    """
    Helper filter class. Accepts a list of single-
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self: ClassVar, data: List) -> List:
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords: Tuple) -> ClassVar:
    """
    Generate filter object for specified keywords
    Save keywords in dictionary and than compare it
    with elements in input list
    """
    filter_funcs = []
    inp_arguments = {}
    for key, value in keywords.items():
        inp_arguments[key] = value

        def keyword_filter_func(data_dict: Dict) -> ClassVar:
            return inp_arguments.items() <= data_dict.items()

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)
