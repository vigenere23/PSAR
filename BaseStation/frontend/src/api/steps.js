export default {
  async getSteps () {
    return {
      ongoingStep: 'déplacer robot vers tableau de commande sens',
      previousSteps: [
        'calibrer',
        'déplacer robot vers station de lecture résistance',
        'calculer résistance',
        'déplacer robot vers tableau de commande origine',
        'prendre capture caméra robot'
      ],
      upcomingSteps: [
        'prendre capture caméra robot',
        'déplacer robot vers rondelle 1 : rouge',
        'prendre rondelle 1 : rouge',
        'déplacer robot vers rondelle 2 : vert',
        'prendre rondelle 2 : vert',
        'déplacer robot vers rondelle 3 : bleu',
        'prendre rondelle 3 : bleu',
        'etc.'
      ]
    }
  }
}
