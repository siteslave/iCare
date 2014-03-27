$(function(){

    var rpt_anc = {};

    rpt_anc.ajax = {
        do_process: function (cb) {
            app.ajax('/anc/do_process', {}, function (e) {
               e ? cb (e, null) : cb (null);
            });
        },

        get_list: function (t, start, stop, cb) {
            app.ajax('/reports/anc/list', {
                t: t,
                start: start,
                stop: stop
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        search: function (cid, cb) {
            app.ajax('/reports/anc/search', {
                cid: cid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        forecast_filter: function (start_date, end_date, cb) {
            app.ajax('/reports/anc/forecast_filter', {
                s: start_date,
                e: end_date
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total: function (t, cb) {
            app.ajax('/reports/anc/total', {
                t: t
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.total);
            });
        }
    };

    $('#btn_process').on('click', function(e) {
        e.preventDefault();

        if(confirm('คุณต้องการประมวลผลข้อมูลใหม่ ใช่หรือไม่?')) {
            rpt_anc.ajax.do_process(function(e) {
                if(e) {
                    app.alert(e);
                } else {
                    app.alert('ประมวลผลเสร็จเรียบร้อยแล้ว');
                    rpt_anc.get_list('-1');
                }
            });
        }
    });

    $('#btn_refresh').on('click', function(e) {
        e.preventDefault();
        rpt_anc.get_list('-1');
    });

    rpt_anc.set_list = function(v) {

        $('#tbl_list > tbody').empty();

        if($(v).size()) {

            $(v).each(function(i, v) {

                var cov01, cov02, cov03, cov04, cov05;

                $(v.coverages).each(function(i, v) {

                    if(v.ancno == '1') cov01 = v.date_serv ? '<span class="text-success"><strong>' + app.dbpop2thai_date(v.date_serv) + '</strong></span>' : '<span class="text-danger">' + app.dbpop2thai_date(v.forecast) + '</span>';
                    if(v.ancno == '2') cov02 = v.date_serv ? '<span class="text-success"><strong>' + app.dbpop2thai_date(v.date_serv) + '</strong></span>' : '<span class="text-danger">' + app.dbpop2thai_date(v.forecast) + '</span>';
                    if(v.ancno == '3') cov03 = v.date_serv ? '<span class="text-success"><strong>' + app.dbpop2thai_date(v.date_serv) + '</strong></span>' : '<span class="text-danger">' + app.dbpop2thai_date(v.forecast) + '</span>';
                    if(v.ancno == '4') cov04 = v.date_serv ? '<span class="text-success"><strong>' + app.dbpop2thai_date(v.date_serv) + '</strong></span>' : '<span class="text-danger">' + app.dbpop2thai_date(v.forecast) + '</span>';
                    if(v.ancno == '5') cov05 = v.date_serv ? '<span class="text-success"><strong>' + app.dbpop2thai_date(v.date_serv) + '</strong></span>' : '<span class="text-danger">' + app.dbpop2thai_date(v.forecast) + '</span>';
                });

                $('#tbl_list > tbody').append(
                    '<tr>' +
                        '<td>' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td class="text-center">' + v.age.year + '</td>' +
                        '<td class="text-center">' + cov01 + '</td>' +
                        '<td class="text-center">' + cov02 + '</td>' +
                        '<td class="text-center">' + cov03 + '</td>' +
                        '<td class="text-center">' + cov04 + '</td>' +
                        '<td class="text-center">' + cov05 + '</td>' +
                        '</tr>'
                );
            });

        } else {

            $('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบรายการ</td></tr>');

        }

    };

    rpt_anc.get_list = function(t) {

        rpt_anc.ajax.get_total(t, function(e, total) {
            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');
                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('rpt_anc_paging'),
                    onSelect: function(page) {
                        app.set_cookie('rpt_anc_paging', page);

                        rpt_anc.ajax.get_list(t, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                rpt_anc.set_list(rs);
                            }
                        });

                    },
                    onFormat: app.setPagingFormat
                });
            }
        });

    };

    $('#btn_filter').on('click', function(e) {

        e.preventDefault();

        var start_date = $('#txt_start_date').val();
        var end_date = $('#txt_end_date').val();

        if(start_date && end_date) {

            $('#tbl_list > tbody').empty();

            rpt_anc.ajax.forecast_filter(start_date, end_date, function(e, v) {
               if(e) {
                   app.alert(e);
                   $('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบข้อมูล</td></td></tr>');
               } else {
                   $('#paging').fadeOut('slow');
                   rpt_anc.set_list(v);
               }
            });
        } else {
            app.alert('กรุณาระบุช่วงวันที่ต้องการ');
        }
    });

    //search
    $('#btn_search').on('click', function(e) {
        e.preventDefault();

        var cid = $('#txt_query').val();

        if(!cid) {
            app.alert('กรุณาระบุเลขบัตรประชาชน');
        } else {
            rpt_anc.ajax.search(cid, function(e, v) {
                if(e) {
                    app.alert(e);
                } else {
                    $('#paging').fadeOut('slow');
                   rpt_anc.set_list(v);
                }
            });
        }
    });

    //get all list
    rpt_anc.get_list('-1');

});