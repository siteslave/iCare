$(function() {
    var labor = {};

    labor.ajax = {
        get_list: function(start_date, end_date, start, stop, cb) {
            app.ajax('/labor/get_list', {
                start: start,
                stop: stop,
                start_date: start_date,
                end_date: end_date
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total: function(start_date, end_date, cb) {
            app.ajax('/labor/get_total', {
                start_date: start_date,
                end_date: end_date
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        search: function(cid, cb) {
            app.ajax('/reports/risk/search', {
                cid: cid
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        }
    };

    $('#btn_search').on('click', function(e) {
        e.preventDefault();
        var query = $('#txt_query').val();

        if(!query) {
            app.alert('กรุณาระบุเลขบัตรประชาชน');
        } else {
            labor.ajax.search(query, function(err, data) {
                if(err) {
                    app.alert('ไม่พบข้อมูล');
                } else {
                    labor.set_list(data);
                }
            });
        }
    });
    //modal
//
//    rpt_risk.modal = {
//        show_risk: function() {
//            $('#mdl_anc_survey').modal({
//                keyboard: false,
//                backdrop: 'static'
//            });
//        },
//
//        show_anc_history: function() {
//            $('#mdl_anc_history').modal({
//                keyboard: false,
//                backdrop: 'static'
//            });
//        }
//    };

    //set list
    labor.set_list = function(rs) {
        $('#tbl_list > tbody').empty();

        if($(rs).size()) {

            $(rs).each(function(i, v) {

                $('#tbl_list > tbody').append(
                    '<tr>' +
                        '<td>' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td>' + v.age.year + '</td>' +
                        '<td>' + app.strip(v.address, 30) + '</td>' +
                        '<td>' + v.btype + '</td>' +
                        '<td>' + v.bhosp + '</td>' +
                        '<td>' + v.hospcode + '</td>' +
                        '<a href="#" class="btn btn-default" title="ดูข้อมูลคลอด" rel="tooltip">' +
                        '<i class="icon-share"></i>' +
                        '</a>' +
                        '</td>' +
                        '</tr>'
                );
            });

            app.set_runtime();

        } else {
            $('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบรายการ</td></tr>');
        }
    };

    labor.get_list = function() {

        var start_date = $('#txt_start_date').val(),
            end_date = $('#txt_end_date').val();

        labor.ajax.get_total(start_date, end_date, function(e, total) {

            $('#spn_total > strong').html(numeral(total).format('0,0'));

            if (e) {
                app.alert(e);
            } else {

                $('#paging').fadeIn('slow');

                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: 1,
                    onSelect: function(page) {

                        labor.ajax.get_list(start_date, end_date, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                labor.set_list(rs);
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

        var start_date = $('#txt_start_date').val(),
            end_date = $('#txt_end_date').val();

        if(!start_date) {
            app.alert('กรุณาระบุวันที่เริ่มต้น');
        } else if(!end_date) {
            app.alert('กรุณาระบุวันที่สิ้นสุด');
        } else {
            labor.get_list();
        }
    });

    var date_range = app.get_current_date_range();

    $('#txt_start_date').val(date_range.start_date);
    $('#txt_end_date').val(date_range.end_date);

    labor.get_list();
});