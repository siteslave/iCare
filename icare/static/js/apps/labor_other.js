$(function() {
    var labor = {};

    labor.modal = {
        show_labor: function() {
            $('#mdl_labor').modal({
                keyboard: false,
                backdrop: false
            });
        },
        show_anc: function() {
            $('#mdl_anc').modal({
                keyboard: false,
                backdrop: false
            });
        }
    };

    labor.ajax = {
        get_list: function(hospcode, start_date, end_date, start, stop, cb) {
            app.ajax('/labor_other/get_list', {
                start: start,
                stop: stop,
                start_date: start_date,
                end_date: end_date,
                hospcode: hospcode
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total: function(hospcode, start_date, end_date, cb) {
            app.ajax('/labor_other/get_total', {
                start_date: start_date,
                end_date: end_date,
                hospcode: hospcode
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        do_process: function(hospcode, start_date, end_date, cb) {
            app.ajax('/labor_other/do_process', {
                start_date: start_date,
                end_date: end_date,
                hospcode: hospcode
            }, function(e) {
                e ? cb (e, null) : cb (null);
            });
        },

        get_labor: function (hospcode, pid, gravida, cb) {
            app.ajax('/labor_other/get_labor', {
                pid: pid,
                gravida: gravida,
                hospcode: hospcode
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_visit_anc: function (cid, cb) {
            app.ajax('/anc/get_visit_all', {
                cid: cid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        }
    };

    labor.set_anc_visit = function(rs) {

        $('#tbl_anc_visit_list > tbody').empty();

        if($(rs).size()) {
            $.each(rs, function(i, v) {

                var result = v.ancresult == '1' ?
                    '<p class="text-success"><strong>ปกติ</strong></p>' :
                    v.ancresult == '2' ?
                    '<p class="text-danger"><strong>ผิดปกติ</strong></p>' :
                    '<p class="text-muted"><strong>ไม่ได้ตรวจ</strong></p>';

                $('#tbl_anc_visit_list > tbody').append(
                    '<tr>' +
                        '<td class="text-center">' + v.date_serv + '</td>' +
                        '<td>[' + v.hospcode + '] ' + v.hospname + '</td>' +
                        '<td>[' + v.ancplace + '] ' + v.ancplace_name + '</td>' +
                        '<td class="text-center">' + v.gravida + '</td>' +
                        //'<td class="text-center">' + v.ancno + '</td>' +
                        '<td class="text-center">' + v.ga + '</td>' +
                        '<td>' + result + '</td>' +
                        '</tr>'
                );
            });

            app.set_runtime();
        }
        else {
            $('#tbl_anc_visit_list > tbody').append('<tr><td colspan="5">ไม่พบข้อมูล</td></td></tr>');
        }
    };

    $('#btn_process').on('click', function(e) {
        e.preventDefault();

        var start_date = $('#txt_start_date').val(),
            end_date = $('#txt_end_date').val(),
            hospcode = $('#sl_hospitals').val();

        if(!start_date) {
            app.alert('กรุณาระบุวันที่เริ่มต้น');
        } else if(!end_date) {
            app.alert('กรุณาระบุวันที่สิ้นสุด');
        } else {
            labor.ajax.do_process(hospcode, start_date, end_date, function(err) {
               if(err) {
                   app.alert(err);
               } else {
                   app.alert('ประมวลผลเสร็จเรียบร้อยแล้ว');
                   labor.get_list();
               }
            });
        }
    });

//    $('#btn_search').on('click', function(e) {
//        e.preventDefault();
//        var query = $('#txt_query').val();
//
//        if(!query) {
//            app.alert('กรุณาระบุเลขบัตรประชาชน');
//        } else {
//            labor.ajax.search(query, function(err, data) {
//                if(err) {
//                    app.alert('ไม่พบข้อมูล');
//                } else {
//                    labor.set_list(data);
//                }
//            });
//        }
//    });
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
                        '<td class="text-center">' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td class="text-center">' + v.age.year + '</td>' +
                        '<td class="text-center">' + v.bdate + '</td>' +
                        '<td>' + v.house + ' ' + v.address + '</td>' +
                        '<td class="text-center"><div class="btn-group">' +
                        '<a href="#" data-name="btn_get_labor" data-pid="' + v.pid + '" ' +
                        'data-gravida="' + v.gravida + '" data-hospcode="' + v.hospcode + '" class="btn btn-default" title="ดูข้อมูลคลอด" rel="tooltip">' +
                        '<i class="fa fa-th-list"></i>' +
                        '</a>' +
                        '<a href="#" data-name="btn_get_anc" data-cid="' + v.cid + '" ' +
                        'data-gravida="' + v.gravida + '" class="btn btn-default" title="ดูข้อมูลการฝากครรภ์" rel="tooltip">' +
                        '<i class="fa fa-calendar"></i>' +
                        '</a>' +
                        '</div></td>' +
                        '</tr>'
                );
            });

            app.set_runtime();

        } else {
            $('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบรายการ</td></tr>');
        }
    };

    $(document).on('click', 'a[data-name="btn_get_anc"]', function(e) {
        e.preventDefault();

        var cid = $(this).data('cid');

        if(!cid) {
            app.alert('กรุณาระบุเลขบัตรประชาชน');
        } else {
            labor.ajax.get_visit_anc(cid, function(err, data) {
               if(err) {
                   app.alert(err);
               } else {
                   labor.set_anc_visit(data);
                   labor.modal.show_anc();
               }
            });
        }
    });

    $(document).on('click', 'a[data-name="btn_get_labor"]', function(e) {
        e.preventDefault();

        var pid = $(this).data('pid'),
            hospcode = $(this).data('hospcode'),
            gravida = $(this).data('gravida');

        labor.ajax.get_labor(hospcode, pid, gravida, function(err, v) {
            if(err) {
                app.alert(err);
            } else {
                $('#txt_labor_fullname').val(v[0]['fullname']);
                $('#txt_labor_birth').val(v[0]['birth']);
                $('#txt_labor_cid').val(v[0]['cid']);
                $('#txt_labor_gravida').val(v[0]['gravida']);
                $('#txt_labor_bdate').val(v[0]['bdate']);
                $('#sl_bplace').val(v[0]['bplace']);
                $('#txt_labor_hospcode').val(v[0]['bhospcode']);
                $('#txt_labor_hospname').val(v[0]['bhospname']);
                $('#txt_labor_diagcode').val(v[0]['bresultcode']);
                $('#txt_labor_diagname').val(v[0]['bresultname']);
                $('#sl_labor_btype').val(v[0]['btype']);
                $('#sl_labor_bdoctor').val(v[0]['bdoctor']);
                $('#txt_labor_lborn').val(v[0]['lborn']);
                $('#txt_labor_sborn').val(v[0]['sborn']);

                labor.modal.show_labor();
            }
        });
    });

    labor.get_list = function() {

        var start_date = $('#txt_start_date').val(),
            end_date = $('#txt_end_date').val(),
            hospcode = $('#sl_hospitals').val();

        labor.ajax.get_total(hospcode, start_date, end_date, function(e, total) {

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

                        labor.ajax.get_list(hospcode, start_date, end_date, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="6">ไม่พบข้อมูล</td></td></tr>');
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

});