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
      <energy-report></energy-report>
      <board-informations></board-informations>
      <square-diagram></square-diagram>
    </div>
  </div>
</template>

<script>
import Tasks from '@/components/Tasks'
import Camera from '@/components/Camera'
import Resistance from '@/components/Resistance'
import Holder from '@/components/Holder'
import RobotController from '@/components/RobotController'
import EnergyReport from '@/components/EnergyReport'
import BoardInformations from '@/components/BoardInformations'
import SquareDiagram from '@/components/SquareDiagram'

export default {
  name: 'home',
  components: {
    SquareDiagram,
    BoardInformations,
    EnergyReport,
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
@import '~@/styles/colors';

.home-page {
  width: 100%;
  height: 100%;
  display: flex;

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
    border: $full-border;
  }

  .center {
    &__top {
      display: flex;
      width: 100%;
      height: 140px;

      > * {
        border: $full-border;
      }
    }

    &__bottom {
      display: flex;
      flex-shrink: 0;
      flex-grow: 0;
      min-height: 175px;

      > * {
        border: $full-border;
      }
    }
  }

  .right {
    width: 360px;
    flex-shrink: 0;
    flex-grow: 0;
    border: $full-border;
  }

  .tasks {
    flex-grow: 1;
  }

  .resistance {
    flex-grow: 1;
  }

  .world-camera {
    flex-grow: 1;
    border: $full-border;
  }

  .robot-camera {
    height: 100%;
    width: 400px;
  }

  .holder {
    flex-grow: 1;
  }

  .robot-controller {
    height: 100%;
    width: 240px;
  }

  .board-informations {
    border: $full-border;
    height: 100px;
  }
}
</style>
