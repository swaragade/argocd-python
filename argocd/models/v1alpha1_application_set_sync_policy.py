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

class V1alpha1ApplicationSetSyncPolicy(object):
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
        'applications_sync': 'str',
        'preserve_resources_on_deletion': 'bool'
    }

    attribute_map = {
        'applications_sync': 'applicationsSync',
        'preserve_resources_on_deletion': 'preserveResourcesOnDeletion'
    }

    def __init__(self, applications_sync=None, preserve_resources_on_deletion=None):  # noqa: E501
        """V1alpha1ApplicationSetSyncPolicy - a model defined in Swagger"""  # noqa: E501
        self._applications_sync = None
        self._preserve_resources_on_deletion = None
        self.discriminator = None
        if applications_sync is not None:
            self.applications_sync = applications_sync
        if preserve_resources_on_deletion is not None:
            self.preserve_resources_on_deletion = preserve_resources_on_deletion

    @property
    def applications_sync(self):
        """Gets the applications_sync of this V1alpha1ApplicationSetSyncPolicy.  # noqa: E501


        :return: The applications_sync of this V1alpha1ApplicationSetSyncPolicy.  # noqa: E501
        :rtype: str
        """
        return self._applications_sync

    @applications_sync.setter
    def applications_sync(self, applications_sync):
        """Sets the applications_sync of this V1alpha1ApplicationSetSyncPolicy.


        :param applications_sync: The applications_sync of this V1alpha1ApplicationSetSyncPolicy.  # noqa: E501
        :type: str
        """

        self._applications_sync = applications_sync

    @property
    def preserve_resources_on_deletion(self):
        """Gets the preserve_resources_on_deletion of this V1alpha1ApplicationSetSyncPolicy.  # noqa: E501

        PreserveResourcesOnDeletion will preserve resources on deletion. If PreserveResourcesOnDeletion is set to true, these Applications will not be deleted.  # noqa: E501

        :return: The preserve_resources_on_deletion of this V1alpha1ApplicationSetSyncPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_resources_on_deletion

    @preserve_resources_on_deletion.setter
    def preserve_resources_on_deletion(self, preserve_resources_on_deletion):
        """Sets the preserve_resources_on_deletion of this V1alpha1ApplicationSetSyncPolicy.

        PreserveResourcesOnDeletion will preserve resources on deletion. If PreserveResourcesOnDeletion is set to true, these Applications will not be deleted.  # noqa: E501

        :param preserve_resources_on_deletion: The preserve_resources_on_deletion of this V1alpha1ApplicationSetSyncPolicy.  # noqa: E501
        :type: bool
        """

        self._preserve_resources_on_deletion = preserve_resources_on_deletion

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
        if issubclass(V1alpha1ApplicationSetSyncPolicy, dict):
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
        if not isinstance(other, V1alpha1ApplicationSetSyncPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other