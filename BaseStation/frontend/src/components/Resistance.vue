<template>
  <div class="resistance main-divs L">
    <div class="title L">Resistance: {{value}}</div>
    <div class="circles">
      <template v-if="colors.length">
        <div class="circle" v-for="(color, i) in colors" :key="i" :style="{ backgroundColor: getColor(i), borderColor: getColor(i) }" />
      </template>
      <template v-else>
        <div class="circle empty" v-for="i in 3" :key="i" />
      </template>
    </div>
  </div>
</template>

<script>
import { colorsToHex } from '@/assets/js/resistanceColors'

export default {
  name: 'Resistance',
  data () {
    return {
      value: 120,
      colors: [
        'green',
        'blue',
        'purple'
      ]
    }
  },
  methods: {
    getColor (index) {
      return colorsToHex[this.colors[index]]
    }
  }
}
</script>

<style lang="scss">
@import '~@/styles/component';
@import '~@/styles/colors';

.resistance {
  .circles {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
  }

  .circle {
    width: 40px;
    height: 40px;
    margin: 10px;
    border-radius: 50%;
    border-size: 2px;
    border-style: solid;

    &.empty {
      border-color: $accent-color;
    }
  }
}
</style>
