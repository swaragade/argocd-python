# swagger_client.ClusterServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_service_create**](ClusterServiceApi.md#cluster_service_create) | **POST** /api/v1/clusters | Create creates a cluster
[**cluster_service_delete**](ClusterServiceApi.md#cluster_service_delete) | **DELETE** /api/v1/clusters/{id.value} | Delete deletes a cluster
[**cluster_service_get**](ClusterServiceApi.md#cluster_service_get) | **GET** /api/v1/clusters/{id.value} | Get returns a cluster by server address
[**cluster_service_invalidate_cache**](ClusterServiceApi.md#cluster_service_invalidate_cache) | **POST** /api/v1/clusters/{id.value}/invalidate-cache | InvalidateCache invalidates cluster cache
[**cluster_service_list**](ClusterServiceApi.md#cluster_service_list) | **GET** /api/v1/clusters | List returns list of clusters
[**cluster_service_rotate_auth**](ClusterServiceApi.md#cluster_service_rotate_auth) | **POST** /api/v1/clusters/{id.value}/rotate-auth | RotateAuth rotates the bearer token used for a cluster
[**cluster_service_update**](ClusterServiceApi.md#cluster_service_update) | **PUT** /api/v1/clusters/{id.value} | Update updates a cluster

# **cluster_service_create**
> V1alpha1Cluster cluster_service_create(body, upsert=upsert)

Create creates a cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterServiceApi()
body = swagger_client.V1alpha1Cluster() # V1alpha1Cluster | 
upsert = true # bool |  (optional)

try:
    # Create creates a cluster
    api_response = api_instance.cluster_service_create(body, upsert=upsert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterServiceApi->cluster_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1Cluster**](V1alpha1Cluster.md)|  | 
 **upsert** | **bool**|  | [optional] 

### Return type

[**V1alpha1Cluster**](V1alpha1Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_service_delete**
> ClusterClusterResponse cluster_service_delete(id_value, server=server, name=name, id_type=id_type)

Delete deletes a cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterServiceApi()
id_value = 'id_value_example' # str | value holds the cluster server URL or cluster name
server = 'server_example' # str |  (optional)
name = 'name_example' # str |  (optional)
id_type = 'id_type_example' # str | type is the type of the specified cluster identifier ( \"server\" - default, \"name\" ). (optional)

try:
    # Delete deletes a cluster
    api_response = api_instance.cluster_service_delete(id_value, server=server, name=name, id_type=id_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterServiceApi->cluster_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_value** | **str**| value holds the cluster server URL or cluster name | 
 **server** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **id_type** | **str**| type is the type of the specified cluster identifier ( \&quot;server\&quot; - default, \&quot;name\&quot; ). | [optional] 

### Return type

[**ClusterClusterResponse**](ClusterClusterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_service_get**
> V1alpha1Cluster cluster_service_get(id_value, server=server, name=name, id_type=id_type)

Get returns a cluster by server address

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterServiceApi()
id_value = 'id_value_example' # str | value holds the cluster server URL or cluster name
server = 'server_example' # str |  (optional)
name = 'name_example' # str |  (optional)
id_type = 'id_type_example' # str | type is the type of the specified cluster identifier ( \"server\" - default, \"name\" ). (optional)

try:
    # Get returns a cluster by server address
    api_response = api_instance.cluster_service_get(id_value, server=server, name=name, id_type=id_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterServiceApi->cluster_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_value** | **str**| value holds the cluster server URL or cluster name | 
 **server** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **id_type** | **str**| type is the type of the specified cluster identifier ( \&quot;server\&quot; - default, \&quot;name\&quot; ). | [optional] 

### Return type

[**V1alpha1Cluster**](V1alpha1Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_service_invalidate_cache**
> V1alpha1Cluster cluster_service_invalidate_cache(id_value)

InvalidateCache invalidates cluster cache

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterServiceApi()
id_value = 'id_value_example' # str | value holds the cluster server URL or cluster name

try:
    # InvalidateCache invalidates cluster cache
    api_response = api_instance.cluster_service_invalidate_cache(id_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterServiceApi->cluster_service_invalidate_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_value** | **str**| value holds the cluster server URL or cluster name | 

### Return type

[**V1alpha1Cluster**](V1alpha1Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_service_list**
> V1alpha1ClusterList cluster_service_list(server=server, name=name, id_type=id_type, id_value=id_value)

List returns list of clusters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterServiceApi()
server = 'server_example' # str |  (optional)
name = 'name_example' # str |  (optional)
id_type = 'id_type_example' # str | type is the type of the specified cluster identifier ( \"server\" - default, \"name\" ). (optional)
id_value = 'id_value_example' # str | value holds the cluster server URL or cluster name. (optional)

try:
    # List returns list of clusters
    api_response = api_instance.cluster_service_list(server=server, name=name, id_type=id_type, id_value=id_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterServiceApi->cluster_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **id_type** | **str**| type is the type of the specified cluster identifier ( \&quot;server\&quot; - default, \&quot;name\&quot; ). | [optional] 
 **id_value** | **str**| value holds the cluster server URL or cluster name. | [optional] 

### Return type

[**V1alpha1ClusterList**](V1alpha1ClusterList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_service_rotate_auth**
> ClusterClusterResponse cluster_service_rotate_auth(id_value)

RotateAuth rotates the bearer token used for a cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterServiceApi()
id_value = 'id_value_example' # str | value holds the cluster server URL or cluster name

try:
    # RotateAuth rotates the bearer token used for a cluster
    api_response = api_instance.cluster_service_rotate_auth(id_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterServiceApi->cluster_service_rotate_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_value** | **str**| value holds the cluster server URL or cluster name | 

### Return type

[**ClusterClusterResponse**](ClusterClusterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_service_update**
> V1alpha1Cluster cluster_service_update(body, id_value, updated_fields=updated_fields, id_type=id_type)

Update updates a cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterServiceApi()
body = swagger_client.V1alpha1Cluster() # V1alpha1Cluster | 
id_value = 'id_value_example' # str | value holds the cluster server URL or cluster name
updated_fields = ['updated_fields_example'] # list[str] |  (optional)
id_type = 'id_type_example' # str | type is the type of the specified cluster identifier ( \"server\" - default, \"name\" ). (optional)

try:
    # Update updates a cluster
    api_response = api_instance.cluster_service_update(body, id_value, updated_fields=updated_fields, id_type=id_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterServiceApi->cluster_service_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1Cluster**](V1alpha1Cluster.md)|  | 
 **id_value** | **str**| value holds the cluster server URL or cluster name | 
 **updated_fields** | [**list[str]**](str.md)|  | [optional] 
 **id_type** | **str**| type is the type of the specified cluster identifier ( \&quot;server\&quot; - default, \&quot;name\&quot; ). | [optional] 

### Return type

[**V1alpha1Cluster**](V1alpha1Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

