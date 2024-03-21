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

class V1alpha1SyncOperationResult(object):
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
        'managed_namespace_metadata': 'V1alpha1ManagedNamespaceMetadata',
        'resources': 'list[V1alpha1ResourceResult]',
        'revision': 'str',
        'revisions': 'list[str]',
        'source': 'V1alpha1ApplicationSource',
        'sources': 'list[V1alpha1ApplicationSource]'
    }

    attribute_map = {
        'managed_namespace_metadata': 'managedNamespaceMetadata',
        'resources': 'resources',
        'revision': 'revision',
        'revisions': 'revisions',
        'source': 'source',
        'sources': 'sources'
    }

    def __init__(self, managed_namespace_metadata=None, resources=None, revision=None, revisions=None, source=None, sources=None):  # noqa: E501
        """V1alpha1SyncOperationResult - a model defined in Swagger"""  # noqa: E501
        self._managed_namespace_metadata = None
        self._resources = None
        self._revision = None
        self._revisions = None
        self._source = None
        self._sources = None
        self.discriminator = None
        if managed_namespace_metadata is not None:
            self.managed_namespace_metadata = managed_namespace_metadata
        if resources is not None:
            self.resources = resources
        if revision is not None:
            self.revision = revision
        if revisions is not None:
            self.revisions = revisions
        if source is not None:
            self.source = source
        if sources is not None:
            self.sources = sources

    @property
    def managed_namespace_metadata(self):
        """Gets the managed_namespace_metadata of this V1alpha1SyncOperationResult.  # noqa: E501


        :return: The managed_namespace_metadata of this V1alpha1SyncOperationResult.  # noqa: E501
        :rtype: V1alpha1ManagedNamespaceMetadata
        """
        return self._managed_namespace_metadata

    @managed_namespace_metadata.setter
    def managed_namespace_metadata(self, managed_namespace_metadata):
        """Sets the managed_namespace_metadata of this V1alpha1SyncOperationResult.


        :param managed_namespace_metadata: The managed_namespace_metadata of this V1alpha1SyncOperationResult.  # noqa: E501
        :type: V1alpha1ManagedNamespaceMetadata
        """

        self._managed_namespace_metadata = managed_namespace_metadata

    @property
    def resources(self):
        """Gets the resources of this V1alpha1SyncOperationResult.  # noqa: E501


        :return: The resources of this V1alpha1SyncOperationResult.  # noqa: E501
        :rtype: list[V1alpha1ResourceResult]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this V1alpha1SyncOperationResult.


        :param resources: The resources of this V1alpha1SyncOperationResult.  # noqa: E501
        :type: list[V1alpha1ResourceResult]
        """

        self._resources = resources

    @property
    def revision(self):
        """Gets the revision of this V1alpha1SyncOperationResult.  # noqa: E501


        :return: The revision of this V1alpha1SyncOperationResult.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this V1alpha1SyncOperationResult.


        :param revision: The revision of this V1alpha1SyncOperationResult.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def revisions(self):
        """Gets the revisions of this V1alpha1SyncOperationResult.  # noqa: E501


        :return: The revisions of this V1alpha1SyncOperationResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._revisions

    @revisions.setter
    def revisions(self, revisions):
        """Sets the revisions of this V1alpha1SyncOperationResult.


        :param revisions: The revisions of this V1alpha1SyncOperationResult.  # noqa: E501
        :type: list[str]
        """

        self._revisions = revisions

    @property
    def source(self):
        """Gets the source of this V1alpha1SyncOperationResult.  # noqa: E501


        :return: The source of this V1alpha1SyncOperationResult.  # noqa: E501
        :rtype: V1alpha1ApplicationSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this V1alpha1SyncOperationResult.


        :param source: The source of this V1alpha1SyncOperationResult.  # noqa: E501
        :type: V1alpha1ApplicationSource
        """

        self._source = source

    @property
    def sources(self):
        """Gets the sources of this V1alpha1SyncOperationResult.  # noqa: E501


        :return: The sources of this V1alpha1SyncOperationResult.  # noqa: E501
        :rtype: list[V1alpha1ApplicationSource]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this V1alpha1SyncOperationResult.


        :param sources: The sources of this V1alpha1SyncOperationResult.  # noqa: E501
        :type: list[V1alpha1ApplicationSource]
        """

        self._sources = sources

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
        if issubclass(V1alpha1SyncOperationResult, dict):
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
        if not isinstance(other, V1alpha1SyncOperationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
