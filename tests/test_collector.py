import xltoy
from xltoy.collector import Collector
import os

base_data_url = os.path.join(os.path.dirname(os.path.dirname(xltoy.__file__)),'data')

def coll1(url):
    url=os.path.join(base_data_url,url)
    c = Collector(url)



if __name__ == '__main__':
    coll1('gla_model.xlsx')