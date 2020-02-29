from injector import Module, Binder
from src.argparser import args
from src.domain.sequence.TaskContainer import TaskContainer
from src.domain.sequence.TaskContainerFactory import TaskContainerFactory


class SequenceContext(Module):

    def configure(self, binder: Binder):
        if args.sequence:
            binder.bind(
                TaskContainer,
                to=TaskContainerFactory().get_class(args.sequence)
            )
