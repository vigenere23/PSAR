<template>
  <div class="steps">
    <p v-for="(step, i) in previousSteps" :key="-1-i" class="previous">
      {{ `✓ ${step}` }}
    </p>

    <p class="current">{{ `➜ ${ongoingStep}` }}</p>

    <p v-for="(step, i) in upcomingSteps" :key="i">
      {{ `. ${step}` }}
    </p>
  </div>
</template>

<script>
// TODO this is temporary
import { steps } from '@/data/steps'
import { on } from '../api/eventHandlers/sequence'

export default {
  name: 'steps',
  data () {
    return {
      ongoingStep: '',
      previousSteps: [],
      upcomingSteps: []
    }
  },
  mounted () {
    this.previousSteps = steps.previousSteps
    this.upcomingSteps = steps.upcomingSteps
    this.ongoingStep = steps.ongoingStep

    on('task_started', (task) => { console.log(`task '${task}' started`) })
    on('task_ended', (task) => { console.log(`task '${task}' ended`) })
  }
}
</script>

<style lang="scss">
@import '~styles/fonts';
@import '../assets/scss/fonts';

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

  .previous {
    color: grey;
  }

  button {
    align-self: end;
  }
}
</style>
