$(function() {
    ///mch/process

    var rpt_mch = {};

    rpt_mch.ajax = {
        get_total: function (start_date, end_date, cb) {
            app.ajax('/reports/mch/total', {
                s: start_date,
                e: end_date
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        search: function (cid, cb) {
            app.ajax('/reports/mch/search', { cid: cid}, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_list: function (start_date, end_date, start, stop, cb) {
            app.ajax('/reports/mch/list', {
                's': start_date,
                'e': end_date,
                'start': start,
                'stop': stop
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        process: function (cb) {
            app.ajax('/reports/mch/process', {}, function (e) {
               e ? cb (e, null) : cb (null);
            });
        }
    };

    $('#btn_process').on('click', function(e) {
        e.preventDefault();

        if (confirm('คุณต้องการประมวลผลข้อมูล ใช่หรือไม่?')) {
            rpt_mch.ajax.process(function (e) {
                if (e) {
                    app.alert(e);
                } else {
                    app.alert('ประมวลผลข้อมูลเสร็จเรียบร้อยแล้ว');
                }
            });
        }
    });

    rpt_mch.set_list = function(rs) {

        if($(rs).size()) {
            $(rs).each(function(i, r) {
                var cov01, cov02, cov03, cov04, cov05;

                $(r.ppcares).each(function(i, v) {

                    if(v.no == '1') cov01 = v.is_forecast == 'N' ? '<span class="text-success"><strong>' + app.dbpop2thai_date(v.date_serv) + '</strong></span>' : '<span class="text-danger">' + app.dbpop2thai_date(v.date_serv) + '</span>';
                    if(v.no == '2') cov02 = v.is_forecast == 'N' ? '<span class="text-success"><strong>' + app.dbpop2thai_date(v.date_serv) + '</strong></span>' : '<span class="text-danger">' + app.dbpop2thai_date(v.date_serv) + '</span>';
                    if(v.no == '3') cov03 = v.is_forecast == 'N' ? '<span class="text-success"><strong>' + app.dbpop2thai_date(v.date_serv) + '</strong></span>' : '<span class="text-danger">' + app.dbpop2thai_date(v.date_serv) + '</span>';

                });

                $('#tbl_list > tbody').append(
                    '<tr>' +
                        '<td>' + r.cid + '</td>' +
                        '<td>' + r.fullname + '</td>' +
                        '<td>' + r.age.year + '</td>' +
                        '<td>' + r.bdate + '</td>' +
                        '<td>' + cov01 + '</td>' +
                        '<td>' + cov02 + '</td>' +
                        '<td>' + cov03 + '</td>' +
                        //'<td><a href="#" class="btn btn-primary"><i class="icon-share"></i></a></td>' +
                        '</tr>'
                );
            });
        } else {
            $('#tbl_list > tbody').append('<tr><td colspan="7">ไม่พบรายการ</td></tr>');
        }
    };

    rpt_mch.get_list = function() {

        var start = $('#txt_start_date').val();
        var end = $('#txt_end_date').val();

        $('#tbl_list > tbody').empty();

        rpt_mch.ajax.get_total(start, end, function(e, total) {
            if (e) {
                app.alert(e);
                $('#tbl_list > tbody').append('<tr><td colspan="7">ไม่พบรายการ</td></tr>');
            } else {

                $('#paging').fadeIn('slow');

                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: 1,
                    onSelect: function(page) {

                        rpt_mch.ajax.get_list(start, end, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="7">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                rpt_mch.set_list(rs);
                            }
                        });

                    },
                    onFormat: function(type){
                        switch (type) {

                            case 'block':

                                if (!this.active)
                                    return '<li class="disabled"><a href="">' + this.value + '</a></li>';
                                else if (this.value != this.page)
                                    return '<li><a href="#' + this.value + '">' + this.value + '</a></li>';
                                return '<li class="active"><a href="#">' + this.value + '</a></li>';

                            case 'right':
                            case 'left':

                                if (!this.active) {
                                    return "";
                                }
                                return '<li><a href="#' + this.value + '">' + this.value + '</a></li>';

                            case 'next':

                                if (this.active) {
                                    return '<li><a href="#' + this.value + '">&raquo;</a></li>';
                                }
                                return '<li class="disabled"><a href="">&raquo;</a></li>';

                            case 'prev':

                                if (this.active) {
                                    return '<li><a href="#' + this.value + '">&laquo;</a></li>';
                                }
                                return '<li class="disabled"><a href="">&laquo;</a></li>';

                            case 'first':

                                if (this.active) {
                                    return '<li><a href="#' + this.value + '">&lt;</a></li>';
                                }
                                return '<li class="disabled"><a href="">&lt;</a></li>';

                            case 'last':

                                if (this.active) {
                                    return '<li><a href="#' + this.value + '">&gt;</a></li>';
                                }
                                return '<li class="disabled"><a href="">&gt;</a></li>';

                            case 'fill':
                                if (this.active) {
                                    return '<li class="disabled"><a href="#">...</a></li>';
                                }
                        }
                        return ""; // return nothing for missing branches
                    }
                });
            }
        });
    };

    //filter by date
    $('#btn_filter').on('click', function(e) {
        e.preventDefault();

        if (!$('#txt_start_date').val() || !$('#txt_end_date').val()) {
            app.alert('กรุณาระบุช่วงเวลาที่ต้องการ');
        } else {
            rpt_mch.get_list();
        }
    });

    //refresh
    $('#btn_refresh').on('click', function(e) {
        e.preventDefault();
        $('#txt_start_date').val('');
        $('#txt_end_date').val('');

        rpt_mch.get_list();
    });

    //get list with out filter
    rpt_mch.get_list();

});