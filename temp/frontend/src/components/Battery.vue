<template>
  <div class="battery">
    <span class="label">Robot:</span>
    <div class="batteryIcon">
      <div class="batteryContainer" :style="{ width: `${containerWidth}px` }" />
      <div class="charge" :style="{ width: `${charge * containerWidth}px` }" />
    </div>
    <div class="chargeValue">{{ charge * 100 }}%</div>
  </div>
</template>

<script>
export default {
  name: 'Battery',
  data () {
    return {
      containerWidth: 40,
      charge: 0.4 // in %
    }
  }
}
</script>

<style lang="scss">
@import '~@/styles/colors';

.battery {
  display: flex;
  align-items: center;

  .batteryContainer {
    height: 10px;
    background: none;
    border: solid 1px $text-color;
  }

  .charge {
    height: 10px;
    background: $text-color;
    position: absolute;
    top: 0;
    left: 0;
  }

  .batteryIcon {
    margin-right: 10px;
  }

  .label {
    margin-right: 5px;
  }
}
</style>
