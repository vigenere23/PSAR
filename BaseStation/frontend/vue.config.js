const path = require('path')
module.exports = {
  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src/'),
        'styles': path.resolve(__dirname, 'src/assets/scss')
      }
    }
  }
}
