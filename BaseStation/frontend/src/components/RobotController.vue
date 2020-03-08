<template>
    <div class="test-module">
      <div class="arrow-container">
        <div class="void"></div>
        <div class="arrow" id="arrowUp" @mousedown="goForward" @mouseup="stopForward"></div>
        <div class="void"></div>
        <div class="arrow" id="arrowLeft" @mousedown="goLeft" @mouseup="stopLeft"></div>
        <div class="void"></div>
        <div class="arrow" id="arrowRight" @mousedown="goRight" @mouseup="stopRight"></div>
        <div class="void"></div>
        <div class="arrow" id="arrowDown" @mousedown="goBack" @mouseup="stopBack"></div>
        <div class="void"></div>
      </div>
    </div>
</template>

<script>
import { sendMove } from '@/api/eventEmitters/debugRobot'

export default {
  name: 'RobotController',
  data () {
    return {
      interval: false,
      unit: 0,
      y: 0,
      x: 0,
      speed: 25
    }
  },
  methods: {
    goLeft () {
      this.x -= this.speed
      sendMove(this.x, this.y)
    },
    goRight () {
      this.x += this.speed
      sendMove(this.x, this.y)
      console.log('right')
    },
    goForward () {
      this.y += this.speed
      sendMove(this.x, this.y)
    },
    goBack () {
      this.y -= this.speed
      sendMove(this.x, this.y)
    },
    stopLeft () {
      this.x += this.speed
      sendMove(this.x, this.y)
    },
    stopRight () {
      this.x -= this.speed
      sendMove(this.x, this.y)
    },
    stopBack () {
      this.y += this.speed
      sendMove(this.x, this.y)
    },
    stopForward () {
      this.y -= this.speed
      sendMove(this.x, this.y)
    }
  }
}
</script>

<style lang="scss">
$arrow-size: 60px;
$border-size: $arrow-size / 5;

.test-module {
  display:flex;
  justify-content: center;
  align-items: center;
}

.arrow-container {
  width: $arrow-size * 3;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;

  .arrow {
    height: $arrow-size;
    width: $arrow-size;
    border-right: $border-size solid;
    border-bottom: $border-size solid;
  }

  .arrow:active {
    border-right: $border-size solid white;
    border-bottom: $border-size solid white;
  }

  #arrowUp {
    transform: rotate(-135deg);
  }

  #arrowDown {
    transform: rotate(45deg);
  }

  #arrowLeft {
    transform: rotate(135deg);
  }

  #arrowRight {
    transform: rotate(-45deg);
  }

  .void {
    height: $arrow-size;
    width: $arrow-size;
  }
}
</style>
