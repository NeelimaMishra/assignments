"""
This file contain class to form base_url fo stackexchange
"""
import sys, os
sys.path.append(os.path.abspath('..'))
from utilities import utils

class ApiLib:
    def __init__(self, domain, api_version):
        self.domain = domain
        self.api_version = api_version
        self.base_url = '/'.join([self.domain, self.api_version])

    def get_request(self, params):
        return utils.get_request(self.badge_url, params)
        
    def post_request(self):
        pass

    def put_request(self):
        pass
        
    def delete_request(self):
        pass
        
    def patch_request(self):
        pass

class BadgeApiLib(ApiLib):
    def __init__(self, domain="https://api.stackexchange.com", api_version="2.2", api_type='badges'):
        ApiLib.__init__(self, domain, api_version)
        self.badge_url = '/'.join([self.base_url, api_type])
        
    def get_badges(self, call_parameters, by=''):
        if by == 'ids':
            ids = call_parameters['ids']
            self.badge_url = '/'.join([self.badge_url, ids])

        elif by == 'recipients_by_id':
            ids = call_parameters['ids']
            self.badge_url = '/'.join([self.badge_url, ids, 'recipients'])

        elif by == '':
            pass

        else:
            self.badge_url = '/'.join([self.badge_url, by])

        return self.get_request(call_parameters)