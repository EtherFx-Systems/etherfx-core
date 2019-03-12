from .net.proto.TaskMetadata_pb2 import TaskMetadata, ExecTaskRequest
from .net.grpc_client import TaskClient


class Promise:
    def __init__(self, client, module, function, args, kwargs, _class=None):
        self.__module = module
        self.__function = function
        self.__args = args
        self.__kwargs = kwargs
        self.__class = _class
        self.__task_id = None
        self.__client = client

    def __meta__(self):
        return TaskMetadata(
            module=self.__module,
            function=self.__function,
            args=len(self.__args),
            kwargs=self.__kwargs.keys(),
            _class=self.__class,
        )

    def ether_set_task_id(self, task_id):
        self.__task_id = task_id

    def ether_task_id(self):
        return self.__task_id

    def ether_send_args(self, client, stub):
        if len(self.__args) > 0:
            for idx, arg in enumerate(self.__args):
                stub.AddArgument(client.make_argument(self.__task_id, idx, arg))

    def ether_send_kwargs(self, client, stub):
        if len(self.__kwargs.keys()) > 0:
            for key, arg in self.__kwargs.items():
                stub.AddArgument(client.make_argument(self.__task_id, key, arg))

    def ether_send(self, client):
        self.__client.send_promise(self)

    def exec(self):
        return self.__client.exec_promise(self)
