import grpc

import jobupload_pb2

def get_line(file):
    for line in file:
        yield jobupload_pb2.line(content=line)

def upload(parameters, filename):
    # connect
    channel = grpc.insecure_channel('localhost:50051')
    stub = jobupload_pb2.JobUploadStub(channel)

    # parameters
    response = stub.param(jobupload_pb2.parameters(content=parameters))
    print(response.message)

    # upload
    print(filename)
    with open(filename, 'r') as file:
        #TODO more efficient method?
        line_iterator = get_line(file)
        response = stub.upload(line_iterator)
        print(response.message)

#if __name__ == '__main__':
#    run()

