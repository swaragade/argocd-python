# swagger_client.VersionServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_service_version**](VersionServiceApi.md#version_service_version) | **GET** /api/version | Version returns version information of the API server

# **version_service_version**
> VersionVersionMessage version_service_version()

Version returns version information of the API server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionServiceApi()

try:
    # Version returns version information of the API server
    api_response = api_instance.version_service_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionServiceApi->version_service_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionVersionMessage**](VersionVersionMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

