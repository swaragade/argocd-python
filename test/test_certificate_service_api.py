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
from swagger_client.api.certificate_service_api import CertificateServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCertificateServiceApi(unittest.TestCase):
    """CertificateServiceApi unit test stubs"""

    def setUp(self):
        self.api = CertificateServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_certificate_service_create_certificate(self):
        """Test case for certificate_service_create_certificate

        Creates repository certificates on the server  # noqa: E501
        """
        pass

    def test_certificate_service_delete_certificate(self):
        """Test case for certificate_service_delete_certificate

        Delete the certificates that match the RepositoryCertificateQuery  # noqa: E501
        """
        pass

    def test_certificate_service_list_certificates(self):
        """Test case for certificate_service_list_certificates

        List all available repository certificates  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
