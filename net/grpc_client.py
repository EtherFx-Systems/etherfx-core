import grpc
import net.proto.TaskService_pb2_grpc as TaskService
from net.proto.TaskMetadata_pb2 import  TaskMetadata, TaskArgument
from net.proto.TaskCommon_pb2 import StatusCode

class TaskClient:
    def __init__(self, host, port, cert_file = None):
        self.__channel = grpc.insecure_channel(f'${host}:${port}')
        self.__client = TaskService.TaskServiceStub(self.__channel)

    def send_promise(self, promise):
        _task = TaskMetadata(module= promise.__module,
                             function = promise.__function,
                             args = len(promise.__args),
                             kwargs = promise.__kwargs.keys(),
                             _class = promise.__class)

        #sends the task metadata, resp is the TaskReceived
        resp = self.__client.AddTask(_task)
        if resp.status.code == StatusCode.OK:
            promise.__task_id = resp.task_id
        else:
            #add error class
            pass

    def exec_promise(self, Promise):
        pass