# RepositoryParameterAnnouncement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array** | **list[str]** | array is the default value of the parameter if the parameter is an array. | [optional] 
**collection_type** | **str** | collectionType is the type of value this parameter holds - either a single value (a string) or a collection (array or map). If collectionType is set, only the field with that type will be used. If collectionType is not set, &#x60;string&#x60; is the default. If collectionType is set to an invalid value, a validation error is thrown. | [optional] 
**item_type** | **str** | itemType determines the primitive data type represented by the parameter. Parameters are always encoded as strings, but this field lets them be interpreted as other primitive types. | [optional] 
**map** | **dict(str, str)** | map is the default value of the parameter if the parameter is a map. | [optional] 
**name** | **str** | name is the name identifying a parameter. | [optional] 
**required** | **bool** | required defines if this given parameter is mandatory. | [optional] 
**string** | **str** | string is the default value of the parameter if the parameter is a string. | [optional] 
**title** | **str** | title is a human-readable text of the parameter name. | [optional] 
**tooltip** | **str** | tooltip is a human-readable description of the parameter. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

