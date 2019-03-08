from net.proto.TaskMetadata_pb2 import TaskMetadata, ExecTaskRequest
from net.grpc_client import TaskClientInstance
class Promise:
    def __init__(self, module, function, args, kwargs, _class=None):
        self.__module = module
        self.__function = function
        self.__args = args
        self.__kwargs = kwargs
        self.__class = _class
        self.__task_id = None
    
    def __meta__(self):
        return TaskMetadata(module   = self.__module,
                            function = self.__function,
                            args     = len(self.__args),
                            kwargs   = self.__kwargs.keys(),
                            _class   = self.__class)
    def set_task_id(self, task_id):
        self.__task_id = task_id
    def task_id(self):
        return self.__task_id

    def send_args(self, client):
        if len(self.__args) > 0:
            for idx, arg in enumerate(self.__args):
                client.AddArgument.future(client.make_argument(self.__task_id, idx, arg))
    def send_kwargs(self, client):
        if len(self.__kwargs.keys()) > 0:
            for key, arg in self.__kwargs.items():
                client.AddArgument.future(client.make_argument(self.__task_id, key, arg))


    def exec(self, client):
        return client.exec_promise(self)