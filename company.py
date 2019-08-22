from .api import http_method

company_endpoint = {
    'search_by_name': 'transactors',
    'search_by_sic_id': 'transactor/{}',                # id
    'search_by_external_id': 'transactor/{}/{}/{}',     # countrycode, service, id
    'list_country_codes': 'lookups/countries',
    'list_external_ids': 'lookups/services',
    'get_external_ids': 'transactor/{}/externalids'     # id
}

class Company:
    def __init__(self, api):
        self.api = api

    def search_by_name(self, countrycode, name, postcode=None, city=None, streetname=None, streetnumber=None, phonenumber=None, legalform=None, page=None):
        param_data = {'countrycode': countrycode, 'name': name}
        if postcode != None:
            param_data['postcode'] = postcode
        elif streetname != None:
            param_data['streetname'] = streetname
        elif streetnumber != None:
            param_data['streetnumber'] = streetnumber
        elif phonenumber != None:
            param_data['phonenumber'] = phonenumber
        elif legalform != None:
            param_data['legalform'] = legalform
        elif page != None:
            param_data['page'] = page
        return self.api.request(http_method.get, company_endpoint['search_by_name'], parameter=param_data)

    def search_by_sic_id(self, id):
        return self.api.request(http_method.get, company_endpoint['search_by_sic_id'].format(id))

    def search_by_external_id(self, countrycode, service, id):
        return self.api.request(http_method.get, company_endpoint['search_by_external_id'].format(countrycode, service, id))

    def list_country_codes(self):
        return self.api.request(http_method.get, company_endpoint['list_country_codes'])

    def list_external_ids(self):
        return self.api.request(http_method.get, company_endpoint['list_external_ids'])

    def get_external_ids(self, id):
        return self.api.request(http_method.get, company_endpoint['get_external_ids'].format(id))
