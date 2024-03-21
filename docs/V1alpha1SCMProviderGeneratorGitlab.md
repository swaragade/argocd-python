# V1alpha1SCMProviderGeneratorGitlab

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_branches** | **bool** | Scan all branches instead of just the default branch. | [optional] 
**api** | **str** | The Gitlab API URL to talk to. | [optional] 
**group** | **str** | Gitlab group to scan. Required.  You can use either the project id (recommended) or the full namespaced path. | [optional] 
**include_shared_projects** | **bool** |  | [optional] 
**include_subgroups** | **bool** |  | [optional] 
**insecure** | **bool** |  | [optional] 
**token_ref** | [**V1alpha1SecretRef**](V1alpha1SecretRef.md) |  | [optional] 
**topic** | **str** | Filter repos list based on Gitlab Topic. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

