# swagger_client.CertificateServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificate_service_create_certificate**](CertificateServiceApi.md#certificate_service_create_certificate) | **POST** /api/v1/certificates | Creates repository certificates on the server
[**certificate_service_delete_certificate**](CertificateServiceApi.md#certificate_service_delete_certificate) | **DELETE** /api/v1/certificates | Delete the certificates that match the RepositoryCertificateQuery
[**certificate_service_list_certificates**](CertificateServiceApi.md#certificate_service_list_certificates) | **GET** /api/v1/certificates | List all available repository certificates

# **certificate_service_create_certificate**
> V1alpha1RepositoryCertificateList certificate_service_create_certificate(body, upsert=upsert)

Creates repository certificates on the server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificateServiceApi()
body = swagger_client.V1alpha1RepositoryCertificateList() # V1alpha1RepositoryCertificateList | List of certificates to be created
upsert = true # bool | Whether to upsert already existing certificates. (optional)

try:
    # Creates repository certificates on the server
    api_response = api_instance.certificate_service_create_certificate(body, upsert=upsert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateServiceApi->certificate_service_create_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1RepositoryCertificateList**](V1alpha1RepositoryCertificateList.md)| List of certificates to be created | 
 **upsert** | **bool**| Whether to upsert already existing certificates. | [optional] 

### Return type

[**V1alpha1RepositoryCertificateList**](V1alpha1RepositoryCertificateList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certificate_service_delete_certificate**
> V1alpha1RepositoryCertificateList certificate_service_delete_certificate(host_name_pattern=host_name_pattern, cert_type=cert_type, cert_sub_type=cert_sub_type)

Delete the certificates that match the RepositoryCertificateQuery

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificateServiceApi()
host_name_pattern = 'host_name_pattern_example' # str | A file-glob pattern (not regular expression) the host name has to match. (optional)
cert_type = 'cert_type_example' # str | The type of the certificate to match (ssh or https). (optional)
cert_sub_type = 'cert_sub_type_example' # str | The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). (optional)

try:
    # Delete the certificates that match the RepositoryCertificateQuery
    api_response = api_instance.certificate_service_delete_certificate(host_name_pattern=host_name_pattern, cert_type=cert_type, cert_sub_type=cert_sub_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateServiceApi->certificate_service_delete_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name_pattern** | **str**| A file-glob pattern (not regular expression) the host name has to match. | [optional] 
 **cert_type** | **str**| The type of the certificate to match (ssh or https). | [optional] 
 **cert_sub_type** | **str**| The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). | [optional] 

### Return type

[**V1alpha1RepositoryCertificateList**](V1alpha1RepositoryCertificateList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certificate_service_list_certificates**
> V1alpha1RepositoryCertificateList certificate_service_list_certificates(host_name_pattern=host_name_pattern, cert_type=cert_type, cert_sub_type=cert_sub_type)

List all available repository certificates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificateServiceApi()
host_name_pattern = 'host_name_pattern_example' # str | A file-glob pattern (not regular expression) the host name has to match. (optional)
cert_type = 'cert_type_example' # str | The type of the certificate to match (ssh or https). (optional)
cert_sub_type = 'cert_sub_type_example' # str | The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). (optional)

try:
    # List all available repository certificates
    api_response = api_instance.certificate_service_list_certificates(host_name_pattern=host_name_pattern, cert_type=cert_type, cert_sub_type=cert_sub_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateServiceApi->certificate_service_list_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name_pattern** | **str**| A file-glob pattern (not regular expression) the host name has to match. | [optional] 
 **cert_type** | **str**| The type of the certificate to match (ssh or https). | [optional] 
 **cert_sub_type** | **str**| The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). | [optional] 

### Return type

[**V1alpha1RepositoryCertificateList**](V1alpha1RepositoryCertificateList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

