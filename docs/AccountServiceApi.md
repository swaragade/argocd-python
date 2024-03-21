# swagger_client.AccountServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_service_can_i**](AccountServiceApi.md#account_service_can_i) | **GET** /api/v1/account/can-i/{resource}/{action}/{subresource} | CanI checks if the current account has permission to perform an action
[**account_service_create_token**](AccountServiceApi.md#account_service_create_token) | **POST** /api/v1/account/{name}/token | CreateToken creates a token
[**account_service_delete_token**](AccountServiceApi.md#account_service_delete_token) | **DELETE** /api/v1/account/{name}/token/{id} | DeleteToken deletes a token
[**account_service_get_account**](AccountServiceApi.md#account_service_get_account) | **GET** /api/v1/account/{name} | GetAccount returns an account
[**account_service_list_accounts**](AccountServiceApi.md#account_service_list_accounts) | **GET** /api/v1/account | ListAccounts returns the list of accounts
[**account_service_update_password**](AccountServiceApi.md#account_service_update_password) | **PUT** /api/v1/account/password | UpdatePassword updates an account&#x27;s password to a new value

# **account_service_can_i**
> AccountCanIResponse account_service_can_i(resource, action, subresource)

CanI checks if the current account has permission to perform an action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountServiceApi()
resource = 'resource_example' # str | 
action = 'action_example' # str | 
subresource = 'subresource_example' # str | 

try:
    # CanI checks if the current account has permission to perform an action
    api_response = api_instance.account_service_can_i(resource, action, subresource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServiceApi->account_service_can_i: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **action** | **str**|  | 
 **subresource** | **str**|  | 

### Return type

[**AccountCanIResponse**](AccountCanIResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_service_create_token**
> AccountCreateTokenResponse account_service_create_token(body, name)

CreateToken creates a token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountServiceApi()
body = swagger_client.AccountCreateTokenRequest() # AccountCreateTokenRequest | 
name = 'name_example' # str | 

try:
    # CreateToken creates a token
    api_response = api_instance.account_service_create_token(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServiceApi->account_service_create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCreateTokenRequest**](AccountCreateTokenRequest.md)|  | 
 **name** | **str**|  | 

### Return type

[**AccountCreateTokenResponse**](AccountCreateTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_service_delete_token**
> AccountEmptyResponse account_service_delete_token(name, id)

DeleteToken deletes a token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountServiceApi()
name = 'name_example' # str | 
id = 'id_example' # str | 

try:
    # DeleteToken deletes a token
    api_response = api_instance.account_service_delete_token(name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServiceApi->account_service_delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**AccountEmptyResponse**](AccountEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_service_get_account**
> AccountAccount account_service_get_account(name)

GetAccount returns an account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountServiceApi()
name = 'name_example' # str | 

try:
    # GetAccount returns an account
    api_response = api_instance.account_service_get_account(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServiceApi->account_service_get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**AccountAccount**](AccountAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_service_list_accounts**
> AccountAccountsList account_service_list_accounts()

ListAccounts returns the list of accounts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountServiceApi()

try:
    # ListAccounts returns the list of accounts
    api_response = api_instance.account_service_list_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServiceApi->account_service_list_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountAccountsList**](AccountAccountsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_service_update_password**
> AccountUpdatePasswordResponse account_service_update_password(body)

UpdatePassword updates an account's password to a new value

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountServiceApi()
body = swagger_client.AccountUpdatePasswordRequest() # AccountUpdatePasswordRequest | 

try:
    # UpdatePassword updates an account's password to a new value
    api_response = api_instance.account_service_update_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServiceApi->account_service_update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountUpdatePasswordRequest**](AccountUpdatePasswordRequest.md)|  | 

### Return type

[**AccountUpdatePasswordResponse**](AccountUpdatePasswordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

