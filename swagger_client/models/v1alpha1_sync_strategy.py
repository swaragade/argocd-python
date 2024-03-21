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

class V1alpha1SyncStrategy(object):
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
        'apply': 'V1alpha1SyncStrategyApply',
        'hook': 'V1alpha1SyncStrategyHook'
    }

    attribute_map = {
        'apply': 'apply',
        'hook': 'hook'
    }

    def __init__(self, apply=None, hook=None):  # noqa: E501
        """V1alpha1SyncStrategy - a model defined in Swagger"""  # noqa: E501
        self._apply = None
        self._hook = None
        self.discriminator = None
        if apply is not None:
            self.apply = apply
        if hook is not None:
            self.hook = hook

    @property
    def apply(self):
        """Gets the apply of this V1alpha1SyncStrategy.  # noqa: E501


        :return: The apply of this V1alpha1SyncStrategy.  # noqa: E501
        :rtype: V1alpha1SyncStrategyApply
        """
        return self._apply

    @apply.setter
    def apply(self, apply):
        """Sets the apply of this V1alpha1SyncStrategy.


        :param apply: The apply of this V1alpha1SyncStrategy.  # noqa: E501
        :type: V1alpha1SyncStrategyApply
        """

        self._apply = apply

    @property
    def hook(self):
        """Gets the hook of this V1alpha1SyncStrategy.  # noqa: E501


        :return: The hook of this V1alpha1SyncStrategy.  # noqa: E501
        :rtype: V1alpha1SyncStrategyHook
        """
        return self._hook

    @hook.setter
    def hook(self, hook):
        """Sets the hook of this V1alpha1SyncStrategy.


        :param hook: The hook of this V1alpha1SyncStrategy.  # noqa: E501
        :type: V1alpha1SyncStrategyHook
        """

        self._hook = hook

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
        if issubclass(V1alpha1SyncStrategy, dict):
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
        if not isinstance(other, V1alpha1SyncStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
