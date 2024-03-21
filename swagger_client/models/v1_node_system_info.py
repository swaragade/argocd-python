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

class V1NodeSystemInfo(object):
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
        'architecture': 'str',
        'boot_id': 'str',
        'container_runtime_version': 'str',
        'kernel_version': 'str',
        'kube_proxy_version': 'str',
        'kubelet_version': 'str',
        'machine_id': 'str',
        'operating_system': 'str',
        'os_image': 'str',
        'system_uuid': 'str'
    }

    attribute_map = {
        'architecture': 'architecture',
        'boot_id': 'bootID',
        'container_runtime_version': 'containerRuntimeVersion',
        'kernel_version': 'kernelVersion',
        'kube_proxy_version': 'kubeProxyVersion',
        'kubelet_version': 'kubeletVersion',
        'machine_id': 'machineID',
        'operating_system': 'operatingSystem',
        'os_image': 'osImage',
        'system_uuid': 'systemUUID'
    }

    def __init__(self, architecture=None, boot_id=None, container_runtime_version=None, kernel_version=None, kube_proxy_version=None, kubelet_version=None, machine_id=None, operating_system=None, os_image=None, system_uuid=None):  # noqa: E501
        """V1NodeSystemInfo - a model defined in Swagger"""  # noqa: E501
        self._architecture = None
        self._boot_id = None
        self._container_runtime_version = None
        self._kernel_version = None
        self._kube_proxy_version = None
        self._kubelet_version = None
        self._machine_id = None
        self._operating_system = None
        self._os_image = None
        self._system_uuid = None
        self.discriminator = None
        if architecture is not None:
            self.architecture = architecture
        if boot_id is not None:
            self.boot_id = boot_id
        if container_runtime_version is not None:
            self.container_runtime_version = container_runtime_version
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if kube_proxy_version is not None:
            self.kube_proxy_version = kube_proxy_version
        if kubelet_version is not None:
            self.kubelet_version = kubelet_version
        if machine_id is not None:
            self.machine_id = machine_id
        if operating_system is not None:
            self.operating_system = operating_system
        if os_image is not None:
            self.os_image = os_image
        if system_uuid is not None:
            self.system_uuid = system_uuid

    @property
    def architecture(self):
        """Gets the architecture of this V1NodeSystemInfo.  # noqa: E501


        :return: The architecture of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this V1NodeSystemInfo.


        :param architecture: The architecture of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._architecture = architecture

    @property
    def boot_id(self):
        """Gets the boot_id of this V1NodeSystemInfo.  # noqa: E501

        Boot ID reported by the node.  # noqa: E501

        :return: The boot_id of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._boot_id

    @boot_id.setter
    def boot_id(self, boot_id):
        """Sets the boot_id of this V1NodeSystemInfo.

        Boot ID reported by the node.  # noqa: E501

        :param boot_id: The boot_id of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._boot_id = boot_id

    @property
    def container_runtime_version(self):
        """Gets the container_runtime_version of this V1NodeSystemInfo.  # noqa: E501

        ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2).  # noqa: E501

        :return: The container_runtime_version of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._container_runtime_version

    @container_runtime_version.setter
    def container_runtime_version(self, container_runtime_version):
        """Sets the container_runtime_version of this V1NodeSystemInfo.

        ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2).  # noqa: E501

        :param container_runtime_version: The container_runtime_version of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._container_runtime_version = container_runtime_version

    @property
    def kernel_version(self):
        """Gets the kernel_version of this V1NodeSystemInfo.  # noqa: E501

        Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).  # noqa: E501

        :return: The kernel_version of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        """Sets the kernel_version of this V1NodeSystemInfo.

        Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).  # noqa: E501

        :param kernel_version: The kernel_version of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._kernel_version = kernel_version

    @property
    def kube_proxy_version(self):
        """Gets the kube_proxy_version of this V1NodeSystemInfo.  # noqa: E501

        KubeProxy Version reported by the node.  # noqa: E501

        :return: The kube_proxy_version of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._kube_proxy_version

    @kube_proxy_version.setter
    def kube_proxy_version(self, kube_proxy_version):
        """Sets the kube_proxy_version of this V1NodeSystemInfo.

        KubeProxy Version reported by the node.  # noqa: E501

        :param kube_proxy_version: The kube_proxy_version of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._kube_proxy_version = kube_proxy_version

    @property
    def kubelet_version(self):
        """Gets the kubelet_version of this V1NodeSystemInfo.  # noqa: E501

        Kubelet Version reported by the node.  # noqa: E501

        :return: The kubelet_version of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_version

    @kubelet_version.setter
    def kubelet_version(self, kubelet_version):
        """Sets the kubelet_version of this V1NodeSystemInfo.

        Kubelet Version reported by the node.  # noqa: E501

        :param kubelet_version: The kubelet_version of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._kubelet_version = kubelet_version

    @property
    def machine_id(self):
        """Gets the machine_id of this V1NodeSystemInfo.  # noqa: E501


        :return: The machine_id of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this V1NodeSystemInfo.


        :param machine_id: The machine_id of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._machine_id = machine_id

    @property
    def operating_system(self):
        """Gets the operating_system of this V1NodeSystemInfo.  # noqa: E501


        :return: The operating_system of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this V1NodeSystemInfo.


        :param operating_system: The operating_system of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._operating_system = operating_system

    @property
    def os_image(self):
        """Gets the os_image of this V1NodeSystemInfo.  # noqa: E501

        OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).  # noqa: E501

        :return: The os_image of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._os_image

    @os_image.setter
    def os_image(self, os_image):
        """Sets the os_image of this V1NodeSystemInfo.

        OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).  # noqa: E501

        :param os_image: The os_image of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._os_image = os_image

    @property
    def system_uuid(self):
        """Gets the system_uuid of this V1NodeSystemInfo.  # noqa: E501


        :return: The system_uuid of this V1NodeSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._system_uuid

    @system_uuid.setter
    def system_uuid(self, system_uuid):
        """Sets the system_uuid of this V1NodeSystemInfo.


        :param system_uuid: The system_uuid of this V1NodeSystemInfo.  # noqa: E501
        :type: str
        """

        self._system_uuid = system_uuid

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
        if issubclass(V1NodeSystemInfo, dict):
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
        if not isinstance(other, V1NodeSystemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
