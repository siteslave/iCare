$(function() {
    var milk = {};

    milk.ajax = {
        get_list: function (start, stop, cb) {
            app.ajax('/reports/milk/list', {
                start: start,
                stop: stop
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total: function (cb) {
            app.ajax('/reports/milk/total', {}, function (e, v) {
               e ? cb (e, null) : cb (null, v.total);
            });
        },

        do_process: function (cb) {
            app.ajax('/reports/milk/process', {}, function (e, v) {
               e ? cb (e, null) : cb (null);
            });
        }
    };

    milk.set_list = function(v) {

        $('#tbl_list > tbody').empty();

        if($(v).size()) {

            $(v).each(function(i, v) {

                $('#tbl_list > tbody').append(
                    '<tr>' +
                        '<td class="text-center">' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td class="text-center">' + v.birth + '</td>' +
                        '<td class="text-center">' + v.age.year + '-' + v.age.month + '-' + v.age.day + '</td>' +
                        '<td class="text-center">' + numeral(v.total).format('0, 0') + '</td>' +
                        '<td>' + v.address + '</td>' +
                        '</tr>'
                );
            });

            app.set_runtime();

        } else {

            $('#tbl_list > tbody').append('<tr><td colspan="6">ไม่พบรายการ</td></tr>');

        }

    };

    milk.get_list = function() {

        milk.ajax.get_total(function(e, total) {

            $('#spn_total > strong').html(numeral(total).format('0,0'));

            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');
                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('rpt_milk'),
                    onSelect: function(page) {
                        app.set_cookie('rpt_milk', page);

                        milk.ajax.get_list(this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="6">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                milk.set_list(rs);
                            }
                        });

                    },
                    onFormat: app.setPagingFormat
                });
            }
        });

    };

    $('#btn_process').on('click', function(e) {
        e.preventDefault();

        if(confirm('คุณต้องการประมวลผลข้อมูลหรือไม่?')) {
            milk.ajax.do_process(function(e) {
                if(e) {
                    app.alert(e);
                } else {
                    app.alert('ประมวลผลข้อมูลเสร็จเรียบร้อยแล้ว');
                    //get list
                    milk.get_list();
                }
            });
        }
    });

    $('#btn_refresh').on('click', function(e) {
        e.preventDefault();

        milk.get_list();
    });

    milk.get_list();

});