<template>
  <div class="steps">
    <p v-for="(step, i) in previousSteps" :key="-1-i">
      {{ `✓ ${step}` }}
    </p>

    <p class="current">{{ `➜ ${ongoingStep}` }}</p>

    <p v-for="(step, i) in upcomingSteps" :key="i">
      {{ `. ${step}` }}
    </p>
  </div>
</template>

<script>
import api from '@/api/steps'

export default {
  name: 'steps',
  data () {
    return {
      ongoingStep: '',
      previousSteps: [],
      upcomingSteps: []
    }
  },
  async mounted () {
    const response = await api.getSteps()
    this.previousSteps = response.previousSteps
    this.upcomingSteps = response.upcomingSteps
    this.ongoingStep = response.ongoingStep
  }
}
</script>

<style lang="scss">
@import '~styles/fonts';

.steps {
  font-family: $monospace;
  padding: 8px;
  height: 9em;
  width: 500px;
  overflow: auto;

  p {
    margin: 0;
    font-size: 14px;
  }

  .current {
    font-weight: 700;
  }
}
</style>
