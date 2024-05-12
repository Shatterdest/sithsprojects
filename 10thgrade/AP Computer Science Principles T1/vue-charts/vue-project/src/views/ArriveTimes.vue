<template>
  <div>
    <div class="select-wrap">
      <label for="select">Selected: {{ select }}</label>
      <select v-model="select" name="select" id="select">
        <option disabled value="">--Select a Train--</option>
        <option value="">All</option>
        <option>B</option>
        <option>D</option>
        <option>F</option>
        <option>M</option>
      </select>
    </div>
    <div v-if="data[0]">
      <div v-if="select === ''">
        <div v-for="item in data" :key="item.id">
          <div v-if="stops[item.vehicle.vehicle.stopId]" class="card">
            <h2>{{ item.vehicle.vehicle.trip.routeId }}</h2>
            <h2>{{ routes[item.vehicle.vehicle.trip.routeId].route_long_name }}</h2>
            <h2>Currently stopped at: {{ stops[item.vehicle.vehicle.stopId].stop_name }}</h2>

            <h3 v-for="stop in item.tripUpdate.tripUpdate.stopTimeUpdate" :key="stop.arrival.time">
              <h3 v-if="stops[stop.stopId]">
                Arrives at {{ stops[stop.stopId].stop_name }} in
                {{ timeToStop(stop.arrival.time) }} minutes.
              </h3>
            </h3>
          </div>
        </div>
      </div>
      <div v-else>
        <div v-if="sort(select)[0]">
          <div v-for="item in sort(select)" :key="item.id">
            <div v-if="stops[item.vehicle.vehicle.stopId]" class="card">
              <h2>{{ item.vehicle.vehicle.trip.routeId }}</h2>
              <h2>{{ routes[item.vehicle.vehicle.trip.routeId].route_long_name }}</h2>
              <h2>Currently stopped at: {{ stops[item.vehicle.vehicle.stopId].stop_name }}</h2>
              <h3
                v-for="stop in item.tripUpdate.tripUpdate.stopTimeUpdate"
                :key="stop.arrival.time"
              >
                <h3 v-if="stops[stop.stopId]">
                  Arrives at {{ stops[stop.stopId].stop_name }} in
                  {{ timeToStop(stop.arrival.time) }} minutes.
                </h3>
              </h3>
            </div>
          </div>
        </div>
        <div v-else class="text-center">Information Not Available!</div>
      </div>
    </div>
      <h1 v-else class="text-center" >No Data Available! Please refresh or try again later!</h1>
  </div>
</template>

<script setup>
import { usedata as data } from '@/stores/store'
import { stops } from '@/stores/google_transit/stops'
import { routes } from '@/stores/google_transit/routes'
import { onBeforeMount, ref } from 'vue'
import { fetchData } from '@/stores/store'
import { timeToStop } from '@/stores/store'

const select = ref('')

onBeforeMount(() => {
  fetchData('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm')
})

const sort = function (route) {
  const sorted = []
  data.value.forEach((piece) => {
    if (piece.vehicle.vehicle.trip.routeId == route) {
      sorted.push(piece)
    }
  })
  return sorted
}
</script>

<style lang="css" scoped>
h2 {
  font-size: 1.5rem;
}

h3 {
  font-size: 1.2rem;
}

.card {
  border: solid black 5px;
  width: 90vw;
  margin: auto;
  margin-bottom: 1%;
  padding: 1%;
}

.select-wrap {
  text-align: center;
}

select {
  display: block;
  margin: 1% auto;
}
</style>
@/stores/google_transit/stops
