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

class V1alpha1SyncPolicy(object):
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
        'automated': 'V1alpha1SyncPolicyAutomated',
        'managed_namespace_metadata': 'V1alpha1ManagedNamespaceMetadata',
        'retry': 'V1alpha1RetryStrategy',
        'sync_options': 'list[str]'
    }

    attribute_map = {
        'automated': 'automated',
        'managed_namespace_metadata': 'managedNamespaceMetadata',
        'retry': 'retry',
        'sync_options': 'syncOptions'
    }

    def __init__(self, automated=None, managed_namespace_metadata=None, retry=None, sync_options=None):  # noqa: E501
        """V1alpha1SyncPolicy - a model defined in Swagger"""  # noqa: E501
        self._automated = None
        self._managed_namespace_metadata = None
        self._retry = None
        self._sync_options = None
        self.discriminator = None
        if automated is not None:
            self.automated = automated
        if managed_namespace_metadata is not None:
            self.managed_namespace_metadata = managed_namespace_metadata
        if retry is not None:
            self.retry = retry
        if sync_options is not None:
            self.sync_options = sync_options

    @property
    def automated(self):
        """Gets the automated of this V1alpha1SyncPolicy.  # noqa: E501


        :return: The automated of this V1alpha1SyncPolicy.  # noqa: E501
        :rtype: V1alpha1SyncPolicyAutomated
        """
        return self._automated

    @automated.setter
    def automated(self, automated):
        """Sets the automated of this V1alpha1SyncPolicy.


        :param automated: The automated of this V1alpha1SyncPolicy.  # noqa: E501
        :type: V1alpha1SyncPolicyAutomated
        """

        self._automated = automated

    @property
    def managed_namespace_metadata(self):
        """Gets the managed_namespace_metadata of this V1alpha1SyncPolicy.  # noqa: E501


        :return: The managed_namespace_metadata of this V1alpha1SyncPolicy.  # noqa: E501
        :rtype: V1alpha1ManagedNamespaceMetadata
        """
        return self._managed_namespace_metadata

    @managed_namespace_metadata.setter
    def managed_namespace_metadata(self, managed_namespace_metadata):
        """Sets the managed_namespace_metadata of this V1alpha1SyncPolicy.


        :param managed_namespace_metadata: The managed_namespace_metadata of this V1alpha1SyncPolicy.  # noqa: E501
        :type: V1alpha1ManagedNamespaceMetadata
        """

        self._managed_namespace_metadata = managed_namespace_metadata

    @property
    def retry(self):
        """Gets the retry of this V1alpha1SyncPolicy.  # noqa: E501


        :return: The retry of this V1alpha1SyncPolicy.  # noqa: E501
        :rtype: V1alpha1RetryStrategy
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        """Sets the retry of this V1alpha1SyncPolicy.


        :param retry: The retry of this V1alpha1SyncPolicy.  # noqa: E501
        :type: V1alpha1RetryStrategy
        """

        self._retry = retry

    @property
    def sync_options(self):
        """Gets the sync_options of this V1alpha1SyncPolicy.  # noqa: E501


        :return: The sync_options of this V1alpha1SyncPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._sync_options

    @sync_options.setter
    def sync_options(self, sync_options):
        """Sets the sync_options of this V1alpha1SyncPolicy.


        :param sync_options: The sync_options of this V1alpha1SyncPolicy.  # noqa: E501
        :type: list[str]
        """

        self._sync_options = sync_options

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
        if issubclass(V1alpha1SyncPolicy, dict):
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
        if not isinstance(other, V1alpha1SyncPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other