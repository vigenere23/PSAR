from pinject import BindingSpec
from src.argparser import args
from src.domain.sequence.task_containers import MainTaskContainer
from src.domain.sequence.tasks import RetryableTask
from .EventEmittersContext import EventEmittersContext


class SequenceContext(BindingSpec):

    def configure(self, bind):
        if args.sequence == 'main':
            bind('retryable_task', to_class=RetryableTask)
            bind('task_container', to_class=MainTaskContainer)

    def dependencies(self):
        return [
            EventEmittersContext()
        ]
