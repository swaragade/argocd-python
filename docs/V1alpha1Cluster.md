# V1alpha1Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** |  | [optional] 
**cluster_resources** | **bool** | Indicates if cluster level resources should be managed. This setting is used only if cluster is connected in a namespaced mode. | [optional] 
**config** | [**V1alpha1ClusterConfig**](V1alpha1ClusterConfig.md) |  | [optional] 
**connection_state** | [**V1alpha1ConnectionState**](V1alpha1ConnectionState.md) |  | [optional] 
**info** | [**V1alpha1ClusterInfo**](V1alpha1ClusterInfo.md) |  | [optional] 
**labels** | **dict(str, str)** |  | [optional] 
**name** | **str** |  | [optional] 
**namespaces** | **list[str]** | Holds list of namespaces which are accessible in that cluster. Cluster level resources will be ignored if namespace list is not empty. | [optional] 
**project** | **str** |  | [optional] 
**refresh_requested_at** | [**V1Time**](V1Time.md) |  | [optional] 
**server** | **str** |  | [optional] 
**server_version** | **str** |  | [optional] 
**shard** | **int** | Shard contains optional shard number. Calculated on the fly by the application controller if not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

