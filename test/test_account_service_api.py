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
from swagger_client.api.account_service_api import AccountServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAccountServiceApi(unittest.TestCase):
    """AccountServiceApi unit test stubs"""

    def setUp(self):
        self.api = AccountServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_account_service_can_i(self):
        """Test case for account_service_can_i

        CanI checks if the current account has permission to perform an action  # noqa: E501
        """
        pass

    def test_account_service_create_token(self):
        """Test case for account_service_create_token

        CreateToken creates a token  # noqa: E501
        """
        pass

    def test_account_service_delete_token(self):
        """Test case for account_service_delete_token

        DeleteToken deletes a token  # noqa: E501
        """
        pass

    def test_account_service_get_account(self):
        """Test case for account_service_get_account

        GetAccount returns an account  # noqa: E501
        """
        pass

    def test_account_service_list_accounts(self):
        """Test case for account_service_list_accounts

        ListAccounts returns the list of accounts  # noqa: E501
        """
        pass

    def test_account_service_update_password(self):
        """Test case for account_service_update_password

        UpdatePassword updates an account's password to a new value  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()