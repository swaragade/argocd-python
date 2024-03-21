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


class ApplicationSetServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def application_set_service_create(self, body, **kwargs):  # noqa: E501
        """Create creates an applicationset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.application_set_service_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1alpha1ApplicationSet body: (required)
        :param bool upsert:
        :return: V1alpha1ApplicationSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.application_set_service_create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.application_set_service_create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def application_set_service_create_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create creates an applicationset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.application_set_service_create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1alpha1ApplicationSet body: (required)
        :param bool upsert:
        :return: V1alpha1ApplicationSet
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
                    " to method application_set_service_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `application_set_service_create`")  # noqa: E501

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
            '/api/v1/applicationsets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1alpha1ApplicationSet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def application_set_service_delete(self, name, **kwargs):  # noqa: E501
        """Delete deletes an application set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.application_set_service_delete(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str appset_namespace: The application set namespace. Default empty is argocd control plane namespace.
        :return: ApplicationsetApplicationSetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.application_set_service_delete_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.application_set_service_delete_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def application_set_service_delete_with_http_info(self, name, **kwargs):  # noqa: E501
        """Delete deletes an application set  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.application_set_service_delete_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str appset_namespace: The application set namespace. Default empty is argocd control plane namespace.
        :return: ApplicationsetApplicationSetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'appset_namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method application_set_service_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `application_set_service_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'appset_namespace' in params:
            query_params.append(('appsetNamespace', params['appset_namespace']))  # noqa: E501

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
            '/api/v1/applicationsets/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationsetApplicationSetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def application_set_service_get(self, name, **kwargs):  # noqa: E501
        """Get returns an applicationset by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.application_set_service_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: the applicationsets's name (required)
        :param str appset_namespace: The application set namespace. Default empty is argocd control plane namespace.
        :return: V1alpha1ApplicationSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.application_set_service_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.application_set_service_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def application_set_service_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """Get returns an applicationset by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.application_set_service_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: the applicationsets's name (required)
        :param str appset_namespace: The application set namespace. Default empty is argocd control plane namespace.
        :return: V1alpha1ApplicationSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'appset_namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method application_set_service_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `application_set_service_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'appset_namespace' in params:
            query_params.append(('appsetNamespace', params['appset_namespace']))  # noqa: E501

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
            '/api/v1/applicationsets/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1alpha1ApplicationSet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def application_set_service_list(self, **kwargs):  # noqa: E501
        """List returns list of applicationset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.application_set_service_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] projects: the project names to restrict returned list applicationsets.
        :param str selector: the selector to restrict returned list to applications only with matched labels.
        :param str appset_namespace: The application set namespace. Default empty is argocd control plane namespace.
        :return: V1alpha1ApplicationSetList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.application_set_service_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.application_set_service_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def application_set_service_list_with_http_info(self, **kwargs):  # noqa: E501
        """List returns list of applicationset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.application_set_service_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] projects: the project names to restrict returned list applicationsets.
        :param str selector: the selector to restrict returned list to applications only with matched labels.
        :param str appset_namespace: The application set namespace. Default empty is argocd control plane namespace.
        :return: V1alpha1ApplicationSetList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['projects', 'selector', 'appset_namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method application_set_service_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'projects' in params:
            query_params.append(('projects', params['projects']))  # noqa: E501
            collection_formats['projects'] = 'multi'  # noqa: E501
        if 'selector' in params:
            query_params.append(('selector', params['selector']))  # noqa: E501
        if 'appset_namespace' in params:
            query_params.append(('appsetNamespace', params['appset_namespace']))  # noqa: E501

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
            '/api/v1/applicationsets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1alpha1ApplicationSetList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
