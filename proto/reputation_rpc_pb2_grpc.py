# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto.reputation_rpc_pb2 as reputation__rpc__pb2


class RPCServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddSource = channel.unary_unary(
            "/reputation.rpc.RPCService/AddSource",
            request_serializer=reputation__rpc__pb2.AddSourceRequest.SerializeToString,
            response_deserializer=reputation__rpc__pb2.AddSourceResponse.FromString,
        )
        self.GetTopMiners = channel.unary_unary(
            "/reputation.rpc.RPCService/GetTopMiners",
            request_serializer=reputation__rpc__pb2.GetTopMinersRequest.SerializeToString,
            response_deserializer=reputation__rpc__pb2.GetTopMinersResponse.FromString,
        )


class RPCServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddSource(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetTopMiners(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_RPCServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "AddSource": grpc.unary_unary_rpc_method_handler(
            servicer.AddSource,
            request_deserializer=reputation__rpc__pb2.AddSourceRequest.FromString,
            response_serializer=reputation__rpc__pb2.AddSourceResponse.SerializeToString,
        ),
        "GetTopMiners": grpc.unary_unary_rpc_method_handler(
            servicer.GetTopMiners,
            request_deserializer=reputation__rpc__pb2.GetTopMinersRequest.FromString,
            response_serializer=reputation__rpc__pb2.GetTopMinersResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "reputation.rpc.RPCService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class RPCService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddSource(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/reputation.rpc.RPCService/AddSource",
            reputation__rpc__pb2.AddSourceRequest.SerializeToString,
            reputation__rpc__pb2.AddSourceResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetTopMiners(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/reputation.rpc.RPCService/GetTopMiners",
            reputation__rpc__pb2.GetTopMinersRequest.SerializeToString,
            reputation__rpc__pb2.GetTopMinersResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
