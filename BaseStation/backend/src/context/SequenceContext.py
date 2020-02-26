from pinject import BindingSpec
from src.argparser import args
from src.domain.sequence import TaskContainerFactory
from .EventEmittersContext import EventEmittersContext


class SequenceContext(BindingSpec):

    def configure(self, bind, require):
        if args.sequence:
            bind(
                'task_container',
                to_class=TaskContainerFactory().get_class(args.sequence))

    def dependencies(self):
        return [
            EventEmittersContext()
        ]
