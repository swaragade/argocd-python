# argocd.RepositoryServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repository_service_create_repository**](RepositoryServiceApi.md#repository_service_create_repository) | **POST** /api/v1/repositories | CreateRepository creates a new repository configuration
[**repository_service_delete_repository**](RepositoryServiceApi.md#repository_service_delete_repository) | **DELETE** /api/v1/repositories/{repo} | DeleteRepository deletes a repository from the configuration
[**repository_service_get**](RepositoryServiceApi.md#repository_service_get) | **GET** /api/v1/repositories/{repo} | Get returns a repository or its credentials
[**repository_service_get_app_details**](RepositoryServiceApi.md#repository_service_get_app_details) | **POST** /api/v1/repositories/{source.repoURL}/appdetails | GetAppDetails returns application details by given path
[**repository_service_get_helm_charts**](RepositoryServiceApi.md#repository_service_get_helm_charts) | **GET** /api/v1/repositories/{repo}/helmcharts | GetHelmCharts returns list of helm charts in the specified repository
[**repository_service_list_apps**](RepositoryServiceApi.md#repository_service_list_apps) | **GET** /api/v1/repositories/{repo}/apps | ListApps returns list of apps in the repo
[**repository_service_list_refs**](RepositoryServiceApi.md#repository_service_list_refs) | **GET** /api/v1/repositories/{repo}/refs | 
[**repository_service_list_repositories**](RepositoryServiceApi.md#repository_service_list_repositories) | **GET** /api/v1/repositories | ListRepositories gets a list of all configured repositories
[**repository_service_update_repository**](RepositoryServiceApi.md#repository_service_update_repository) | **PUT** /api/v1/repositories/{repo.repo} | UpdateRepository updates a repository configuration
[**repository_service_validate_access**](RepositoryServiceApi.md#repository_service_validate_access) | **POST** /api/v1/repositories/{repo}/validate | ValidateAccess validates access to a repository with given parameters

# **repository_service_create_repository**
> V1alpha1Repository repository_service_create_repository(body, upsert=upsert, creds_only=creds_only)

CreateRepository creates a new repository configuration

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepositoryServiceApi()
body = argocd.V1alpha1Repository() # V1alpha1Repository | Repository definition
upsert = true # bool | Whether to create in upsert mode. (optional)
creds_only = true # bool | Whether to operate on credential set instead of repository. (optional)

try:
    # CreateRepository creates a new repository configuration
    api_response = api_instance.repository_service_create_repository(body, upsert=upsert, creds_only=creds_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryServiceApi->repository_service_create_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1Repository**](V1alpha1Repository.md)| Repository definition | 
 **upsert** | **bool**| Whether to create in upsert mode. | [optional] 
 **creds_only** | **bool**| Whether to operate on credential set instead of repository. | [optional] 

### Return type

[**V1alpha1Repository**](V1alpha1Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_service_delete_repository**
> RepositoryRepoResponse repository_service_delete_repository(repo, force_refresh=force_refresh)

DeleteRepository deletes a repository from the configuration

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepositoryServiceApi()
repo = 'repo_example' # str | Repo URL for query
force_refresh = true # bool | Whether to force a cache refresh on repo's connection state. (optional)

try:
    # DeleteRepository deletes a repository from the configuration
    api_response = api_instance.repository_service_delete_repository(repo, force_refresh=force_refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryServiceApi->repository_service_delete_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query | 
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#x27;s connection state. | [optional] 

### Return type

[**RepositoryRepoResponse**](RepositoryRepoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_service_get**
> V1alpha1Repository repository_service_get(repo, force_refresh=force_refresh)

Get returns a repository or its credentials

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepositoryServiceApi()
repo = 'repo_example' # str | Repo URL for query
force_refresh = true # bool | Whether to force a cache refresh on repo's connection state. (optional)

try:
    # Get returns a repository or its credentials
    api_response = api_instance.repository_service_get(repo, force_refresh=force_refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryServiceApi->repository_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query | 
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#x27;s connection state. | [optional] 

### Return type

[**V1alpha1Repository**](V1alpha1Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_service_get_app_details**
> RepositoryRepoAppDetailsResponse repository_service_get_app_details(body, source_repo_url)

GetAppDetails returns application details by given path

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepositoryServiceApi()
body = argocd.RepositoryRepoAppDetailsQuery() # RepositoryRepoAppDetailsQuery | 
source_repo_url = 'source_repo_url_example' # str | RepoURL is the URL to the repository (Git or Helm) that contains the application manifests

try:
    # GetAppDetails returns application details by given path
    api_response = api_instance.repository_service_get_app_details(body, source_repo_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryServiceApi->repository_service_get_app_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepositoryRepoAppDetailsQuery**](RepositoryRepoAppDetailsQuery.md)|  | 
 **source_repo_url** | **str**| RepoURL is the URL to the repository (Git or Helm) that contains the application manifests | 

### Return type

[**RepositoryRepoAppDetailsResponse**](RepositoryRepoAppDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_service_get_helm_charts**
> RepositoryHelmChartsResponse repository_service_get_helm_charts(repo, force_refresh=force_refresh)

GetHelmCharts returns list of helm charts in the specified repository

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepositoryServiceApi()
repo = 'repo_example' # str | Repo URL for query
force_refresh = true # bool | Whether to force a cache refresh on repo's connection state. (optional)

try:
    # GetHelmCharts returns list of helm charts in the specified repository
    api_response = api_instance.repository_service_get_helm_charts(repo, force_refresh=force_refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryServiceApi->repository_service_get_helm_charts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query | 
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#x27;s connection state. | [optional] 

### Return type

[**RepositoryHelmChartsResponse**](RepositoryHelmChartsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_service_list_apps**
> RepositoryRepoAppsResponse repository_service_list_apps(repo, revision=revision, app_name=app_name, app_project=app_project)

ListApps returns list of apps in the repo

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepositoryServiceApi()
repo = 'repo_example' # str | 
revision = 'revision_example' # str |  (optional)
app_name = 'app_name_example' # str |  (optional)
app_project = 'app_project_example' # str |  (optional)

try:
    # ListApps returns list of apps in the repo
    api_response = api_instance.repository_service_list_apps(repo, revision=revision, app_name=app_name, app_project=app_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryServiceApi->repository_service_list_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**|  | 
 **revision** | **str**|  | [optional] 
 **app_name** | **str**|  | [optional] 
 **app_project** | **str**|  | [optional] 

### Return type

[**RepositoryRepoAppsResponse**](RepositoryRepoAppsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_service_list_refs**
> RepositoryRefs repository_service_list_refs(repo, force_refresh=force_refresh)



### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepositoryServiceApi()
repo = 'repo_example' # str | Repo URL for query
force_refresh = true # bool | Whether to force a cache refresh on repo's connection state. (optional)

try:
    api_response = api_instance.repository_service_list_refs(repo, force_refresh=force_refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryServiceApi->repository_service_list_refs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query | 
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#x27;s connection state. | [optional] 

### Return type

[**RepositoryRefs**](RepositoryRefs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_service_list_repositories**
> V1alpha1RepositoryList repository_service_list_repositories(repo=repo, force_refresh=force_refresh)

ListRepositories gets a list of all configured repositories

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepositoryServiceApi()
repo = 'repo_example' # str | Repo URL for query. (optional)
force_refresh = true # bool | Whether to force a cache refresh on repo's connection state. (optional)

try:
    # ListRepositories gets a list of all configured repositories
    api_response = api_instance.repository_service_list_repositories(repo=repo, force_refresh=force_refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryServiceApi->repository_service_list_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query. | [optional] 
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#x27;s connection state. | [optional] 

### Return type

[**V1alpha1RepositoryList**](V1alpha1RepositoryList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_service_update_repository**
> V1alpha1Repository repository_service_update_repository(body, repo_repo)

UpdateRepository updates a repository configuration

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepositoryServiceApi()
body = argocd.V1alpha1Repository() # V1alpha1Repository | 
repo_repo = 'repo_repo_example' # str | Repo contains the URL to the remote repository

try:
    # UpdateRepository updates a repository configuration
    api_response = api_instance.repository_service_update_repository(body, repo_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryServiceApi->repository_service_update_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1Repository**](V1alpha1Repository.md)|  | 
 **repo_repo** | **str**| Repo contains the URL to the remote repository | 

### Return type

[**V1alpha1Repository**](V1alpha1Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_service_validate_access**
> RepositoryRepoResponse repository_service_validate_access(body, repo, username=username, password=password, ssh_private_key=ssh_private_key, insecure=insecure, tls_client_cert_data=tls_client_cert_data, tls_client_cert_key=tls_client_cert_key, type=type, name=name, enable_oci=enable_oci, github_app_private_key=github_app_private_key, github_app_id=github_app_id, github_app_installation_id=github_app_installation_id, github_app_enterprise_base_url=github_app_enterprise_base_url, proxy=proxy, project=project, gcp_service_account_key=gcp_service_account_key, force_http_basic_auth=force_http_basic_auth)

ValidateAccess validates access to a repository with given parameters

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepositoryServiceApi()
body = 'body_example' # str | The URL to the repo
repo = 'repo_example' # str | The URL to the repo
username = 'username_example' # str | Username for accessing repo. (optional)
password = 'password_example' # str | Password for accessing repo. (optional)
ssh_private_key = 'ssh_private_key_example' # str | Private key data for accessing SSH repository. (optional)
insecure = true # bool | Whether to skip certificate or host key validation. (optional)
tls_client_cert_data = 'tls_client_cert_data_example' # str | TLS client cert data for accessing HTTPS repository. (optional)
tls_client_cert_key = 'tls_client_cert_key_example' # str | TLS client cert key for accessing HTTPS repository. (optional)
type = 'type_example' # str | The type of the repo. (optional)
name = 'name_example' # str | The name of the repo. (optional)
enable_oci = true # bool | Whether helm-oci support should be enabled for this repo. (optional)
github_app_private_key = 'github_app_private_key_example' # str | Github App Private Key PEM data. (optional)
github_app_id = 'github_app_id_example' # str | Github App ID of the app used to access the repo. (optional)
github_app_installation_id = 'github_app_installation_id_example' # str | Github App Installation ID of the installed GitHub App. (optional)
github_app_enterprise_base_url = 'github_app_enterprise_base_url_example' # str | Github App Enterprise base url if empty will default to https://api.github.com. (optional)
proxy = 'proxy_example' # str | HTTP/HTTPS proxy to access the repository. (optional)
project = 'project_example' # str | Reference between project and repository that allow you automatically to be added as item inside SourceRepos project entity. (optional)
gcp_service_account_key = 'gcp_service_account_key_example' # str | Google Cloud Platform service account key. (optional)
force_http_basic_auth = true # bool | Whether to force HTTP basic auth. (optional)

try:
    # ValidateAccess validates access to a repository with given parameters
    api_response = api_instance.repository_service_validate_access(body, repo, username=username, password=password, ssh_private_key=ssh_private_key, insecure=insecure, tls_client_cert_data=tls_client_cert_data, tls_client_cert_key=tls_client_cert_key, type=type, name=name, enable_oci=enable_oci, github_app_private_key=github_app_private_key, github_app_id=github_app_id, github_app_installation_id=github_app_installation_id, github_app_enterprise_base_url=github_app_enterprise_base_url, proxy=proxy, project=project, gcp_service_account_key=gcp_service_account_key, force_http_basic_auth=force_http_basic_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryServiceApi->repository_service_validate_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The URL to the repo | 
 **repo** | **str**| The URL to the repo | 
 **username** | **str**| Username for accessing repo. | [optional] 
 **password** | **str**| Password for accessing repo. | [optional] 
 **ssh_private_key** | **str**| Private key data for accessing SSH repository. | [optional] 
 **insecure** | **bool**| Whether to skip certificate or host key validation. | [optional] 
 **tls_client_cert_data** | **str**| TLS client cert data for accessing HTTPS repository. | [optional] 
 **tls_client_cert_key** | **str**| TLS client cert key for accessing HTTPS repository. | [optional] 
 **type** | **str**| The type of the repo. | [optional] 
 **name** | **str**| The name of the repo. | [optional] 
 **enable_oci** | **bool**| Whether helm-oci support should be enabled for this repo. | [optional] 
 **github_app_private_key** | **str**| Github App Private Key PEM data. | [optional] 
 **github_app_id** | **str**| Github App ID of the app used to access the repo. | [optional] 
 **github_app_installation_id** | **str**| Github App Installation ID of the installed GitHub App. | [optional] 
 **github_app_enterprise_base_url** | **str**| Github App Enterprise base url if empty will default to https://api.github.com. | [optional] 
 **proxy** | **str**| HTTP/HTTPS proxy to access the repository. | [optional] 
 **project** | **str**| Reference between project and repository that allow you automatically to be added as item inside SourceRepos project entity. | [optional] 
 **gcp_service_account_key** | **str**| Google Cloud Platform service account key. | [optional] 
 **force_http_basic_auth** | **bool**| Whether to force HTTP basic auth. | [optional] 

### Return type

[**RepositoryRepoResponse**](RepositoryRepoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

