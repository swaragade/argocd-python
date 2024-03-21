# swagger_client.ApplicationServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_service_create**](ApplicationServiceApi.md#application_service_create) | **POST** /api/v1/applications | Create creates an application
[**application_service_delete**](ApplicationServiceApi.md#application_service_delete) | **DELETE** /api/v1/applications/{name} | Delete deletes an application
[**application_service_delete_resource**](ApplicationServiceApi.md#application_service_delete_resource) | **DELETE** /api/v1/applications/{name}/resource | DeleteResource deletes a single application resource
[**application_service_get**](ApplicationServiceApi.md#application_service_get) | **GET** /api/v1/applications/{name} | Get returns an application by name
[**application_service_get_application_sync_windows**](ApplicationServiceApi.md#application_service_get_application_sync_windows) | **GET** /api/v1/applications/{name}/syncwindows | Get returns sync windows of the application
[**application_service_get_manifests**](ApplicationServiceApi.md#application_service_get_manifests) | **GET** /api/v1/applications/{name}/manifests | GetManifests returns application manifests
[**application_service_get_manifests_with_files**](ApplicationServiceApi.md#application_service_get_manifests_with_files) | **POST** /api/v1/applications/manifestsWithFiles | GetManifestsWithFiles returns application manifests using provided files to generate them
[**application_service_get_resource**](ApplicationServiceApi.md#application_service_get_resource) | **GET** /api/v1/applications/{name}/resource | GetResource returns single application resource
[**application_service_list**](ApplicationServiceApi.md#application_service_list) | **GET** /api/v1/applications | List returns list of applications
[**application_service_list_links**](ApplicationServiceApi.md#application_service_list_links) | **GET** /api/v1/applications/{name}/links | ListLinks returns the list of all application deep links
[**application_service_list_resource_actions**](ApplicationServiceApi.md#application_service_list_resource_actions) | **GET** /api/v1/applications/{name}/resource/actions | ListResourceActions returns list of resource actions
[**application_service_list_resource_events**](ApplicationServiceApi.md#application_service_list_resource_events) | **GET** /api/v1/applications/{name}/events | ListResourceEvents returns a list of event resources
[**application_service_list_resource_links**](ApplicationServiceApi.md#application_service_list_resource_links) | **GET** /api/v1/applications/{name}/resource/links | ListResourceLinks returns the list of all resource deep links
[**application_service_managed_resources**](ApplicationServiceApi.md#application_service_managed_resources) | **GET** /api/v1/applications/{applicationName}/managed-resources | ManagedResources returns list of managed resources
[**application_service_patch**](ApplicationServiceApi.md#application_service_patch) | **PATCH** /api/v1/applications/{name} | Patch patch an application
[**application_service_patch_resource**](ApplicationServiceApi.md#application_service_patch_resource) | **POST** /api/v1/applications/{name}/resource | PatchResource patch single application resource
[**application_service_pod_logs**](ApplicationServiceApi.md#application_service_pod_logs) | **GET** /api/v1/applications/{name}/pods/{podName}/logs | PodLogs returns stream of log entries for the specified pod. Pod
[**application_service_pod_logs2**](ApplicationServiceApi.md#application_service_pod_logs2) | **GET** /api/v1/applications/{name}/logs | PodLogs returns stream of log entries for the specified pod. Pod
[**application_service_resource_tree**](ApplicationServiceApi.md#application_service_resource_tree) | **GET** /api/v1/applications/{applicationName}/resource-tree | ResourceTree returns resource tree
[**application_service_revision_chart_details**](ApplicationServiceApi.md#application_service_revision_chart_details) | **GET** /api/v1/applications/{name}/revisions/{revision}/chartdetails | Get the chart metadata (description, maintainers, home) for a specific revision of the application
[**application_service_revision_metadata**](ApplicationServiceApi.md#application_service_revision_metadata) | **GET** /api/v1/applications/{name}/revisions/{revision}/metadata | Get the meta-data (author, date, tags, message) for a specific revision of the application
[**application_service_rollback**](ApplicationServiceApi.md#application_service_rollback) | **POST** /api/v1/applications/{name}/rollback | Rollback syncs an application to its target state
[**application_service_run_resource_action**](ApplicationServiceApi.md#application_service_run_resource_action) | **POST** /api/v1/applications/{name}/resource/actions | RunResourceAction run resource action
[**application_service_sync**](ApplicationServiceApi.md#application_service_sync) | **POST** /api/v1/applications/{name}/sync | Sync syncs an application to its target state
[**application_service_terminate_operation**](ApplicationServiceApi.md#application_service_terminate_operation) | **DELETE** /api/v1/applications/{name}/operation | TerminateOperation terminates the currently running operation
[**application_service_update**](ApplicationServiceApi.md#application_service_update) | **PUT** /api/v1/applications/{application.metadata.name} | Update updates an application
[**application_service_update_spec**](ApplicationServiceApi.md#application_service_update_spec) | **PUT** /api/v1/applications/{name}/spec | UpdateSpec updates an application spec
[**application_service_watch**](ApplicationServiceApi.md#application_service_watch) | **GET** /api/v1/stream/applications | Watch returns stream of application change events
[**application_service_watch_resource_tree**](ApplicationServiceApi.md#application_service_watch_resource_tree) | **GET** /api/v1/stream/applications/{applicationName}/resource-tree | Watch returns stream of application resource tree

# **application_service_create**
> V1alpha1Application application_service_create(body, upsert=upsert, validate=validate)

Create creates an application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
body = swagger_client.V1alpha1Application() # V1alpha1Application | 
upsert = true # bool |  (optional)
validate = true # bool |  (optional)

try:
    # Create creates an application
    api_response = api_instance.application_service_create(body, upsert=upsert, validate=validate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1Application**](V1alpha1Application.md)|  | 
 **upsert** | **bool**|  | [optional] 
 **validate** | **bool**|  | [optional] 

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_delete**
> ApplicationApplicationResponse application_service_delete(name, cascade=cascade, propagation_policy=propagation_policy, app_namespace=app_namespace, project=project)

Delete deletes an application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | 
cascade = true # bool |  (optional)
propagation_policy = 'propagation_policy_example' # str |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # Delete deletes an application
    api_response = api_instance.application_service_delete(name, cascade=cascade, propagation_policy=propagation_policy, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **cascade** | **bool**|  | [optional] 
 **propagation_policy** | **str**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**ApplicationApplicationResponse**](ApplicationApplicationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_delete_resource**
> ApplicationApplicationResponse application_service_delete_resource(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, force=force, orphan=orphan, app_namespace=app_namespace, project=project)

DeleteResource deletes a single application resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
force = true # bool |  (optional)
orphan = true # bool |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # DeleteResource deletes a single application resource
    api_response = api_instance.application_service_delete_resource(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, force=force, orphan=orphan, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_delete_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **force** | **bool**|  | [optional] 
 **orphan** | **bool**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**ApplicationApplicationResponse**](ApplicationApplicationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_get**
> V1alpha1Application application_service_get(name, refresh=refresh, projects=projects, resource_version=resource_version, selector=selector, repo=repo, app_namespace=app_namespace, project=project)

Get returns an application by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | the application's name
refresh = 'refresh_example' # str | forces application reconciliation if set to 'hard'. (optional)
projects = ['projects_example'] # list[str] | the project names to restrict returned list applications. (optional)
resource_version = 'resource_version_example' # str | when specified with a watch call, shows changes that occur after that particular version of a resource. (optional)
selector = 'selector_example' # str | the selector to restrict returned list to applications only with matched labels. (optional)
repo = 'repo_example' # str | the repoURL to restrict returned list applications. (optional)
app_namespace = 'app_namespace_example' # str | the application's namespace. (optional)
project = ['project_example'] # list[str] | the project names to restrict returned list applications (legacy name for backwards-compatibility). (optional)

try:
    # Get returns an application by name
    api_response = api_instance.application_service_get(name, refresh=refresh, projects=projects, resource_version=resource_version, selector=selector, repo=repo, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#x27;s name | 
 **refresh** | **str**| forces application reconciliation if set to &#x27;hard&#x27;. | [optional] 
 **projects** | [**list[str]**](str.md)| the project names to restrict returned list applications. | [optional] 
 **resource_version** | **str**| when specified with a watch call, shows changes that occur after that particular version of a resource. | [optional] 
 **selector** | **str**| the selector to restrict returned list to applications only with matched labels. | [optional] 
 **repo** | **str**| the repoURL to restrict returned list applications. | [optional] 
 **app_namespace** | **str**| the application&#x27;s namespace. | [optional] 
 **project** | [**list[str]**](str.md)| the project names to restrict returned list applications (legacy name for backwards-compatibility). | [optional] 

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_get_application_sync_windows**
> ApplicationApplicationSyncWindowsResponse application_service_get_application_sync_windows(name, app_namespace=app_namespace, project=project)

Get returns sync windows of the application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | 
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # Get returns sync windows of the application
    api_response = api_instance.application_service_get_application_sync_windows(name, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_get_application_sync_windows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**ApplicationApplicationSyncWindowsResponse**](ApplicationApplicationSyncWindowsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_get_manifests**
> RepositoryManifestResponse application_service_get_manifests(name, revision=revision, app_namespace=app_namespace, project=project)

GetManifests returns application manifests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | 
revision = 'revision_example' # str |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # GetManifests returns application manifests
    api_response = api_instance.application_service_get_manifests(name, revision=revision, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_get_manifests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **revision** | **str**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**RepositoryManifestResponse**](RepositoryManifestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_get_manifests_with_files**
> RepositoryManifestResponse application_service_get_manifests_with_files(body)

GetManifestsWithFiles returns application manifests using provided files to generate them

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
body = swagger_client.ApplicationApplicationManifestQueryWithFilesWrapper() # ApplicationApplicationManifestQueryWithFilesWrapper |  (streaming inputs)

try:
    # GetManifestsWithFiles returns application manifests using provided files to generate them
    api_response = api_instance.application_service_get_manifests_with_files(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_get_manifests_with_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationApplicationManifestQueryWithFilesWrapper**](ApplicationApplicationManifestQueryWithFilesWrapper.md)|  (streaming inputs) | 

### Return type

[**RepositoryManifestResponse**](RepositoryManifestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_get_resource**
> ApplicationApplicationResourceResponse application_service_get_resource(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)

GetResource returns single application resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # GetResource returns single application resource
    api_response = api_instance.application_service_get_resource(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_get_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**ApplicationApplicationResourceResponse**](ApplicationApplicationResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_list**
> V1alpha1ApplicationList application_service_list(name=name, refresh=refresh, projects=projects, resource_version=resource_version, selector=selector, repo=repo, app_namespace=app_namespace, project=project)

List returns list of applications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | the application's name. (optional)
refresh = 'refresh_example' # str | forces application reconciliation if set to 'hard'. (optional)
projects = ['projects_example'] # list[str] | the project names to restrict returned list applications. (optional)
resource_version = 'resource_version_example' # str | when specified with a watch call, shows changes that occur after that particular version of a resource. (optional)
selector = 'selector_example' # str | the selector to restrict returned list to applications only with matched labels. (optional)
repo = 'repo_example' # str | the repoURL to restrict returned list applications. (optional)
app_namespace = 'app_namespace_example' # str | the application's namespace. (optional)
project = ['project_example'] # list[str] | the project names to restrict returned list applications (legacy name for backwards-compatibility). (optional)

try:
    # List returns list of applications
    api_response = api_instance.application_service_list(name=name, refresh=refresh, projects=projects, resource_version=resource_version, selector=selector, repo=repo, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#x27;s name. | [optional] 
 **refresh** | **str**| forces application reconciliation if set to &#x27;hard&#x27;. | [optional] 
 **projects** | [**list[str]**](str.md)| the project names to restrict returned list applications. | [optional] 
 **resource_version** | **str**| when specified with a watch call, shows changes that occur after that particular version of a resource. | [optional] 
 **selector** | **str**| the selector to restrict returned list to applications only with matched labels. | [optional] 
 **repo** | **str**| the repoURL to restrict returned list applications. | [optional] 
 **app_namespace** | **str**| the application&#x27;s namespace. | [optional] 
 **project** | [**list[str]**](str.md)| the project names to restrict returned list applications (legacy name for backwards-compatibility). | [optional] 

### Return type

[**V1alpha1ApplicationList**](V1alpha1ApplicationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_list_links**
> ApplicationLinksResponse application_service_list_links(name, namespace=namespace, project=project)

ListLinks returns the list of all application deep links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # ListLinks returns the list of all application deep links
    api_response = api_instance.application_service_list_links(name, namespace=namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_list_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**ApplicationLinksResponse**](ApplicationLinksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_list_resource_actions**
> ApplicationResourceActionsListResponse application_service_list_resource_actions(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)

ListResourceActions returns list of resource actions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # ListResourceActions returns list of resource actions
    api_response = api_instance.application_service_list_resource_actions(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_list_resource_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**ApplicationResourceActionsListResponse**](ApplicationResourceActionsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_list_resource_events**
> V1EventList application_service_list_resource_events(name, resource_namespace=resource_namespace, resource_name=resource_name, resource_uid=resource_uid, app_namespace=app_namespace, project=project)

ListResourceEvents returns a list of event resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | 
resource_namespace = 'resource_namespace_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
resource_uid = 'resource_uid_example' # str |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # ListResourceEvents returns a list of event resources
    api_response = api_instance.application_service_list_resource_events(name, resource_namespace=resource_namespace, resource_name=resource_name, resource_uid=resource_uid, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_list_resource_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **resource_namespace** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **resource_uid** | **str**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**V1EventList**](V1EventList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_list_resource_links**
> ApplicationLinksResponse application_service_list_resource_links(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)

ListResourceLinks returns the list of all resource deep links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # ListResourceLinks returns the list of all resource deep links
    api_response = api_instance.application_service_list_resource_links(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_list_resource_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**ApplicationLinksResponse**](ApplicationLinksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_managed_resources**
> ApplicationManagedResourcesResponse application_service_managed_resources(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)

ManagedResources returns list of managed resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
application_name = 'application_name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
name = 'name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # ManagedResources returns list of managed resources
    api_response = api_instance.application_service_managed_resources(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_managed_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**ApplicationManagedResourcesResponse**](ApplicationManagedResourcesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_patch**
> V1alpha1Application application_service_patch(body, name)

Patch patch an application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
body = swagger_client.ApplicationApplicationPatchRequest() # ApplicationApplicationPatchRequest | 
name = 'name_example' # str | 

try:
    # Patch patch an application
    api_response = api_instance.application_service_patch(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationApplicationPatchRequest**](ApplicationApplicationPatchRequest.md)|  | 
 **name** | **str**|  | 

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_patch_resource**
> ApplicationApplicationResourceResponse application_service_patch_resource(body, name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, patch_type=patch_type, app_namespace=app_namespace, project=project)

PatchResource patch single application resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
body = 'body_example' # str | 
name = 'name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
patch_type = 'patch_type_example' # str |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # PatchResource patch single application resource
    api_response = api_instance.application_service_patch_resource(body, name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, patch_type=patch_type, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_patch_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **patch_type** | **str**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**ApplicationApplicationResourceResponse**](ApplicationApplicationResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_pod_logs**
> StreamResultOfApplicationLogEntry application_service_pod_logs(name, pod_name, namespace=namespace, container=container, since_seconds=since_seconds, since_time_seconds=since_time_seconds, since_time_nanos=since_time_nanos, tail_lines=tail_lines, follow=follow, until_time=until_time, filter=filter, kind=kind, group=group, resource_name=resource_name, previous=previous, app_namespace=app_namespace, project=project)

PodLogs returns stream of log entries for the specified pod. Pod

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | 
pod_name = 'pod_name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
container = 'container_example' # str |  (optional)
since_seconds = 'since_seconds_example' # str |  (optional)
since_time_seconds = 'since_time_seconds_example' # str | Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. (optional)
since_time_nanos = 56 # int | Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. (optional)
tail_lines = 'tail_lines_example' # str |  (optional)
follow = true # bool |  (optional)
until_time = 'until_time_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
group = 'group_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
previous = true # bool |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # PodLogs returns stream of log entries for the specified pod. Pod
    api_response = api_instance.application_service_pod_logs(name, pod_name, namespace=namespace, container=container, since_seconds=since_seconds, since_time_seconds=since_time_seconds, since_time_nanos=since_time_nanos, tail_lines=tail_lines, follow=follow, until_time=until_time, filter=filter, kind=kind, group=group, resource_name=resource_name, previous=previous, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_pod_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **pod_name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **container** | **str**|  | [optional] 
 **since_seconds** | **str**|  | [optional] 
 **since_time_seconds** | **str**| Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. | [optional] 
 **since_time_nanos** | **int**| Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. | [optional] 
 **tail_lines** | **str**|  | [optional] 
 **follow** | **bool**|  | [optional] 
 **until_time** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **previous** | **bool**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**StreamResultOfApplicationLogEntry**](StreamResultOfApplicationLogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_pod_logs2**
> StreamResultOfApplicationLogEntry application_service_pod_logs2(name, namespace=namespace, pod_name=pod_name, container=container, since_seconds=since_seconds, since_time_seconds=since_time_seconds, since_time_nanos=since_time_nanos, tail_lines=tail_lines, follow=follow, until_time=until_time, filter=filter, kind=kind, group=group, resource_name=resource_name, previous=previous, app_namespace=app_namespace, project=project)

PodLogs returns stream of log entries for the specified pod. Pod

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
pod_name = 'pod_name_example' # str |  (optional)
container = 'container_example' # str |  (optional)
since_seconds = 'since_seconds_example' # str |  (optional)
since_time_seconds = 'since_time_seconds_example' # str | Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. (optional)
since_time_nanos = 56 # int | Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. (optional)
tail_lines = 'tail_lines_example' # str |  (optional)
follow = true # bool |  (optional)
until_time = 'until_time_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
group = 'group_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
previous = true # bool |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # PodLogs returns stream of log entries for the specified pod. Pod
    api_response = api_instance.application_service_pod_logs2(name, namespace=namespace, pod_name=pod_name, container=container, since_seconds=since_seconds, since_time_seconds=since_time_seconds, since_time_nanos=since_time_nanos, tail_lines=tail_lines, follow=follow, until_time=until_time, filter=filter, kind=kind, group=group, resource_name=resource_name, previous=previous, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_pod_logs2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **pod_name** | **str**|  | [optional] 
 **container** | **str**|  | [optional] 
 **since_seconds** | **str**|  | [optional] 
 **since_time_seconds** | **str**| Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. | [optional] 
 **since_time_nanos** | **int**| Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. | [optional] 
 **tail_lines** | **str**|  | [optional] 
 **follow** | **bool**|  | [optional] 
 **until_time** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **previous** | **bool**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**StreamResultOfApplicationLogEntry**](StreamResultOfApplicationLogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_resource_tree**
> V1alpha1ApplicationTree application_service_resource_tree(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)

ResourceTree returns resource tree

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
application_name = 'application_name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
name = 'name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # ResourceTree returns resource tree
    api_response = api_instance.application_service_resource_tree(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_resource_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**V1alpha1ApplicationTree**](V1alpha1ApplicationTree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_revision_chart_details**
> V1alpha1ChartDetails application_service_revision_chart_details(name, revision, app_namespace=app_namespace, project=project)

Get the chart metadata (description, maintainers, home) for a specific revision of the application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | the application's name
revision = 'revision_example' # str | the revision of the app
app_namespace = 'app_namespace_example' # str | the application's namespace. (optional)
project = 'project_example' # str |  (optional)

try:
    # Get the chart metadata (description, maintainers, home) for a specific revision of the application
    api_response = api_instance.application_service_revision_chart_details(name, revision, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_revision_chart_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#x27;s name | 
 **revision** | **str**| the revision of the app | 
 **app_namespace** | **str**| the application&#x27;s namespace. | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**V1alpha1ChartDetails**](V1alpha1ChartDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_revision_metadata**
> V1alpha1RevisionMetadata application_service_revision_metadata(name, revision, app_namespace=app_namespace, project=project)

Get the meta-data (author, date, tags, message) for a specific revision of the application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | the application's name
revision = 'revision_example' # str | the revision of the app
app_namespace = 'app_namespace_example' # str | the application's namespace. (optional)
project = 'project_example' # str |  (optional)

try:
    # Get the meta-data (author, date, tags, message) for a specific revision of the application
    api_response = api_instance.application_service_revision_metadata(name, revision, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_revision_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#x27;s name | 
 **revision** | **str**| the revision of the app | 
 **app_namespace** | **str**| the application&#x27;s namespace. | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**V1alpha1RevisionMetadata**](V1alpha1RevisionMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_rollback**
> V1alpha1Application application_service_rollback(body, name)

Rollback syncs an application to its target state

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
body = swagger_client.ApplicationApplicationRollbackRequest() # ApplicationApplicationRollbackRequest | 
name = 'name_example' # str | 

try:
    # Rollback syncs an application to its target state
    api_response = api_instance.application_service_rollback(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_rollback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationApplicationRollbackRequest**](ApplicationApplicationRollbackRequest.md)|  | 
 **name** | **str**|  | 

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_run_resource_action**
> ApplicationApplicationResponse application_service_run_resource_action(body, name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)

RunResourceAction run resource action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
body = 'body_example' # str | 
name = 'name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # RunResourceAction run resource action
    api_response = api_instance.application_service_run_resource_action(body, name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_run_resource_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**ApplicationApplicationResponse**](ApplicationApplicationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_sync**
> V1alpha1Application application_service_sync(body, name)

Sync syncs an application to its target state

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
body = swagger_client.ApplicationApplicationSyncRequest() # ApplicationApplicationSyncRequest | 
name = 'name_example' # str | 

try:
    # Sync syncs an application to its target state
    api_response = api_instance.application_service_sync(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationApplicationSyncRequest**](ApplicationApplicationSyncRequest.md)|  | 
 **name** | **str**|  | 

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_terminate_operation**
> ApplicationOperationTerminateResponse application_service_terminate_operation(name, app_namespace=app_namespace, project=project)

TerminateOperation terminates the currently running operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | 
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # TerminateOperation terminates the currently running operation
    api_response = api_instance.application_service_terminate_operation(name, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_terminate_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**ApplicationOperationTerminateResponse**](ApplicationOperationTerminateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_update**
> V1alpha1Application application_service_update(body, application_metadata_name, validate=validate, project=project)

Update updates an application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
body = swagger_client.V1alpha1Application() # V1alpha1Application | 
application_metadata_name = 'application_metadata_name_example' # str | Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional
validate = true # bool |  (optional)
project = 'project_example' # str |  (optional)

try:
    # Update updates an application
    api_response = api_instance.application_service_update(body, application_metadata_name, validate=validate, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1Application**](V1alpha1Application.md)|  | 
 **application_metadata_name** | **str**| Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional | 
 **validate** | **bool**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_update_spec**
> V1alpha1ApplicationSpec application_service_update_spec(body, name, validate=validate, app_namespace=app_namespace, project=project)

UpdateSpec updates an application spec

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
body = swagger_client.V1alpha1ApplicationSpec() # V1alpha1ApplicationSpec | 
name = 'name_example' # str | 
validate = true # bool |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # UpdateSpec updates an application spec
    api_response = api_instance.application_service_update_spec(body, name, validate=validate, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_update_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1ApplicationSpec**](V1alpha1ApplicationSpec.md)|  | 
 **name** | **str**|  | 
 **validate** | **bool**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**V1alpha1ApplicationSpec**](V1alpha1ApplicationSpec.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_watch**
> StreamResultOfV1alpha1ApplicationWatchEvent application_service_watch(name=name, refresh=refresh, projects=projects, resource_version=resource_version, selector=selector, repo=repo, app_namespace=app_namespace, project=project)

Watch returns stream of application change events

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
name = 'name_example' # str | the application's name. (optional)
refresh = 'refresh_example' # str | forces application reconciliation if set to 'hard'. (optional)
projects = ['projects_example'] # list[str] | the project names to restrict returned list applications. (optional)
resource_version = 'resource_version_example' # str | when specified with a watch call, shows changes that occur after that particular version of a resource. (optional)
selector = 'selector_example' # str | the selector to restrict returned list to applications only with matched labels. (optional)
repo = 'repo_example' # str | the repoURL to restrict returned list applications. (optional)
app_namespace = 'app_namespace_example' # str | the application's namespace. (optional)
project = ['project_example'] # list[str] | the project names to restrict returned list applications (legacy name for backwards-compatibility). (optional)

try:
    # Watch returns stream of application change events
    api_response = api_instance.application_service_watch(name=name, refresh=refresh, projects=projects, resource_version=resource_version, selector=selector, repo=repo, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#x27;s name. | [optional] 
 **refresh** | **str**| forces application reconciliation if set to &#x27;hard&#x27;. | [optional] 
 **projects** | [**list[str]**](str.md)| the project names to restrict returned list applications. | [optional] 
 **resource_version** | **str**| when specified with a watch call, shows changes that occur after that particular version of a resource. | [optional] 
 **selector** | **str**| the selector to restrict returned list to applications only with matched labels. | [optional] 
 **repo** | **str**| the repoURL to restrict returned list applications. | [optional] 
 **app_namespace** | **str**| the application&#x27;s namespace. | [optional] 
 **project** | [**list[str]**](str.md)| the project names to restrict returned list applications (legacy name for backwards-compatibility). | [optional] 

### Return type

[**StreamResultOfV1alpha1ApplicationWatchEvent**](StreamResultOfV1alpha1ApplicationWatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_service_watch_resource_tree**
> StreamResultOfV1alpha1ApplicationTree application_service_watch_resource_tree(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)

Watch returns stream of application resource tree

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationServiceApi()
application_name = 'application_name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
name = 'name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
app_namespace = 'app_namespace_example' # str |  (optional)
project = 'project_example' # str |  (optional)

try:
    # Watch returns stream of application resource tree
    api_response = api_instance.application_service_watch_resource_tree(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind, app_namespace=app_namespace, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->application_service_watch_resource_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **app_namespace** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 

### Return type

[**StreamResultOfV1alpha1ApplicationTree**](StreamResultOfV1alpha1ApplicationTree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

