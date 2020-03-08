<template>
  <div class="sequence-control-buttons">
    <StartButton
      v-if="!started"
      :loading="startStopLoading"
      :disabled="startStopLoading"
      @click="start"
    />
    <StopButton
      v-else
      :loading="startStopLoading"
      :disabled="startStopLoading"
      @click="stop"
    />

    <PauseButton
      v-if="!paused"
      :loading="pauseResumeLoading"
      :disabled="pauseResumeLoading || startStopLoading || !started"
      @click="pause"
    />
    <ResumeButton
      v-else-if="paused"
      :loading="pauseResumeLoading"
      :disabled="pauseResumeLoading || startStopLoading || !started"
      @click="resume"
    />
  </div>
</template>

<script>
import StartButton from '@/components/sequenceControlButtons/StartButton'
import StopButton from '@/components/sequenceControlButtons/StopButton'
import PauseButton from '@/components/sequenceControlButtons/PauseButton'
import ResumeButton from '@/components/sequenceControlButtons/ResumeButton'
import { sendStartSequence, sendStopSequence } from '@/api/eventEmitters/sequence'
import { on } from '@/api/eventHandlers/sequence'

export default {
  name: 'SequenceControlButtons',
  components: {
    StartButton,
    StopButton,
    PauseButton,
    ResumeButton
  },
  data () {
    return {
      started: false,
      startStopLoading: false,
      pauseResumeLoading: false
    }
  },
  mounted () {
    on('started', () => {
      console.log('sequence started')
      this.started = true
      this.startStopLoading = false
    })
    on('ended', () => {
      console.log('sequence ended')
      this.started = false
      this.startStopLoading = false
    })
  },
  computed: {
    startStopText () {
      return this.started
        ? 'stop'
        : 'start'
    },
    startStopColor () {
      return this.started
        ? 'red'
        : 'green'
    }
  },
  methods: {
    start () {
      this.startStopLoading = true
      sendStartSequence()
    },
    stop () {
      this.startStopLoading = true
      sendStopSequence()
    },
    pause () {
      // TODO
    },
    resume () {
      // TODO
    }
  }
}
</script>
