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

class V1alpha1ApplicationSetTemplateMeta(object):
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
        'annotations': 'dict(str, str)',
        'finalizers': 'list[str]',
        'labels': 'dict(str, str)',
        'name': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'finalizers': 'finalizers',
        'labels': 'labels',
        'name': 'name',
        'namespace': 'namespace'
    }

    def __init__(self, annotations=None, finalizers=None, labels=None, name=None, namespace=None):  # noqa: E501
        """V1alpha1ApplicationSetTemplateMeta - a model defined in Swagger"""  # noqa: E501
        self._annotations = None
        self._finalizers = None
        self._labels = None
        self._name = None
        self._namespace = None
        self.discriminator = None
        if annotations is not None:
            self.annotations = annotations
        if finalizers is not None:
            self.finalizers = finalizers
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace

    @property
    def annotations(self):
        """Gets the annotations of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501


        :return: The annotations of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this V1alpha1ApplicationSetTemplateMeta.


        :param annotations: The annotations of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def finalizers(self):
        """Gets the finalizers of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501


        :return: The finalizers of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501
        :rtype: list[str]
        """
        return self._finalizers

    @finalizers.setter
    def finalizers(self, finalizers):
        """Sets the finalizers of this V1alpha1ApplicationSetTemplateMeta.


        :param finalizers: The finalizers of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501
        :type: list[str]
        """

        self._finalizers = finalizers

    @property
    def labels(self):
        """Gets the labels of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501


        :return: The labels of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this V1alpha1ApplicationSetTemplateMeta.


        :param labels: The labels of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501


        :return: The name of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1ApplicationSetTemplateMeta.


        :param name: The name of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501


        :return: The namespace of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1alpha1ApplicationSetTemplateMeta.


        :param namespace: The namespace of this V1alpha1ApplicationSetTemplateMeta.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if issubclass(V1alpha1ApplicationSetTemplateMeta, dict):
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
        if not isinstance(other, V1alpha1ApplicationSetTemplateMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other