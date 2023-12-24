# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spacemesh/v1/mesh.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from src.generated_code.spacemesh.v1 import mesh_types_pb2 as spacemesh_dot_v1_dot_mesh__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17spacemesh/v1/mesh.proto\x12\x0cspacemesh.v1\x1a\x1dspacemesh/v1/mesh_types.proto2\xb3\n\n\x0bMeshService\x12R\n\x0bGenesisTime\x12 .spacemesh.v1.GenesisTimeRequest\x1a!.spacemesh.v1.GenesisTimeResponse\x12U\n\x0c\x43urrentLayer\x12!.spacemesh.v1.CurrentLayerRequest\x1a\".spacemesh.v1.CurrentLayerResponse\x12U\n\x0c\x43urrentEpoch\x12!.spacemesh.v1.CurrentEpochRequest\x1a\".spacemesh.v1.CurrentEpochResponse\x12L\n\tGenesisID\x12\x1e.spacemesh.v1.GenesisIDRequest\x1a\x1f.spacemesh.v1.GenesisIDResponse\x12[\n\x0e\x45pochNumLayers\x12#.spacemesh.v1.EpochNumLayersRequest\x1a$.spacemesh.v1.EpochNumLayersResponse\x12X\n\rLayerDuration\x12\".spacemesh.v1.LayerDurationRequest\x1a#.spacemesh.v1.LayerDurationResponse\x12y\n\x18MaxTransactionsPerSecond\x12-.spacemesh.v1.MaxTransactionsPerSecondRequest\x1a..spacemesh.v1.MaxTransactionsPerSecondResponse\x12m\n\x14\x41\x63\x63ountMeshDataQuery\x12).spacemesh.v1.AccountMeshDataQueryRequest\x1a*.spacemesh.v1.AccountMeshDataQueryResponse\x12R\n\x0bLayersQuery\x12 .spacemesh.v1.LayersQueryRequest\x1a!.spacemesh.v1.LayersQueryResponse\x12r\n\x15\x41\x63\x63ountMeshDataStream\x12*.spacemesh.v1.AccountMeshDataStreamRequest\x1a+.spacemesh.v1.AccountMeshDataStreamResponse0\x01\x12T\n\x0bLayerStream\x12 .spacemesh.v1.LayerStreamRequest\x1a!.spacemesh.v1.LayerStreamResponse0\x01\x12T\n\x0b\x45pochStream\x12 .spacemesh.v1.EpochStreamRequest\x1a!.spacemesh.v1.EpochStreamResponse0\x01\x12W\n\x10MalfeasanceQuery\x12 .spacemesh.v1.MalfeasanceRequest\x1a!.spacemesh.v1.MalfeasanceResponse\x12\x66\n\x11MalfeasanceStream\x12&.spacemesh.v1.MalfeasanceStreamRequest\x1a\'.spacemesh.v1.MalfeasanceStreamResponse0\x01\x42\x34Z2github.com/spacemeshos/api/release/go/spacemesh/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spacemesh.v1.mesh_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/spacemeshos/api/release/go/spacemesh/v1'
  _globals['_MESHSERVICE']._serialized_start=73
  _globals['_MESHSERVICE']._serialized_end=1404
# @@protoc_insertion_point(module_scope)