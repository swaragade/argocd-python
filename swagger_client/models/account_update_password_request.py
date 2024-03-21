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

class AccountUpdatePasswordRequest(object):
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
        'current_password': 'str',
        'name': 'str',
        'new_password': 'str'
    }

    attribute_map = {
        'current_password': 'currentPassword',
        'name': 'name',
        'new_password': 'newPassword'
    }

    def __init__(self, current_password=None, name=None, new_password=None):  # noqa: E501
        """AccountUpdatePasswordRequest - a model defined in Swagger"""  # noqa: E501
        self._current_password = None
        self._name = None
        self._new_password = None
        self.discriminator = None
        if current_password is not None:
            self.current_password = current_password
        if name is not None:
            self.name = name
        if new_password is not None:
            self.new_password = new_password

    @property
    def current_password(self):
        """Gets the current_password of this AccountUpdatePasswordRequest.  # noqa: E501


        :return: The current_password of this AccountUpdatePasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._current_password

    @current_password.setter
    def current_password(self, current_password):
        """Sets the current_password of this AccountUpdatePasswordRequest.


        :param current_password: The current_password of this AccountUpdatePasswordRequest.  # noqa: E501
        :type: str
        """

        self._current_password = current_password

    @property
    def name(self):
        """Gets the name of this AccountUpdatePasswordRequest.  # noqa: E501


        :return: The name of this AccountUpdatePasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountUpdatePasswordRequest.


        :param name: The name of this AccountUpdatePasswordRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def new_password(self):
        """Gets the new_password of this AccountUpdatePasswordRequest.  # noqa: E501


        :return: The new_password of this AccountUpdatePasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this AccountUpdatePasswordRequest.


        :param new_password: The new_password of this AccountUpdatePasswordRequest.  # noqa: E501
        :type: str
        """

        self._new_password = new_password

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
        if issubclass(AccountUpdatePasswordRequest, dict):
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
        if not isinstance(other, AccountUpdatePasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other