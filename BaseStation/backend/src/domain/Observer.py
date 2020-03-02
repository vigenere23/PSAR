class Observer:
    def __init__(self):
        self.__listeners = []

    def add_listener(self, fn):
        self.__listeners.append(fn)

    def remove_listener(self, fn):
        self.__listeners.remove(fn)

    def trig_listeners(self, *args, **kwargs):
        for fn in self.__listeners:
            fn(*args, **kwargs)
