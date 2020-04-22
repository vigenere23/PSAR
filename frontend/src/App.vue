<template>
  <v-app id="app">
    <v-app-bar
      app
      color="primary"
      dark
    >
      <Timer></Timer>
      <SequenceControlButtons></SequenceControlButtons>
    </v-app-bar>

    <v-content id="content">
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import { on } from '@/api/eventHandlers/index'
import Timer from '@/components/Timer'
import SequenceControlButtons from '@/components/SequenceControlButtons'

export default {
  name: 'App',
  components: {
    Timer,
    SequenceControlButtons
  },
  mounted () {
    on('connect', () => console.log('connected'))
    on('message', (message) => console.log(message))
  }
}
</script>

<style lang="scss">
@import '~@/styles/reset';
@include reset;

#app {
  #content {
    overflow-x: auto;
  }
}

::-webkit-scrollbar {
  width: 0;
  height: 0;
  background: transparent //no ugly scrollbar
}
</style>
