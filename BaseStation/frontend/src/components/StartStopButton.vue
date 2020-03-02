<template>
  <div class="startStopButton">
    <div class="startButton" v-if="!started" @click="start">START</div>
    <div class="stopButton" v-else @click="stop">STOP</div>
  </div>
</template>

<script>
import { startSequence, stopSequence } from '../api/SequenceSocketEventEmitter'

export default {
  name: 'StartStopButton',
  data () {
    return {
      interval: false,
      started: false
    }
  },
  methods: {
    start () {
      this.started = true
      startSequence()
    },
    stop () {
      this.started = false
      stopSequence()
    }
  }
}
</script>

<style lang="scss">
  .startStopButton {
    .startButton {
      width: 100%;
      height: 100%;
      background: green;
    }

    .stopButton {
      width: 100%;
      height: 100%;
      background: red;
    }

    .button:active {
      background: blue;
    }
  }
</style>
