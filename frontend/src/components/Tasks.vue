<template>
  <v-stepper v-model="ongoingTaskIndex" vertical class="tasks">
    <div class="title R">Étapes de la séquence </div>
    <template v-for="(task, i) in tasks">
      <v-stepper-step :key="i" :step="i + 1" :complete="doneTasks.includes(task)">
        {{ task }}
      </v-stepper-step>
    </template>
  </v-stepper>
</template>

<script>
import { on } from '../api/eventHandlers/sequence'

export default {
  name: 'steps',
  data () {
    return {
      // TODO fetch
      upcomingTasks: [
        'Task one',
        'Task two',
        'Task three',
        'Task four'
      ],
      doneTasks: [],
      ongoingTaskIndex: 0
    }
  },
  mounted () {
    on('started', (response) => this.resetTasks(response.tasks))
    on('task_started', this.onTaskStarted)
    on('task_ended', this.onTaskEnded)
  },
  computed: {
    tasks () {
      return this.doneTasks.concat(this.upcomingTasks)
    }
  },
  methods: {
    resetTasks (tasks) {
      this.doneTasks = []
      this.ongoingTaskIndex = 0
      this.upcomingTasks = tasks
    },
    onTaskStarted (task) {
      console.log(`Task '${task}' started`)
      const index = this.upcomingTasks.indexOf(task)
      if (index !== -1) {
        this.ongoingTaskIndex = this.doneTasks.length + index + 1
      }
    },
    onTaskEnded (task) {
      console.log(`Task '${task}' ended`)
      const index = this.upcomingTasks.indexOf(task)
      if (index !== -1) {
        this.doneTasks.push(task)
        this.upcomingTasks.splice(index, 1)
      }
    }
  }
}
</script>
