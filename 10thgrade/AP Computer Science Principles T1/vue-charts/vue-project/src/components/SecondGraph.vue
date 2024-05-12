<template>
  <div class="why-does-this-work">{{ dataForChart(data) }}</div>
  <Doughnut :key=0 id="my-chart-id" :options="chartOptions" :data="chartData" />
</template>

<script setup>
import { Doughnut } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { usedata as data, dataForChart, fetchData } from '@/stores/store'
import { onMounted } from 'vue'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
const chartNumbers = dataForChart(data)
let chartData = {
  labels: ['B', 'F', 'D', 'M'],
  datasets: [
    {
      label: 'Most common time to stop per line in minutes',
      backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
      data: Array
    }
  ]
}

onMounted(() => {
  fetchData('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm')
  chartData = {
    labels: ['B', 'F', 'D', 'M'],
    datasets: [
      {
        label: 'Most common time to stop per line in minutes',
        backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
        data: chartNumbers
      }
    ]
  }
  setInterval(function () {
    chartData = {
      labels: ['B', 'F', 'D', 'M'],
      datasets: [
        {
          label: 'Most common time to stop per line in minutes',
          backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
          data: chartNumbers
        }
      ]
    }
    this.key++
  }, 1000)
})

const chartOptions = {
  maintainAspectRatio: true,
  aspectRatio: 16 / 9,
  responsive: true
}
</script>

<style lang="css" scoped>
.why-does-this-work {
  visibility: hidden;
}
</style>
