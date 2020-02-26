from pinject import BindingSpec
from src.infrastructure.event_emitters.socket import SequenceSocketEventEmitter
from src.argparser import args


class EventEmittersContext(BindingSpec):

    def configure(self, bind):
        if args.event_type == 'socket':
            bind('sequence_event_emitter', to_class=SequenceSocketEventEmitter)
