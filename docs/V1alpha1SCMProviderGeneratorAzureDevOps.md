# V1alpha1SCMProviderGeneratorAzureDevOps

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_ref** | [**V1alpha1SecretRef**](V1alpha1SecretRef.md) |  | [optional] 
**all_branches** | **bool** | Scan all branches instead of just the default branch. | [optional] 
**api** | **str** | The URL to Azure DevOps. If blank, use https://dev.azure.com. | [optional] 
**organization** | **str** | Azure Devops organization. Required. E.g. \&quot;my-organization\&quot;. | [optional] 
**team_project** | **str** | Azure Devops team project. Required. E.g. \&quot;my-team\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

