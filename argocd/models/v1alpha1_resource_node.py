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
from argocd.models.v1alpha1_resource_ref import V1alpha1ResourceRef  # noqa: F401,E501

class V1alpha1ResourceNode(V1alpha1ResourceRef):
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
        'created_at': 'V1Time',
        'health': 'V1alpha1HealthStatus',
        'images': 'list[str]',
        'info': 'list[V1alpha1InfoItem]',
        'networking_info': 'V1alpha1ResourceNetworkingInfo',
        'parent_refs': 'list[V1alpha1ResourceRef]',
        'resource_version': 'str'
    }
    if hasattr(V1alpha1ResourceRef, "swagger_types"):
        swagger_types.update(V1alpha1ResourceRef.swagger_types)

    attribute_map = {
        'created_at': 'createdAt',
        'health': 'health',
        'images': 'images',
        'info': 'info',
        'networking_info': 'networkingInfo',
        'parent_refs': 'parentRefs',
        'resource_version': 'resourceVersion'
    }
    if hasattr(V1alpha1ResourceRef, "attribute_map"):
        attribute_map.update(V1alpha1ResourceRef.attribute_map)

    def __init__(self, created_at=None, health=None, images=None, info=None, networking_info=None, parent_refs=None, resource_version=None, *args, **kwargs):  # noqa: E501
        """V1alpha1ResourceNode - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._health = None
        self._images = None
        self._info = None
        self._networking_info = None
        self._parent_refs = None
        self._resource_version = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if health is not None:
            self.health = health
        if images is not None:
            self.images = images
        if info is not None:
            self.info = info
        if networking_info is not None:
            self.networking_info = networking_info
        if parent_refs is not None:
            self.parent_refs = parent_refs
        if resource_version is not None:
            self.resource_version = resource_version
        V1alpha1ResourceRef.__init__(self, *args, **kwargs)

    @property
    def created_at(self):
        """Gets the created_at of this V1alpha1ResourceNode.  # noqa: E501


        :return: The created_at of this V1alpha1ResourceNode.  # noqa: E501
        :rtype: V1Time
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V1alpha1ResourceNode.


        :param created_at: The created_at of this V1alpha1ResourceNode.  # noqa: E501
        :type: V1Time
        """

        self._created_at = created_at

    @property
    def health(self):
        """Gets the health of this V1alpha1ResourceNode.  # noqa: E501


        :return: The health of this V1alpha1ResourceNode.  # noqa: E501
        :rtype: V1alpha1HealthStatus
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this V1alpha1ResourceNode.


        :param health: The health of this V1alpha1ResourceNode.  # noqa: E501
        :type: V1alpha1HealthStatus
        """

        self._health = health

    @property
    def images(self):
        """Gets the images of this V1alpha1ResourceNode.  # noqa: E501


        :return: The images of this V1alpha1ResourceNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this V1alpha1ResourceNode.


        :param images: The images of this V1alpha1ResourceNode.  # noqa: E501
        :type: list[str]
        """

        self._images = images

    @property
    def info(self):
        """Gets the info of this V1alpha1ResourceNode.  # noqa: E501


        :return: The info of this V1alpha1ResourceNode.  # noqa: E501
        :rtype: list[V1alpha1InfoItem]
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this V1alpha1ResourceNode.


        :param info: The info of this V1alpha1ResourceNode.  # noqa: E501
        :type: list[V1alpha1InfoItem]
        """

        self._info = info

    @property
    def networking_info(self):
        """Gets the networking_info of this V1alpha1ResourceNode.  # noqa: E501


        :return: The networking_info of this V1alpha1ResourceNode.  # noqa: E501
        :rtype: V1alpha1ResourceNetworkingInfo
        """
        return self._networking_info

    @networking_info.setter
    def networking_info(self, networking_info):
        """Sets the networking_info of this V1alpha1ResourceNode.


        :param networking_info: The networking_info of this V1alpha1ResourceNode.  # noqa: E501
        :type: V1alpha1ResourceNetworkingInfo
        """

        self._networking_info = networking_info

    @property
    def parent_refs(self):
        """Gets the parent_refs of this V1alpha1ResourceNode.  # noqa: E501


        :return: The parent_refs of this V1alpha1ResourceNode.  # noqa: E501
        :rtype: list[V1alpha1ResourceRef]
        """
        return self._parent_refs

    @parent_refs.setter
    def parent_refs(self, parent_refs):
        """Sets the parent_refs of this V1alpha1ResourceNode.


        :param parent_refs: The parent_refs of this V1alpha1ResourceNode.  # noqa: E501
        :type: list[V1alpha1ResourceRef]
        """

        self._parent_refs = parent_refs

    @property
    def resource_version(self):
        """Gets the resource_version of this V1alpha1ResourceNode.  # noqa: E501


        :return: The resource_version of this V1alpha1ResourceNode.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this V1alpha1ResourceNode.


        :param resource_version: The resource_version of this V1alpha1ResourceNode.  # noqa: E501
        :type: str
        """

        self._resource_version = resource_version

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
        if issubclass(V1alpha1ResourceNode, dict):
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
        if not isinstance(other, V1alpha1ResourceNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
