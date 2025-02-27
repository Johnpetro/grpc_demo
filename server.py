from concurrent import futures
import time
import grpc
from auto_gen import greet_pb2_grpc
from auto_gen import greet_pb2

class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self,request,context):
        print("SayHello Request Made:")
        print(request)
        # here is the area whre the grpc pesporm some staff 
        hello_reply = greet_pb2.HelloReply(message="Hello")
        hello_reply.message = f"{request.greeting} {request.name}"
        return hello_reply

    def ParrotSaysHello(self, request, context):
        # print("The parroteSayse hallow")
        # print(request)
        # for i in range(3):
        #     hello_reply =greet_pb2.HelloReply(greeting = "Bonjour", name = "YouTube")
        #     hello_reply.message = f"{request.greeting} {request.name} {i+1}"
        #     yield hello_reply
        #     time.sleep(3)
        print("ParrotSaysHello Request Made:")
        print(request)

        for i in range(3):
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name} {i + 1}"
            yield hello_reply
            time.sleep(3)
    
    # server stremming

    def ChattyClientSaysHello(self, request,context):
        print("the chattingClientSay Hellow")
        print(request)


        









def serve():
     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
     greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(),server)
     server.add_insecure_port("localhost:50051")
     server.start()
     print("Server started on port 50051")
     server.wait_for_termination()

if __name__ == "__main__":
      serve()



