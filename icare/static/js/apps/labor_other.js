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
                backdrop: 'static'
            });
        },

        show_anc_history: function() {
            $('#mdl_anc_history').modal({
                keyboard: false,
                backdrop: 'static'
            });
        }
    };

    //set list
    rpt_risk.set_list = function(rs) {
        $('#tbl_list > tbody').empty();

        if($(rs).size()) {

            $(rs).each(function(i, v) {

                $('#tbl_list > tbody').append(
                    '<tr>' +
                        '<td>' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td>' + v.age.year + '</td>' +
                        '<td>' + app.strip(v.address, 30) + '</td>' +
                        '<td>10707 รพท. มหาสารคาม</td>' +
                        '<td>' +
                        '<a href="#" class="btn btn-default" title="ดูข้อมูลคลอด" rel="tooltip">' +
                        '<i class="icon-share"></i>' +
                        '</a>' +
                        '</td>' +
                        '</tr>'
                );
            });

            app.set_runtime();

        } else {
            $('#tbl_list > tbody').append('<tr><td colspan="6">ไม่พบรายการ</td></tr>');
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
                                $('#tbl_list > tbody').append('<tr><td colspan="6">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                rpt_risk.set_list(rs);
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
                        '<td>' + v.date_serv + '</td>' +
                        '<td>' + v.gravida + '</td>' +
                        '<td>' + v.ancno + '</td>' +
                        '<td>' + v.ga + '</td>' +
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

    //get list all
    rpt_risk.get_list('0');
});