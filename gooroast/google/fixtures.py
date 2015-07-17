from cafe.drivers.unittest.fixtures import BaseTestFixture

from goocafe.google.client import GoogleClient
from goocafe.google.config import GoogleFormatConfig, GoogleServerConfig


class GoogleTestFixture(BaseTestFixture):

    @classmethod
    def setUpClass(cls):
        super(GoogleTestFixture, cls).setUpClass()

        server_config = GoogleServerConfig()
        format_config = GoogleFormatConfig()

        cls.client = GoogleClient(format_config.input, format_config.output,
                                  server_config.endpoint)

    @classmethod
    def tearDownClass(cls):
        super(GoogleTestFixture, cls).tearDownClass()
