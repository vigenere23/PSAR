<template>
    <div
      class="robot-controller main-divs"
      tabindex="0"
      @keydown.up="goForward" @keyup.up="stopForward"
      @keydown.left="goLeft" @keyup.left="stopLeft"
      @keydown.right="goRight" @keyup.right="stopRight"
      @keydown.down="goBack" @keyup.down="stopBack"
    >
      <div class="arrows">
        <div class="void"></div>
        <div class="arrow" :class="{ active: !!actives['up'] }" id="arrow-up" @mousedown="goForward" @mouseup="stopForward" />
        <div class="void"></div>
        <div class="arrow" :class="{ active: !!actives['left'] }" id="arrow-left" @mousedown="goLeft" @mouseup="stopLeft" />
        <div class="void"></div>
        <div class="arrow" :class="{ active: !!actives['right'] }" id="arrow-right" @mousedown="goRight" @mouseup="stopRight" />
        <div class="void"></div>
        <div class="arrow" :class="{ active: !!actives['down'] }" id="arrow-down" @mousedown="goBack" @mouseup="stopBack" />
        <div class="void"></div>
      </div>
    </div>
</template>

<script>
import { sendMove } from '@/api/eventEmitters/debugRobot'
import Vue from 'vue'

export default {
  name: 'RobotController',
  data () {
    return {
      interval: false,
      unit: 0,
      y: 0,
      x: 0,
      speed: 25,
      actives: {}
    }
  },
  methods: {
    goLeft () {
      Vue.set(this.actives, 'left', true)
      this.x -= this.speed
      sendMove(this.x, this.y)
    },
    goRight () {
      Vue.set(this.actives, 'right', true)
      this.x += this.speed
      sendMove(this.x, this.y)
    },
    goForward () {
      Vue.set(this.actives, 'up', true)
      this.y += this.speed
      sendMove(this.x, this.y)
    },
    goBack () {
      Vue.set(this.actives, 'down', true)
      this.y -= this.speed
      sendMove(this.x, this.y)
    },
    stopLeft () {
      Vue.set(this.actives, 'left', false)
      this.x += this.speed
      sendMove(this.x, this.y)
    },
    stopRight () {
      Vue.set(this.actives, 'right', false)
      this.x -= this.speed
      sendMove(this.x, this.y)
    },
    stopForward () {
      Vue.set(this.actives, 'up', false)
      this.y -= this.speed
      sendMove(this.x, this.y)
    },
    stopBack () {
      Vue.set(this.actives, 'down', false)
      this.y += this.speed
      sendMove(this.x, this.y)
    }
  }
}
</script>

<style lang="scss">
@import '~@/styles/component';
@import '~@/styles/colors';

$arrow-size: 45px;
$border-size: $arrow-size / 5;

.robot-controller {
  display:flex;
  justify-content: center;
  align-items: center;

  .arrows {
    width: $arrow-size * 3;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;

    .arrow {
      height: $arrow-size;
      width: $arrow-size;
      border-right: $border-size solid $accent-color;
      border-bottom: $border-size solid $accent-color;

      &.active, &:active {
        border-right: $border-size solid $border-color;
        border-bottom: $border-size solid $border-color;
      }
    }

    #arrow-up {
      transform: rotate(-135deg);
    }

    #arrow-down {
      transform: rotate(45deg);
    }

    #arrow-left {
      transform: rotate(135deg);
    }

    #arrow-right {
      transform: rotate(-45deg);
    }

    .void {
      height: $arrow-size;
      width: $arrow-size;
    }
  }
}
</style>
