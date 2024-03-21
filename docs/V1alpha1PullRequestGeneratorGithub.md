# V1alpha1PullRequestGeneratorGithub

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** | The GitHub API URL to talk to. If blank, use https://api.github.com/. | [optional] 
**app_secret_name** | **str** | AppSecretName is a reference to a GitHub App repo-creds secret with permission to access pull requests. | [optional] 
**labels** | **list[str]** |  | [optional] 
**owner** | **str** | GitHub org or user to scan. Required. | [optional] 
**repo** | **str** | GitHub repo name to scan. Required. | [optional] 
**token_ref** | [**V1alpha1SecretRef**](V1alpha1SecretRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

