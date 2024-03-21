# argocd.ProjectServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_service_create**](ProjectServiceApi.md#project_service_create) | **POST** /api/v1/projects | Create a new project
[**project_service_create_token**](ProjectServiceApi.md#project_service_create_token) | **POST** /api/v1/projects/{project}/roles/{role}/token | Create a new project token
[**project_service_delete**](ProjectServiceApi.md#project_service_delete) | **DELETE** /api/v1/projects/{name} | Delete deletes a project
[**project_service_delete_token**](ProjectServiceApi.md#project_service_delete_token) | **DELETE** /api/v1/projects/{project}/roles/{role}/token/{iat} | Delete a new project token
[**project_service_get**](ProjectServiceApi.md#project_service_get) | **GET** /api/v1/projects/{name} | Get returns a project by name
[**project_service_get_detailed_project**](ProjectServiceApi.md#project_service_get_detailed_project) | **GET** /api/v1/projects/{name}/detailed | GetDetailedProject returns a project that include project, global project and scoped resources by name
[**project_service_get_global_projects**](ProjectServiceApi.md#project_service_get_global_projects) | **GET** /api/v1/projects/{name}/globalprojects | Get returns a virtual project by name
[**project_service_get_sync_windows_state**](ProjectServiceApi.md#project_service_get_sync_windows_state) | **GET** /api/v1/projects/{name}/syncwindows | GetSchedulesState returns true if there are any active sync syncWindows
[**project_service_list**](ProjectServiceApi.md#project_service_list) | **GET** /api/v1/projects | List returns list of projects
[**project_service_list_events**](ProjectServiceApi.md#project_service_list_events) | **GET** /api/v1/projects/{name}/events | ListEvents returns a list of project events
[**project_service_list_links**](ProjectServiceApi.md#project_service_list_links) | **GET** /api/v1/projects/{name}/links | ListLinks returns all deep links for the particular project
[**project_service_update**](ProjectServiceApi.md#project_service_update) | **PUT** /api/v1/projects/{project.metadata.name} | Update updates a project

# **project_service_create**
> V1alpha1AppProject project_service_create(body)

Create a new project

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.ProjectServiceApi()
body = argocd.ProjectProjectCreateRequest() # ProjectProjectCreateRequest | 

try:
    # Create a new project
    api_response = api_instance.project_service_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->project_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectProjectCreateRequest**](ProjectProjectCreateRequest.md)|  | 

### Return type

[**V1alpha1AppProject**](V1alpha1AppProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_create_token**
> ProjectProjectTokenResponse project_service_create_token(body, project, role)

Create a new project token

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.ProjectServiceApi()
body = argocd.ProjectProjectTokenCreateRequest() # ProjectProjectTokenCreateRequest | 
project = 'project_example' # str | 
role = 'role_example' # str | 

try:
    # Create a new project token
    api_response = api_instance.project_service_create_token(body, project, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->project_service_create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectProjectTokenCreateRequest**](ProjectProjectTokenCreateRequest.md)|  | 
 **project** | **str**|  | 
 **role** | **str**|  | 

### Return type

[**ProjectProjectTokenResponse**](ProjectProjectTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_delete**
> ProjectEmptyResponse project_service_delete(name)

Delete deletes a project

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.ProjectServiceApi()
name = 'name_example' # str | 

try:
    # Delete deletes a project
    api_response = api_instance.project_service_delete(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->project_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ProjectEmptyResponse**](ProjectEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_delete_token**
> ProjectEmptyResponse project_service_delete_token(project, role, iat, id=id)

Delete a new project token

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.ProjectServiceApi()
project = 'project_example' # str | 
role = 'role_example' # str | 
iat = 'iat_example' # str | 
id = 'id_example' # str |  (optional)

try:
    # Delete a new project token
    api_response = api_instance.project_service_delete_token(project, role, iat, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->project_service_delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
 **role** | **str**|  | 
 **iat** | **str**|  | 
 **id** | **str**|  | [optional] 

### Return type

[**ProjectEmptyResponse**](ProjectEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_get**
> V1alpha1AppProject project_service_get(name)

Get returns a project by name

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.ProjectServiceApi()
name = 'name_example' # str | 

try:
    # Get returns a project by name
    api_response = api_instance.project_service_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->project_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**V1alpha1AppProject**](V1alpha1AppProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_get_detailed_project**
> ProjectDetailedProjectsResponse project_service_get_detailed_project(name)

GetDetailedProject returns a project that include project, global project and scoped resources by name

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.ProjectServiceApi()
name = 'name_example' # str | 

try:
    # GetDetailedProject returns a project that include project, global project and scoped resources by name
    api_response = api_instance.project_service_get_detailed_project(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->project_service_get_detailed_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ProjectDetailedProjectsResponse**](ProjectDetailedProjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_get_global_projects**
> ProjectGlobalProjectsResponse project_service_get_global_projects(name)

Get returns a virtual project by name

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.ProjectServiceApi()
name = 'name_example' # str | 

try:
    # Get returns a virtual project by name
    api_response = api_instance.project_service_get_global_projects(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->project_service_get_global_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ProjectGlobalProjectsResponse**](ProjectGlobalProjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_get_sync_windows_state**
> ProjectSyncWindowsResponse project_service_get_sync_windows_state(name)

GetSchedulesState returns true if there are any active sync syncWindows

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.ProjectServiceApi()
name = 'name_example' # str | 

try:
    # GetSchedulesState returns true if there are any active sync syncWindows
    api_response = api_instance.project_service_get_sync_windows_state(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->project_service_get_sync_windows_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ProjectSyncWindowsResponse**](ProjectSyncWindowsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_list**
> V1alpha1AppProjectList project_service_list(name=name)

List returns list of projects

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.ProjectServiceApi()
name = 'name_example' # str |  (optional)

try:
    # List returns list of projects
    api_response = api_instance.project_service_list(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->project_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**V1alpha1AppProjectList**](V1alpha1AppProjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_list_events**
> V1EventList project_service_list_events(name)

ListEvents returns a list of project events

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.ProjectServiceApi()
name = 'name_example' # str | 

try:
    # ListEvents returns a list of project events
    api_response = api_instance.project_service_list_events(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->project_service_list_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**V1EventList**](V1EventList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_list_links**
> ApplicationLinksResponse project_service_list_links(name)

ListLinks returns all deep links for the particular project

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.ProjectServiceApi()
name = 'name_example' # str | 

try:
    # ListLinks returns all deep links for the particular project
    api_response = api_instance.project_service_list_links(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->project_service_list_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ApplicationLinksResponse**](ApplicationLinksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_service_update**
> V1alpha1AppProject project_service_update(body, project_metadata_name)

Update updates a project

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.ProjectServiceApi()
body = argocd.ProjectProjectUpdateRequest() # ProjectProjectUpdateRequest | 
project_metadata_name = 'project_metadata_name_example' # str | Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional

try:
    # Update updates a project
    api_response = api_instance.project_service_update(body, project_metadata_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->project_service_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectProjectUpdateRequest**](ProjectProjectUpdateRequest.md)|  | 
 **project_metadata_name** | **str**| Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional | 

### Return type

[**V1alpha1AppProject**](V1alpha1AppProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

