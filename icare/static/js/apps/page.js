
google.load('visualization', '1', {packages:['gauge']});
google.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
      ['Label', 'Value'],
      ['ANC 5  ครั้ง', 80]
    ]);

    var data2 = google.visualization.arrayToDataTable([
      ['Label', 'Value'],
      ['12 สัปดาห์', 48]
    ]);

    var options = {
      width: 200, height: 200,
      redFrom: 0, redTo: 50,
      yellowFrom:51, yellowTo: 89,
      greenFrom: 90, greenTo: 100,
      minorTicks: 5
    };

    var options2 = {
      width: 200, height: 200,
      redFrom: 0, redTo: 39,
      yellowFrom:40, yellowTo: 59,
      greenFrom: 60, greenTo: 100,
      minorTicks: 5
    };

    var chart = new google.visualization.Gauge(document.getElementById('anc_chart'));
    chart.draw(data, options);

    var chart = new google.visualization.Gauge(document.getElementById('anc_chart2'));
    chart.draw(data2, options2);
}


$(function() {
    var pages = {};
    ///
    pages.ajax = {
        get_mch_list: function(cb) {
            app.ajax('/reports/mch/get_forecast_dashboard', {}, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_anc_list: function(cb) {
            app.ajax('/reports/anc/get_forecast_dashboard', {}, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        }
    };

    pages.ajax.get_mch_list(function(e, v) {

        $('#tbl_mch_list > tbody').empty();

        if(e) {
            app.alert(e);
            $('#tbl_mch_list > tbody').append('<tr><td colspan="3">ไม่พบรายการ</td></tr>');
        } else {

            if($(v).size()) {
                $('#spn_mch_total').html($(v).size().toFixed());
                var i = 0;
                $(v).each(function(ix, r) {
                   if(i <= 4) {
                        $('#tbl_mch_list > tbody').append(
                            '<tr>' +
                                '<td>' + r.cid + '</td>' +
                                '<td>' + r.fullname + '</td>' +
                                '<td>' + r.age.year + '</td>' +
                            '</tr>'
                        );
                   }
                   i++;
                });
            } else {
                $('#tbl_mch_list > tbody').append('<tr><td colspan="3">ไม่พบรายการ</td></tr>');
            }
        }
    });

    pages.ajax.get_anc_list(function(e, v) {

        $('#tbl_anc_list > tbody').empty();

        if(e) {
            app.alert(e);
            $('#tbl_anc_list > tbody').append('<tr><td colspan="3">ไม่พบรายการ</td></tr>');
        } else {

            if($(v).size()) {
                $('#spn_anc_total').html($(v).size().toFixed());
                var i = 0;
                $(v).each(function(ix, r) {
                   if(i <= 4) {
                        $('#tbl_anc_list > tbody').append(
                            '<tr>' +
                                '<td>' + r.cid + '</td>' +
                                '<td>' + r.fullname + '</td>' +
                                '<td>' + r.age.year + '</td>' +
                            '</tr>'
                        );
                   }
                   i++;
                });
            } else {
                $('#tbl_anc_list > tbody').append('<tr><td colspan="3">ไม่พบรายการ</td></tr>');
            }
        }
    });
});