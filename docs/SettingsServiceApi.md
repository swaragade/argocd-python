# swagger_client.SettingsServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_service_get**](SettingsServiceApi.md#settings_service_get) | **GET** /api/v1/settings | Get returns Argo CD settings
[**settings_service_get_plugins**](SettingsServiceApi.md#settings_service_get_plugins) | **GET** /api/v1/settings/plugins | Get returns Argo CD plugins

# **settings_service_get**
> ClusterSettings settings_service_get()

Get returns Argo CD settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SettingsServiceApi()

try:
    # Get returns Argo CD settings
    api_response = api_instance.settings_service_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsServiceApi->settings_service_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterSettings**](ClusterSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_service_get_plugins**
> ClusterSettingsPluginsResponse settings_service_get_plugins()

Get returns Argo CD plugins

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SettingsServiceApi()

try:
    # Get returns Argo CD plugins
    api_response = api_instance.settings_service_get_plugins()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsServiceApi->settings_service_get_plugins: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterSettingsPluginsResponse**](ClusterSettingsPluginsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

