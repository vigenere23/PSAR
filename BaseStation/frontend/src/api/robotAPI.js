const axios = require('axios')

const httpClient = axios.create({
  baseURL: 'http://localhost:8080',
  headers: {
    'Content-Type': 'application/json'
  }
})

const END_POINT = '/inquiryy'

const moveY = (units) => httpClient.post(END_POINT, { units })
  .catch((error) => { return error.response })

const moveX = (units) => httpClient.post(END_POINT, { units })
  .catch((error) => { return error.response })

export {
  moveX,
  moveY
}
