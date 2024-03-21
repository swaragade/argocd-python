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

class V1Event(object):
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
        'action': 'str',
        'count': 'int',
        'event_time': 'V1MicroTime',
        'first_timestamp': 'V1Time',
        'involved_object': 'V1ObjectReference',
        'last_timestamp': 'V1Time',
        'message': 'str',
        'metadata': 'V1ObjectMeta',
        'reason': 'str',
        'related': 'V1ObjectReference',
        'reporting_component': 'str',
        'reporting_instance': 'str',
        'series': 'V1EventSeries',
        'source': 'V1EventSource',
        'type': 'str'
    }

    attribute_map = {
        'action': 'action',
        'count': 'count',
        'event_time': 'eventTime',
        'first_timestamp': 'firstTimestamp',
        'involved_object': 'involvedObject',
        'last_timestamp': 'lastTimestamp',
        'message': 'message',
        'metadata': 'metadata',
        'reason': 'reason',
        'related': 'related',
        'reporting_component': 'reportingComponent',
        'reporting_instance': 'reportingInstance',
        'series': 'series',
        'source': 'source',
        'type': 'type'
    }

    def __init__(self, action=None, count=None, event_time=None, first_timestamp=None, involved_object=None, last_timestamp=None, message=None, metadata=None, reason=None, related=None, reporting_component=None, reporting_instance=None, series=None, source=None, type=None):  # noqa: E501
        """V1Event - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._count = None
        self._event_time = None
        self._first_timestamp = None
        self._involved_object = None
        self._last_timestamp = None
        self._message = None
        self._metadata = None
        self._reason = None
        self._related = None
        self._reporting_component = None
        self._reporting_instance = None
        self._series = None
        self._source = None
        self._type = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if count is not None:
            self.count = count
        if event_time is not None:
            self.event_time = event_time
        if first_timestamp is not None:
            self.first_timestamp = first_timestamp
        if involved_object is not None:
            self.involved_object = involved_object
        if last_timestamp is not None:
            self.last_timestamp = last_timestamp
        if message is not None:
            self.message = message
        if metadata is not None:
            self.metadata = metadata
        if reason is not None:
            self.reason = reason
        if related is not None:
            self.related = related
        if reporting_component is not None:
            self.reporting_component = reporting_component
        if reporting_instance is not None:
            self.reporting_instance = reporting_instance
        if series is not None:
            self.series = series
        if source is not None:
            self.source = source
        if type is not None:
            self.type = type

    @property
    def action(self):
        """Gets the action of this V1Event.  # noqa: E501


        :return: The action of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this V1Event.


        :param action: The action of this V1Event.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def count(self):
        """Gets the count of this V1Event.  # noqa: E501


        :return: The count of this V1Event.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this V1Event.


        :param count: The count of this V1Event.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def event_time(self):
        """Gets the event_time of this V1Event.  # noqa: E501


        :return: The event_time of this V1Event.  # noqa: E501
        :rtype: V1MicroTime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this V1Event.


        :param event_time: The event_time of this V1Event.  # noqa: E501
        :type: V1MicroTime
        """

        self._event_time = event_time

    @property
    def first_timestamp(self):
        """Gets the first_timestamp of this V1Event.  # noqa: E501


        :return: The first_timestamp of this V1Event.  # noqa: E501
        :rtype: V1Time
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp):
        """Sets the first_timestamp of this V1Event.


        :param first_timestamp: The first_timestamp of this V1Event.  # noqa: E501
        :type: V1Time
        """

        self._first_timestamp = first_timestamp

    @property
    def involved_object(self):
        """Gets the involved_object of this V1Event.  # noqa: E501


        :return: The involved_object of this V1Event.  # noqa: E501
        :rtype: V1ObjectReference
        """
        return self._involved_object

    @involved_object.setter
    def involved_object(self, involved_object):
        """Sets the involved_object of this V1Event.


        :param involved_object: The involved_object of this V1Event.  # noqa: E501
        :type: V1ObjectReference
        """

        self._involved_object = involved_object

    @property
    def last_timestamp(self):
        """Gets the last_timestamp of this V1Event.  # noqa: E501


        :return: The last_timestamp of this V1Event.  # noqa: E501
        :rtype: V1Time
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        """Sets the last_timestamp of this V1Event.


        :param last_timestamp: The last_timestamp of this V1Event.  # noqa: E501
        :type: V1Time
        """

        self._last_timestamp = last_timestamp

    @property
    def message(self):
        """Gets the message of this V1Event.  # noqa: E501


        :return: The message of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1Event.


        :param message: The message of this V1Event.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def metadata(self):
        """Gets the metadata of this V1Event.  # noqa: E501


        :return: The metadata of this V1Event.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1Event.


        :param metadata: The metadata of this V1Event.  # noqa: E501
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def reason(self):
        """Gets the reason of this V1Event.  # noqa: E501


        :return: The reason of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1Event.


        :param reason: The reason of this V1Event.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def related(self):
        """Gets the related of this V1Event.  # noqa: E501


        :return: The related of this V1Event.  # noqa: E501
        :rtype: V1ObjectReference
        """
        return self._related

    @related.setter
    def related(self, related):
        """Sets the related of this V1Event.


        :param related: The related of this V1Event.  # noqa: E501
        :type: V1ObjectReference
        """

        self._related = related

    @property
    def reporting_component(self):
        """Gets the reporting_component of this V1Event.  # noqa: E501


        :return: The reporting_component of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._reporting_component

    @reporting_component.setter
    def reporting_component(self, reporting_component):
        """Sets the reporting_component of this V1Event.


        :param reporting_component: The reporting_component of this V1Event.  # noqa: E501
        :type: str
        """

        self._reporting_component = reporting_component

    @property
    def reporting_instance(self):
        """Gets the reporting_instance of this V1Event.  # noqa: E501


        :return: The reporting_instance of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._reporting_instance

    @reporting_instance.setter
    def reporting_instance(self, reporting_instance):
        """Sets the reporting_instance of this V1Event.


        :param reporting_instance: The reporting_instance of this V1Event.  # noqa: E501
        :type: str
        """

        self._reporting_instance = reporting_instance

    @property
    def series(self):
        """Gets the series of this V1Event.  # noqa: E501


        :return: The series of this V1Event.  # noqa: E501
        :rtype: V1EventSeries
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this V1Event.


        :param series: The series of this V1Event.  # noqa: E501
        :type: V1EventSeries
        """

        self._series = series

    @property
    def source(self):
        """Gets the source of this V1Event.  # noqa: E501


        :return: The source of this V1Event.  # noqa: E501
        :rtype: V1EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this V1Event.


        :param source: The source of this V1Event.  # noqa: E501
        :type: V1EventSource
        """

        self._source = source

    @property
    def type(self):
        """Gets the type of this V1Event.  # noqa: E501


        :return: The type of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1Event.


        :param type: The type of this V1Event.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(V1Event, dict):
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
        if not isinstance(other, V1Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
