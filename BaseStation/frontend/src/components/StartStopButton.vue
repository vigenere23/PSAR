<template>
  <div class="startStopButton">
    <div class="startButton" v-if="!started && !loading" @click="start">START</div>
    <div class="stopButton" v-else-if="started && !loading" @click="stop">STOP</div>
    <div class="loadingButton" v-else>LOADING...</div>
  </div>
</template>

<script>
import { sendStartSequence, sendStopSequence } from '@/api/eventEmitters/sequence'
import { on } from '@/api/eventHandlers/sequence'

export default {
  name: 'StartStopButton',
  data () {
    return {
      interval: false,
      started: false,
      loading: false
    }
  },
  mounted () {
    on('started', () => {
      console.log('sequence started')
      this.started = true
      this.loading = false
    })
    on('ended', () => {
      console.log('sequence ended')
      this.started = false
      this.loading = false
    })
  },
  methods: {
    start () {
      this.loading = true
      sendStartSequence()
    },
    stop () {
      this.loading = true
      sendStopSequence()
    }
  }
}
</script>

<style lang="scss">
  .startStopButton {

    > * {
      width: 100%;
      height: 100%;
    }

    .startButton {
      background-color: green;
    }

    .stopButton {
      background-color: red;
    }

    .loadingButton {
      background-color: grey;
    }

    .button:active {
      background: blue;
    }
  }
</style>
