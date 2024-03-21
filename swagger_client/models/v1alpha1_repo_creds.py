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

class V1alpha1RepoCreds(object):
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
        'enable_oci': 'bool',
        'force_http_basic_auth': 'bool',
        'gcp_service_account_key': 'str',
        'github_app_enterprise_base_url': 'str',
        'github_app_id': 'int',
        'github_app_installation_id': 'int',
        'github_app_private_key': 'str',
        'password': 'str',
        'proxy': 'str',
        'ssh_private_key': 'str',
        'tls_client_cert_data': 'str',
        'tls_client_cert_key': 'str',
        'type': 'str',
        'url': 'str',
        'username': 'str'
    }

    attribute_map = {
        'enable_oci': 'enableOCI',
        'force_http_basic_auth': 'forceHttpBasicAuth',
        'gcp_service_account_key': 'gcpServiceAccountKey',
        'github_app_enterprise_base_url': 'githubAppEnterpriseBaseUrl',
        'github_app_id': 'githubAppID',
        'github_app_installation_id': 'githubAppInstallationID',
        'github_app_private_key': 'githubAppPrivateKey',
        'password': 'password',
        'proxy': 'proxy',
        'ssh_private_key': 'sshPrivateKey',
        'tls_client_cert_data': 'tlsClientCertData',
        'tls_client_cert_key': 'tlsClientCertKey',
        'type': 'type',
        'url': 'url',
        'username': 'username'
    }

    def __init__(self, enable_oci=None, force_http_basic_auth=None, gcp_service_account_key=None, github_app_enterprise_base_url=None, github_app_id=None, github_app_installation_id=None, github_app_private_key=None, password=None, proxy=None, ssh_private_key=None, tls_client_cert_data=None, tls_client_cert_key=None, type=None, url=None, username=None):  # noqa: E501
        """V1alpha1RepoCreds - a model defined in Swagger"""  # noqa: E501
        self._enable_oci = None
        self._force_http_basic_auth = None
        self._gcp_service_account_key = None
        self._github_app_enterprise_base_url = None
        self._github_app_id = None
        self._github_app_installation_id = None
        self._github_app_private_key = None
        self._password = None
        self._proxy = None
        self._ssh_private_key = None
        self._tls_client_cert_data = None
        self._tls_client_cert_key = None
        self._type = None
        self._url = None
        self._username = None
        self.discriminator = None
        if enable_oci is not None:
            self.enable_oci = enable_oci
        if force_http_basic_auth is not None:
            self.force_http_basic_auth = force_http_basic_auth
        if gcp_service_account_key is not None:
            self.gcp_service_account_key = gcp_service_account_key
        if github_app_enterprise_base_url is not None:
            self.github_app_enterprise_base_url = github_app_enterprise_base_url
        if github_app_id is not None:
            self.github_app_id = github_app_id
        if github_app_installation_id is not None:
            self.github_app_installation_id = github_app_installation_id
        if github_app_private_key is not None:
            self.github_app_private_key = github_app_private_key
        if password is not None:
            self.password = password
        if proxy is not None:
            self.proxy = proxy
        if ssh_private_key is not None:
            self.ssh_private_key = ssh_private_key
        if tls_client_cert_data is not None:
            self.tls_client_cert_data = tls_client_cert_data
        if tls_client_cert_key is not None:
            self.tls_client_cert_key = tls_client_cert_key
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if username is not None:
            self.username = username

    @property
    def enable_oci(self):
        """Gets the enable_oci of this V1alpha1RepoCreds.  # noqa: E501


        :return: The enable_oci of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: bool
        """
        return self._enable_oci

    @enable_oci.setter
    def enable_oci(self, enable_oci):
        """Sets the enable_oci of this V1alpha1RepoCreds.


        :param enable_oci: The enable_oci of this V1alpha1RepoCreds.  # noqa: E501
        :type: bool
        """

        self._enable_oci = enable_oci

    @property
    def force_http_basic_auth(self):
        """Gets the force_http_basic_auth of this V1alpha1RepoCreds.  # noqa: E501


        :return: The force_http_basic_auth of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: bool
        """
        return self._force_http_basic_auth

    @force_http_basic_auth.setter
    def force_http_basic_auth(self, force_http_basic_auth):
        """Sets the force_http_basic_auth of this V1alpha1RepoCreds.


        :param force_http_basic_auth: The force_http_basic_auth of this V1alpha1RepoCreds.  # noqa: E501
        :type: bool
        """

        self._force_http_basic_auth = force_http_basic_auth

    @property
    def gcp_service_account_key(self):
        """Gets the gcp_service_account_key of this V1alpha1RepoCreds.  # noqa: E501


        :return: The gcp_service_account_key of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: str
        """
        return self._gcp_service_account_key

    @gcp_service_account_key.setter
    def gcp_service_account_key(self, gcp_service_account_key):
        """Sets the gcp_service_account_key of this V1alpha1RepoCreds.


        :param gcp_service_account_key: The gcp_service_account_key of this V1alpha1RepoCreds.  # noqa: E501
        :type: str
        """

        self._gcp_service_account_key = gcp_service_account_key

    @property
    def github_app_enterprise_base_url(self):
        """Gets the github_app_enterprise_base_url of this V1alpha1RepoCreds.  # noqa: E501


        :return: The github_app_enterprise_base_url of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: str
        """
        return self._github_app_enterprise_base_url

    @github_app_enterprise_base_url.setter
    def github_app_enterprise_base_url(self, github_app_enterprise_base_url):
        """Sets the github_app_enterprise_base_url of this V1alpha1RepoCreds.


        :param github_app_enterprise_base_url: The github_app_enterprise_base_url of this V1alpha1RepoCreds.  # noqa: E501
        :type: str
        """

        self._github_app_enterprise_base_url = github_app_enterprise_base_url

    @property
    def github_app_id(self):
        """Gets the github_app_id of this V1alpha1RepoCreds.  # noqa: E501


        :return: The github_app_id of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: int
        """
        return self._github_app_id

    @github_app_id.setter
    def github_app_id(self, github_app_id):
        """Sets the github_app_id of this V1alpha1RepoCreds.


        :param github_app_id: The github_app_id of this V1alpha1RepoCreds.  # noqa: E501
        :type: int
        """

        self._github_app_id = github_app_id

    @property
    def github_app_installation_id(self):
        """Gets the github_app_installation_id of this V1alpha1RepoCreds.  # noqa: E501


        :return: The github_app_installation_id of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: int
        """
        return self._github_app_installation_id

    @github_app_installation_id.setter
    def github_app_installation_id(self, github_app_installation_id):
        """Sets the github_app_installation_id of this V1alpha1RepoCreds.


        :param github_app_installation_id: The github_app_installation_id of this V1alpha1RepoCreds.  # noqa: E501
        :type: int
        """

        self._github_app_installation_id = github_app_installation_id

    @property
    def github_app_private_key(self):
        """Gets the github_app_private_key of this V1alpha1RepoCreds.  # noqa: E501


        :return: The github_app_private_key of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: str
        """
        return self._github_app_private_key

    @github_app_private_key.setter
    def github_app_private_key(self, github_app_private_key):
        """Sets the github_app_private_key of this V1alpha1RepoCreds.


        :param github_app_private_key: The github_app_private_key of this V1alpha1RepoCreds.  # noqa: E501
        :type: str
        """

        self._github_app_private_key = github_app_private_key

    @property
    def password(self):
        """Gets the password of this V1alpha1RepoCreds.  # noqa: E501


        :return: The password of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this V1alpha1RepoCreds.


        :param password: The password of this V1alpha1RepoCreds.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def proxy(self):
        """Gets the proxy of this V1alpha1RepoCreds.  # noqa: E501


        :return: The proxy of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this V1alpha1RepoCreds.


        :param proxy: The proxy of this V1alpha1RepoCreds.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    @property
    def ssh_private_key(self):
        """Gets the ssh_private_key of this V1alpha1RepoCreds.  # noqa: E501


        :return: The ssh_private_key of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: str
        """
        return self._ssh_private_key

    @ssh_private_key.setter
    def ssh_private_key(self, ssh_private_key):
        """Sets the ssh_private_key of this V1alpha1RepoCreds.


        :param ssh_private_key: The ssh_private_key of this V1alpha1RepoCreds.  # noqa: E501
        :type: str
        """

        self._ssh_private_key = ssh_private_key

    @property
    def tls_client_cert_data(self):
        """Gets the tls_client_cert_data of this V1alpha1RepoCreds.  # noqa: E501


        :return: The tls_client_cert_data of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: str
        """
        return self._tls_client_cert_data

    @tls_client_cert_data.setter
    def tls_client_cert_data(self, tls_client_cert_data):
        """Sets the tls_client_cert_data of this V1alpha1RepoCreds.


        :param tls_client_cert_data: The tls_client_cert_data of this V1alpha1RepoCreds.  # noqa: E501
        :type: str
        """

        self._tls_client_cert_data = tls_client_cert_data

    @property
    def tls_client_cert_key(self):
        """Gets the tls_client_cert_key of this V1alpha1RepoCreds.  # noqa: E501


        :return: The tls_client_cert_key of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: str
        """
        return self._tls_client_cert_key

    @tls_client_cert_key.setter
    def tls_client_cert_key(self, tls_client_cert_key):
        """Sets the tls_client_cert_key of this V1alpha1RepoCreds.


        :param tls_client_cert_key: The tls_client_cert_key of this V1alpha1RepoCreds.  # noqa: E501
        :type: str
        """

        self._tls_client_cert_key = tls_client_cert_key

    @property
    def type(self):
        """Gets the type of this V1alpha1RepoCreds.  # noqa: E501

        Type specifies the type of the repoCreds. Can be either \"git\" or \"helm. \"git\" is assumed if empty or absent.  # noqa: E501

        :return: The type of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1alpha1RepoCreds.

        Type specifies the type of the repoCreds. Can be either \"git\" or \"helm. \"git\" is assumed if empty or absent.  # noqa: E501

        :param type: The type of this V1alpha1RepoCreds.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this V1alpha1RepoCreds.  # noqa: E501


        :return: The url of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V1alpha1RepoCreds.


        :param url: The url of this V1alpha1RepoCreds.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def username(self):
        """Gets the username of this V1alpha1RepoCreds.  # noqa: E501


        :return: The username of this V1alpha1RepoCreds.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this V1alpha1RepoCreds.


        :param username: The username of this V1alpha1RepoCreds.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(V1alpha1RepoCreds, dict):
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
        if not isinstance(other, V1alpha1RepoCreds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
