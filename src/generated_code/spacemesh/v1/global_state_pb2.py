# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spacemesh/v1/global_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from src.generated_code.spacemesh.v1 import global_state_types_pb2 as spacemesh_dot_v1_dot_global__state__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fspacemesh/v1/global_state.proto\x12\x0cspacemesh.v1\x1a%spacemesh/v1/global_state_types.proto2\x9f\x06\n\x12GlobalStateService\x12^\n\x0fGlobalStateHash\x12$.spacemesh.v1.GlobalStateHashRequest\x1a%.spacemesh.v1.GlobalStateHashResponse\x12\x46\n\x07\x41\x63\x63ount\x12\x1c.spacemesh.v1.AccountRequest\x1a\x1d.spacemesh.v1.AccountResponse\x12\x61\n\x10\x41\x63\x63ountDataQuery\x12%.spacemesh.v1.AccountDataQueryRequest\x1a&.spacemesh.v1.AccountDataQueryResponse\x12\x61\n\x10SmesherDataQuery\x12%.spacemesh.v1.SmesherDataQueryRequest\x1a&.spacemesh.v1.SmesherDataQueryResponse\x12\x66\n\x11\x41\x63\x63ountDataStream\x12&.spacemesh.v1.AccountDataStreamRequest\x1a\'.spacemesh.v1.AccountDataStreamResponse0\x01\x12l\n\x13SmesherRewardStream\x12(.spacemesh.v1.SmesherRewardStreamRequest\x1a).spacemesh.v1.SmesherRewardStreamResponse0\x01\x12]\n\x0e\x41ppEventStream\x12#.spacemesh.v1.AppEventStreamRequest\x1a$.spacemesh.v1.AppEventStreamResponse0\x01\x12\x66\n\x11GlobalStateStream\x12&.spacemesh.v1.GlobalStateStreamRequest\x1a\'.spacemesh.v1.GlobalStateStreamResponse0\x01\x42\x34Z2github.com/spacemeshos/api/release/go/spacemesh/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spacemesh.v1.global_state_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/spacemeshos/api/release/go/spacemesh/v1'
  _globals['_GLOBALSTATESERVICE']._serialized_start=89
  _globals['_GLOBALSTATESERVICE']._serialized_end=888
# @@protoc_insertion_point(module_scope)
