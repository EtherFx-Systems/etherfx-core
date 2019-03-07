import grpc
import dill as pickle
import net.proto.TaskService_pb2_grpc as TaskService
from net.proto.TaskMetadata_pb2 import TaskMetadata, TaskArgument, ArgumentMetadata, ARGUMENT, KEYWORD_ARGUMENT
from net.proto.TaskCommon_pb2 import OK

class TaskClient:
    def __init__(self, host, port, cert_file = None):
        self.__channel = grpc.insecure_channel(f'${host}:${port}')
        self.__client = TaskService.TaskServiceStub(self.__channel)

    def send_promise(self, promise):
        _task = promise.__meta__()
        #sends the task metadata, resp is the TaskReceived
        resp = self.__client.AddTask(_task)
        if resp.status.code == OK:
            promise.__task_id = resp.task_id
            for arg in promise.__args:
                # C H O N K
                self.__client
        else:
            #add error class
            pass

    def make_argument(self, task_id, ord, arg):
        arg_seq = ArgumentMetadata(task_id = task_id)
        if isinstance(ord, str):
            arg_seq.arg_type = KEYWORD_ARGUMENT
            arg_seq.name = ord
        else:
            arg_seq.arg_type = ARGUMENT
            arg_seq.num = ord
        yield TaskArgument(arg_seq = arg_seq)

        bin_arg = pickle.dumps(arg)
        mv_arg = memoryview(bin_arg)
        chunks = len(bin_arg) / (1 << 20)
        for i in range(chunks):
            yield TaskArgument(arg = mv_arg[i * chunks : (i + 1) * chunks])

    def exec_promise(self, Promise):
        pass