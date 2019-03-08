import grpc
import dill as pickle
import net.proto.TaskService_pb2_grpc as TaskService
from net.proto.TaskMetadata_pb2 import TaskMetadata, TaskArgument, ArgumentMetadata, ARGUMENT, KEYWORD_ARGUMENT
from net.proto.TaskCommon_pb2 import OK

class ConnectionError(Exception):
    def __init__(self, message):
        self.message = message

class TaskClient:
    def __init__(self, host, port, cert_file = None):
        self.__channel = grpc.insecure_channel(f'{host}:{port}')
        self.__client = TaskService.TaskServiceStub(self.__channel)

    def send_promise(self, promise):
        task = promise.__meta__()
        # Sends the task metadata, resp is the TaskReceived
        resp = self.__client.AddTask(task)
        if resp.status.code == OK:
            promise.set_task_id(resp.task_id)
            promise.send_args(self.__client)
            promise.send_kwargs(self.__client)
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
        mv_arg = memoryview(bin_arg)
        chunks = len(bin_arg) / (1 << 20)
        for i in range(chunks):
            yield TaskArgument(arg = mv_arg[i * chunks : (i + 1) * chunks])

    def exec_promise(self, promise):
        pass

global TaskClientInstance
TaskClientInstance = TaskClient('0.0.0.0', '8080')