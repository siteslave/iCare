$(function() {

    var wlt2500 = {}

    wlt2500.ajax = {
        get_list: function (start, stop, cb) {
            app.ajax('/reports/newborn/wlt2500_list', {
                start: start,
                stop: stop
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total: function (cb) {
            app.ajax('/reports/newborn/wlt2500_total', {}, function (e, v) {
               e ? cb (e, null) : cb (null, v.total);
            });
        },

        search: function (cid, cb) {
            app.ajax('/reports/newborn/wlt2500_search', {cid: cid}, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_newborn: function (hospcode, pid, cb) {
            app.ajax('/babies/get_newborn', {
                'hospcode': hospcode,
                'pid': pid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        }
    };

    wlt2500.modal = {
        show_newborn: function() {
            $('#mdl_newborn').modal({
                keyboard: false,
                backdrop: 'static'
            });
        }
    };

    wlt2500.set_list = function(v) {

        $('#tbl_list > tbody').empty();

        if($(v).size()) {

            $(v).each(function(i, v) {

                $('#tbl_list > tbody').append(
                    '<tr>' +
                        '<td>' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td>' + v.age.year + '-' + v.age.month + '-' + v.age.day + '</td>' +
                        '<td>' + v.birth + '</td>' +
                        '<td>' + numeral(v.bweight).format('0, 0') + '</td>' +
                        '<td>' + v.address + '</td>' +
                        '<td><a href="#" class="btn btn-default" data-name="btn_get_newborn_detail" '+
                        'data-pid="' + v.pid + '" data-hospcode="' + v.hospcode + '" data-cid="' + v.cid + '" ' +
                        'data-gravida="' + v.gravida + '" data-fullname="' + v.fullname + '" rel="tooltip" title="ดูข้อมูลการคลอด"> '+
                        '<i class="icon-share"></i></a></td>' +
                        '</tr>'
                );
            });

            app.set_runtime();

        } else {

            $('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบรายการ</td></tr>');

        }

    };

    wlt2500.get_list = function() {

        wlt2500.ajax.get_total(function(e, total) {
            $('#spn_total strong').html(numeral(total).format('0,0'));

            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');
                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('rpt_newborn_wlt'),
                    onSelect: function(page) {
                        app.set_cookie('rpt_newborn_wlt', page);

                        wlt2500.ajax.get_list(this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                wlt2500.set_list(rs);
                            }
                        });

                    },
                    onFormat: function(type){
                        switch (type) {

                            case 'block':

                                if (!this.active)
                                    return '<li class="disabled"><a href="#">' + this.value + '</a></li>';
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
                                return '<li class="disabled"><a href="#">&raquo;</a></li>';

                            case 'prev':

                                if (this.active) {
                                    return '<li><a href="#' + this.value + '">&laquo;</a></li>';
                                }
                                return '<li class="disabled"><a href="#">&laquo;</a></li>';

                            case 'first':

                                if (this.active) {
                                    return '<li><a href="#' + this.value + '">&lt;</a></li>';
                                }
                                return '<li class="disabled"><a href="#">&lt;</a></li>';

                            case 'last':

                                if (this.active) {
                                    return '<li><a href="#' + this.value + '">&gt;</a></li>';
                                }
                                return '<li class="disabled"><a href="#">&gt;</a></li>';

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

    $('#btn_search').on('click', function(e) {
        e.preventDefault();
        var cid = $('#txt_query').val();

        if(cid) {
            wlt2500.search(cid);
        } else {
            app.alert('กรุณาระบุเลขบัตรประชาชน');
        }
    });

    wlt2500.search = function(cid) {

        $('#tbl_list > tbody').empty();
        $('#paging').fadeOut('slow');

        wlt2500.ajax.search(cid, function(e, v) {
            if(e) {
                app.alert(e);
                $('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบข้อมูล</td></td></tr>');
            } else {
                wlt2500.set_list(v);
            }
        });

    };

    $('#btn_refresh').on('click', function(e) {
        e.preventDefault();

        wlt2500.get_list();
    });


    $(document).on('click', 'a[data-name="btn_get_newborn_detail"]', function(e) {
        e.preventDefault();

        var pid = $(this).data('pid'),
            hospcode = $(this).data('hospcode'),
            fullname = $(this).data('fullname'),
            cid = $(this).data('cid'),
            gravida = $(this).data('gravida');

        wlt2500.ajax.get_newborn(hospcode, pid, function(e, v) {
            if(e) {
                app.alert(e);
            } else {
                $('#txt_fullname').val(fullname);
                $('#txt_cid').val(cid);
                $('#txt_gravida').val(gravida);

                wlt2500.set_newborn_detail(v);
            }
        });
    });

    wlt2500.set_newborn_detail = function(v) {

        wlt2500.clear_newborn_form();
        wlt2500.set_newborn(v[0]);

        wlt2500.modal.show_newborn();

    };

    wlt2500.clear_newborn_form = function() {
        $('#txt_bdate').val('');
        $('#txt_btime').val('');
        $('#txt_mother_cid').val('');
        $('#txt_mother_name').val('');
        app.set_first_selected($('#sl_bplace'));
        $('#txt_bhosp_code').val('');
        $('#txt_bhosp_name').val('');
        app.set_first_selected($('#sl_birthno'));
        app.set_first_selected($('#sl_btype'));
        app.set_first_selected($('#sl_bdoctor'));
        $('#txt_bweight').val('');
        $('#txt_asphyxia').val('');
        app.set_first_selected($('#sl_vitk'));
        app.set_first_selected($('#sl_tsh'));
        $('#txt_tshresult').val('');
    };

    wlt2500.set_newborn = function(v) {
        $('#txt_bdate').val(v.bdate);
        $('#txt_btime').val(v.btime);
        $('#txt_mother_cid').val(v.mother.cid);
        $('#txt_mother_name').val(v.mother.fullname);
        $('#sl_bplace').val(v.bplace);
        $('#txt_bhosp_code').val(v.bhosp_code);
        $('#txt_bhosp_name').val(v.bhosp_name);
        $('#sl_birthno').val(v.birthno);
        $('#sl_btype').val(v.btype);
        $('#sl_bdoctor').val(v.bdoctor);
        $('#txt_bweight').val(v.bweight);
        $('#txt_asphyxia').val(v.asphyxia);
        $('#sl_vitk').val(v.vitk);
        $('#sl_tsh').val(v.tsh);
        $('#txt_tshresult').val(v.tshresult);
    };

    wlt2500.get_list();
});