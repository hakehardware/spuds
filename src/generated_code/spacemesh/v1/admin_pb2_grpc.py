# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from src.generated_code.spacemesh.v1 import admin_types_pb2 as spacemesh_dot_v1_dot_admin__types__pb2


class AdminServiceStub(object):
    """AdminService offers the set of administrative RPCs.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckpointStream = channel.unary_stream(
                '/spacemesh.v1.AdminService/CheckpointStream',
                request_serializer=spacemesh_dot_v1_dot_admin__types__pb2.CheckpointStreamRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_admin__types__pb2.CheckpointStreamResponse.FromString,
                )
        self.Recover = channel.unary_unary(
                '/spacemesh.v1.AdminService/Recover',
                request_serializer=spacemesh_dot_v1_dot_admin__types__pb2.RecoverRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.EventsStream = channel.unary_stream(
                '/spacemesh.v1.AdminService/EventsStream',
                request_serializer=spacemesh_dot_v1_dot_admin__types__pb2.EventStreamRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_admin__types__pb2.Event.FromString,
                )
        self.PeerInfoStream = channel.unary_stream(
                '/spacemesh.v1.AdminService/PeerInfoStream',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_admin__types__pb2.PeerInfo.FromString,
                )


class AdminServiceServicer(object):
    """AdminService offers the set of administrative RPCs.
    """

    def CheckpointStream(self, request, context):
        """Returns the checkpoint data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Recover(self, request, context):
        """Recovers from the provided checkpoint data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EventsStream(self, request, context):
        """Events that are relevant for node operator
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PeerInfoStream(self, request, context):
        """PeerInfo returns info for all connected peers. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdminServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckpointStream': grpc.unary_stream_rpc_method_handler(
                    servicer.CheckpointStream,
                    request_deserializer=spacemesh_dot_v1_dot_admin__types__pb2.CheckpointStreamRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_admin__types__pb2.CheckpointStreamResponse.SerializeToString,
            ),
            'Recover': grpc.unary_unary_rpc_method_handler(
                    servicer.Recover,
                    request_deserializer=spacemesh_dot_v1_dot_admin__types__pb2.RecoverRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'EventsStream': grpc.unary_stream_rpc_method_handler(
                    servicer.EventsStream,
                    request_deserializer=spacemesh_dot_v1_dot_admin__types__pb2.EventStreamRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_admin__types__pb2.Event.SerializeToString,
            ),
            'PeerInfoStream': grpc.unary_stream_rpc_method_handler(
                    servicer.PeerInfoStream,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=spacemesh_dot_v1_dot_admin__types__pb2.PeerInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spacemesh.v1.AdminService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AdminService(object):
    """AdminService offers the set of administrative RPCs.
    """

    @staticmethod
    def CheckpointStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spacemesh.v1.AdminService/CheckpointStream',
            spacemesh_dot_v1_dot_admin__types__pb2.CheckpointStreamRequest.SerializeToString,
            spacemesh_dot_v1_dot_admin__types__pb2.CheckpointStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Recover(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.AdminService/Recover',
            spacemesh_dot_v1_dot_admin__types__pb2.RecoverRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EventsStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spacemesh.v1.AdminService/EventsStream',
            spacemesh_dot_v1_dot_admin__types__pb2.EventStreamRequest.SerializeToString,
            spacemesh_dot_v1_dot_admin__types__pb2.Event.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PeerInfoStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spacemesh.v1.AdminService/PeerInfoStream',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            spacemesh_dot_v1_dot_admin__types__pb2.PeerInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
