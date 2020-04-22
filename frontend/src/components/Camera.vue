<template>
  <div class="camera main-divs R">
    <p>No signal</p>
  </div>
</template>

<script>
export default {
  name: 'Camera'
}
</script>

<style lang="scss">
@import '~@/styles/colors';

.camera {
  justify-content: center;
  background: $no-signals;

  p {
    margin: 0;
    font-weight: bold;
  }
}
</style>
