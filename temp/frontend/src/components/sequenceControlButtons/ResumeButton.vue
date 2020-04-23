<template>
  <v-btn
    class="ml-4"
    color="grey"
    :loading="loading"
    :disabled="disabled"
    @click="$emit('click')"
  >
    <v-icon left>mdi-play</v-icon>
    Resume
  </v-btn>
</template>

<script>
export default {
  name: 'ResumeButton',
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
