# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TaskCommon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TaskCommon.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10TaskCommon.proto\"4\n\x06Status\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x0b.StatusCode\x12\x0f\n\x07message\x18\x02 \x01(\t*\x1f\n\nStatusCode\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x62\x06proto3')
)

_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=74,
  serialized_end=105,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
OK = 0
ERROR = 1



_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='Status.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='Status.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=72,
)

_STATUS.fields_by_name['code'].enum_type = _STATUSCODE
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'TaskCommon_pb2'
  # @@protoc_insertion_point(class_scope:Status)
  ))
_sym_db.RegisterMessage(Status)


# @@protoc_insertion_point(module_scope)
