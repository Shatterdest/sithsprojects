<template>
  <div class="header flex flex-col w-1/2 justify-center m-auto">
  </div>
  <Bar :data="chartData" :options="chartOptions" :key="key" class="mb-36" />
</template>

<script setup>
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  ArcElement
} from 'chart.js'
import { fetchData, routes } from '@/stores/store'
import { doLabels } from '@/stores/store'
import { onBeforeMount } from 'vue'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement)
let key = 0
let chartData = {
  labels: ['B', 'F', 'D', 'M'],
  datasets: [
    {
      label: 'Number of Routes for the B,F,D,M at any given time',
      backgroundColor: '#f87979',
      data: routes.value
    }
  ]
}

const props = ['data']
const data = props.data
onBeforeMount(() => {
  rereload()
})

const chartOptions = {
  maintainAspectRatio: true,
  aspectRatio: 16 / 9,
  responsive: true
}

function reload() {
  fetchData('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm')
  doLabels(data)
  key += 1
  console.log('reloading' + routes.value)
  chartData = {
  labels: ['B', 'F', 'D', 'M'],
  datasets: [
    {
      label: 'Number of Routes for the B,F,D,M at any given time',
      backgroundColor: '#f87979',
      data: routes.value
    }
  ]
}
  console.log('reloaded')
}

function rereload() {
  reload()
  setInterval(reload(), 5000)
}


</script>
<style scoped></style>
