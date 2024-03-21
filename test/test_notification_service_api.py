# coding: utf-8

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.notification_service_api import NotificationServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestNotificationServiceApi(unittest.TestCase):
    """NotificationServiceApi unit test stubs"""

    def setUp(self):
        self.api = NotificationServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_notification_service_list_services(self):
        """Test case for notification_service_list_services

        List returns list of services  # noqa: E501
        """
        pass

    def test_notification_service_list_templates(self):
        """Test case for notification_service_list_templates

        List returns list of templates  # noqa: E501
        """
        pass

    def test_notification_service_list_triggers(self):
        """Test case for notification_service_list_triggers

        List returns list of triggers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()