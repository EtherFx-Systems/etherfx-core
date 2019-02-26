class Promise:
    def __init__(self, module, function, args, kwargs, _class=None):
        self.__module = module
        self.__function = function
        self.__args = args
        self.__kwargs = kwargs
        self.__class = _class
        self.__task_id = None
    
    def exec(self):
        #Halt on pending results
        pass
