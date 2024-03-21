# coding: utf-8

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V1alpha1ClusterCacheInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'apis_count': 'int',
        'last_cache_sync_time': 'V1Time',
        'resources_count': 'int'
    }

    attribute_map = {
        'apis_count': 'apisCount',
        'last_cache_sync_time': 'lastCacheSyncTime',
        'resources_count': 'resourcesCount'
    }

    def __init__(self, apis_count=None, last_cache_sync_time=None, resources_count=None):  # noqa: E501
        """V1alpha1ClusterCacheInfo - a model defined in Swagger"""  # noqa: E501
        self._apis_count = None
        self._last_cache_sync_time = None
        self._resources_count = None
        self.discriminator = None
        if apis_count is not None:
            self.apis_count = apis_count
        if last_cache_sync_time is not None:
            self.last_cache_sync_time = last_cache_sync_time
        if resources_count is not None:
            self.resources_count = resources_count

    @property
    def apis_count(self):
        """Gets the apis_count of this V1alpha1ClusterCacheInfo.  # noqa: E501


        :return: The apis_count of this V1alpha1ClusterCacheInfo.  # noqa: E501
        :rtype: int
        """
        return self._apis_count

    @apis_count.setter
    def apis_count(self, apis_count):
        """Sets the apis_count of this V1alpha1ClusterCacheInfo.


        :param apis_count: The apis_count of this V1alpha1ClusterCacheInfo.  # noqa: E501
        :type: int
        """

        self._apis_count = apis_count

    @property
    def last_cache_sync_time(self):
        """Gets the last_cache_sync_time of this V1alpha1ClusterCacheInfo.  # noqa: E501


        :return: The last_cache_sync_time of this V1alpha1ClusterCacheInfo.  # noqa: E501
        :rtype: V1Time
        """
        return self._last_cache_sync_time

    @last_cache_sync_time.setter
    def last_cache_sync_time(self, last_cache_sync_time):
        """Sets the last_cache_sync_time of this V1alpha1ClusterCacheInfo.


        :param last_cache_sync_time: The last_cache_sync_time of this V1alpha1ClusterCacheInfo.  # noqa: E501
        :type: V1Time
        """

        self._last_cache_sync_time = last_cache_sync_time

    @property
    def resources_count(self):
        """Gets the resources_count of this V1alpha1ClusterCacheInfo.  # noqa: E501


        :return: The resources_count of this V1alpha1ClusterCacheInfo.  # noqa: E501
        :rtype: int
        """
        return self._resources_count

    @resources_count.setter
    def resources_count(self, resources_count):
        """Sets the resources_count of this V1alpha1ClusterCacheInfo.


        :param resources_count: The resources_count of this V1alpha1ClusterCacheInfo.  # noqa: E501
        :type: int
        """

        self._resources_count = resources_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1alpha1ClusterCacheInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1ClusterCacheInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other