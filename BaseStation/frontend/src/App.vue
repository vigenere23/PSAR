<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="scss">
@import '~styles/reset';
@include reset;

#app {
  background: pink;
}
</style>

<script>
import { on } from '@/api/eventHandlers/index'

export default {
  mounted () {
    on('connect', () => console.log('connected'))
    on('message', (message) => console.log(message))
  }
}
</script>
