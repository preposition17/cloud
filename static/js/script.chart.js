const temp_config = {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature for last hour',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [],
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
};

const hum_config = {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Humidity for last hour',
            backgroundColor: 'rgb(85,255,167)',
            borderColor: 'rgb(85,255,167)',
            data: [],
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
};


const tempChart = new Chart(
    document.getElementById('temp_canvas'),
    temp_config
);

const humChart = new Chart(
    document.getElementById('hum_canvas'),
    hum_config
);


waitFor(last_data, function () {
    last_data.forEach((element) => {

        var date = new Date(element.time * 1000);

        var hours = date.getHours();
        var minutes = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes();

        tempChart.data.labels.push(hours + ":" + minutes);
        tempChart.data.datasets[0].data.push(element.temp);

        humChart.data.labels.push(hours + ":" + minutes);
        humChart.data.datasets[0].data.push(element.hum);

    });
    tempChart.update();
    humChart.update();
});

