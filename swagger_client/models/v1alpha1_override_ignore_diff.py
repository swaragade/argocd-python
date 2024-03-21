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

class V1alpha1OverrideIgnoreDiff(object):
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
        'j_son_pointers': 'list[str]',
        'jq_path_expressions': 'list[str]',
        'managed_fields_managers': 'list[str]'
    }

    attribute_map = {
        'j_son_pointers': 'jSONPointers',
        'jq_path_expressions': 'jqPathExpressions',
        'managed_fields_managers': 'managedFieldsManagers'
    }

    def __init__(self, j_son_pointers=None, jq_path_expressions=None, managed_fields_managers=None):  # noqa: E501
        """V1alpha1OverrideIgnoreDiff - a model defined in Swagger"""  # noqa: E501
        self._j_son_pointers = None
        self._jq_path_expressions = None
        self._managed_fields_managers = None
        self.discriminator = None
        if j_son_pointers is not None:
            self.j_son_pointers = j_son_pointers
        if jq_path_expressions is not None:
            self.jq_path_expressions = jq_path_expressions
        if managed_fields_managers is not None:
            self.managed_fields_managers = managed_fields_managers

    @property
    def j_son_pointers(self):
        """Gets the j_son_pointers of this V1alpha1OverrideIgnoreDiff.  # noqa: E501


        :return: The j_son_pointers of this V1alpha1OverrideIgnoreDiff.  # noqa: E501
        :rtype: list[str]
        """
        return self._j_son_pointers

    @j_son_pointers.setter
    def j_son_pointers(self, j_son_pointers):
        """Sets the j_son_pointers of this V1alpha1OverrideIgnoreDiff.


        :param j_son_pointers: The j_son_pointers of this V1alpha1OverrideIgnoreDiff.  # noqa: E501
        :type: list[str]
        """

        self._j_son_pointers = j_son_pointers

    @property
    def jq_path_expressions(self):
        """Gets the jq_path_expressions of this V1alpha1OverrideIgnoreDiff.  # noqa: E501


        :return: The jq_path_expressions of this V1alpha1OverrideIgnoreDiff.  # noqa: E501
        :rtype: list[str]
        """
        return self._jq_path_expressions

    @jq_path_expressions.setter
    def jq_path_expressions(self, jq_path_expressions):
        """Sets the jq_path_expressions of this V1alpha1OverrideIgnoreDiff.


        :param jq_path_expressions: The jq_path_expressions of this V1alpha1OverrideIgnoreDiff.  # noqa: E501
        :type: list[str]
        """

        self._jq_path_expressions = jq_path_expressions

    @property
    def managed_fields_managers(self):
        """Gets the managed_fields_managers of this V1alpha1OverrideIgnoreDiff.  # noqa: E501


        :return: The managed_fields_managers of this V1alpha1OverrideIgnoreDiff.  # noqa: E501
        :rtype: list[str]
        """
        return self._managed_fields_managers

    @managed_fields_managers.setter
    def managed_fields_managers(self, managed_fields_managers):
        """Sets the managed_fields_managers of this V1alpha1OverrideIgnoreDiff.


        :param managed_fields_managers: The managed_fields_managers of this V1alpha1OverrideIgnoreDiff.  # noqa: E501
        :type: list[str]
        """

        self._managed_fields_managers = managed_fields_managers

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
        if issubclass(V1alpha1OverrideIgnoreDiff, dict):
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
        if not isinstance(other, V1alpha1OverrideIgnoreDiff):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
