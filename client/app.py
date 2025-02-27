from concurrent import futures
import time
import sys
import grpc
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from auto_gen import greet_pb2_grpc
from auto_gen import greet_pb2


# def get_client_stream_requests():
    # while True:
    #     name = input("Please enter a name (or nothing to stop chatting): ")

    #     if name == "":
    #         break

    #     hello_request = greet_pb2.HelloRequest(greeting = "Hello", name = name)
    #     yield hello_request
    #     time.sleep(1)



def run():
    with  grpc.insecure_channel('localhost:50051') as channel :
        stub = greet_pb2_grpc.GreeterStub(channel) 
        print("1. SayHello - Unary")
        print("2. ParrotSaysHello - Server Side Streaming")
        print("3. ChattyClientSaysHello - Client Side Streaming")
        print("4. InteractingHello - Both Streaming")
        rpc_call = input("Which rpc would you like to make: ")

        if rpc_call =="1":
            hello_request = greet_pb2.HelloRequest(name = "YouTube",greeting = "Bonjour")
            hello_reply = stub.SayHello(hello_request)
            print("SayHello Response Received:")
            print(hello_reply)

        elif rpc_call =="2":
           hello_request = greet_pb2.HelloRequest(greeting="mambo_vp",name="mr wick")
           hello_replies = stub.ParrotSaysHello(hello_request)
           
           for hello_reply in hello_replies:
                print("parrotSay Response Send..")
                print(hello_reply)


        elif rpc_call =="3":
        elif rpc_call =="4":
           print("no Implemantation")

if __name__ == "__main__":
    run()