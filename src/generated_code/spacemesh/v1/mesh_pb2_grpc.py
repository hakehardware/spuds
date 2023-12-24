# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from src.generated_code.spacemesh.v1 import mesh_types_pb2 as spacemesh_dot_v1_dot_mesh__types__pb2


class MeshServiceStub(object):
    """Readonly API for basic mesh info
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenesisTime = channel.unary_unary(
                '/spacemesh.v1.MeshService/GenesisTime',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.GenesisTimeRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.GenesisTimeResponse.FromString,
                )
        self.CurrentLayer = channel.unary_unary(
                '/spacemesh.v1.MeshService/CurrentLayer',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.CurrentLayerRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.CurrentLayerResponse.FromString,
                )
        self.CurrentEpoch = channel.unary_unary(
                '/spacemesh.v1.MeshService/CurrentEpoch',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.CurrentEpochRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.CurrentEpochResponse.FromString,
                )
        self.GenesisID = channel.unary_unary(
                '/spacemesh.v1.MeshService/GenesisID',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.GenesisIDRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.GenesisIDResponse.FromString,
                )
        self.EpochNumLayers = channel.unary_unary(
                '/spacemesh.v1.MeshService/EpochNumLayers',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.EpochNumLayersRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.EpochNumLayersResponse.FromString,
                )
        self.LayerDuration = channel.unary_unary(
                '/spacemesh.v1.MeshService/LayerDuration',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.LayerDurationRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.LayerDurationResponse.FromString,
                )
        self.MaxTransactionsPerSecond = channel.unary_unary(
                '/spacemesh.v1.MeshService/MaxTransactionsPerSecond',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.MaxTransactionsPerSecondRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.MaxTransactionsPerSecondResponse.FromString,
                )
        self.AccountMeshDataQuery = channel.unary_unary(
                '/spacemesh.v1.MeshService/AccountMeshDataQuery',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.AccountMeshDataQueryRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.AccountMeshDataQueryResponse.FromString,
                )
        self.LayersQuery = channel.unary_unary(
                '/spacemesh.v1.MeshService/LayersQuery',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.LayersQueryRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.LayersQueryResponse.FromString,
                )
        self.AccountMeshDataStream = channel.unary_stream(
                '/spacemesh.v1.MeshService/AccountMeshDataStream',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.AccountMeshDataStreamRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.AccountMeshDataStreamResponse.FromString,
                )
        self.LayerStream = channel.unary_stream(
                '/spacemesh.v1.MeshService/LayerStream',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.LayerStreamRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.LayerStreamResponse.FromString,
                )
        self.EpochStream = channel.unary_stream(
                '/spacemesh.v1.MeshService/EpochStream',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.EpochStreamRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.EpochStreamResponse.FromString,
                )
        self.MalfeasanceQuery = channel.unary_unary(
                '/spacemesh.v1.MeshService/MalfeasanceQuery',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.MalfeasanceRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.MalfeasanceResponse.FromString,
                )
        self.MalfeasanceStream = channel.unary_stream(
                '/spacemesh.v1.MeshService/MalfeasanceStream',
                request_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.MalfeasanceStreamRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.MalfeasanceStreamResponse.FromString,
                )


class MeshServiceServicer(object):
    """Readonly API for basic mesh info
    """

    def GenesisTime(self, request, context):
        """Network genesis time as unix epoch time
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CurrentLayer(self, request, context):
        """Current layer number
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CurrentEpoch(self, request, context):
        """Current epoch number
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenesisID(self, request, context):
        """Genesis ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EpochNumLayers(self, request, context):
        """Number of layers per epoch (a network parameter)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LayerDuration(self, request, context):
        """Layer duration (a network parameter)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MaxTransactionsPerSecond(self, request, context):
        """Number of transactions per second (a network parameter)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountMeshDataQuery(self, request, context):
        """//////// Queries
        Queries return paginated, historical data.

        Get account data query
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LayersQuery(self, request, context):
        """Layers data query
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountMeshDataStream(self, request, context):
        """//////// Streams
        Streams return live, new data as it becomes available to the node and not
        historical data.

        A stream of transactions and activations from an account.
        Includes simple coin transactions with the account as the destination.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LayerStream(self, request, context):
        """Layer with blocks, transactions and activations
        Sent each time layer data changes. Designed for heavy-duty clients.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EpochStream(self, request, context):
        """Epoch activation transactions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MalfeasanceQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MalfeasanceStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeshServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenesisTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GenesisTime,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.GenesisTimeRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.GenesisTimeResponse.SerializeToString,
            ),
            'CurrentLayer': grpc.unary_unary_rpc_method_handler(
                    servicer.CurrentLayer,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.CurrentLayerRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.CurrentLayerResponse.SerializeToString,
            ),
            'CurrentEpoch': grpc.unary_unary_rpc_method_handler(
                    servicer.CurrentEpoch,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.CurrentEpochRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.CurrentEpochResponse.SerializeToString,
            ),
            'GenesisID': grpc.unary_unary_rpc_method_handler(
                    servicer.GenesisID,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.GenesisIDRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.GenesisIDResponse.SerializeToString,
            ),
            'EpochNumLayers': grpc.unary_unary_rpc_method_handler(
                    servicer.EpochNumLayers,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.EpochNumLayersRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.EpochNumLayersResponse.SerializeToString,
            ),
            'LayerDuration': grpc.unary_unary_rpc_method_handler(
                    servicer.LayerDuration,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.LayerDurationRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.LayerDurationResponse.SerializeToString,
            ),
            'MaxTransactionsPerSecond': grpc.unary_unary_rpc_method_handler(
                    servicer.MaxTransactionsPerSecond,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.MaxTransactionsPerSecondRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.MaxTransactionsPerSecondResponse.SerializeToString,
            ),
            'AccountMeshDataQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.AccountMeshDataQuery,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.AccountMeshDataQueryRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.AccountMeshDataQueryResponse.SerializeToString,
            ),
            'LayersQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.LayersQuery,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.LayersQueryRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.LayersQueryResponse.SerializeToString,
            ),
            'AccountMeshDataStream': grpc.unary_stream_rpc_method_handler(
                    servicer.AccountMeshDataStream,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.AccountMeshDataStreamRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.AccountMeshDataStreamResponse.SerializeToString,
            ),
            'LayerStream': grpc.unary_stream_rpc_method_handler(
                    servicer.LayerStream,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.LayerStreamRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.LayerStreamResponse.SerializeToString,
            ),
            'EpochStream': grpc.unary_stream_rpc_method_handler(
                    servicer.EpochStream,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.EpochStreamRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.EpochStreamResponse.SerializeToString,
            ),
            'MalfeasanceQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.MalfeasanceQuery,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.MalfeasanceRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.MalfeasanceResponse.SerializeToString,
            ),
            'MalfeasanceStream': grpc.unary_stream_rpc_method_handler(
                    servicer.MalfeasanceStream,
                    request_deserializer=spacemesh_dot_v1_dot_mesh__types__pb2.MalfeasanceStreamRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_mesh__types__pb2.MalfeasanceStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spacemesh.v1.MeshService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MeshService(object):
    """Readonly API for basic mesh info
    """

    @staticmethod
    def GenesisTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.MeshService/GenesisTime',
            spacemesh_dot_v1_dot_mesh__types__pb2.GenesisTimeRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.GenesisTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CurrentLayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.MeshService/CurrentLayer',
            spacemesh_dot_v1_dot_mesh__types__pb2.CurrentLayerRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.CurrentLayerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CurrentEpoch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.MeshService/CurrentEpoch',
            spacemesh_dot_v1_dot_mesh__types__pb2.CurrentEpochRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.CurrentEpochResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenesisID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.MeshService/GenesisID',
            spacemesh_dot_v1_dot_mesh__types__pb2.GenesisIDRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.GenesisIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EpochNumLayers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.MeshService/EpochNumLayers',
            spacemesh_dot_v1_dot_mesh__types__pb2.EpochNumLayersRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.EpochNumLayersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LayerDuration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.MeshService/LayerDuration',
            spacemesh_dot_v1_dot_mesh__types__pb2.LayerDurationRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.LayerDurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MaxTransactionsPerSecond(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.MeshService/MaxTransactionsPerSecond',
            spacemesh_dot_v1_dot_mesh__types__pb2.MaxTransactionsPerSecondRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.MaxTransactionsPerSecondResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountMeshDataQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.MeshService/AccountMeshDataQuery',
            spacemesh_dot_v1_dot_mesh__types__pb2.AccountMeshDataQueryRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.AccountMeshDataQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LayersQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.MeshService/LayersQuery',
            spacemesh_dot_v1_dot_mesh__types__pb2.LayersQueryRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.LayersQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AccountMeshDataStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spacemesh.v1.MeshService/AccountMeshDataStream',
            spacemesh_dot_v1_dot_mesh__types__pb2.AccountMeshDataStreamRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.AccountMeshDataStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LayerStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spacemesh.v1.MeshService/LayerStream',
            spacemesh_dot_v1_dot_mesh__types__pb2.LayerStreamRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.LayerStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EpochStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spacemesh.v1.MeshService/EpochStream',
            spacemesh_dot_v1_dot_mesh__types__pb2.EpochStreamRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.EpochStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MalfeasanceQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.MeshService/MalfeasanceQuery',
            spacemesh_dot_v1_dot_mesh__types__pb2.MalfeasanceRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.MalfeasanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MalfeasanceStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spacemesh.v1.MeshService/MalfeasanceStream',
            spacemesh_dot_v1_dot_mesh__types__pb2.MalfeasanceStreamRequest.SerializeToString,
            spacemesh_dot_v1_dot_mesh__types__pb2.MalfeasanceStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
