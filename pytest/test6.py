import pytest
class myplugin:
    def pytest_sessionfinish(self):
        print('*** test run reporting finishing')

pytest.main(['-qq'],plugins=[myplugin()])