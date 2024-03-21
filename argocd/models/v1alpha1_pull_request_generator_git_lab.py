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

class V1alpha1PullRequestGeneratorGitLab(object):
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
        'labels': 'list[str]',
        'project': 'str',
        'pull_request_state': 'str',
        'token_ref': 'V1alpha1SecretRef'
    }

    attribute_map = {
        'api': 'api',
        'insecure': 'insecure',
        'labels': 'labels',
        'project': 'project',
        'pull_request_state': 'pullRequestState',
        'token_ref': 'tokenRef'
    }

    def __init__(self, api=None, insecure=None, labels=None, project=None, pull_request_state=None, token_ref=None):  # noqa: E501
        """V1alpha1PullRequestGeneratorGitLab - a model defined in Swagger"""  # noqa: E501
        self._api = None
        self._insecure = None
        self._labels = None
        self._project = None
        self._pull_request_state = None
        self._token_ref = None
        self.discriminator = None
        if api is not None:
            self.api = api
        if insecure is not None:
            self.insecure = insecure
        if labels is not None:
            self.labels = labels
        if project is not None:
            self.project = project
        if pull_request_state is not None:
            self.pull_request_state = pull_request_state
        if token_ref is not None:
            self.token_ref = token_ref

    @property
    def api(self):
        """Gets the api of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501

        The GitLab API URL to talk to. If blank, uses https://gitlab.com/.  # noqa: E501

        :return: The api of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501
        :rtype: str
        """
        return self._api

    @api.setter
    def api(self, api):
        """Sets the api of this V1alpha1PullRequestGeneratorGitLab.

        The GitLab API URL to talk to. If blank, uses https://gitlab.com/.  # noqa: E501

        :param api: The api of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501
        :type: str
        """

        self._api = api

    @property
    def insecure(self):
        """Gets the insecure of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501


        :return: The insecure of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this V1alpha1PullRequestGeneratorGitLab.


        :param insecure: The insecure of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

    @property
    def labels(self):
        """Gets the labels of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501


        :return: The labels of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1alpha1PullRequestGeneratorGitLab.


        :param labels: The labels of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def project(self):
        """Gets the project of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501

        GitLab project to scan. Required.  # noqa: E501

        :return: The project of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this V1alpha1PullRequestGeneratorGitLab.

        GitLab project to scan. Required.  # noqa: E501

        :param project: The project of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def pull_request_state(self):
        """Gets the pull_request_state of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501


        :return: The pull_request_state of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501
        :rtype: str
        """
        return self._pull_request_state

    @pull_request_state.setter
    def pull_request_state(self, pull_request_state):
        """Sets the pull_request_state of this V1alpha1PullRequestGeneratorGitLab.


        :param pull_request_state: The pull_request_state of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501
        :type: str
        """

        self._pull_request_state = pull_request_state

    @property
    def token_ref(self):
        """Gets the token_ref of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501


        :return: The token_ref of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501
        :rtype: V1alpha1SecretRef
        """
        return self._token_ref

    @token_ref.setter
    def token_ref(self, token_ref):
        """Sets the token_ref of this V1alpha1PullRequestGeneratorGitLab.


        :param token_ref: The token_ref of this V1alpha1PullRequestGeneratorGitLab.  # noqa: E501
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
        if issubclass(V1alpha1PullRequestGeneratorGitLab, dict):
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
        if not isinstance(other, V1alpha1PullRequestGeneratorGitLab):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other