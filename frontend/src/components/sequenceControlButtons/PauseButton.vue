<template>
  <v-btn
    class="ml-4"
    color="grey"
    :loading="loading"
    :disabled="disabled"
    @click="$emit('click')"
  >
    <v-icon left>mdi-pause</v-icon>
    Pause
  </v-btn>
</template>

<script>
export default {
  name: 'PauseButton',
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
