# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spacemesh/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from src.generated_code.spacemesh.v1 import tx_types_pb2 as spacemesh_dot_v1_dot_tx__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15spacemesh/v1/tx.proto\x12\x0cspacemesh.v1\x1a\x1bspacemesh/v1/tx_types.proto2\x9a\x04\n\x12TransactionService\x12\x64\n\x11SubmitTransaction\x12&.spacemesh.v1.SubmitTransactionRequest\x1a\'.spacemesh.v1.SubmitTransactionResponse\x12\x61\n\x10ParseTransaction\x12%.spacemesh.v1.ParseTransactionRequest\x1a&.spacemesh.v1.ParseTransactionResponse\x12\x64\n\x11TransactionsState\x12&.spacemesh.v1.TransactionsStateRequest\x1a\'.spacemesh.v1.TransactionsStateResponse\x12x\n\x17TransactionsStateStream\x12,.spacemesh.v1.TransactionsStateStreamRequest\x1a-.spacemesh.v1.TransactionsStateStreamResponse0\x01\x12[\n\rStreamResults\x12\'.spacemesh.v1.TransactionResultsRequest\x1a\x1f.spacemesh.v1.TransactionResult0\x01\x42\x34Z2github.com/spacemeshos/api/release/go/spacemesh/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spacemesh.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/spacemeshos/api/release/go/spacemesh/v1'
  _globals['_TRANSACTIONSERVICE']._serialized_start=69
  _globals['_TRANSACTIONSERVICE']._serialized_end=607
# @@protoc_insertion_point(module_scope)
