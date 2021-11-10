import json 
import requests

from .exceptions import RangeValuesExpected
from .response import Response

class Q:
    """
    The query Builder class
    """
    def __init__(self, **kwargs):
        self.filter = {}
        self.exclude = {}
        self.aggregates = []
        # seperate out filters and excludes
        for param, value in kwargs.items():
            # __ notation for negation
            if param[:2] == '__':
                # double underscore means negation
                # I just mad that rule
                # And i really like that
                param = param[2:]
                self.exclude[f"-{param}"] = value
            # __in notation for range query
            if param[-4:] == "__in":
                # range query
                # enclode in square brackets
                if not isinstance(value, list):
                    raise RangeValuesExpected()
                else:
                    param = param.strip("__in")
                    self.filter[param] = value
            # accepts scalar and iters, change iters to tuple
            else:
                # a normal parameter
                if isinstance(value, str) or isinstance(value, int):
                    pass
                else:
                    value = tuple(value)
                self.filter[param] = value
        self.aggregates.append({**self.filter, **self.exclude})

    def compile(self):
        query_list = []
        for query in self.aggregates:
            part_query = ""
            for param, value in query.items():
                encoded_value = json.dumps(value).replace(",", " ")
                if isinstance(value, tuple):
                    encoded_value = encoded_value.replace("[", "(").replace("]", ")")
                sub_query = f"{param}:{encoded_value}"
                part_query += f" {sub_query}"
            query_list.append(part_query)
        return " OR ".join(query_list)

    def __or__(self, other):
        # by default all params are AND'ed
        # like django ORM
        # and to OR them, explicitly use | operator
        other_aggregate = {**other.filter, **other.exclude}
        new_q = Q()
        new_q.aggregates = [(self.aggregates[0])]
        new_q.aggregates.append(other_aggregate)
        return new_q


class Executor:
    def __init__(self, core):
        self.core = core
        self.wt = "json"
        self.base_url = core.get_base_url

    def query(self, **kwargs):
        self.q = Q(**kwargs)
        return self

    def facet(self, facet_fields):
        pass

    def get(self, sort=None, start=0, rows=10):
        params = {}
        params["q"] = self.q.compile()
        params["fl"] = self.core.fields
        params["start"] = start
        params["rows"] = rows
        params["wt"] = self.wt

        end_point = self.base_url + "select"
        raw_response = requests.get(url=end_point, params=params)
        return Response(raw_response)

    def paginate(self, sort=None, start=0, rows=10):
        pass



