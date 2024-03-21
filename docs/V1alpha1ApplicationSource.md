# V1alpha1ApplicationSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart** | **str** | Chart is a Helm chart name, and must be specified for applications sourced from a Helm repo. | [optional] 
**directory** | [**V1alpha1ApplicationSourceDirectory**](V1alpha1ApplicationSourceDirectory.md) |  | [optional] 
**helm** | [**V1alpha1ApplicationSourceHelm**](V1alpha1ApplicationSourceHelm.md) |  | [optional] 
**kustomize** | [**V1alpha1ApplicationSourceKustomize**](V1alpha1ApplicationSourceKustomize.md) |  | [optional] 
**path** | **str** | Path is a directory path within the Git repository, and is only valid for applications sourced from Git. | [optional] 
**plugin** | [**V1alpha1ApplicationSourcePlugin**](V1alpha1ApplicationSourcePlugin.md) |  | [optional] 
**ref** | **str** | Ref is reference to another source within sources field. This field will not be used if used with a &#x60;source&#x60; tag. | [optional] 
**repo_url** | **str** |  | [optional] 
**target_revision** | **str** | TargetRevision defines the revision of the source to sync the application to. In case of Git, this can be commit, tag, or branch. If omitted, will equal to HEAD. In case of Helm, this is a semver tag for the Chart&#x27;s version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

