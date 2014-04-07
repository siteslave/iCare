$(function() {
    var anc_12ws = {};

    anc_12ws.ajax = {
        get_list: function (start, stop, cb) {

            app.ajax('/reports/anc_12ws/list', {
                start: start,
                stop: stop
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total: function (cb) {
            app.ajax('/reports/anc_12ws/total', {}, function (e, v) {
               e ? cb (e, null) : cb (null, v.total);
            });
        },

        get_visit_all: function (cid, cb) {
            app.ajax('/anc/get_visit_all', {
                cid: cid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        do_process: function (cb) {
            app.ajax('/anc/do_process_12weeks', {}, function (e, v) {
               e ? cb (e, null) : cb (null);
            });
        }
    };

    anc_12ws.modal = {
        show_anc_visit: function() {
            $('#mdl_visit_anc').modal({
                keyboard: false,
                backdrop: false
            });
        }
    };

    anc_12ws.set_list = function(v) {

        $('#tbl_list > tbody').empty();

        if($(v).size()) {

            $(v).each(function(i, v) {

                $('#tbl_list > tbody').append(
                    '<tr>' +
                        '<td class="text-center">' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td class="text-center">' + v.birth + '</td>' +
                        '<td class="text-center">' + v.age.year + '-' + v.age.month + '-' + v.age.day + '</td>' +
                        '<td class="visible-lg">' + v.address + '</td>' +
                        '<td class="text-center"><div class="btn-group">' +
                        '<a href="#" class="btn btn-default" data-cid="' + v.cid + '" data-name="btn_get_anc"><i class="fa fa-th-list"></i></a>' +
                        '</div></td>' +
                        '</tr>'
                );
            });

            app.set_runtime();

        } else {

            $('#tbl_list > tbody').append('<tr><td colspan="5">ไม่พบรายการ</td></tr>');

        }

    };

    anc_12ws.set_anc_list = function(v) {

        $('#tbl_anc_visit > tbody').empty();

        if($(v).size()) {

            $(v).each(function(i, v) {
                i++;
                $('#tbl_anc_visit > tbody').append(
                    '<tr>' +
                        '<td class="text-center">' + i + '</td>' +
                        '<td class="text-center">' + v.date_serv + '</td>' +
                        '<td class="text-center">' + v.ga + '</td>' +
                        '<td>[' + v.hospcode + '] ' + v.hospname + '</td>' +
                        '<td>[' + v.ancplace + '] ' + v.ancplace_name + '</td>' +
                        '</tr>'
                );
            });

            app.set_runtime();

        } else {

            $('#tbl_anc_visit > tbody').append('<tr><td colspan="5">ไม่พบรายการ</td></tr>');

        }

    };

    $(document).on('click', 'a[data-name="btn_get_anc"]', function(e) {
        e.preventDefault();

        var cid = $(this).data('cid');

        anc_12ws.ajax.get_visit_all(cid, function(err, data) {
           if(err) {
               app.alert('ไม่สามารถแสดงข้อมูลได้ : ' + err);
           } else {
                anc_12ws.set_anc_list(data);
               anc_12ws.modal.show_anc_visit();
           }
        });
    });

    anc_12ws.get_list = function() {

        anc_12ws.ajax.get_total(function(e, total) {
            if (e) {
                $('#spn_total > strong').html('0');
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');

                $('#spn_total > strong').html(numeral(total).format('0,0'));

                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('rpt_anc_12ws'),
                    onSelect: function(page) {
                        app.set_cookie('rpt_anc_12ws', page);

                        anc_12ws.ajax.get_list(this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="5">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                anc_12ws.set_list(rs);
                            }
                        });

                    },
                    onFormat: app.setPagingFormat
                });
            }
        });

    };

    //process
    $('#btn_do_process').on('click', function(e) {
        e.preventDefault();

        if(confirm('คุณต้องการประมวลผลข้อมูลใหม่ใช่หรือไม่')) {
            anc_12ws.ajax.do_process(function(e) {
                if(e) {
                    app.alert(e);
                } else {
                    app.alert('ประมวลผลข้อมูลเสร็จเรียบร้อยแล้ว');
                    anc_12ws.get_list();
                }
            });
        }
    })

    anc_12ws.get_list();

});