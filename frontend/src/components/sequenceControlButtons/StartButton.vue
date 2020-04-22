<template>
  <v-btn
    class="ml-4"
    color="green"
    :loading="loading"
    :disabled="disabled"
    @click="$emit('click')"
  >
    <v-icon left>mdi-playlist-play</v-icon>
    Start
  </v-btn>
</template>

<script>
export default {
  name: 'StartButton',
  props: {
    loading: {
      type: Boolean,
      default: false
    },
    disabled: {
      type: Boolean,
      default: false
    }
  }
}
</script>
