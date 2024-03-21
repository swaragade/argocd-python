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

class V1alpha1ApplicationSource(object):
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
        'chart': 'str',
        'directory': 'V1alpha1ApplicationSourceDirectory',
        'helm': 'V1alpha1ApplicationSourceHelm',
        'kustomize': 'V1alpha1ApplicationSourceKustomize',
        'path': 'str',
        'plugin': 'V1alpha1ApplicationSourcePlugin',
        'ref': 'str',
        'repo_url': 'str',
        'target_revision': 'str'
    }

    attribute_map = {
        'chart': 'chart',
        'directory': 'directory',
        'helm': 'helm',
        'kustomize': 'kustomize',
        'path': 'path',
        'plugin': 'plugin',
        'ref': 'ref',
        'repo_url': 'repoURL',
        'target_revision': 'targetRevision'
    }

    def __init__(self, chart=None, directory=None, helm=None, kustomize=None, path=None, plugin=None, ref=None, repo_url=None, target_revision=None):  # noqa: E501
        """V1alpha1ApplicationSource - a model defined in Swagger"""  # noqa: E501
        self._chart = None
        self._directory = None
        self._helm = None
        self._kustomize = None
        self._path = None
        self._plugin = None
        self._ref = None
        self._repo_url = None
        self._target_revision = None
        self.discriminator = None
        if chart is not None:
            self.chart = chart
        if directory is not None:
            self.directory = directory
        if helm is not None:
            self.helm = helm
        if kustomize is not None:
            self.kustomize = kustomize
        if path is not None:
            self.path = path
        if plugin is not None:
            self.plugin = plugin
        if ref is not None:
            self.ref = ref
        if repo_url is not None:
            self.repo_url = repo_url
        if target_revision is not None:
            self.target_revision = target_revision

    @property
    def chart(self):
        """Gets the chart of this V1alpha1ApplicationSource.  # noqa: E501

        Chart is a Helm chart name, and must be specified for applications sourced from a Helm repo.  # noqa: E501

        :return: The chart of this V1alpha1ApplicationSource.  # noqa: E501
        :rtype: str
        """
        return self._chart

    @chart.setter
    def chart(self, chart):
        """Sets the chart of this V1alpha1ApplicationSource.

        Chart is a Helm chart name, and must be specified for applications sourced from a Helm repo.  # noqa: E501

        :param chart: The chart of this V1alpha1ApplicationSource.  # noqa: E501
        :type: str
        """

        self._chart = chart

    @property
    def directory(self):
        """Gets the directory of this V1alpha1ApplicationSource.  # noqa: E501


        :return: The directory of this V1alpha1ApplicationSource.  # noqa: E501
        :rtype: V1alpha1ApplicationSourceDirectory
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this V1alpha1ApplicationSource.


        :param directory: The directory of this V1alpha1ApplicationSource.  # noqa: E501
        :type: V1alpha1ApplicationSourceDirectory
        """

        self._directory = directory

    @property
    def helm(self):
        """Gets the helm of this V1alpha1ApplicationSource.  # noqa: E501


        :return: The helm of this V1alpha1ApplicationSource.  # noqa: E501
        :rtype: V1alpha1ApplicationSourceHelm
        """
        return self._helm

    @helm.setter
    def helm(self, helm):
        """Sets the helm of this V1alpha1ApplicationSource.


        :param helm: The helm of this V1alpha1ApplicationSource.  # noqa: E501
        :type: V1alpha1ApplicationSourceHelm
        """

        self._helm = helm

    @property
    def kustomize(self):
        """Gets the kustomize of this V1alpha1ApplicationSource.  # noqa: E501


        :return: The kustomize of this V1alpha1ApplicationSource.  # noqa: E501
        :rtype: V1alpha1ApplicationSourceKustomize
        """
        return self._kustomize

    @kustomize.setter
    def kustomize(self, kustomize):
        """Sets the kustomize of this V1alpha1ApplicationSource.


        :param kustomize: The kustomize of this V1alpha1ApplicationSource.  # noqa: E501
        :type: V1alpha1ApplicationSourceKustomize
        """

        self._kustomize = kustomize

    @property
    def path(self):
        """Gets the path of this V1alpha1ApplicationSource.  # noqa: E501

        Path is a directory path within the Git repository, and is only valid for applications sourced from Git.  # noqa: E501

        :return: The path of this V1alpha1ApplicationSource.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1alpha1ApplicationSource.

        Path is a directory path within the Git repository, and is only valid for applications sourced from Git.  # noqa: E501

        :param path: The path of this V1alpha1ApplicationSource.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def plugin(self):
        """Gets the plugin of this V1alpha1ApplicationSource.  # noqa: E501


        :return: The plugin of this V1alpha1ApplicationSource.  # noqa: E501
        :rtype: V1alpha1ApplicationSourcePlugin
        """
        return self._plugin

    @plugin.setter
    def plugin(self, plugin):
        """Sets the plugin of this V1alpha1ApplicationSource.


        :param plugin: The plugin of this V1alpha1ApplicationSource.  # noqa: E501
        :type: V1alpha1ApplicationSourcePlugin
        """

        self._plugin = plugin

    @property
    def ref(self):
        """Gets the ref of this V1alpha1ApplicationSource.  # noqa: E501

        Ref is reference to another source within sources field. This field will not be used if used with a `source` tag.  # noqa: E501

        :return: The ref of this V1alpha1ApplicationSource.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this V1alpha1ApplicationSource.

        Ref is reference to another source within sources field. This field will not be used if used with a `source` tag.  # noqa: E501

        :param ref: The ref of this V1alpha1ApplicationSource.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def repo_url(self):
        """Gets the repo_url of this V1alpha1ApplicationSource.  # noqa: E501


        :return: The repo_url of this V1alpha1ApplicationSource.  # noqa: E501
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this V1alpha1ApplicationSource.


        :param repo_url: The repo_url of this V1alpha1ApplicationSource.  # noqa: E501
        :type: str
        """

        self._repo_url = repo_url

    @property
    def target_revision(self):
        """Gets the target_revision of this V1alpha1ApplicationSource.  # noqa: E501

        TargetRevision defines the revision of the source to sync the application to. In case of Git, this can be commit, tag, or branch. If omitted, will equal to HEAD. In case of Helm, this is a semver tag for the Chart's version.  # noqa: E501

        :return: The target_revision of this V1alpha1ApplicationSource.  # noqa: E501
        :rtype: str
        """
        return self._target_revision

    @target_revision.setter
    def target_revision(self, target_revision):
        """Sets the target_revision of this V1alpha1ApplicationSource.

        TargetRevision defines the revision of the source to sync the application to. In case of Git, this can be commit, tag, or branch. If omitted, will equal to HEAD. In case of Helm, this is a semver tag for the Chart's version.  # noqa: E501

        :param target_revision: The target_revision of this V1alpha1ApplicationSource.  # noqa: E501
        :type: str
        """

        self._target_revision = target_revision

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
        if issubclass(V1alpha1ApplicationSource, dict):
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
        if not isinstance(other, V1alpha1ApplicationSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other