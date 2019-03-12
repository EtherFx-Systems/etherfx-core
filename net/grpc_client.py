import grpc
import dill as pickle
from .proto.TaskService_pb2_grpc import TaskServiceStub
from .proto.TaskMetadata_pb2 import TaskMetadata, TaskArgument, ArgumentMetadata, ARGUMENT, KEYWORD_ARGUMENT
from .proto.TaskCommon_pb2 import OK
from math import ceil

class ConnectionError(Exception):
    def __init__(self, message):
        self.message = message

class TaskClient:
    def __init__(self, host, port, cert_file = None):
        self.__channel = grpc.insecure_channel(f'{host}:{port}')
        self.__client = TaskServiceStub(self.__channel)

    def send_promise(self, promise):
        task = promise.__meta__()
        # Sends the task metadata, resp is the TaskReceived
        resp = self.__client.AddTask(task)
        if resp.status.code == OK:
            promise.ether_set_task_id(resp.task_id)
            promise.ether_send_args(self, self.__client)
            promise.ether_send_kwargs(self, self.__client)
        else:
            raise ConnectionError("Promise could not be registered to the Orchestrator")

    def make_argument(self, task_id, ord, arg):
        # Send Metadata First
        arg_seq = ArgumentMetadata(task_id = task_id)
        if isinstance(ord, str):
            arg_seq.arg_type = KEYWORD_ARGUMENT
            arg_seq.name = ord
        else:
            arg_seq.arg_type = ARGUMENT
            arg_seq.num = ord
        yield TaskArgument(arg_seq = arg_seq)

        #Chunk and yield actual argument bytes
        bin_arg = pickle.dumps(arg)
        print(bin_arg)
        mv_arg = memoryview(bin_arg)
        chunks = len(bin_arg) / (1 << 20)
        # for i in range(ceil(chunks)):
        yield TaskArgument(arg=bin_arg)#(arg = mv_arg[i * (1 << 20) : (i + 1) * (1 << 20)])

    def exec_promise(self, promise):
        pass

global TaskClientInstance
TaskClientInstance = TaskClient('0.0.0.0', '8080')