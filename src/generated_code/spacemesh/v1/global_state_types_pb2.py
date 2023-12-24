# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spacemesh/v1/global_state_types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from src.generated_code.spacemesh.v1 import types_pb2 as spacemesh_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%spacemesh/v1/global_state_types.proto\x12\x0cspacemesh.v1\x1a\x18spacemesh/v1/types.proto\"F\n\x0c\x41\x63\x63ountState\x12\x0f\n\x07\x63ounter\x18\x01 \x01(\x04\x12%\n\x07\x62\x61lance\x18\x02 \x01(\x0b\x32\x14.spacemesh.v1.Amount\"\x9e\x01\n\x07\x41\x63\x63ount\x12+\n\naccount_id\x18\x01 \x01(\x0b\x32\x17.spacemesh.v1.AccountId\x12\x31\n\rstate_current\x18\x02 \x01(\x0b\x32\x1a.spacemesh.v1.AccountState\x12\x33\n\x0fstate_projected\x18\x03 \x01(\x0b\x32\x1a.spacemesh.v1.AccountState\"=\n\x0e\x41\x63\x63ountRequest\x12+\n\naccount_id\x18\x01 \x01(\x0b\x32\x17.spacemesh.v1.AccountId\"A\n\x0f\x41\x63\x63ountResponse\x12.\n\x0f\x61\x63\x63ount_wrapper\x18\x01 \x01(\x0b\x32\x15.spacemesh.v1.Account\"\\\n\x11\x41\x63\x63ountDataFilter\x12+\n\naccount_id\x18\x01 \x01(\x0b\x32\x17.spacemesh.v1.AccountId\x12\x1a\n\x12\x61\x63\x63ount_data_flags\x18\x02 \x01(\r\"K\n\x18\x41\x63\x63ountDataStreamRequest\x12/\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x1f.spacemesh.v1.AccountDataFilter\"E\n\x19\x41\x63\x63ountDataStreamResponse\x12(\n\x05\x64\x61tum\x18\x01 \x01(\x0b\x32\x19.spacemesh.v1.AccountData\"o\n\x17\x41\x63\x63ountDataQueryRequest\x12/\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x1f.spacemesh.v1.AccountDataFilter\x12\x13\n\x0bmax_results\x18\x02 \x01(\r\x12\x0e\n\x06offset\x18\x03 \x01(\r\"\xfe\x03\n\x12TransactionReceipt\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.spacemesh.v1.TransactionId\x12\x42\n\x06result\x18\x02 \x01(\x0e\x32\x32.spacemesh.v1.TransactionReceipt.TransactionResult\x12\x10\n\x08gas_used\x18\x03 \x01(\x04\x12!\n\x03\x66\x65\x65\x18\x04 \x01(\x0b\x32\x14.spacemesh.v1.Amount\x12(\n\x05layer\x18\x05 \x01(\x0b\x32\x19.spacemesh.v1.LayerNumber\x12\r\n\x05index\x18\x06 \x01(\r\x12\x10\n\x08svm_data\x18\x07 \x01(\x0c\"\xfa\x01\n\x11TransactionResult\x12\"\n\x1eTRANSACTION_RESULT_UNSPECIFIED\x10\x00\x12\x1f\n\x1bTRANSACTION_RESULT_EXECUTED\x10\x01\x12\"\n\x1eTRANSACTION_RESULT_BAD_COUNTER\x10\x02\x12(\n$TRANSACTION_RESULT_RUNTIME_EXCEPTION\x10\x03\x12\'\n#TRANSACTION_RESULT_INSUFFICIENT_GAS\x10\x04\x12)\n%TRANSACTION_RESULT_INSUFFICIENT_FUNDS\x10\x05\"\xa5\x01\n\x0b\x41\x63\x63ountData\x12&\n\x06reward\x18\x01 \x01(\x0b\x32\x14.spacemesh.v1.RewardH\x00\x12\x33\n\x07receipt\x18\x02 \x01(\x0b\x32 .spacemesh.v1.TransactionReceiptH\x00\x12\x30\n\x0f\x61\x63\x63ount_wrapper\x18\x03 \x01(\x0b\x32\x15.spacemesh.v1.AccountH\x00\x42\x07\n\x05\x64\x61tum\"b\n\x18\x41\x63\x63ountDataQueryResponse\x12\x15\n\rtotal_results\x18\x01 \x01(\r\x12/\n\x0c\x61\x63\x63ount_item\x18\x02 \x03(\x0b\x32\x19.spacemesh.v1.AccountData\"A\n\x1aSmesherRewardStreamRequest\x12#\n\x02id\x18\x01 \x01(\x0b\x32\x17.spacemesh.v1.SmesherId\"C\n\x1bSmesherRewardStreamResponse\x12$\n\x06reward\x18\x01 \x01(\x0b\x32\x14.spacemesh.v1.Reward\"k\n\x17SmesherDataQueryRequest\x12+\n\nsmesher_id\x18\x01 \x01(\x0b\x32\x17.spacemesh.v1.SmesherId\x12\x13\n\x0bmax_results\x18\x02 \x01(\r\x12\x0e\n\x06offset\x18\x03 \x01(\r\"X\n\x18SmesherDataQueryResponse\x12\x15\n\rtotal_results\x18\x01 \x01(\r\x12%\n\x07rewards\x18\x02 \x03(\x0b\x32\x14.spacemesh.v1.Reward\"N\n\x0fGlobalStateHash\x12\x11\n\troot_hash\x18\x01 \x01(\x0c\x12(\n\x05layer\x18\x02 \x01(\x0b\x32\x19.spacemesh.v1.LayerNumber\"\x18\n\x16GlobalStateHashRequest\"J\n\x17GlobalStateHashResponse\x12/\n\x08response\x18\x01 \x01(\x0b\x32\x1d.spacemesh.v1.GlobalStateHash\";\n\x18GlobalStateStreamRequest\x12\x1f\n\x17global_state_data_flags\x18\x01 \x01(\r\"\xe0\x01\n\x0fGlobalStateData\x12&\n\x06reward\x18\x01 \x01(\x0b\x32\x14.spacemesh.v1.RewardH\x00\x12\x33\n\x07receipt\x18\x02 \x01(\x0b\x32 .spacemesh.v1.TransactionReceiptH\x00\x12\x30\n\x0f\x61\x63\x63ount_wrapper\x18\x03 \x01(\x0b\x32\x15.spacemesh.v1.AccountH\x00\x12\x35\n\x0cglobal_state\x18\x04 \x01(\x0b\x32\x1d.spacemesh.v1.GlobalStateHashH\x00\x42\x07\n\x05\x64\x61tum\"I\n\x19GlobalStateStreamResponse\x12,\n\x05\x64\x61tum\x18\x01 \x01(\x0b\x32\x1d.spacemesh.v1.GlobalStateData\"\x17\n\x15\x41ppEventStreamRequest\"?\n\x16\x41ppEventStreamResponse\x12%\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x16.spacemesh.v1.AppEvent*\x9c\x01\n\x0f\x41\x63\x63ountDataFlag\x12!\n\x1d\x41\x43\x43OUNT_DATA_FLAG_UNSPECIFIED\x10\x00\x12)\n%ACCOUNT_DATA_FLAG_TRANSACTION_RECEIPT\x10\x01\x12\x1c\n\x18\x41\x43\x43OUNT_DATA_FLAG_REWARD\x10\x02\x12\x1d\n\x19\x41\x43\x43OUNT_DATA_FLAG_ACCOUNT\x10\x04*\xe2\x01\n\x13GlobalStateDataFlag\x12&\n\"GLOBAL_STATE_DATA_FLAG_UNSPECIFIED\x10\x00\x12.\n*GLOBAL_STATE_DATA_FLAG_TRANSACTION_RECEIPT\x10\x01\x12!\n\x1dGLOBAL_STATE_DATA_FLAG_REWARD\x10\x02\x12\"\n\x1eGLOBAL_STATE_DATA_FLAG_ACCOUNT\x10\x04\x12,\n(GLOBAL_STATE_DATA_FLAG_GLOBAL_STATE_HASH\x10\x08\x42\x34Z2github.com/spacemeshos/api/release/go/spacemesh/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spacemesh.v1.global_state_types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/spacemeshos/api/release/go/spacemesh/v1'
  _globals['_ACCOUNTDATAFLAG']._serialized_start=2551
  _globals['_ACCOUNTDATAFLAG']._serialized_end=2707
  _globals['_GLOBALSTATEDATAFLAG']._serialized_start=2710
  _globals['_GLOBALSTATEDATAFLAG']._serialized_end=2936
  _globals['_ACCOUNTSTATE']._serialized_start=81
  _globals['_ACCOUNTSTATE']._serialized_end=151
  _globals['_ACCOUNT']._serialized_start=154
  _globals['_ACCOUNT']._serialized_end=312
  _globals['_ACCOUNTREQUEST']._serialized_start=314
  _globals['_ACCOUNTREQUEST']._serialized_end=375
  _globals['_ACCOUNTRESPONSE']._serialized_start=377
  _globals['_ACCOUNTRESPONSE']._serialized_end=442
  _globals['_ACCOUNTDATAFILTER']._serialized_start=444
  _globals['_ACCOUNTDATAFILTER']._serialized_end=536
  _globals['_ACCOUNTDATASTREAMREQUEST']._serialized_start=538
  _globals['_ACCOUNTDATASTREAMREQUEST']._serialized_end=613
  _globals['_ACCOUNTDATASTREAMRESPONSE']._serialized_start=615
  _globals['_ACCOUNTDATASTREAMRESPONSE']._serialized_end=684
  _globals['_ACCOUNTDATAQUERYREQUEST']._serialized_start=686
  _globals['_ACCOUNTDATAQUERYREQUEST']._serialized_end=797
  _globals['_TRANSACTIONRECEIPT']._serialized_start=800
  _globals['_TRANSACTIONRECEIPT']._serialized_end=1310
  _globals['_TRANSACTIONRECEIPT_TRANSACTIONRESULT']._serialized_start=1060
  _globals['_TRANSACTIONRECEIPT_TRANSACTIONRESULT']._serialized_end=1310
  _globals['_ACCOUNTDATA']._serialized_start=1313
  _globals['_ACCOUNTDATA']._serialized_end=1478
  _globals['_ACCOUNTDATAQUERYRESPONSE']._serialized_start=1480
  _globals['_ACCOUNTDATAQUERYRESPONSE']._serialized_end=1578
  _globals['_SMESHERREWARDSTREAMREQUEST']._serialized_start=1580
  _globals['_SMESHERREWARDSTREAMREQUEST']._serialized_end=1645
  _globals['_SMESHERREWARDSTREAMRESPONSE']._serialized_start=1647
  _globals['_SMESHERREWARDSTREAMRESPONSE']._serialized_end=1714
  _globals['_SMESHERDATAQUERYREQUEST']._serialized_start=1716
  _globals['_SMESHERDATAQUERYREQUEST']._serialized_end=1823
  _globals['_SMESHERDATAQUERYRESPONSE']._serialized_start=1825
  _globals['_SMESHERDATAQUERYRESPONSE']._serialized_end=1913
  _globals['_GLOBALSTATEHASH']._serialized_start=1915
  _globals['_GLOBALSTATEHASH']._serialized_end=1993
  _globals['_GLOBALSTATEHASHREQUEST']._serialized_start=1995
  _globals['_GLOBALSTATEHASHREQUEST']._serialized_end=2019
  _globals['_GLOBALSTATEHASHRESPONSE']._serialized_start=2021
  _globals['_GLOBALSTATEHASHRESPONSE']._serialized_end=2095
  _globals['_GLOBALSTATESTREAMREQUEST']._serialized_start=2097
  _globals['_GLOBALSTATESTREAMREQUEST']._serialized_end=2156
  _globals['_GLOBALSTATEDATA']._serialized_start=2159
  _globals['_GLOBALSTATEDATA']._serialized_end=2383
  _globals['_GLOBALSTATESTREAMRESPONSE']._serialized_start=2385
  _globals['_GLOBALSTATESTREAMRESPONSE']._serialized_end=2458
  _globals['_APPEVENTSTREAMREQUEST']._serialized_start=2460
  _globals['_APPEVENTSTREAMREQUEST']._serialized_end=2483
  _globals['_APPEVENTSTREAMRESPONSE']._serialized_start=2485
  _globals['_APPEVENTSTREAMRESPONSE']._serialized_end=2548
# @@protoc_insertion_point(module_scope)
