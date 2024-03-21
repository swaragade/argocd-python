# argocd.GPGKeyServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_pg_key_service_create**](GPGKeyServiceApi.md#g_pg_key_service_create) | **POST** /api/v1/gpgkeys | Create one or more GPG public keys in the server&#x27;s configuration
[**g_pg_key_service_delete**](GPGKeyServiceApi.md#g_pg_key_service_delete) | **DELETE** /api/v1/gpgkeys | Delete specified GPG public key from the server&#x27;s configuration
[**g_pg_key_service_get**](GPGKeyServiceApi.md#g_pg_key_service_get) | **GET** /api/v1/gpgkeys/{keyID} | Get information about specified GPG public key from the server
[**g_pg_key_service_list**](GPGKeyServiceApi.md#g_pg_key_service_list) | **GET** /api/v1/gpgkeys | List all available repository certificates

# **g_pg_key_service_create**
> GpgkeyGnuPGPublicKeyCreateResponse g_pg_key_service_create(body, upsert=upsert)

Create one or more GPG public keys in the server's configuration

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.GPGKeyServiceApi()
body = argocd.V1alpha1GnuPGPublicKey() # V1alpha1GnuPGPublicKey | Raw key data of the GPG key(s) to create
upsert = true # bool | Whether to upsert already existing public keys. (optional)

try:
    # Create one or more GPG public keys in the server's configuration
    api_response = api_instance.g_pg_key_service_create(body, upsert=upsert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GPGKeyServiceApi->g_pg_key_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1GnuPGPublicKey**](V1alpha1GnuPGPublicKey.md)| Raw key data of the GPG key(s) to create | 
 **upsert** | **bool**| Whether to upsert already existing public keys. | [optional] 

### Return type

[**GpgkeyGnuPGPublicKeyCreateResponse**](GpgkeyGnuPGPublicKeyCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_pg_key_service_delete**
> GpgkeyGnuPGPublicKeyResponse g_pg_key_service_delete(key_id=key_id)

Delete specified GPG public key from the server's configuration

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.GPGKeyServiceApi()
key_id = 'key_id_example' # str | The GPG key ID to query for. (optional)

try:
    # Delete specified GPG public key from the server's configuration
    api_response = api_instance.g_pg_key_service_delete(key_id=key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GPGKeyServiceApi->g_pg_key_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The GPG key ID to query for. | [optional] 

### Return type

[**GpgkeyGnuPGPublicKeyResponse**](GpgkeyGnuPGPublicKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_pg_key_service_get**
> V1alpha1GnuPGPublicKey g_pg_key_service_get(key_id)

Get information about specified GPG public key from the server

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.GPGKeyServiceApi()
key_id = 'key_id_example' # str | The GPG key ID to query for

try:
    # Get information about specified GPG public key from the server
    api_response = api_instance.g_pg_key_service_get(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GPGKeyServiceApi->g_pg_key_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The GPG key ID to query for | 

### Return type

[**V1alpha1GnuPGPublicKey**](V1alpha1GnuPGPublicKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_pg_key_service_list**
> V1alpha1GnuPGPublicKeyList g_pg_key_service_list(key_id=key_id)

List all available repository certificates

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.GPGKeyServiceApi()
key_id = 'key_id_example' # str | The GPG key ID to query for. (optional)

try:
    # List all available repository certificates
    api_response = api_instance.g_pg_key_service_list(key_id=key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GPGKeyServiceApi->g_pg_key_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The GPG key ID to query for. | [optional] 

### Return type

[**V1alpha1GnuPGPublicKeyList**](V1alpha1GnuPGPublicKeyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

