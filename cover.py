from .api import http_method

cover_endpoint = {
    'get_by_id': 'coverage/{}',             # cover-id
    'get_covers': 'coverage?version=2'
}

class Cover:
    def __init__(self, api):
        self.api = api

    def get_by_id(self, id):
        raise NotImplementedError

    def covers(self, status=None, from_date=None, to_date=None, page=None, page_size=None, sort_by=None, sorting_order=None):
        raise NotImplementedError
