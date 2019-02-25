class Promise:
    def __init__(module, function, args, kwargs, _class=None):
        self.__module = module
        self.__function = function
        self.__args = args
        self.__kwargs = kwargs
        self.__class = _class
    
    def exec(self):
        #Halt on pending results
        pass
