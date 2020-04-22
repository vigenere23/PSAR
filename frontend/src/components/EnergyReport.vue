<template>
  <div class="energy-report main-divs">
    <div class="title R">Rapport énergétique</div>
    <battery></battery>
    <p class="title">Consommation</p>
    <div class="report">
      <div><p><span class="label">Robot:</span> {{robot}}V</p>
        <p><span class="label">Roue 1:</span> {{r1}}V</p>
        <p><span class="label">Roue 2:</span> {{r2}}V</p>
      </div>
      <div>
        <p><span class="label">Préhenseur:</span> {{prehenseur}}V</p>
        <p><span class="label">Roue 3:</span> {{r3}}V</p>
        <p><span class="label">Roue 4:</span> {{r4}}V</p>
      </div>
    </div>
  </div>
</template>

<script>
import Battery from './Battery'
export default {
  name: 'EnergyReport',
  components: { Battery },
  data () {
    return {
      robot: 10,
      r1: 20,
      r2: 30,
      r3: 40,
      r4: 50,
      prehenseur: 60
    }
  }
}
</script>

<style lang="scss">

  .energy-report {
    .battery {
      align-self: flex-end;
      margin-top: 10px;
      margin-right: 10px;
    }

    .report {
      display: flex;
      justify-content: space-around;
      width: 100%;
    }

    .label {
      font-weight: bold;
    }
  }

</style>
