$(function () {

    var chart_builder = JSON.parse('{{ chart_builder|escapejs|safe }}')
    
    for(var plot in chart_builder){
        if(Object.keys(chart_builder[plot]).length !== 0) {
            $('#render_target').append(
                '<div class="col-md-'+chart_builder[plot].col_size+'">'+'<div class="card">'+'<div class="card-body">'+'<div id="chart">'+'<canvas id="'+chart_builder[plot].id_name+'" style="min-height: 250px; height: 250px; max-height: 250px; max-width: 100%;"></canvas>'+'</div>'+'</div>'+'</div>'+'</div>'
            )
            var chartCanvas = $('#'+chart_builder[plot].id_name).get(0).getContext('2d')
            var chartData = {
                labels: chart_builder[plot].data.labels,
                datasets: [{
                    label: chart_builder[plot].data.datasets.label,
                    fill: chart_builder[plot].data.datasets.fill,
                    data: chart_builder[plot].data.datasets.data
                }]
            }
            var chartOptions = {
                maintainAspectRatio: chart_builder[plot].options.maintainAspectRatio,
                responsive: chart_builder[plot].options.responsive 
            }
            new Chart(chartCanvas,{
                type: chart_builder[plot].type,
                data: chartData,
                options: chartOptions
            })
        
        }
    }

})