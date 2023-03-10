# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import videoconnector_pb2 as proto_dot_videoconnector__pb2


class VideoConnectorStub(object):
    """CameraConnector
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterClient = channel.unary_unary(
                '/videoconnector.VideoConnector/RegisterClient',
                request_serializer=proto_dot_videoconnector__pb2.RegisterRequest.SerializeToString,
                response_deserializer=proto_dot_videoconnector__pb2.RegisterResponse.FromString,
                )
        self.UnRegisterClient = channel.unary_unary(
                '/videoconnector.VideoConnector/UnRegisterClient',
                request_serializer=proto_dot_videoconnector__pb2.UnRegisterRequest.SerializeToString,
                response_deserializer=proto_dot_videoconnector__pb2.UnRegisterResponse.FromString,
                )
        self.GetCommand = channel.unary_unary(
                '/videoconnector.VideoConnector/GetCommand',
                request_serializer=proto_dot_videoconnector__pb2.CommandRequest.SerializeToString,
                response_deserializer=proto_dot_videoconnector__pb2.CommandList.FromString,
                )
        self.DeliverSourceInfo = channel.unary_unary(
                '/videoconnector.VideoConnector/DeliverSourceInfo',
                request_serializer=proto_dot_videoconnector__pb2.SourceInfoRequest.SerializeToString,
                response_deserializer=proto_dot_videoconnector__pb2.ServerAckResponse.FromString,
                )
        self.TransferImage = channel.unary_unary(
                '/videoconnector.VideoConnector/TransferImage',
                request_serializer=proto_dot_videoconnector__pb2.TransferImageRequest.SerializeToString,
                response_deserializer=proto_dot_videoconnector__pb2.ServerAckResponse.FromString,
                )


class VideoConnectorServicer(object):
    """CameraConnector
    """

    def RegisterClient(self, request, context):
        """Method to register a new client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnRegisterClient(self, request, context):
        """Method to unregister a client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCommand(self, request, context):
        """get commands for connector
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeliverSourceInfo(self, request, context):
        """get debug info on current video source
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransferImage(self, request, context):
        """used to transfer an image
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VideoConnectorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterClient': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterClient,
                    request_deserializer=proto_dot_videoconnector__pb2.RegisterRequest.FromString,
                    response_serializer=proto_dot_videoconnector__pb2.RegisterResponse.SerializeToString,
            ),
            'UnRegisterClient': grpc.unary_unary_rpc_method_handler(
                    servicer.UnRegisterClient,
                    request_deserializer=proto_dot_videoconnector__pb2.UnRegisterRequest.FromString,
                    response_serializer=proto_dot_videoconnector__pb2.UnRegisterResponse.SerializeToString,
            ),
            'GetCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCommand,
                    request_deserializer=proto_dot_videoconnector__pb2.CommandRequest.FromString,
                    response_serializer=proto_dot_videoconnector__pb2.CommandList.SerializeToString,
            ),
            'DeliverSourceInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.DeliverSourceInfo,
                    request_deserializer=proto_dot_videoconnector__pb2.SourceInfoRequest.FromString,
                    response_serializer=proto_dot_videoconnector__pb2.ServerAckResponse.SerializeToString,
            ),
            'TransferImage': grpc.unary_unary_rpc_method_handler(
                    servicer.TransferImage,
                    request_deserializer=proto_dot_videoconnector__pb2.TransferImageRequest.FromString,
                    response_serializer=proto_dot_videoconnector__pb2.ServerAckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'videoconnector.VideoConnector', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VideoConnector(object):
    """CameraConnector
    """

    @staticmethod
    def RegisterClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/videoconnector.VideoConnector/RegisterClient',
            proto_dot_videoconnector__pb2.RegisterRequest.SerializeToString,
            proto_dot_videoconnector__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnRegisterClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/videoconnector.VideoConnector/UnRegisterClient',
            proto_dot_videoconnector__pb2.UnRegisterRequest.SerializeToString,
            proto_dot_videoconnector__pb2.UnRegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/videoconnector.VideoConnector/GetCommand',
            proto_dot_videoconnector__pb2.CommandRequest.SerializeToString,
            proto_dot_videoconnector__pb2.CommandList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeliverSourceInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/videoconnector.VideoConnector/DeliverSourceInfo',
            proto_dot_videoconnector__pb2.SourceInfoRequest.SerializeToString,
            proto_dot_videoconnector__pb2.ServerAckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransferImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/videoconnector.VideoConnector/TransferImage',
            proto_dot_videoconnector__pb2.TransferImageRequest.SerializeToString,
            proto_dot_videoconnector__pb2.ServerAckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
