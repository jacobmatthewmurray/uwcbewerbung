
$(function() {
    $.ajax({
        url: "data",
        dataType: "json",
        type: "GET",
        success: function(result){

            var ctx = document.getElementById("chartTopLeft").getContext("2d");

            var labels = result.map(function(e) {
                return e.bundesland__bundesland;
            });

            var data = result.map(function(e) {
                return e.schoolcnt;
            });

            new Chart (ctx, {
                type: 'bar',
                            
                data: {
                    labels: labels,
                    datasets: [{
                        label: "School Count",
                        backgroundColor: 'rgb(153, 204, 204)',
                        data: data,
                    }]
                },

                options: {
                    scales: {
                        xAxes: [{
                            ticks: {
                                autoSkip: false
                            }
                        }]
                    }
                }

            });
        }    
    }) 
});