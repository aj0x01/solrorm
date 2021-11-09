from .exceptions import InvalidSolrResponse

class Response:

    def __init__(self, raw):

        try:
            assert raw.status_code == 200
        except AssertionError:
            raise InvalidSolrResponse()
        self._raw = raw

        self.url = raw.url

        response = raw.json()
        self.total = response['response']['numFound']

        self.docs = response['response']['docs']
        self.count = len(response['response']['docs'])

    def transform(self, field, callback, *args, **kwargs):
        # transforms response
        # used to mutate response, one doc at a time
        for doc in self.docs:
            doc[field] = callback(doc, *args, **kwargs)
        