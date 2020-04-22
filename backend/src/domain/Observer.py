class Observer:
    def __init__(self):
        self.__listeners = []
        self.__last_args = None
        self.__last_kwargs = None

    def add_listener(self, fn):
        self.__listeners.append(fn)

    def remove_listener(self, fn):
        self.__listeners.remove(fn)

    def trig_listeners(self, *args, **kwargs):
        self.__last_args = args
        self.__last_kwargs = kwargs
        for fn in self.__listeners:
            fn(*args, **kwargs)
            
    def trig_listeners_with_last_event(self):
        if self.__last_args is not None or self.__last_kwargs is not None:
            self.trig_listeners(*self.__last_args, **self.__last_kwargs)
