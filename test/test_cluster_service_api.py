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
from swagger_client.api.cluster_service_api import ClusterServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestClusterServiceApi(unittest.TestCase):
    """ClusterServiceApi unit test stubs"""

    def setUp(self):
        self.api = ClusterServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cluster_service_create(self):
        """Test case for cluster_service_create

        Create creates a cluster  # noqa: E501
        """
        pass

    def test_cluster_service_delete(self):
        """Test case for cluster_service_delete

        Delete deletes a cluster  # noqa: E501
        """
        pass

    def test_cluster_service_get(self):
        """Test case for cluster_service_get

        Get returns a cluster by server address  # noqa: E501
        """
        pass

    def test_cluster_service_invalidate_cache(self):
        """Test case for cluster_service_invalidate_cache

        InvalidateCache invalidates cluster cache  # noqa: E501
        """
        pass

    def test_cluster_service_list(self):
        """Test case for cluster_service_list

        List returns list of clusters  # noqa: E501
        """
        pass

    def test_cluster_service_rotate_auth(self):
        """Test case for cluster_service_rotate_auth

        RotateAuth rotates the bearer token used for a cluster  # noqa: E501
        """
        pass

    def test_cluster_service_update(self):
        """Test case for cluster_service_update

        Update updates a cluster  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()