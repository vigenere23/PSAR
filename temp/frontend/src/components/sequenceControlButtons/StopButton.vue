<template>
  <v-btn
    class="ml-4"
    color="red"
    :loading="loading"
    :disabled="disabled"
    @click="$emit('click')"
  >
    <v-icon left>mdi-stop</v-icon>
    Stop
  </v-btn>
</template>

<script>
export default {
  name: 'StopButton',
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
