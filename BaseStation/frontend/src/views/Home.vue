<template>
  <div class="home-page">
    <steps></steps>
    <camera class="RCamera"></camera>
    <resistance></resistance>
    <camera class="WCamera"></camera>
    <StartStopButton></StartStopButton>
    <Holder></Holder>
    <Time></Time>
    <test-module></test-module>
  </div>
</template>

<script>
import Steps from '@/components/Steps/'
import Camera from '@/components/Camera/'
import Resistance from '@/components/Resistance/'
import StartStopButton from '@/components/StartStopButton/'
import Time from '@/components/Time/'
import Holder from '@/components/Holder/'
import TestModule from '@/components/TestModule/'

export default {
  name: 'home',
  components: {
    TestModule,
    Holder,
    Time,
    StartStopButton,
    Resistance,
    Camera,
    Steps
  }
}
</script>

<style lang="scss">
  @import '~styles/fonts';

  .home-page {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    align-content: flex-start;
    height: 720px;
  }

  .steps {
    border: solid;
    background: lightgreen;
    width: 280px;
    height: 540px;
  }

  .resistance {
    margin-left: -40px;
    width: 420px;
    height: 130px;
    border: solid;
  }

  .WCamera {
    margin-left: -40px;
    height: 410px;
    width: 730px;
    border: solid;
    background: purple;
  }

  .RCamera {
    width: 320px;
    height: 180px;
    border: solid;
    background: purple;
  }

  .startStopButton {
    width: 205px;
    height: 180px;
    border: solid;
  }

  .time {
    width: 485px;
    height: 180px;
    background: aqua;
    margin-top: 410px;
    margin-left: -485px;
    border: solid;
  }

  .holder {
    width: 320px;
    height: 130px;
    background: coral;
    margin-left: -320px;
    border: solid;
  }

  .testModule {
    height: 800px;
    width: 526px;
    background: green;
    border: solid;
  }
</style>
