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

class V1alpha1PullRequestGeneratorFilter(object):
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
        'branch_match': 'str',
        'target_branch_match': 'str'
    }

    attribute_map = {
        'branch_match': 'branchMatch',
        'target_branch_match': 'targetBranchMatch'
    }

    def __init__(self, branch_match=None, target_branch_match=None):  # noqa: E501
        """V1alpha1PullRequestGeneratorFilter - a model defined in Swagger"""  # noqa: E501
        self._branch_match = None
        self._target_branch_match = None
        self.discriminator = None
        if branch_match is not None:
            self.branch_match = branch_match
        if target_branch_match is not None:
            self.target_branch_match = target_branch_match

    @property
    def branch_match(self):
        """Gets the branch_match of this V1alpha1PullRequestGeneratorFilter.  # noqa: E501


        :return: The branch_match of this V1alpha1PullRequestGeneratorFilter.  # noqa: E501
        :rtype: str
        """
        return self._branch_match

    @branch_match.setter
    def branch_match(self, branch_match):
        """Sets the branch_match of this V1alpha1PullRequestGeneratorFilter.


        :param branch_match: The branch_match of this V1alpha1PullRequestGeneratorFilter.  # noqa: E501
        :type: str
        """

        self._branch_match = branch_match

    @property
    def target_branch_match(self):
        """Gets the target_branch_match of this V1alpha1PullRequestGeneratorFilter.  # noqa: E501


        :return: The target_branch_match of this V1alpha1PullRequestGeneratorFilter.  # noqa: E501
        :rtype: str
        """
        return self._target_branch_match

    @target_branch_match.setter
    def target_branch_match(self, target_branch_match):
        """Sets the target_branch_match of this V1alpha1PullRequestGeneratorFilter.


        :param target_branch_match: The target_branch_match of this V1alpha1PullRequestGeneratorFilter.  # noqa: E501
        :type: str
        """

        self._target_branch_match = target_branch_match

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
        if issubclass(V1alpha1PullRequestGeneratorFilter, dict):
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
        if not isinstance(other, V1alpha1PullRequestGeneratorFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
