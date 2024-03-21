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

class V1alpha1PullRequestGeneratorGitea(object):
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
        'api': 'str',
        'insecure': 'bool',
        'owner': 'str',
        'repo': 'str',
        'token_ref': 'V1alpha1SecretRef'
    }

    attribute_map = {
        'api': 'api',
        'insecure': 'insecure',
        'owner': 'owner',
        'repo': 'repo',
        'token_ref': 'tokenRef'
    }

    def __init__(self, api=None, insecure=None, owner=None, repo=None, token_ref=None):  # noqa: E501
        """V1alpha1PullRequestGeneratorGitea - a model defined in Swagger"""  # noqa: E501
        self._api = None
        self._insecure = None
        self._owner = None
        self._repo = None
        self._token_ref = None
        self.discriminator = None
        if api is not None:
            self.api = api
        if insecure is not None:
            self.insecure = insecure
        if owner is not None:
            self.owner = owner
        if repo is not None:
            self.repo = repo
        if token_ref is not None:
            self.token_ref = token_ref

    @property
    def api(self):
        """Gets the api of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501


        :return: The api of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501
        :rtype: str
        """
        return self._api

    @api.setter
    def api(self, api):
        """Sets the api of this V1alpha1PullRequestGeneratorGitea.


        :param api: The api of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501
        :type: str
        """

        self._api = api

    @property
    def insecure(self):
        """Gets the insecure of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501

        Allow insecure tls, for self-signed certificates; default: false.  # noqa: E501

        :return: The insecure of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this V1alpha1PullRequestGeneratorGitea.

        Allow insecure tls, for self-signed certificates; default: false.  # noqa: E501

        :param insecure: The insecure of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

    @property
    def owner(self):
        """Gets the owner of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501

        Gitea org or user to scan. Required.  # noqa: E501

        :return: The owner of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this V1alpha1PullRequestGeneratorGitea.

        Gitea org or user to scan. Required.  # noqa: E501

        :param owner: The owner of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def repo(self):
        """Gets the repo of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501

        Gitea repo name to scan. Required.  # noqa: E501

        :return: The repo of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this V1alpha1PullRequestGeneratorGitea.

        Gitea repo name to scan. Required.  # noqa: E501

        :param repo: The repo of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501
        :type: str
        """

        self._repo = repo

    @property
    def token_ref(self):
        """Gets the token_ref of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501


        :return: The token_ref of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501
        :rtype: V1alpha1SecretRef
        """
        return self._token_ref

    @token_ref.setter
    def token_ref(self, token_ref):
        """Sets the token_ref of this V1alpha1PullRequestGeneratorGitea.


        :param token_ref: The token_ref of this V1alpha1PullRequestGeneratorGitea.  # noqa: E501
        :type: V1alpha1SecretRef
        """

        self._token_ref = token_ref

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
        if issubclass(V1alpha1PullRequestGeneratorGitea, dict):
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
        if not isinstance(other, V1alpha1PullRequestGeneratorGitea):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
