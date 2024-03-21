# V1alpha1ApplicationSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**V1alpha1ApplicationDestination**](V1alpha1ApplicationDestination.md) |  | [optional] 
**ignore_differences** | [**list[V1alpha1ResourceIgnoreDifferences]**](V1alpha1ResourceIgnoreDifferences.md) |  | [optional] 
**info** | [**list[V1alpha1Info]**](V1alpha1Info.md) |  | [optional] 
**project** | **str** | Project is a reference to the project this application belongs to. The empty string means that application belongs to the &#x27;default&#x27; project. | [optional] 
**revision_history_limit** | **int** | RevisionHistoryLimit limits the number of items kept in the application&#x27;s revision history, which is used for informational purposes as well as for rollbacks to previous versions. This should only be changed in exceptional circumstances. Setting to zero will store no history. This will reduce storage used. Increasing will increase the space used to store the history, so we do not recommend increasing it. Default is 10. | [optional] 
**source** | [**V1alpha1ApplicationSource**](V1alpha1ApplicationSource.md) |  | [optional] 
**sources** | [**list[V1alpha1ApplicationSource]**](V1alpha1ApplicationSource.md) |  | [optional] 
**sync_policy** | [**V1alpha1SyncPolicy**](V1alpha1SyncPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

