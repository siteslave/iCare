var epidem = {};

epidem.ajax = {
    get_total: function (start_date, end_date, code506, ptstatus, cb) {
        app.ajax('/epidem/get_total', {
            start_date: start_date,
            end_date: end_date,
            code506: code506,
            ptstatus: ptstatus
        }, function(e, v) {
            e ? cb (e, null) : cb (null, v.total);
        });
    },

    get_list: function (start_date, end_date, code506, ptstatus, s, t, cb) {
        app.ajax('/epidem/get_list', {
            start_date: start_date,
            end_date: end_date,
            code506: code506,
            ptstatus: ptstatus,
            start: s,
            stop: t
        }, function (e, v) {
           e ? cb (e, null) : cb (null, v.rows);
        });
    },

    get_info: function (h, p, s, d, cb) {
        app.ajax('/epidem/get_info', {
            hospcode: h,
            pid: p,
            seq: s,
            diagcode: d
        }, function (e, v) {
           e ? cb (e, null) : cb (null, v.rows);
        });
    }
};

epidem.modal = {
    show_info: function() {
        $('#mdl_info').modal({
            keyboard: false,
            backdrop: 'static'
        });
    }
};

epidem.set_list = function(rs) {
    if(rs.length > 0) {
        $.each(rs, function(i, v) {
            var sex = v.sex == '1' ? 'ชาย' : 'หญิง';
            var tr_death = v.ptstatus == '2' ? 'class="danger"' : '';
            var ptstatus = v.ptstatus == '1' ? 'หาย' :
                v.ptstatus == '2' ? 'ตาย' :
                    v.ptstatus == '3' ? 'ยังรักษาอยู่' :
                        v.ptstatus == '9' ? 'ไม่ทราบ' : '-';

            $('#tbl_list > tbody').append(
                '<tr '+ tr_death +'>' +
                    '<td>'+ v.illdate +'</td>' +
                    '<td>'+ v.cid +'</td>' +
                    '<td>'+ v.fullname +'</td>' +
                    '<td class="hidden-md hidden-sm">'+ app.clear_null(v.age.year) + '-' + app.clear_null(v.age.month) + '-' + app.clear_null(v.age.day) +'</td>' +
                    '<td class="hidden-md hidden-sm">'+ sex +'</td>' +
                    '<td>'+ v.ill_address +'</td>' +
                    '<td>'+ ptstatus +'</td>' +
                    '<td>['+ v.code506 + '] ' + v.code506_name +'</td>' +
                    '<td>' +
                    '<a href="javascript:void(0);" class="btn btn-default btn-sm" rel="tooltip" title="ดูข้อมูล" data-name="btn_get_info" ' +
                    'data-hospcode="'+ v.hospcode +'" data-seq="'+ v.seq +'" data-pid="'+ v.pid +'" data-diagcode="'+ v.diagcode +'">' +
                    '<i class="icon-share"></i></a>' +
                    '</td>' +
                '</tr>'
            );
        });

        app.set_runtime();

    } else {
        $('#tbl_list > tbody').append('<tr><td colspan="9">ไม่พบข้อมูล</td></td></tr>');
    }
};

epidem.set_info = function(v) {
    $('#txt_fullname').val(v.fullname);
    $('#txt_birth').val(v.birth);
    $('#txt_age').val(v.age.year + ' ปี ' + v.age.month + ' เดือน ' + v.age.day + ' วัน');

    $('#spn_an').html(v.an);
    $('#spn_date_serv').html(v.date_serv);
    $('#spn_illdate').html(v.illdate);
    $('#spn_diag').html(v.diag);
    $('#spn_code506').html(v.code506);
    $('#spn_complication').html(v.complication);
    $('#spn_address').html(v.ill_address);

    var ptstatus = v.ptstatus == '1' ? 'หาย' :
    v.ptstatus == '2' ? 'ตาย' :
        v.ptstatus == '3' ? 'ยังรักษาอยู่' :
            v.ptstatus == '9' ? 'ไม่ทราบ' : '-';

    $('#spn_ptstatus').html(ptstatus);
    $('#spn_lat_lng').html(v.latLng);

    epidem.modal.show_info();
};

epidem.get_list = function(start_date, end_date, code506, ptstatus) {
    epidem.ajax.get_total(start_date, end_date, code506, ptstatus, function(e, total) {
            if (e) {
                $('#paging').fadeOut('slow');
                app.alert(e);
                $('#tbl_list > tbody').empty();
                $('#tbl_list > tbody').append('<tr><td colspan="9">ไม่พบข้อมูล</td></td></tr>');
            } else {
                $('#paging').fadeIn('slow');
                $('#spn_total').html(numeral(total).format('0,0'));
                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('epidem_paging'),
                    onSelect: function(page) {
                        app.set_cookie('epidem_paging', page);

                        epidem.ajax.get_list(start_date, end_date, code506, ptstatus, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="9">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                epidem.set_list(rs);
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


$(function() {
    $('#btn_result').on('click', function(e) {

        e.preventDefault();

        var start_date = $('#txt_start_date').val(),
            end_date = $('#txt_end_date').val(),
            code506 = $('#sl_code506').val(),
            ptstatus = $('#sl_ptstatus').val();

        if(!start_date && !end_date) {
            app.alert('กรุณาระบุวันที่เริ่มต้น - สิ้นสุด');
        } else {
            //do search
            epidem.get_list(start_date, end_date, code506, ptstatus);
        }
    });

    $(document).on('click', 'a[data-name="btn_get_info"]', function(e) {
        var hospcode = $(this).data('hospcode'),
            pid = $(this).data('pid'),
            diagcode = $(this).data('diagcode'),
            seq = $(this).data('seq');

            epidem.ajax.get_info(hospcode, pid, seq, diagcode, function(err, rs) {
                if(err) {
                    app.alert('ไม่พบข้อมูล');
                } else {
                    epidem.set_info(rs);
                }
            });
    });
});