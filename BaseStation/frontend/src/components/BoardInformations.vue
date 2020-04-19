<template>
  <div class="board-informations main-divs">
    <div class="title R">Coins et directions des rondelles</div>
    <div class="content">
      <div>{{ firstPuckPosition }}</div>
      <div>{{ secondPuckPosition }}</div>
      <div>{{ thirdPuckPosition }}</div>
      <div v-if="clockwise">
        <v-icon class="arrow">
        mdi-subdirectory-arrow-left
        </v-icon>
      </div>
      <div v-else>
        <v-icon class="arrow">
          mdi-subdirectory-arrow-right
        </v-icon>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BoardInformations',
  data () {
    return {
      firstPuckPosition: 2,
      secondPuckPosition: 3,
      thirdPuckPosition: 4,
      clockwise: true
    }
  }
}
</script>

<style lang="scss">
@import '~@/styles/fonts';
@import '~@/styles/colors';

.board-informations {
  .content {
    display: flex;
    width: 100%;

    > div {
      border: $full-border;
      flex-grow: 1;
      display: flex;
      justify-content: center;
      align-items: center;
      font-weight: bold;

      .arrow {
        transform: rotate(180deg);
      }
    }
  }
}
</style>
