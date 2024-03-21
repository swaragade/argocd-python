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

class V1alpha1OperationInitiator(object):
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
        'automated': 'bool',
        'username': 'str'
    }

    attribute_map = {
        'automated': 'automated',
        'username': 'username'
    }

    def __init__(self, automated=None, username=None):  # noqa: E501
        """V1alpha1OperationInitiator - a model defined in Swagger"""  # noqa: E501
        self._automated = None
        self._username = None
        self.discriminator = None
        if automated is not None:
            self.automated = automated
        if username is not None:
            self.username = username

    @property
    def automated(self):
        """Gets the automated of this V1alpha1OperationInitiator.  # noqa: E501

        Automated is set to true if operation was initiated automatically by the application controller.  # noqa: E501

        :return: The automated of this V1alpha1OperationInitiator.  # noqa: E501
        :rtype: bool
        """
        return self._automated

    @automated.setter
    def automated(self, automated):
        """Sets the automated of this V1alpha1OperationInitiator.

        Automated is set to true if operation was initiated automatically by the application controller.  # noqa: E501

        :param automated: The automated of this V1alpha1OperationInitiator.  # noqa: E501
        :type: bool
        """

        self._automated = automated

    @property
    def username(self):
        """Gets the username of this V1alpha1OperationInitiator.  # noqa: E501


        :return: The username of this V1alpha1OperationInitiator.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this V1alpha1OperationInitiator.


        :param username: The username of this V1alpha1OperationInitiator.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(V1alpha1OperationInitiator, dict):
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
        if not isinstance(other, V1alpha1OperationInitiator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
