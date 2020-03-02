<template>
  <div class="startStopButton">
    <div class="startButton" v-if="!started" @click="start">START</div>
    <div class="stopButton" v-else @click="stop">STOP</div>
  </div>
</template>

<script>
import io from 'socket.io-client'
const path = 'http://localhost:5000'
const socket = io.connect(path)
const sequenceSocket = io.connect(path + '/sequence')
const logMessage = message => console.log(message)

export default {

  name: 'StartStopButton',
  data () {
    return {
      interval: false,
      started: false
    }
  },
  beforeMount () {
    socket.on('connect', () => {
      sequenceSocket.emit('start')
      console.log('worked')
    })
    socket.on('message', logMessage)
  },
  methods: {
    start () {
      this.started = true
    },

    stop () {
      this.started = false
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
