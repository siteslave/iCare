$(function() {
    var rpt_risk = {};

    rpt_risk.ajax = {
        get_list: function(t, start, stop, cb) {
            app.ajax('/reports/risk/list', {
                t: t,
                start: start,
                stop: stop
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_list_by_group: function(start_date, end_date, cb) {
            app.ajax('/reports/risk/get_anc_risk_by_group', {
                start_date: start_date,
                end_date: end_date
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_risk_list_by_type: function(choice, start_date, end_date, cb) {
            app.ajax('/reports/risk/get_risk_list_by_type', {
                start_date: start_date,
                end_date: end_date,
                choice: choice
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        search: function(cid, cb) {
            app.ajax('/reports/risk/search', {
                cid: cid
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        anc_history: function(cid, cb) {
            app.ajax('/reports/risk/anc_history', {
                cid: cid
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        detail: function(id, cb) {
            app.ajax('/reports/risk/detail', {
                id: id
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total: function(t, cb) {
            app.ajax('/reports/risk/total', {
                t: t
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        }
    };

    //modal

    rpt_risk.modal = {
        show_risk: function() {
            $('#mdl_anc_survey').modal({
                keyboard: false,
                backdrop: false
            });
        },

        show_anc_history: function() {
            $('#mdl_anc_history').modal({
                keyboard: false,
                backdrop: false
            });
        },

        show_risk_list: function() {
            $('#mdl_risk_list').modal({
                keyboard: false,
                backdrop: false
            });
        }
    };

    //set list
    rpt_risk.set_list = function(rs) {
        $('#tbl_list > tbody').empty();

        if($(rs).size()) {

            $(rs).each(function(i, v) {

                var is_risk = v.is_risk == 'Y' ? '<i class="fa fa-ok"></i>' : '<i class="fa fa-minus"></i>';
                var tr_risk = v.is_risk == 'Y' ? 'class="warning"' : '';

                var screen_list =
                    '<div class="btn-group">' +
                                '<button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">' +
                                '<i class="fa fa-calendar"></i> <span class="caret"></span>' +
                                '</button>' +
                        '<ul class="dropdown-menu pull-right" role="menu">';

                if($(v.screen_date).size()) {
                    $(v.screen_date).each(function(i, v) {
                        //var d = new Date(v.last_update);
                        //var new_date = d.getDate() + '/' + (d.getMonth() + 1) + '/' + d.getFullYear();
                        screen_list +=
                                        '<li class="dropdown-header">DATE SCREEN</li>' +
                                        '<li><a href="#" data-name="btn_get_risk_screen_detail" data-id="' + v.id + '" title="ดูข้อมูล">' +
                                            '<i class="fa fa-edit"></i> ' + app.string_to_jsdate(v.last_update) + '</a></li>'
                    });

                    screen_list += '</ul></div>';
                }

                $('#tbl_list > tbody').append(
                    '<tr ' + tr_risk + '>' +
                        '<td class="text-center">' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td>' + v.birth + '</td>' +
                        '<td class="text-center">' + v.age.year + '</td>' +
                        '<td>' + app.strip(v.address, 50) + '</td>' +
                        '<td class="text-center">' + is_risk + '</td>' +
                        '<td class="text-center" class="text-center"><a href="#" class="btn btn-success" data-name="btn_anc_history" ' +
                        'data-cid="' + v.cid + '" title="ดูประวัติการฝากครรภ์"><i class="fa fa-th-list"></i></a></td>' +
                        '<td class="text-center">' + screen_list + '</td>' +
                        '</tr>'
                );
            });

        } else {
            $('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบรายการ</td></tr>');
        }
    };

    rpt_risk.get_list = function(t) {

        rpt_risk.ajax.get_total(t, function(e, total) {

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

                        rpt_risk.ajax.get_list(t, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                rpt_risk.set_list(rs);
                            }
                        });

                    },
                    onFormat: app.setPagingFormat
                });
            }
        });
    };

    rpt_risk.search = function(cid) {

        $('#tbl_list > tbody').empty();

        rpt_risk.ajax.search(cid, function(e, data) {
            if(e) {
                app.alert(e);
                $('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบข้อมูล</td></td></tr>');
            } else {
                $('#paging').fadeOut('slow');
                rpt_risk.set_list(data);
            }
        });
    };

    $('button[data-name="btn_filter"]').on('click', function(e) {
        e.preventDefault();
        //get filter type
        var t = $(this).data('value');
        //get list
        rpt_risk.get_list(t);

    });

    $('#btn_search').on('click', function(e) {
        e.preventDefault();

        var cid = $('#txt_query').val();

        if(!cid) {
            app.alert('กรุณาระบุเลขบัตรประชาชน');
        } else {
            //do search
            rpt_risk.search(cid);
        }
    });

    //set risk detail
    rpt_risk.set_risk_detail = function(v) {
        v = v[0];

        $('#sl1').val(v['ch1']);
        $('#sl2').val(v['ch2']);
        $('#sl3').val(v['ch3']);
        $('#sl4').val(v['ch4']);
        $('#sl5').val(v['ch5']);
        $('#sl6').val(v['ch6']);
        $('#sl7').val(v['ch7']);
        $('#sl8').val(v['ch8']);
        $('#sl9').val(v['ch9']);
        $('#sl10').val(v['ch10']);
        $('#sl11').val(v['ch11']);
        $('#sl12').val(v['ch12']);
        $('#sl13').val(v['ch13']);
        $('#sl14').val(v['ch14']);
        $('#sl15').val(v['ch15']);
        $('#sl16').val(v['ch16']);
        $('#sl17').val(v['ch17']);
        $('#sl18').val(v['ch18']);

        $('#txt_ans_other_ill').val(v['other_ill']);

        rpt_risk.modal.show_risk();
    };

    //get screen detail
    $(document).on('click', 'a[data-name="btn_get_risk_screen_detail"]', function(e) {
        e.preventDefault();

        var id = $(this).data('id');

        //get detail
        rpt_risk.ajax.detail(id, function(e, v) {
            if(e) {
                app.alert(e);
            } else {
                rpt_risk.set_risk_detail(v);
            }
        });
    });
    //set anc history
    rpt_risk.set_anc_history = function(v) {

        $('#tbl_anc_history > tbody').empty();

        if($(v).size()) {
            $(v).each(function(i, v) {
                var result = v.ancresult == '1' ?
                    '<p class="text-success"><strong>ปกติ</strong></p>' :
                    v.ancresult == '2' ?
                    '<p class="text-danger"><strong>ผิดปกติ</strong></p>' :
                    '<p class="text-muted"><strong>ไม่ได้ตรวจ</strong></p>';

                $('#tbl_anc_history > tbody').append(
                    '<tr>' +
                        '<td>[' + v.hospcode + '] ' + v.hospname + '</td>' +
                        '<td class="text-center">' + v.date_serv + '</td>' +
                        '<td class="text-center">' + v.gravida + '</td>' +
                        '<td class="text-center">' + v.ancno + '</td>' +
                        '<td class="text-center">' + v.ga + '</td>' +
                        '<td>' + result + '</td>' +
                        '</tr>'
                );
            });
        } else {
             $('#tbl_anc_history > tbody').append(
                 '<tr><td colspan="6">ไม่พบรายการ</td></tr>'
             );
        }

        rpt_risk.modal.show_anc_history();

    };

    //get anc history
    rpt_risk.get_anc_history = function(cid) {
        rpt_risk.ajax.anc_history(cid, function(e, v) {
           if(e) {
               app.alert(e);
           } else {
                rpt_risk.set_anc_history(v);
           }
        });
    };

    $(document).on('click', 'a[data-name="btn_anc_history"]', function(e) {
        e.preventDefault();

        var cid = $(this).data('cid');
        rpt_risk.get_anc_history(cid);
    });

    rpt_risk.get_risk_list = function(start_date, end_date) {

        if(!start_date) {
            app.alert('กรุณาระบุวันที่เริ่มต้น');
        } else if(!end_date) {
            app.alert('กรุณาระบุวันที่สิ้นสุด');
        } else {
            rpt_risk.ajax.get_list_by_group(start_date, end_date, function(err, data) {
               if(err) {
                   app.alert(err);
               } else {

                   $('a[data-name="btn_get_risk_list"]').each(function() {
                        $(this).removeAttr('disabled');
                   });

                   $('#spn_ch01').html('<strong>' + data[0].risk01 + '</strong>');
                   $('#spn_ch02').html('<strong>' + data[0].risk02 + '</strong>');
                   $('#spn_ch03').html('<strong>' + data[0].risk03 + '</strong>');
                   $('#spn_ch04').html('<strong>' + data[0].risk04 + '</strong>');
                   $('#spn_ch05').html('<strong>' + data[0].risk05 + '</strong>');
                   $('#spn_ch06').html('<strong>' + data[0].risk06 + '</strong>');
                   $('#spn_ch07').html('<strong>' + data[0].risk07 + '</strong>');
                   $('#spn_ch08').html('<strong>' + data[0].risk08 + '</strong>');
                   $('#spn_ch09').html('<strong>' + data[0].risk09 + '</strong>');
                   $('#spn_ch10').html('<strong>' + data[0].risk10 + '</strong>');
                   $('#spn_ch11').html('<strong>' + data[0].risk11 + '</strong>');
                   $('#spn_ch12').html('<strong>' + data[0].risk12 + '</strong>');
                   $('#spn_ch13').html('<strong>' + data[0].risk13 + '</strong>');
                   $('#spn_ch14').html('<strong>' + data[0].risk14 + '</strong>');
                   $('#spn_ch15').html('<strong>' + data[0].risk15 + '</strong>');
                   $('#spn_ch16').html('<strong>' + data[0].risk16 + '</strong>');
                   $('#spn_ch17').html('<strong>' + data[0].risk17 + '</strong>');
                   $('#spn_ch18').html('<strong>' + data[0].risk18 + '</strong>');
               }
            });
        }
    };

    $('#btn_clear_filter_by_group').on('click', function(e) {
        e.preventDefault();
        rpt_risk.clear_before_filter();
    });

    rpt_risk.clear_before_filter = function() {

        $('a[data-name="btn_get_risk_list"]').each(function() {
            $(this).attr('disabled', 'disabled');
        });

        $('#txt_start_date').val('');
        $('#txt_end_date').val('');

       $('#spn_ch01').html('<strong>0</strong>');
       $('#spn_ch02').html('<strong>0</strong>');
       $('#spn_ch03').html('<strong>0</strong>');
       $('#spn_ch04').html('<strong>0</strong>');
       $('#spn_ch05').html('<strong>0</strong>');
       $('#spn_ch06').html('<strong>0</strong>');
       $('#spn_ch07').html('<strong>0</strong>');
       $('#spn_ch08').html('<strong>0</strong>');
       $('#spn_ch09').html('<strong>0</strong>');
       $('#spn_ch10').html('<strong>0</strong>');
       $('#spn_ch11').html('<strong>0</strong>');
       $('#spn_ch12').html('<strong>0</strong>');
       $('#spn_ch13').html('<strong>0</strong>');
       $('#spn_ch14').html('<strong>0</strong>');
       $('#spn_ch15').html('<strong>0</strong>');
       $('#spn_ch16').html('<strong>0</strong>');
       $('#spn_ch17').html('<strong>0</strong>');
       $('#spn_ch18').html('<strong>0</strong>');
    };
    //get list by group
    $('#btn_filter_by_group').on('click', function(e) {
        e.preventDefault();

        var start_date = $('#txt_start_date').val(),
            end_date = $('#txt_end_date').val();

        rpt_risk.get_risk_list(start_date, end_date);
    });

    rpt_risk.set_risk_list = function(data) {
        $('#tbl_risk_list_by_type > tbody').empty();
        if(data.length) {
            $.each(data, function(i, v) {
               $('#tbl_risk_list_by_type > tbody').append(
                   '<tr>' +
                       '<td class="text-center">' + v.cid + '</td>' +
                       '<td>' + v.fullname + '</td>' +
                       '<td class="text-center">' + v.birth + '</td>' +
                       '<td class="text-center">' + v.age.year + '</td>' +
                   '</tr>'
               );
            });
        } else {
            $('#tbl_risk_list_by_type > tbody').append('<tr><td colspan="4">ไม่พบรายการ</td></tr>');
        }
    };

    $('a[href="#bygroup"]').on('click', function(e) {
        rpt_risk.clear_before_filter();
    });

    $('a[data-name="btn_get_risk_list"]').on('click', function(e) {
        e.preventDefault();

        var choice = $(this).data('choice'),
            start_date = $('#txt_start_date').val(),
            end_date = $('#txt_end_date').val();

        rpt_risk.ajax.get_risk_list_by_type(choice, start_date, end_date, function(err, data) {
            rpt_risk.set_risk_list(data);
            rpt_risk.modal.show_risk_list();
        });
    });
    //get list all
    rpt_risk.get_list('0');
});