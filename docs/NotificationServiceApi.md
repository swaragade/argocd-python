# argocd.NotificationServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_service_list_services**](NotificationServiceApi.md#notification_service_list_services) | **GET** /api/v1/notifications/services | List returns list of services
[**notification_service_list_templates**](NotificationServiceApi.md#notification_service_list_templates) | **GET** /api/v1/notifications/templates | List returns list of templates
[**notification_service_list_triggers**](NotificationServiceApi.md#notification_service_list_triggers) | **GET** /api/v1/notifications/triggers | List returns list of triggers

# **notification_service_list_services**
> NotificationServiceList notification_service_list_services()

List returns list of services

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.NotificationServiceApi()

try:
    # List returns list of services
    api_response = api_instance.notification_service_list_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationServiceApi->notification_service_list_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationServiceList**](NotificationServiceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_service_list_templates**
> NotificationTemplateList notification_service_list_templates()

List returns list of templates

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.NotificationServiceApi()

try:
    # List returns list of templates
    api_response = api_instance.notification_service_list_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationServiceApi->notification_service_list_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationTemplateList**](NotificationTemplateList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_service_list_triggers**
> NotificationTriggerList notification_service_list_triggers()

List returns list of triggers

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.NotificationServiceApi()

try:
    # List returns list of triggers
    api_response = api_instance.notification_service_list_triggers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationServiceApi->notification_service_list_triggers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationTriggerList**](NotificationTriggerList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

