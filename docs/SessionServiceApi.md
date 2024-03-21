# swagger_client.SessionServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**session_service_create**](SessionServiceApi.md#session_service_create) | **POST** /api/v1/session | Create a new JWT for authentication and set a cookie if using HTTP
[**session_service_delete**](SessionServiceApi.md#session_service_delete) | **DELETE** /api/v1/session | Delete an existing JWT cookie if using HTTP
[**session_service_get_user_info**](SessionServiceApi.md#session_service_get_user_info) | **GET** /api/v1/session/userinfo | Get the current user&#x27;s info

# **session_service_create**
> SessionSessionResponse session_service_create(body)

Create a new JWT for authentication and set a cookie if using HTTP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionServiceApi()
body = swagger_client.SessionSessionCreateRequest() # SessionSessionCreateRequest | 

try:
    # Create a new JWT for authentication and set a cookie if using HTTP
    api_response = api_instance.session_service_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionServiceApi->session_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionSessionCreateRequest**](SessionSessionCreateRequest.md)|  | 

### Return type

[**SessionSessionResponse**](SessionSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_service_delete**
> SessionSessionResponse session_service_delete()

Delete an existing JWT cookie if using HTTP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionServiceApi()

try:
    # Delete an existing JWT cookie if using HTTP
    api_response = api_instance.session_service_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionServiceApi->session_service_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionSessionResponse**](SessionSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_service_get_user_info**
> SessionGetUserInfoResponse session_service_get_user_info()

Get the current user's info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionServiceApi()

try:
    # Get the current user's info
    api_response = api_instance.session_service_get_user_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionServiceApi->session_service_get_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionGetUserInfoResponse**](SessionGetUserInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

