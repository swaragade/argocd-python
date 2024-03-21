# ClusterSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_label_key** | **str** |  | [optional] 
**apps_in_any_namespace_enabled** | **bool** |  | [optional] 
**config_management_plugins** | [**list[V1alpha1ConfigManagementPlugin]**](V1alpha1ConfigManagementPlugin.md) | Deprecated: use sidecar plugins instead. | [optional] 
**controller_namespace** | **str** |  | [optional] 
**dex_config** | [**ClusterDexConfig**](ClusterDexConfig.md) |  | [optional] 
**exec_enabled** | **bool** |  | [optional] 
**google_analytics** | [**ClusterGoogleAnalyticsConfig**](ClusterGoogleAnalyticsConfig.md) |  | [optional] 
**help** | [**ClusterHelp**](ClusterHelp.md) |  | [optional] 
**kustomize_options** | [**V1alpha1KustomizeOptions**](V1alpha1KustomizeOptions.md) |  | [optional] 
**kustomize_versions** | **list[str]** |  | [optional] 
**oidc_config** | [**ClusterOIDCConfig**](ClusterOIDCConfig.md) |  | [optional] 
**password_pattern** | **str** |  | [optional] 
**plugins** | [**list[ClusterPlugin]**](ClusterPlugin.md) |  | [optional] 
**resource_overrides** | [**dict(str, V1alpha1ResourceOverride)**](V1alpha1ResourceOverride.md) |  | [optional] 
**status_badge_enabled** | **bool** |  | [optional] 
**status_badge_root_url** | **str** |  | [optional] 
**tracking_method** | **str** |  | [optional] 
**ui_banner_content** | **str** |  | [optional] 
**ui_banner_permanent** | **bool** |  | [optional] 
**ui_banner_position** | **str** |  | [optional] 
**ui_banner_url** | **str** |  | [optional] 
**ui_css_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user_logins_disabled** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

