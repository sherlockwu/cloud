from concurrent import futures
import time

import grpc

import jobupload_pb2

class Transfer(jobupload_pb2.JobUploadServicer):

    def upload(self, request_iterator, context):
        f = open('/Users/sherlock/Desktop/test_out_1.py', 'w');
        for line in request_iterator:
            f.write(line.content)
        f.close()
        return jobupload_pb2.Status(message='File OK')

    def param(self, request, context):
        parameters = request
        print(parameters.content)
        return jobupload_pb2.Status(message='Parameters OK')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    jobupload_pb2.add_JobUploadServicer_to_server(Transfer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)



if __name__ == '__main__':
    serve()
