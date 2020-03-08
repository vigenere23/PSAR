<template>
  <div class="home-page">
    <div class="left">
      <Tasks />
    </div>

    <div class="center">
      <div class="center__top">
        <Resistance class="resistance" />
        <Holder class="holder" />
      </div>
      <Camera class="world-camera" />
      <div class="center__bottom">
        <RobotController class="robot-controller" />
        <Camera class="robot-camera" />
      </div>
    </div>

    <div class="right">
      <span>Other modules here</span>
    </div>
  </div>
</template>

<script>
import Tasks from '@/components/Tasks'
import Camera from '@/components/Camera'
import Resistance from '@/components/Resistance'
import Holder from '@/components/Holder'
import RobotController from '@/components/RobotController'

export default {
  name: 'home',
  components: {
    RobotController,
    Holder,
    Resistance,
    Camera,
    Tasks
  }
}
</script>

<style lang="scss">
@import '~@/styles/fonts';

.home-page {
  width: 100%;
  height: 100%;
  display: flex;

  > * {
    border: solid 1px black;
  }

  .left, .center, .right {
    flex-grow: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
  }

  .left {
    width: 280px;
    flex-shrink: 0;
    flex-grow: 0;
  }

  .center {
    > * {
      border: solid 1px black;
    }

    &__top {
      display: flex;
      width: 100%;
      height: 140px;
    }

    &__bottom {
      display: flex;
      height: 240px;
    }
  }

  .right {
    width: 360px;
    flex-shrink: 0;
    flex-grow: 0;
  }

  .tasks {
    flex-grow: 1;
  }

  .resistance {
    background-color: red;
    flex-grow: 1;
  }

  .world-camera {
    background-color: purple;
    flex-grow: 1;
  }

  .robot-camera {
    background-color: purple;
    height: 100%;
    width: 400px;
  }

  .holder {
    background-color: coral;
    flex-grow: 1;
  }

  .robot-controller {
    background-color: green;
    height: 100%;
    width: 240px;
  }
}
</style>
