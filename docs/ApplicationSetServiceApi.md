# swagger_client.ApplicationSetServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_set_service_create**](ApplicationSetServiceApi.md#application_set_service_create) | **POST** /api/v1/applicationsets | Create creates an applicationset
[**application_set_service_delete**](ApplicationSetServiceApi.md#application_set_service_delete) | **DELETE** /api/v1/applicationsets/{name} | Delete deletes an application set
[**application_set_service_get**](ApplicationSetServiceApi.md#application_set_service_get) | **GET** /api/v1/applicationsets/{name} | Get returns an applicationset by name
[**application_set_service_list**](ApplicationSetServiceApi.md#application_set_service_list) | **GET** /api/v1/applicationsets | List returns list of applicationset

# **application_set_service_create**
> V1alpha1ApplicationSet application_set_service_create(body, upsert=upsert)

Create creates an applicationset

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationSetServiceApi()
body = swagger_client.V1alpha1ApplicationSet() # V1alpha1ApplicationSet | 
upsert = true # bool |  (optional)

try:
    # Create creates an applicationset
    api_response = api_instance.application_set_service_create(body, upsert=upsert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationSetServiceApi->application_set_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1ApplicationSet**](V1alpha1ApplicationSet.md)|  | 
 **upsert** | **bool**|  | [optional] 

### Return type

[**V1alpha1ApplicationSet**](V1alpha1ApplicationSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_set_service_delete**
> ApplicationsetApplicationSetResponse application_set_service_delete(name, appset_namespace=appset_namespace)

Delete deletes an application set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationSetServiceApi()
name = 'name_example' # str | 
appset_namespace = 'appset_namespace_example' # str | The application set namespace. Default empty is argocd control plane namespace. (optional)

try:
    # Delete deletes an application set
    api_response = api_instance.application_set_service_delete(name, appset_namespace=appset_namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationSetServiceApi->application_set_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **appset_namespace** | **str**| The application set namespace. Default empty is argocd control plane namespace. | [optional] 

### Return type

[**ApplicationsetApplicationSetResponse**](ApplicationsetApplicationSetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_set_service_get**
> V1alpha1ApplicationSet application_set_service_get(name, appset_namespace=appset_namespace)

Get returns an applicationset by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationSetServiceApi()
name = 'name_example' # str | the applicationsets's name
appset_namespace = 'appset_namespace_example' # str | The application set namespace. Default empty is argocd control plane namespace. (optional)

try:
    # Get returns an applicationset by name
    api_response = api_instance.application_set_service_get(name, appset_namespace=appset_namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationSetServiceApi->application_set_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the applicationsets&#x27;s name | 
 **appset_namespace** | **str**| The application set namespace. Default empty is argocd control plane namespace. | [optional] 

### Return type

[**V1alpha1ApplicationSet**](V1alpha1ApplicationSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_set_service_list**
> V1alpha1ApplicationSetList application_set_service_list(projects=projects, selector=selector, appset_namespace=appset_namespace)

List returns list of applicationset

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationSetServiceApi()
projects = ['projects_example'] # list[str] | the project names to restrict returned list applicationsets. (optional)
selector = 'selector_example' # str | the selector to restrict returned list to applications only with matched labels. (optional)
appset_namespace = 'appset_namespace_example' # str | The application set namespace. Default empty is argocd control plane namespace. (optional)

try:
    # List returns list of applicationset
    api_response = api_instance.application_set_service_list(projects=projects, selector=selector, appset_namespace=appset_namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationSetServiceApi->application_set_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects** | [**list[str]**](str.md)| the project names to restrict returned list applicationsets. | [optional] 
 **selector** | **str**| the selector to restrict returned list to applications only with matched labels. | [optional] 
 **appset_namespace** | **str**| The application set namespace. Default empty is argocd control plane namespace. | [optional] 

### Return type

[**V1alpha1ApplicationSetList**](V1alpha1ApplicationSetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

