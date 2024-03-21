# V1alpha1PullRequestGeneratorGitLab

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** | The GitLab API URL to talk to. If blank, uses https://gitlab.com/. | [optional] 
**insecure** | **bool** |  | [optional] 
**labels** | **list[str]** |  | [optional] 
**project** | **str** | GitLab project to scan. Required. | [optional] 
**pull_request_state** | **str** |  | [optional] 
**token_ref** | [**V1alpha1SecretRef**](V1alpha1SecretRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

