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

class ApplicationApplicationRollbackRequest(object):
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
        'app_namespace': 'str',
        'dry_run': 'bool',
        'id': 'int',
        'name': 'str',
        'project': 'str',
        'prune': 'bool'
    }

    attribute_map = {
        'app_namespace': 'appNamespace',
        'dry_run': 'dryRun',
        'id': 'id',
        'name': 'name',
        'project': 'project',
        'prune': 'prune'
    }

    def __init__(self, app_namespace=None, dry_run=None, id=None, name=None, project=None, prune=None):  # noqa: E501
        """ApplicationApplicationRollbackRequest - a model defined in Swagger"""  # noqa: E501
        self._app_namespace = None
        self._dry_run = None
        self._id = None
        self._name = None
        self._project = None
        self._prune = None
        self.discriminator = None
        if app_namespace is not None:
            self.app_namespace = app_namespace
        if dry_run is not None:
            self.dry_run = dry_run
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project is not None:
            self.project = project
        if prune is not None:
            self.prune = prune

    @property
    def app_namespace(self):
        """Gets the app_namespace of this ApplicationApplicationRollbackRequest.  # noqa: E501


        :return: The app_namespace of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_namespace

    @app_namespace.setter
    def app_namespace(self, app_namespace):
        """Sets the app_namespace of this ApplicationApplicationRollbackRequest.


        :param app_namespace: The app_namespace of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :type: str
        """

        self._app_namespace = app_namespace

    @property
    def dry_run(self):
        """Gets the dry_run of this ApplicationApplicationRollbackRequest.  # noqa: E501


        :return: The dry_run of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this ApplicationApplicationRollbackRequest.


        :param dry_run: The dry_run of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def id(self):
        """Gets the id of this ApplicationApplicationRollbackRequest.  # noqa: E501


        :return: The id of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationApplicationRollbackRequest.


        :param id: The id of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApplicationApplicationRollbackRequest.  # noqa: E501


        :return: The name of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationApplicationRollbackRequest.


        :param name: The name of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project(self):
        """Gets the project of this ApplicationApplicationRollbackRequest.  # noqa: E501


        :return: The project of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ApplicationApplicationRollbackRequest.


        :param project: The project of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def prune(self):
        """Gets the prune of this ApplicationApplicationRollbackRequest.  # noqa: E501


        :return: The prune of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :rtype: bool
        """
        return self._prune

    @prune.setter
    def prune(self, prune):
        """Sets the prune of this ApplicationApplicationRollbackRequest.


        :param prune: The prune of this ApplicationApplicationRollbackRequest.  # noqa: E501
        :type: bool
        """

        self._prune = prune

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
        if issubclass(ApplicationApplicationRollbackRequest, dict):
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
        if not isinstance(other, ApplicationApplicationRollbackRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other