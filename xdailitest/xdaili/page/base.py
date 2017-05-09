class page(object):

    xdaili_url='http://10.60.10.71'
    def __init__(self,selenium_driver,base_url=xdaili_url,parent=None):
        self.base_url=base_url
        self.driver=selenium_driver
        self.timeout=20
        self.parent=parent

    def _open(self,url):
        url=self.base_url+url
        self.driver.get(url)

    def open(self):
        self._open(self.url)

