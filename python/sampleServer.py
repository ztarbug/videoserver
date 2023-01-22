from concurrent import futures
import logging
import grpc
import pprint
import base64

from io import BytesIO
import PIL.Image as Image
import cv2
import numpy as np

from google.protobuf.timestamp_pb2 import Timestamp

import videoconnector_pb2
import videoconnector_pb2_grpc

class VideoServer(videoconnector_pb2_grpc.VideoConnectorServicer):

    command_queue = []

    def __init__(self):
        logging.info("server created")


    def GetCommand(self, request, context):
        print("GetCommand")
        context.set_code(grpc.StatusCode.OK)
        context.set_details('Executed')

        ts = Timestamp()

        resp = videoconnector_pb2.CommandList(serverTimestamp = ts, commands = self.command_queue)
        self.command_queue = []

        return resp

    def TransferImage(self, request, context):
        print("TransferImage")
        context.set_code(grpc.StatusCode.OK)
        context.set_details('Executed')

        ts = Timestamp()
        resp = videoconnector_pb2.ServerAckResponse(serverTimestamp = ts)
        image_bytes = base64.b64decode(request.image)
        pprint.pprint(len(image_bytes))
        image = Image.open(BytesIO(image_bytes))
        image.save("/tmp/pictures/serverimage.jpg")
        return resp

    def DeliverSourceInfo(self, request, context):
        print("DeliverSourceInfo")
        context.set_code(grpc.StatusCode.OK)
        context.set_details('Executed')

        ts = Timestamp()
        resp = videoconnector_pb2.ServerAckResponse(serverTimestamp = ts)
        return resp


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options = [
            ('grpc.max_send_message_length', -1),
            ('grpc.max_receive_message_length', -1)
        ])

    vs = VideoServer()
    vs.command_queue.append(videoconnector_pb2.CommandType.GetSourceInfo)
    vs.command_queue.append(videoconnector_pb2.CommandType.GetImage)

    videoconnector_pb2_grpc.add_VideoConnectorServicer_to_server(vs, server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()