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

class V1alpha1SyncOperation(object):
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
        'dry_run': 'bool',
        'manifests': 'list[str]',
        'prune': 'bool',
        'resources': 'list[V1alpha1SyncOperationResource]',
        'revision': 'str',
        'revisions': 'list[str]',
        'source': 'V1alpha1ApplicationSource',
        'sources': 'list[V1alpha1ApplicationSource]',
        'sync_options': 'list[str]',
        'sync_strategy': 'V1alpha1SyncStrategy'
    }

    attribute_map = {
        'dry_run': 'dryRun',
        'manifests': 'manifests',
        'prune': 'prune',
        'resources': 'resources',
        'revision': 'revision',
        'revisions': 'revisions',
        'source': 'source',
        'sources': 'sources',
        'sync_options': 'syncOptions',
        'sync_strategy': 'syncStrategy'
    }

    def __init__(self, dry_run=None, manifests=None, prune=None, resources=None, revision=None, revisions=None, source=None, sources=None, sync_options=None, sync_strategy=None):  # noqa: E501
        """V1alpha1SyncOperation - a model defined in Swagger"""  # noqa: E501
        self._dry_run = None
        self._manifests = None
        self._prune = None
        self._resources = None
        self._revision = None
        self._revisions = None
        self._source = None
        self._sources = None
        self._sync_options = None
        self._sync_strategy = None
        self.discriminator = None
        if dry_run is not None:
            self.dry_run = dry_run
        if manifests is not None:
            self.manifests = manifests
        if prune is not None:
            self.prune = prune
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
        if sync_options is not None:
            self.sync_options = sync_options
        if sync_strategy is not None:
            self.sync_strategy = sync_strategy

    @property
    def dry_run(self):
        """Gets the dry_run of this V1alpha1SyncOperation.  # noqa: E501


        :return: The dry_run of this V1alpha1SyncOperation.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this V1alpha1SyncOperation.


        :param dry_run: The dry_run of this V1alpha1SyncOperation.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def manifests(self):
        """Gets the manifests of this V1alpha1SyncOperation.  # noqa: E501


        :return: The manifests of this V1alpha1SyncOperation.  # noqa: E501
        :rtype: list[str]
        """
        return self._manifests

    @manifests.setter
    def manifests(self, manifests):
        """Sets the manifests of this V1alpha1SyncOperation.


        :param manifests: The manifests of this V1alpha1SyncOperation.  # noqa: E501
        :type: list[str]
        """

        self._manifests = manifests

    @property
    def prune(self):
        """Gets the prune of this V1alpha1SyncOperation.  # noqa: E501


        :return: The prune of this V1alpha1SyncOperation.  # noqa: E501
        :rtype: bool
        """
        return self._prune

    @prune.setter
    def prune(self, prune):
        """Sets the prune of this V1alpha1SyncOperation.


        :param prune: The prune of this V1alpha1SyncOperation.  # noqa: E501
        :type: bool
        """

        self._prune = prune

    @property
    def resources(self):
        """Gets the resources of this V1alpha1SyncOperation.  # noqa: E501


        :return: The resources of this V1alpha1SyncOperation.  # noqa: E501
        :rtype: list[V1alpha1SyncOperationResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this V1alpha1SyncOperation.


        :param resources: The resources of this V1alpha1SyncOperation.  # noqa: E501
        :type: list[V1alpha1SyncOperationResource]
        """

        self._resources = resources

    @property
    def revision(self):
        """Gets the revision of this V1alpha1SyncOperation.  # noqa: E501

        Revision is the revision (Git) or chart version (Helm) which to sync the application to If omitted, will use the revision specified in app spec.  # noqa: E501

        :return: The revision of this V1alpha1SyncOperation.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this V1alpha1SyncOperation.

        Revision is the revision (Git) or chart version (Helm) which to sync the application to If omitted, will use the revision specified in app spec.  # noqa: E501

        :param revision: The revision of this V1alpha1SyncOperation.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def revisions(self):
        """Gets the revisions of this V1alpha1SyncOperation.  # noqa: E501

        Revisions is the list of revision (Git) or chart version (Helm) which to sync each source in sources field for the application to If omitted, will use the revision specified in app spec.  # noqa: E501

        :return: The revisions of this V1alpha1SyncOperation.  # noqa: E501
        :rtype: list[str]
        """
        return self._revisions

    @revisions.setter
    def revisions(self, revisions):
        """Sets the revisions of this V1alpha1SyncOperation.

        Revisions is the list of revision (Git) or chart version (Helm) which to sync each source in sources field for the application to If omitted, will use the revision specified in app spec.  # noqa: E501

        :param revisions: The revisions of this V1alpha1SyncOperation.  # noqa: E501
        :type: list[str]
        """

        self._revisions = revisions

    @property
    def source(self):
        """Gets the source of this V1alpha1SyncOperation.  # noqa: E501


        :return: The source of this V1alpha1SyncOperation.  # noqa: E501
        :rtype: V1alpha1ApplicationSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this V1alpha1SyncOperation.


        :param source: The source of this V1alpha1SyncOperation.  # noqa: E501
        :type: V1alpha1ApplicationSource
        """

        self._source = source

    @property
    def sources(self):
        """Gets the sources of this V1alpha1SyncOperation.  # noqa: E501


        :return: The sources of this V1alpha1SyncOperation.  # noqa: E501
        :rtype: list[V1alpha1ApplicationSource]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this V1alpha1SyncOperation.


        :param sources: The sources of this V1alpha1SyncOperation.  # noqa: E501
        :type: list[V1alpha1ApplicationSource]
        """

        self._sources = sources

    @property
    def sync_options(self):
        """Gets the sync_options of this V1alpha1SyncOperation.  # noqa: E501


        :return: The sync_options of this V1alpha1SyncOperation.  # noqa: E501
        :rtype: list[str]
        """
        return self._sync_options

    @sync_options.setter
    def sync_options(self, sync_options):
        """Sets the sync_options of this V1alpha1SyncOperation.


        :param sync_options: The sync_options of this V1alpha1SyncOperation.  # noqa: E501
        :type: list[str]
        """

        self._sync_options = sync_options

    @property
    def sync_strategy(self):
        """Gets the sync_strategy of this V1alpha1SyncOperation.  # noqa: E501


        :return: The sync_strategy of this V1alpha1SyncOperation.  # noqa: E501
        :rtype: V1alpha1SyncStrategy
        """
        return self._sync_strategy

    @sync_strategy.setter
    def sync_strategy(self, sync_strategy):
        """Sets the sync_strategy of this V1alpha1SyncOperation.


        :param sync_strategy: The sync_strategy of this V1alpha1SyncOperation.  # noqa: E501
        :type: V1alpha1SyncStrategy
        """

        self._sync_strategy = sync_strategy

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
        if issubclass(V1alpha1SyncOperation, dict):
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
        if not isinstance(other, V1alpha1SyncOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other