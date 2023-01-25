from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
GetImage: CommandType
GetSourceInfo: CommandType
NoNew: CommandType
Resume: CommandType
Stop: CommandType
StopAndShutdown: CommandType

class CommandList(_message.Message):
    __slots__ = ["commands", "serverTimestamp"]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    SERVERTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedScalarFieldContainer[CommandType]
    serverTimestamp: _timestamp_pb2.Timestamp
    def __init__(self, serverTimestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., commands: _Optional[_Iterable[_Union[CommandType, str]]] = ...) -> None: ...

class CommandRequest(_message.Message):
    __slots__ = ["clientTimestamp", "connectorHostname"]
    CLIENTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONNECTORHOSTNAME_FIELD_NUMBER: _ClassVar[int]
    clientTimestamp: _timestamp_pb2.Timestamp
    connectorHostname: str
    def __init__(self, clientTimestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., connectorHostname: _Optional[str] = ...) -> None: ...

class ServerAckResponse(_message.Message):
    __slots__ = ["serverTimestamp"]
    SERVERTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    serverTimestamp: _timestamp_pb2.Timestamp
    def __init__(self, serverTimestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SourceInfoRequest(_message.Message):
    __slots__ = ["clientTimestamp", "sourceInfo"]
    CLIENTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SOURCEINFO_FIELD_NUMBER: _ClassVar[int]
    clientTimestamp: _timestamp_pb2.Timestamp
    sourceInfo: str
    def __init__(self, clientTimestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sourceInfo: _Optional[str] = ...) -> None: ...

class TransferImageRequest(_message.Message):
    __slots__ = ["camera_id", "clientTimestamp", "image"]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    camera_id: int
    clientTimestamp: _timestamp_pb2.Timestamp
    image: bytes
    def __init__(self, clientTimestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., camera_id: _Optional[int] = ..., image: _Optional[bytes] = ...) -> None: ...

class CommandType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
