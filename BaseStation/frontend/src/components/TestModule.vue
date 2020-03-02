<template>
    <div class="testModule">
      <div class="arrowContainer">
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
import { move } from '../api/SequenceSocketEventEmitter'

export default {
  name: 'TestModule',
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
      move(this.x, this.y)
    },
    goRight () {
      this.x += this.speed
      move(this.x, this.y)
      console.log('right')
    },
    goForward () {
      this.y += this.speed
      move(this.x, this.y)
    },
    goBack () {
      this.y -= this.speed
      move(this.x, this.y)
    },
    stopLeft () {
      this.x += this.speed
      move(this.x, this.y)
    },
    stopRight () {
      this.x -= this.speed
      move(this.x, this.y)
    },
    stopBack () {
      this.y += this.speed
      move(this.x, this.y)
    },
    stopForward () {
      this.y -= this.speed
      move(this.x, this.y)
    }
  }
}
</script>

<style lang="scss">
  .testModule {
    display:flex;
    justify-content: center;
    align-items: center;
  }

  .arrow {
    height: 100px;
    width: 100px;
    border-right: 20px solid;
    border-bottom: 20px solid;
  }

  .arrow:active {
    border-right: 20px solid white;
    border-bottom: 20px solid white;
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
    height: 100px;
    width: 100px;
  }

  .arrowContainer {
    width: 300px;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }
</style>
