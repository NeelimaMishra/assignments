"""
This file contains test cases for "Badges" method
"""
import unittest
import time
import sys, os
sys.path.append(os.path.abspath('..'))
from testlibs.badge_lib import BadgeApiLib

class TestClass(unittest.TestCase):
    def setUp(self):
        self.api_obj = BadgeApiLib()
        
    def test_default_badges_1(self):
        params = {'pagesize': 2,
                  'inname': 'android-file',
                  'sort': 'rank',
                  'site': 'stackoverflow'
                  }
        response = self.api_obj.get_badges(params, by='')
        print(response)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data)
        self.assertTrue(len(data['items']))
        self.assertEqual(data['quota_max'], 300)

    def test_badges_by_id_2(self):
        params = {}
        params['page'] = 1
        params['ids'] = "5"
        params['site'] = "stackoverflow"
        response = self.api_obj.get_badges(params, by='ids')
        print(response)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(len(data['items']))
        self.assertEqual(data['quota_max'], 300)
        
    def test_badges_recipients_by_id_3(self):
        params = {'ids': '9',
                  'pagesize': 1,
                  'site': 'stackoverflow'
                  }
        response = self.api_obj.get_badges(params, by='recipients_by_id')
        print(response)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data)
        self.assertTrue(len(data['items']))
        self.assertEqual(data['quota_max'], 300)
        
    def test_badges_by_name_4(self):
        params = {'pagesize': 3,
                  'inname': 'Organizer',
                  'sort': 'name',
                  'site': 'stackoverflow'
                  }
        response = self.api_obj.get_badges(params, by='name')
        print(response)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data)
        self.assertTrue(len(data['items']))
        self.assertEqual(data['quota_max'], 300)
        
    
    def test_badges_by_recipients_5(self):
        params = {'pagesize': 1,
                  'page': 1,
                  'site': 'stackoverflow'
                  }
        response = self.api_obj.get_badges(params, by='recipients')
        print(response)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data)
        self.assertTrue(len(data['items']))
        self.assertEqual(data['quota_max'], 300)
        
    def test_badges_by_tags_6(self):
        params = {'min': 1,
                  'site': 'stackoverflow'
                  }
        response = self.api_obj.get_badges(params, by='tags')
        print(response)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data)
        self.assertTrue(len(data['items']))
        self.assertEqual(data['quota_max'], 300)
        
    def test_badges_todate_fromdate_7(self):
        todate = int(time.time())
        fromdate = int(time.time())- ((60*60*24)*2)
        params = {'pagesize': 1,
                  'sort': 'rank',
                  'site': 'stackoverflow',
                  'page': '1',
                  'todate': 'todate',
                  'fromdate': 'fromdate'
                  }
        response = self.api_obj.get_badges(params, by='')
        print(response)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data)
        self.assertTrue(len(data['items']))
        self.assertEqual(data['quota_max'], 300)
        
    def test_badges_fromdate_todate_8(self):
        todate = int(time.time())- ((60*60*24)*2)
        fromdate = int(time.time())
        params = {'pagesize': 1,
                  'sort': 'rank',
                  'site': 'stackoverflow',
                  'page': '1',
                  'todate': 'todate',
                  'fromdate': 'fromdate'
                  }
        response = self.api_obj.get_badges(params, by='')
        print(response)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data)
        self.assertTrue(len(data['items']))
        self.assertEqual(data['quota_max'], 300)
        
    def test_negative_invalid_paramter_7(self):
        params = {'pagesize': 1,
                  'sort': 'rank',
                  'site': 'stackoverflow',
                  'invalid_key': 'extra'
                  }
        response = self.api_obj.get_badges(params, by='')
        print(response)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data)
        self.assertTrue(len(data['items']))
        self.assertEqual(data['quota_max'], 300)
        
        
if __name__ == '__main__':
    unittest.main()