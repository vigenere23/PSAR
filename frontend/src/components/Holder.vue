<template>
  <div class="holder main-divs R">
    <div class="title R">Status du préhenseur</div>
    <div class="content">
      <div class="status">
        <span>Status:</span>
        <div class="circle" id="first"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Holder'
}
</script>

<style lang="scss">
@import '~@/styles/component';
@import '~@/styles/colors';

.holder {

  .content {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
  }

  .circle {
    width: 40px;
    height: 40px;
    margin: 10px;
    background: none;
    border-radius: 50%;
    border: solid 2px $accent-color;
    background-color: $accent-color;
  }

  .status {
    display: flex;
    flex-direction: row;
    align-items: center;
    font-size: 24px;
    color: $accent-color;
  }
}
</style>
