<template>
    <div class="testModule">
      <div class="arrowContainer">
        <div class="void"></div>
        <div class="arrow" id="arrowUp" @mousedown="goForward" @mouseup="stop"></div>
        <div class="void"></div>
        <div class="arrow" id="arrowLeft" @mousedown="goLeft" @mouseup="stop"></div>
        <div class="void"></div>
        <div class="arrow" id="arrowRight" @mousedown="goRight" @mouseup="stop"></div>
        <div class="void">{{unit}}</div>
        <div class="arrow" id="arrowDown" @mousedown="goBack" @mouseup="stop"></div>
        <div class="void"></div>
      </div>
    </div>
</template>

<script>

export default {
  name: 'TestModule',
  data () {
    return {
      interval: false,
      unit: 0
    }
  },
  methods: {

    goLeft () {
      if (!this.interval) {
        this.interval = setInterval(() => this.unit++, 30)
      }
    },

    goRight () {
      if (!this.interval) {
        this.interval = setInterval(() => this.unit++, 30)
      }
    },

    goForward () {
      if (!this.interval) {
        this.interval = setInterval(() => this.unit++, 30)
      }
    },

    goBack () {
      if (!this.interval) {
        this.interval = setInterval(() => this.unit++, 30)
      }
    },

    stop () {
      clearInterval(this.interval)
      this.interval = false
      this.unit = 0
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
