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

class StreamResultOfV1alpha1ApplicationWatchEvent(object):
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
        'error': 'RuntimeStreamError',
        'result': 'V1alpha1ApplicationWatchEvent'
    }

    attribute_map = {
        'error': 'error',
        'result': 'result'
    }

    def __init__(self, error=None, result=None):  # noqa: E501
        """StreamResultOfV1alpha1ApplicationWatchEvent - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._result = None
        self.discriminator = None
        if error is not None:
            self.error = error
        if result is not None:
            self.result = result

    @property
    def error(self):
        """Gets the error of this StreamResultOfV1alpha1ApplicationWatchEvent.  # noqa: E501


        :return: The error of this StreamResultOfV1alpha1ApplicationWatchEvent.  # noqa: E501
        :rtype: RuntimeStreamError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this StreamResultOfV1alpha1ApplicationWatchEvent.


        :param error: The error of this StreamResultOfV1alpha1ApplicationWatchEvent.  # noqa: E501
        :type: RuntimeStreamError
        """

        self._error = error

    @property
    def result(self):
        """Gets the result of this StreamResultOfV1alpha1ApplicationWatchEvent.  # noqa: E501


        :return: The result of this StreamResultOfV1alpha1ApplicationWatchEvent.  # noqa: E501
        :rtype: V1alpha1ApplicationWatchEvent
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this StreamResultOfV1alpha1ApplicationWatchEvent.


        :param result: The result of this StreamResultOfV1alpha1ApplicationWatchEvent.  # noqa: E501
        :type: V1alpha1ApplicationWatchEvent
        """

        self._result = result

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
        if issubclass(StreamResultOfV1alpha1ApplicationWatchEvent, dict):
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
        if not isinstance(other, StreamResultOfV1alpha1ApplicationWatchEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
