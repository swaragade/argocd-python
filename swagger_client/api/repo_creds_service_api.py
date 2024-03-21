# coding: utf-8

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class RepoCredsServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def repo_creds_service_create_repository_credentials(self, body, **kwargs):  # noqa: E501
        """CreateRepositoryCredentials creates a new repository credential set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repo_creds_service_create_repository_credentials(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1alpha1RepoCreds body: Repository definition (required)
        :param bool upsert: Whether to create in upsert mode.
        :return: V1alpha1RepoCreds
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repo_creds_service_create_repository_credentials_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.repo_creds_service_create_repository_credentials_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def repo_creds_service_create_repository_credentials_with_http_info(self, body, **kwargs):  # noqa: E501
        """CreateRepositoryCredentials creates a new repository credential set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repo_creds_service_create_repository_credentials_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1alpha1RepoCreds body: Repository definition (required)
        :param bool upsert: Whether to create in upsert mode.
        :return: V1alpha1RepoCreds
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'upsert']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repo_creds_service_create_repository_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `repo_creds_service_create_repository_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'upsert' in params:
            query_params.append(('upsert', params['upsert']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repocreds', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1alpha1RepoCreds',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def repo_creds_service_delete_repository_credentials(self, url, **kwargs):  # noqa: E501
        """DeleteRepositoryCredentials deletes a repository credential set from the configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repo_creds_service_delete_repository_credentials(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str url: (required)
        :return: RepocredsRepoCredsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repo_creds_service_delete_repository_credentials_with_http_info(url, **kwargs)  # noqa: E501
        else:
            (data) = self.repo_creds_service_delete_repository_credentials_with_http_info(url, **kwargs)  # noqa: E501
            return data

    def repo_creds_service_delete_repository_credentials_with_http_info(self, url, **kwargs):  # noqa: E501
        """DeleteRepositoryCredentials deletes a repository credential set from the configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repo_creds_service_delete_repository_credentials_with_http_info(url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str url: (required)
        :return: RepocredsRepoCredsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repo_creds_service_delete_repository_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if ('url' not in params or
                params['url'] is None):
            raise ValueError("Missing the required parameter `url` when calling `repo_creds_service_delete_repository_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'url' in params:
            path_params['url'] = params['url']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repocreds/{url}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepocredsRepoCredsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def repo_creds_service_list_repository_credentials(self, **kwargs):  # noqa: E501
        """ListRepositoryCredentials gets a list of all configured repository credential sets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repo_creds_service_list_repository_credentials(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str url: Repo URL for query.
        :return: V1alpha1RepoCredsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repo_creds_service_list_repository_credentials_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.repo_creds_service_list_repository_credentials_with_http_info(**kwargs)  # noqa: E501
            return data

    def repo_creds_service_list_repository_credentials_with_http_info(self, **kwargs):  # noqa: E501
        """ListRepositoryCredentials gets a list of all configured repository credential sets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repo_creds_service_list_repository_credentials_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str url: Repo URL for query.
        :return: V1alpha1RepoCredsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repo_creds_service_list_repository_credentials" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repocreds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1alpha1RepoCredsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def repo_creds_service_update_repository_credentials(self, body, creds_url, **kwargs):  # noqa: E501
        """UpdateRepositoryCredentials updates a repository credential set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repo_creds_service_update_repository_credentials(body, creds_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1alpha1RepoCreds body: (required)
        :param str creds_url: URL is the URL that this credentials matches to (required)
        :return: V1alpha1RepoCreds
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repo_creds_service_update_repository_credentials_with_http_info(body, creds_url, **kwargs)  # noqa: E501
        else:
            (data) = self.repo_creds_service_update_repository_credentials_with_http_info(body, creds_url, **kwargs)  # noqa: E501
            return data

    def repo_creds_service_update_repository_credentials_with_http_info(self, body, creds_url, **kwargs):  # noqa: E501
        """UpdateRepositoryCredentials updates a repository credential set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repo_creds_service_update_repository_credentials_with_http_info(body, creds_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1alpha1RepoCreds body: (required)
        :param str creds_url: URL is the URL that this credentials matches to (required)
        :return: V1alpha1RepoCreds
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'creds_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repo_creds_service_update_repository_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `repo_creds_service_update_repository_credentials`")  # noqa: E501
        # verify the required parameter 'creds_url' is set
        if ('creds_url' not in params or
                params['creds_url'] is None):
            raise ValueError("Missing the required parameter `creds_url` when calling `repo_creds_service_update_repository_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'creds_url' in params:
            path_params['creds.url'] = params['creds_url']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repocreds/{creds.url}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1alpha1RepoCreds',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)