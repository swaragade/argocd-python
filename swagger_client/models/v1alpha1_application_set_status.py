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

class V1alpha1ApplicationSetStatus(object):
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
        'application_status': 'list[V1alpha1ApplicationSetApplicationStatus]',
        'conditions': 'list[V1alpha1ApplicationSetCondition]'
    }

    attribute_map = {
        'application_status': 'applicationStatus',
        'conditions': 'conditions'
    }

    def __init__(self, application_status=None, conditions=None):  # noqa: E501
        """V1alpha1ApplicationSetStatus - a model defined in Swagger"""  # noqa: E501
        self._application_status = None
        self._conditions = None
        self.discriminator = None
        if application_status is not None:
            self.application_status = application_status
        if conditions is not None:
            self.conditions = conditions

    @property
    def application_status(self):
        """Gets the application_status of this V1alpha1ApplicationSetStatus.  # noqa: E501


        :return: The application_status of this V1alpha1ApplicationSetStatus.  # noqa: E501
        :rtype: list[V1alpha1ApplicationSetApplicationStatus]
        """
        return self._application_status

    @application_status.setter
    def application_status(self, application_status):
        """Sets the application_status of this V1alpha1ApplicationSetStatus.


        :param application_status: The application_status of this V1alpha1ApplicationSetStatus.  # noqa: E501
        :type: list[V1alpha1ApplicationSetApplicationStatus]
        """

        self._application_status = application_status

    @property
    def conditions(self):
        """Gets the conditions of this V1alpha1ApplicationSetStatus.  # noqa: E501


        :return: The conditions of this V1alpha1ApplicationSetStatus.  # noqa: E501
        :rtype: list[V1alpha1ApplicationSetCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1alpha1ApplicationSetStatus.


        :param conditions: The conditions of this V1alpha1ApplicationSetStatus.  # noqa: E501
        :type: list[V1alpha1ApplicationSetCondition]
        """

        self._conditions = conditions

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
        if issubclass(V1alpha1ApplicationSetStatus, dict):
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
        if not isinstance(other, V1alpha1ApplicationSetStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
