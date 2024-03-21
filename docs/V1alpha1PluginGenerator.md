# V1alpha1PluginGenerator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map_ref** | [**V1alpha1PluginConfigMapRef**](V1alpha1PluginConfigMapRef.md) |  | [optional] 
**input** | [**V1alpha1PluginInput**](V1alpha1PluginInput.md) |  | [optional] 
**requeue_after_seconds** | **int** | RequeueAfterSeconds determines how long the ApplicationSet controller will wait before reconciling the ApplicationSet again. | [optional] 
**template** | [**V1alpha1ApplicationSetTemplate**](V1alpha1ApplicationSetTemplate.md) |  | [optional] 
**values** | **dict(str, str)** | Values contains key/value pairs which are passed directly as parameters to the template. These values will not be sent as parameters to the plugin. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

