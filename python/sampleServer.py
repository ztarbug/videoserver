from concurrent import futures
from pathlib import Path
import time
import logging
import grpc
import pprint
import base64

from io import BytesIO
import PIL.Image as Image
import cv2
import numpy as np

from google.protobuf.timestamp_pb2 import Timestamp

import clientdata
import videoconnector_pb2
import videoconnector_pb2_grpc

class VideoServer(videoconnector_pb2_grpc.VideoConnectorServicer):

    clients = {}
    number_client = 0

    def __init__(self):
        logging.info("server created")

    def RegisterClient(self, request, context):
        print("register new client")

        cd = clientdata.ClientData()
        cd.client_hostname = request.hostname
        cd.client_id = self.number_client        
        cd.command_queue.append(videoconnector_pb2.CommandType.GetSourceInfo)
        cd.command_queue.append(videoconnector_pb2.CommandType.GetImage)        
        self.clients[cd.client_id] = cd
        self.number_client += 1
        print("number of registered clients " + str(self.number_client))

        context.set_code(grpc.StatusCode.OK)
        context.set_details('Executed')
        resp = videoconnector_pb2.RegisterResponse()
        return resp

    def UnRegisterClient(self, request, context):
        print("unregister client")

        del self.clients[request.client_id]

        self.number_client -= 1
        print("number of registered clients " + str(self.number_client))

        context.set_code(grpc.StatusCode.OK)
        context.set_details('Executed')        
        resp = videoconnector_pb2.UnRegisterResponse()
        return resp

    def GetCommand(self, request, context):
        print("GetCommand")
        context.set_code(grpc.StatusCode.OK)
        context.set_details('Executed')

        ts = Timestamp()

        resp = videoconnector_pb2.CommandList(serverTimestamp = ts, commands = self.clients[request.client_id].command_queue)
        self.clients[request.client_id].command_queue = []

        return resp

    def TransferImage(self, request, context):
        print("TransferImage")
        context.set_code(grpc.StatusCode.OK)
        context.set_details('Executed')

        image_bytes = base64.b64decode(request.image)
        self.SaveImage(image_bytes, request.client_id)        

        ts = Timestamp()
        resp = videoconnector_pb2.ServerAckResponse(serverTimestamp = ts)
        return resp

    def DeliverSourceInfo(self, request, context):
        print("DeliverSourceInfo")
        context.set_code(grpc.StatusCode.OK)
        context.set_details('Executed')

        ts = Timestamp()
        resp = videoconnector_pb2.ServerAckResponse(serverTimestamp = ts)
        return resp

    def SaveImage(self, image, client_id):
        path ="/tmp/pictures/" + str(client_id)
        Path(path).mkdir( parents=True, exist_ok=True )

        pprint.pprint(len(image))
        image = Image.open(BytesIO(image))
        filename = "/" + str(client_id) + "-image-" + time.strftime("%Y%m%d-%H%M%S")
        image.save(path + filename + ".jpg")


def serve():
    cd = clientdata.ClientData()
    cd.client_hostname = "sdgdfgdf"
    cd.client_id = 1
    cd.command_queue = []
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options = [
            ('grpc.max_send_message_length', -1),
            ('grpc.max_receive_message_length', -1)
        ])

    vs = VideoServer()
    videoconnector_pb2_grpc.add_VideoConnectorServicer_to_server(vs, server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()