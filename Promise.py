from net.proto.TaskMetadata_pb2 import TaskMetadata
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

    def exec(self):
        #Halt on pending results
        pass