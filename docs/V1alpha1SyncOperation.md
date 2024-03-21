# V1alpha1SyncOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] 
**manifests** | **list[str]** |  | [optional] 
**prune** | **bool** |  | [optional] 
**resources** | [**list[V1alpha1SyncOperationResource]**](V1alpha1SyncOperationResource.md) |  | [optional] 
**revision** | **str** | Revision is the revision (Git) or chart version (Helm) which to sync the application to If omitted, will use the revision specified in app spec. | [optional] 
**revisions** | **list[str]** | Revisions is the list of revision (Git) or chart version (Helm) which to sync each source in sources field for the application to If omitted, will use the revision specified in app spec. | [optional] 
**source** | [**V1alpha1ApplicationSource**](V1alpha1ApplicationSource.md) |  | [optional] 
**sources** | [**list[V1alpha1ApplicationSource]**](V1alpha1ApplicationSource.md) |  | [optional] 
**sync_options** | **list[str]** |  | [optional] 
**sync_strategy** | [**V1alpha1SyncStrategy**](V1alpha1SyncStrategy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

