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

class RepositoryRepoAppDetailsQuery(object):
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
        'app_name': 'str',
        'app_project': 'str',
        'source': 'V1alpha1ApplicationSource'
    }

    attribute_map = {
        'app_name': 'appName',
        'app_project': 'appProject',
        'source': 'source'
    }

    def __init__(self, app_name=None, app_project=None, source=None):  # noqa: E501
        """RepositoryRepoAppDetailsQuery - a model defined in Swagger"""  # noqa: E501
        self._app_name = None
        self._app_project = None
        self._source = None
        self.discriminator = None
        if app_name is not None:
            self.app_name = app_name
        if app_project is not None:
            self.app_project = app_project
        if source is not None:
            self.source = source

    @property
    def app_name(self):
        """Gets the app_name of this RepositoryRepoAppDetailsQuery.  # noqa: E501


        :return: The app_name of this RepositoryRepoAppDetailsQuery.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this RepositoryRepoAppDetailsQuery.


        :param app_name: The app_name of this RepositoryRepoAppDetailsQuery.  # noqa: E501
        :type: str
        """

        self._app_name = app_name

    @property
    def app_project(self):
        """Gets the app_project of this RepositoryRepoAppDetailsQuery.  # noqa: E501


        :return: The app_project of this RepositoryRepoAppDetailsQuery.  # noqa: E501
        :rtype: str
        """
        return self._app_project

    @app_project.setter
    def app_project(self, app_project):
        """Sets the app_project of this RepositoryRepoAppDetailsQuery.


        :param app_project: The app_project of this RepositoryRepoAppDetailsQuery.  # noqa: E501
        :type: str
        """

        self._app_project = app_project

    @property
    def source(self):
        """Gets the source of this RepositoryRepoAppDetailsQuery.  # noqa: E501


        :return: The source of this RepositoryRepoAppDetailsQuery.  # noqa: E501
        :rtype: V1alpha1ApplicationSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this RepositoryRepoAppDetailsQuery.


        :param source: The source of this RepositoryRepoAppDetailsQuery.  # noqa: E501
        :type: V1alpha1ApplicationSource
        """

        self._source = source

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
        if issubclass(RepositoryRepoAppDetailsQuery, dict):
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
        if not isinstance(other, RepositoryRepoAppDetailsQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other