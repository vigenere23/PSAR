from pinject import BindingSpec
from src.argparser import args
from src.domain.sequence.task_containers import MainTaskContainer
from .EventEmittersContext import EventEmittersContext


class SequenceContext(BindingSpec):

    def configure(self, bind, require):
        if args.sequence == 'main':
            bind('task_container', to_class=MainTaskContainer)

    def dependencies(self):
        return [
            EventEmittersContext()
        ]
