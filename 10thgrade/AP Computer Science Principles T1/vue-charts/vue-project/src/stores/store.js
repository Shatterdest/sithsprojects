import { ref } from 'vue'
import GtfsRealtimeBindings from 'gtfs-realtime-bindings'

export const usedata = ref([])
export const labels = ref([])
export const routes = ref([0, 0, 0, 0])
export const fetchData = async function (urlInput) {
  const data = ref([])
  const gooddata = ref([])
  gooddata.value = []
  usedata.value = []
  try {
    const response = await fetch(urlInput, {
      headers: {
        'x-api-key': 'Lbc0gTUOwm8GvqZgMmu2t3MEktcvreZr8wiuihJn'
        // replace with your GTFS-realtime source's auth token
        // e.g. x-api-key is the header value used for NY's MTA GTFS APIs
      }
    })
    if (!response.ok) {
      const error = new Error(`${response.url}: ${response.status} ${response.statusText}`)
      error.response = response
      throw error
    }
    const buffer = await response.arrayBuffer()
    const feed = GtfsRealtimeBindings.transit_realtime.FeedMessage.decode(new Uint8Array(buffer))
    data.value = feed.entity

    data.value.forEach((el, i) => {
      if (Object.prototype.hasOwnProperty.call(el, 'vehicle')) {
        let pushed = { vehicle: el, tripUpdate: data.value[i - 1] }
        gooddata.value.push(pushed)
      }
    })
    gooddata.value.forEach((el) => {
      usedata.value.push(el)
    })
  } catch (error) {
    console.log(error)
  }
  function createlabels() {
    labels.value = []
    usedata.value.forEach((el) => {
    labels.value.push(el.vehicle.vehicle.trip.routeId)
  })
  }
  createlabels()
  
}

export async function getPosition(options) {
  return new Promise((resolve, reject) =>
    navigator.geolocation.getCurrentPosition(resolve, reject, options)
  )
}

export const timeToStop = function (time) {
  let currentTime = Date.now()
  let currentTimeSeconds = toSeconds(currentTime)
  let timeLeftUntilStop = time - currentTimeSeconds
  return Math.round(timeLeftUntilStop / 60)
}
const toSeconds = function (digit) {
  return Math.round(digit / 1000)
}

export const dataForChart = function () {
  const returnedData = [0, 0, 0, 0]
  const data = usedata.value
  data.forEach((piece) => {
    switch (piece.vehicle.vehicle.trip.routeId) {
      case 'B':
        returnedData[0] = Number(mostCommon(count(piece)))
        break
      case 'D':
        count(piece)
        returnedData[1] = Number(mostCommon(count(piece)))
        break
      case 'F':
        count(piece)
        returnedData[2] = Number(mostCommon(count(piece)))
        break
      case 'M':
        count(piece)
        returnedData[3] = Number(mostCommon(count(piece)))
        break
    }
  })

  return returnedData
}
function count(piece) {
  let count = []
  piece.tripUpdate.tripUpdate.stopTimeUpdate.forEach((stop) => {
    count.push(timeToStop(stop.arrival.time))
  })
  return count
}
function mostCommon(arr) {
  let mode = arr.reduce(
    (a, b, i, arr) =>
      arr.filter((v) => v === a).length >= arr.filter((v) => v === b).length ? a : b,
    null
  )
  if (mode == undefined) {
    return 0
  } else {
    return mode
  }
}

export function doLabels() {
  routes.value= [0,0,0,0]
  labels.value.forEach((el) => {
    if (el === 'B') {
      routes.value[0]++
    } else if (el === 'F') {
      routes.value[1]++
    } else if (el === 'D') {
      routes.value[2]++
    } else {
      routes.value[3]++
    }
  })
}
