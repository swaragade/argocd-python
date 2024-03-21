# V1alpha1SCMProviderGeneratorGithub

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_branches** | **bool** | Scan all branches instead of just the default branch. | [optional] 
**api** | **str** | The GitHub API URL to talk to. If blank, use https://api.github.com/. | [optional] 
**app_secret_name** | **str** | AppSecretName is a reference to a GitHub App repo-creds secret. | [optional] 
**organization** | **str** | GitHub org to scan. Required. | [optional] 
**token_ref** | [**V1alpha1SecretRef**](V1alpha1SecretRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

