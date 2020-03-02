<template>
  <div class="resistance">
    <p>Resistance: {{value}}</p>
    <div class="circlesContainer">
      <div class="circle" id="first"></div>
      <div class="circle" id="second"></div>
      <div class="circle" id="third"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Resistance',
  data () {
    return {
      value: 0
    }
  },
  async mounted () {
    this.value = 120
  }
}
</script>

<style lang="scss">
  .resistance {
    background: red;
    text-align: center;

    .circlesContainer {
      display: flex;
      justify-content: center;

    }

    .circle {
      width: 50px;
      height: 50px;
      margin: 10px;
      background: darkgrey;
      border-radius: 50%
    }
  }

</style>
