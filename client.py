import grpc
import net.TaskService_pb2 as TS

with grpc.insecure_channel('localhost:1111') as channel:
    stup = 