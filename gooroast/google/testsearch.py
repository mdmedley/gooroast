from cafe.drivers.unittest.decorators import tags, DataDrivenFixture,\
    data_driven_test
from cafe.drivers.unittest.datasets import DatasetFileLoader
from cafe.engine.config import EngineConfig

from gooroast.google.fixtures import GoogleTestFixture

ENGINE_CONFIG = EngineConfig()
CLOUDCAFE_DATA_DIRECTORY = ENGINE_CONFIG.data_directory


@DataDrivenFixture
class GoogleSearchTest(GoogleTestFixture):
    @tags(type="foo")
    @data_driven_test(DatasetFileLoader(open("{dir}/{path}".format(
        dir=CLOUDCAFE_DATA_DIRECTORY, path="google.json"))))
    def ddtest_search(self, criteria, status):
        response = self.client.search(criteria)
        self.assertTrue(response.status_code == status,
                        "Response code was not {status}".format(
                            str(response.status_code)))
