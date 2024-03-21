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

class V1alpha1ApplicationSourceKustomize(object):
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
        'common_annotations': 'dict(str, str)',
        'common_annotations_envsubst': 'bool',
        'common_labels': 'dict(str, str)',
        'components': 'list[str]',
        'force_common_annotations': 'bool',
        'force_common_labels': 'bool',
        'images': 'list[str]',
        'name_prefix': 'str',
        'name_suffix': 'str',
        'namespace': 'str',
        'patches': 'list[V1alpha1KustomizePatch]',
        'replicas': 'list[V1alpha1KustomizeReplica]',
        'version': 'str'
    }

    attribute_map = {
        'common_annotations': 'commonAnnotations',
        'common_annotations_envsubst': 'commonAnnotationsEnvsubst',
        'common_labels': 'commonLabels',
        'components': 'components',
        'force_common_annotations': 'forceCommonAnnotations',
        'force_common_labels': 'forceCommonLabels',
        'images': 'images',
        'name_prefix': 'namePrefix',
        'name_suffix': 'nameSuffix',
        'namespace': 'namespace',
        'patches': 'patches',
        'replicas': 'replicas',
        'version': 'version'
    }

    def __init__(self, common_annotations=None, common_annotations_envsubst=None, common_labels=None, components=None, force_common_annotations=None, force_common_labels=None, images=None, name_prefix=None, name_suffix=None, namespace=None, patches=None, replicas=None, version=None):  # noqa: E501
        """V1alpha1ApplicationSourceKustomize - a model defined in Swagger"""  # noqa: E501
        self._common_annotations = None
        self._common_annotations_envsubst = None
        self._common_labels = None
        self._components = None
        self._force_common_annotations = None
        self._force_common_labels = None
        self._images = None
        self._name_prefix = None
        self._name_suffix = None
        self._namespace = None
        self._patches = None
        self._replicas = None
        self._version = None
        self.discriminator = None
        if common_annotations is not None:
            self.common_annotations = common_annotations
        if common_annotations_envsubst is not None:
            self.common_annotations_envsubst = common_annotations_envsubst
        if common_labels is not None:
            self.common_labels = common_labels
        if components is not None:
            self.components = components
        if force_common_annotations is not None:
            self.force_common_annotations = force_common_annotations
        if force_common_labels is not None:
            self.force_common_labels = force_common_labels
        if images is not None:
            self.images = images
        if name_prefix is not None:
            self.name_prefix = name_prefix
        if name_suffix is not None:
            self.name_suffix = name_suffix
        if namespace is not None:
            self.namespace = namespace
        if patches is not None:
            self.patches = patches
        if replicas is not None:
            self.replicas = replicas
        if version is not None:
            self.version = version

    @property
    def common_annotations(self):
        """Gets the common_annotations of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The common_annotations of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._common_annotations

    @common_annotations.setter
    def common_annotations(self, common_annotations):
        """Sets the common_annotations of this V1alpha1ApplicationSourceKustomize.


        :param common_annotations: The common_annotations of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: dict(str, str)
        """

        self._common_annotations = common_annotations

    @property
    def common_annotations_envsubst(self):
        """Gets the common_annotations_envsubst of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The common_annotations_envsubst of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: bool
        """
        return self._common_annotations_envsubst

    @common_annotations_envsubst.setter
    def common_annotations_envsubst(self, common_annotations_envsubst):
        """Sets the common_annotations_envsubst of this V1alpha1ApplicationSourceKustomize.


        :param common_annotations_envsubst: The common_annotations_envsubst of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: bool
        """

        self._common_annotations_envsubst = common_annotations_envsubst

    @property
    def common_labels(self):
        """Gets the common_labels of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The common_labels of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._common_labels

    @common_labels.setter
    def common_labels(self, common_labels):
        """Sets the common_labels of this V1alpha1ApplicationSourceKustomize.


        :param common_labels: The common_labels of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: dict(str, str)
        """

        self._common_labels = common_labels

    @property
    def components(self):
        """Gets the components of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The components of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: list[str]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this V1alpha1ApplicationSourceKustomize.


        :param components: The components of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: list[str]
        """

        self._components = components

    @property
    def force_common_annotations(self):
        """Gets the force_common_annotations of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The force_common_annotations of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: bool
        """
        return self._force_common_annotations

    @force_common_annotations.setter
    def force_common_annotations(self, force_common_annotations):
        """Sets the force_common_annotations of this V1alpha1ApplicationSourceKustomize.


        :param force_common_annotations: The force_common_annotations of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: bool
        """

        self._force_common_annotations = force_common_annotations

    @property
    def force_common_labels(self):
        """Gets the force_common_labels of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The force_common_labels of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: bool
        """
        return self._force_common_labels

    @force_common_labels.setter
    def force_common_labels(self, force_common_labels):
        """Sets the force_common_labels of this V1alpha1ApplicationSourceKustomize.


        :param force_common_labels: The force_common_labels of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: bool
        """

        self._force_common_labels = force_common_labels

    @property
    def images(self):
        """Gets the images of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The images of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this V1alpha1ApplicationSourceKustomize.


        :param images: The images of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: list[str]
        """

        self._images = images

    @property
    def name_prefix(self):
        """Gets the name_prefix of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The name_prefix of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: str
        """
        return self._name_prefix

    @name_prefix.setter
    def name_prefix(self, name_prefix):
        """Sets the name_prefix of this V1alpha1ApplicationSourceKustomize.


        :param name_prefix: The name_prefix of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: str
        """

        self._name_prefix = name_prefix

    @property
    def name_suffix(self):
        """Gets the name_suffix of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The name_suffix of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: str
        """
        return self._name_suffix

    @name_suffix.setter
    def name_suffix(self, name_suffix):
        """Sets the name_suffix of this V1alpha1ApplicationSourceKustomize.


        :param name_suffix: The name_suffix of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: str
        """

        self._name_suffix = name_suffix

    @property
    def namespace(self):
        """Gets the namespace of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The namespace of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1alpha1ApplicationSourceKustomize.


        :param namespace: The namespace of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def patches(self):
        """Gets the patches of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The patches of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: list[V1alpha1KustomizePatch]
        """
        return self._patches

    @patches.setter
    def patches(self, patches):
        """Sets the patches of this V1alpha1ApplicationSourceKustomize.


        :param patches: The patches of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: list[V1alpha1KustomizePatch]
        """

        self._patches = patches

    @property
    def replicas(self):
        """Gets the replicas of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The replicas of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: list[V1alpha1KustomizeReplica]
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this V1alpha1ApplicationSourceKustomize.


        :param replicas: The replicas of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: list[V1alpha1KustomizeReplica]
        """

        self._replicas = replicas

    @property
    def version(self):
        """Gets the version of this V1alpha1ApplicationSourceKustomize.  # noqa: E501


        :return: The version of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1alpha1ApplicationSourceKustomize.


        :param version: The version of this V1alpha1ApplicationSourceKustomize.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(V1alpha1ApplicationSourceKustomize, dict):
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
        if not isinstance(other, V1alpha1ApplicationSourceKustomize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
