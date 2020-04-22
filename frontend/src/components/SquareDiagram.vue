<template>
  <div class="square-diagram main-divs">
    <div class="title R">Status de la station de base</div>
    <div class="container">
      <div class="square">
        <div class="circle circle-L circle-T" :style="{ background: getColor(0)}">1</div>
        <div class="circle circle-R circle-T" :style="{ background: getColor(1)}">2</div>
        <div class="circle circle-R circle-B" :style="{ background: getColor(2)}">3</div>
        <div class="circle circle-L circle-B" :style="{ background: getColor(3)}">4</div>
      </div>
    </div>
  </div>

</template>

<script>
import { colorsToHex } from '@/assets/js/resistanceColors'
export default {
  name: 'Square-diagram',
  data () {
    return {
      circles: [
        'none',
        'green',
        'blue',
        'purple'
      ]
    }
  },
  methods: {
    getColor (index) {
      const color = this.circles[index]
      if (color !== 'none') {
        return colorsToHex[color]
      }
    }
  }
}
</script>

<style lang="scss">
@import '~@/styles/fonts';
@import '~@/styles/colors';

$circle-size: 40px;

.square-diagram {

  .container {
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .square {
    width: 50%;
    padding-top: 50%;
    border: $full-border;
  }

  .circle {
    width: $circle-size;
    height: $circle-size;
    border-radius: 50%;
    border: $full-border;
    background: $first-half-gradient;
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
  }

  .circle-L {
    left: -$circle-size / 2;
  }

  .circle-R {
    right: -$circle-size / 2;
  }

  .circle-T {
    top: -$circle-size / 2;
  }

  .circle-B {
    bottom: -$circle-size / 2;
  }
}
</style>
