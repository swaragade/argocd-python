# V1alpha1PullRequestGeneratorAzureDevOps

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** | The Azure DevOps API URL to talk to. If blank, use https://dev.azure.com/. | [optional] 
**labels** | **list[str]** |  | [optional] 
**organization** | **str** | Azure DevOps org to scan. Required. | [optional] 
**project** | **str** | Azure DevOps project name to scan. Required. | [optional] 
**repo** | **str** | Azure DevOps repo name to scan. Required. | [optional] 
**token_ref** | [**V1alpha1SecretRef**](V1alpha1SecretRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

