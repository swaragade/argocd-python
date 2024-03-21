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

class V1alpha1SCMProviderGeneratorFilter(object):
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
        'label_match': 'str',
        'paths_do_not_exist': 'list[str]',
        'paths_exist': 'list[str]',
        'repository_match': 'str'
    }

    attribute_map = {
        'branch_match': 'branchMatch',
        'label_match': 'labelMatch',
        'paths_do_not_exist': 'pathsDoNotExist',
        'paths_exist': 'pathsExist',
        'repository_match': 'repositoryMatch'
    }

    def __init__(self, branch_match=None, label_match=None, paths_do_not_exist=None, paths_exist=None, repository_match=None):  # noqa: E501
        """V1alpha1SCMProviderGeneratorFilter - a model defined in Swagger"""  # noqa: E501
        self._branch_match = None
        self._label_match = None
        self._paths_do_not_exist = None
        self._paths_exist = None
        self._repository_match = None
        self.discriminator = None
        if branch_match is not None:
            self.branch_match = branch_match
        if label_match is not None:
            self.label_match = label_match
        if paths_do_not_exist is not None:
            self.paths_do_not_exist = paths_do_not_exist
        if paths_exist is not None:
            self.paths_exist = paths_exist
        if repository_match is not None:
            self.repository_match = repository_match

    @property
    def branch_match(self):
        """Gets the branch_match of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501

        A regex which must match the branch name.  # noqa: E501

        :return: The branch_match of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501
        :rtype: str
        """
        return self._branch_match

    @branch_match.setter
    def branch_match(self, branch_match):
        """Sets the branch_match of this V1alpha1SCMProviderGeneratorFilter.

        A regex which must match the branch name.  # noqa: E501

        :param branch_match: The branch_match of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501
        :type: str
        """

        self._branch_match = branch_match

    @property
    def label_match(self):
        """Gets the label_match of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501

        A regex which must match at least one label.  # noqa: E501

        :return: The label_match of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501
        :rtype: str
        """
        return self._label_match

    @label_match.setter
    def label_match(self, label_match):
        """Sets the label_match of this V1alpha1SCMProviderGeneratorFilter.

        A regex which must match at least one label.  # noqa: E501

        :param label_match: The label_match of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501
        :type: str
        """

        self._label_match = label_match

    @property
    def paths_do_not_exist(self):
        """Gets the paths_do_not_exist of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501

        An array of paths, all of which must not exist.  # noqa: E501

        :return: The paths_do_not_exist of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths_do_not_exist

    @paths_do_not_exist.setter
    def paths_do_not_exist(self, paths_do_not_exist):
        """Sets the paths_do_not_exist of this V1alpha1SCMProviderGeneratorFilter.

        An array of paths, all of which must not exist.  # noqa: E501

        :param paths_do_not_exist: The paths_do_not_exist of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501
        :type: list[str]
        """

        self._paths_do_not_exist = paths_do_not_exist

    @property
    def paths_exist(self):
        """Gets the paths_exist of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501

        An array of paths, all of which must exist.  # noqa: E501

        :return: The paths_exist of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths_exist

    @paths_exist.setter
    def paths_exist(self, paths_exist):
        """Sets the paths_exist of this V1alpha1SCMProviderGeneratorFilter.

        An array of paths, all of which must exist.  # noqa: E501

        :param paths_exist: The paths_exist of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501
        :type: list[str]
        """

        self._paths_exist = paths_exist

    @property
    def repository_match(self):
        """Gets the repository_match of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501

        A regex for repo names.  # noqa: E501

        :return: The repository_match of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501
        :rtype: str
        """
        return self._repository_match

    @repository_match.setter
    def repository_match(self, repository_match):
        """Sets the repository_match of this V1alpha1SCMProviderGeneratorFilter.

        A regex for repo names.  # noqa: E501

        :param repository_match: The repository_match of this V1alpha1SCMProviderGeneratorFilter.  # noqa: E501
        :type: str
        """

        self._repository_match = repository_match

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
        if issubclass(V1alpha1SCMProviderGeneratorFilter, dict):
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
        if not isinstance(other, V1alpha1SCMProviderGeneratorFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
