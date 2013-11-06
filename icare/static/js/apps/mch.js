$(function() {
    var mch = {};

    mch.modal = {
        show_postnatal: function() {
            $('#mdl_postnatal').modal({
                keyboard: false,
                backdrop: 'static'
            });
        },

        show_labor: function() {
            $('#mdl_labor').modal({
                keyboard: false,
                backdrop: 'static'
            });
        },

        show_appoint: function() {
            $('#mdl_appointment').modal({
                keyboard: false,
                backdrop: 'static'
            });
        }

    };

    mch.ajax = {
        get_total: function (cb) {
            app.ajax('/mch/get_total', {}, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        search: function (cid, cb) {
            app.ajax('/mch/search', { cid: cid}, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_list: function (s, t, cb) {
            app.ajax('/mch/get_list', { start: s, stop: t }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_postnatal: function (pid, gravida, cb) {
            app.ajax('/mch/get_postnatal', {
                pid: pid,
                gravida: gravida
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_postnatal_all: function (cid, gravida, cb) {
            app.ajax('/mch/get_postnatal_all', {
                cid: cid,
                gravida: gravida
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },
        get_labor: function (cid, gravida, cb) {
            app.ajax('/anc/get_labor', {
                cid: cid,
                gravida: gravida
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_appointment: function (pid, hospcode, seq, cb) {
            app.ajax('/mch/get_appointment', {
                pid: pid,
                hospcode: hospcode,
                seq: seq
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        }
    };

    mch.set_list = function(rs) {

        $('#tbl_list > tbody').empty();

        if($(rs).size()) {
            $.each(rs, function(i, v) {

                var btype = v.btype == '1' ? 'NORMAL' :
                    v.btype == '2' ? 'CESAREAN' :
                        v.btype == '3' ? 'VACUUM' :
                            v.btype == '4' ? 'FORCEPS' :
                                v.btype == '5' ? 'ท่ากัน' :
                                    v.btype == '6' ? 'ABORTION' : '-';
                var tr_class = v.count_postnatal == 3 ? 'class="success"' :
                    v.count_postnatal == '1' ? 'class="warning"' :
                        v.count_postnatal == '0' ? 'class="danger"' : '';

                $('#tbl_list > tbody').append(
                    '<tr ' + tr_class + '>' +
                        '<td>' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td>' + v.birth + '</td>' +
                        '<td class="hidden-md" title="อายุ ณ วันที่คลอด">' + v.age.year +'-' + v.age.month + '-' + v.age.day + '</td>' +
                        '<td>' + v.gravida + '</td>' +
                        '<td class="hidden-md">' + v.bdate + '</td>' +
                        '<td class="hidden-md">[' + v.bhospcode + '] ' + v.bhospname + '</td>' +
                        '<td class="hidden-md">' + btype + '</td>' +
                        '<td>' + v.count_postnatal + '</td>' +
                        '<td><div class="btn-group">' +
                        '<a href="javascript:void(0);" class="btn btn-default btn-small" data-name="btn_labor" ' +
                        'data-cid="' + v.cid + '" data-gravida="' + v.gravida + '" rel="tooltip" title="ข้อมูลการคลอด">' +
                        '<i class="icon-file-text"></i></a>' +
                        '<a href="javascript:void(0);" class="btn btn-default btn-small" data-name="btn_postnatal" ' +
                        'data-pid="' + v.pid + '" data-gravida="' + v.gravida + '" data-fullname="'+ v.fullname +'" ' +
                        'data-cid="'+ v.cid +'" rel="tooltip" title="ข้อมูลเยี่ยมหลังคลอด">' +
                        '<i class="icon-edit"></i></a>' +
                        '<a href="javascript:void(0);" class="btn btn-default btn-small" data-name="btn_all_postnatal" ' +
                        'data-gravida="' + v.gravida + '" ' +
                        'data-cid="'+ v.cid +'" rel="tooltip" title="ข้อมูลเยี่ยมหลังคลอดทั้งหมด">' +
                        '<i class="icon-share"></i></a>' +
                        '</div></td>' +
                        '</tr>'
                );
            });

            app.set_runtime();
        }
        else {
            $('#tbl_list > tbody').append('<tr><td colspan="9">ไม่พบข้อมูล</td></td></tr>');
        }
    };

    $('#btn_search').on('click', function(e) {
        e.preventDefault();

        var cid = $('#txt_query').val();

        if(!cid) {
            app.alert('กรุณาระบุเลขบัตรประชาชนเด็ก ที่ต้องการค้นหา');
        } else {
            mch.search(cid);
        }
    });

    mch.search = function(cid) {

        $('#paging').fadeOut('slow');

        mch.ajax.search(cid, function(e, v) {
            if(e) {
                app.alert(e);
            } else {
                mch.set_list(v);
            }
        });
    };

    $('#btn_refresh').on('click', function(e) {
        e.preventDefault();
        mch.get_list();
    });

    mch.get_list = function() {
        mch.ajax.get_total(function(e, total) {
            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');
                $('#spn_mch_total').html(total.toFixed());
                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('mch_paging'),
                    onSelect: function(page) {
                        app.set_cookie('mch_paging', page);

                        mch.ajax.get_list(this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="10">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                mch.set_list(rs);
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

    mch.set_postnatal = function(data) {

        $('#tbl_postnatal_list > tbody').empty();

        $.each(data, function(i, v) {
            var ppresult = v.ppresult == '1' ? 'ปกติ' :
                v.ppresult == '2' ? 'ผิดปกติ' :
                    v.ppresult == '9' ? 'ไม่ทราบ' : '-';

            $('#tbl_postnatal_list > tbody').append(
                '<tr>' +
                    '<td>'+ v.ppcare +'</td>' +
                    '<td>['+ v.ppplace_code +'] ' + v.ppplace_name + '</td>' +
                    '<td>'+ ppresult +'</td>' +
                    '</tr>'
            );
        });
    }

    $(document).on('click', 'a[data-name="btn_postnatal"]', function(e) {
        e.preventDefault();

        var pid = $(this).data('pid'),
            gravida = $(this).data('gravida'),
            fullname = $(this).data('fullname'),
            cid = $(this).data('cid');

        mch.ajax.get_postnatal(pid, gravida, function(e, v) {
            if(e || $(v).size() == 0) {
                app.alert('ไม่พบข้อมูลการเยี่ยมหลังคลอด');
            } else {
                $('#txt_fullname').val(fullname);
                $('#txt_cid').val(cid);
                $('#txt_postnatal_gravida').val(gravida);

                mch.set_postnatal(v);

                mch.modal.show_postnatal();
            }
        });
    });

    $(document).on('click', 'a[data-name="btn_labor"]', function(e) {

        e.preventDefault();

        var cid = $(this).data('cid'),
            gravida = $(this).data('gravida');

        mch.ajax.get_labor(cid, gravida, function(err, v) {
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
                mch.modal.show_labor()
            }
        });
    });

    $(document).on('click', 'a[data-name="btn_all_postnatal"]', function(e) {
        e.preventDefault();

        var cid = $(this).data('cid'),
            gravida = $(this).data('gravida');

        $('#txt_query_visit').val(cid);
        $('#txt_gravida').val(gravida);
        //search
        $('#btn_search_visit').trigger('click');

        $('a[href="#profile"]').tab('show');
    });

    $('#btn_search_visit').on('click', function(e) {
        e.preventDefault();

        var cid = $('#txt_query_visit').val(),
            gravida = $('#txt_gravida').val();

        if(!cid) {
            app.alert('กรุณาระบุ เลขบัตรประชาชน');
        } else if(!gravida) {
            app.alert('กรุณาระบุครรภ์ที่ต้องการตรวจสอบ');
        } else {
            mch.ajax.get_postnatal_all(cid, gravida, function(e, v) {
                if(e) {
                    $('#tbl_visit_list > tbody').empty();
                    $('#tbl_visit_list > tbody').append('<tr><td colspan="6">ไม่พบข้อมูล</td></td></tr>');
                    app.alert(e);
                } else {
                    $('#tbl_visit_list > tbody').empty();
                    mch.set_visit(v);
                }
            });
        }
    });

    mch.set_visit = function(rs) {

        if($(rs).size()) {

            $.each(rs, function(i, v) {

                i++;

                var result = v.ppresult == '1' ?
                    '<p class="text-success"><strong>ปกติ</strong></p>' :
                    v.ppresult == '2' ?
                    '<p class="text-danger"><strong>ผิดปกติ</strong></p>' :
                    '<p class="text-muted"><strong>ไม่ได้ตรวจ</strong></p>';

                var is_appoint = v.appoint ? '<a href="javascript:void(0);" data-name="btn_get_appointment" class="btn btn-default" title="ข้อมูลนัดครั้งต่อไป" rel="tooltip"' +
                        'data-seq="'+ v.seq +'" data-pid="'+ v.pid +'" data-hospcode="' + v.hospcode + '">' +
                        '<i class="icon-calendar"></i></a>' : '<p class="text-muted"><i class="icon-minus"></i></p>';

                $('#tbl_visit_list > tbody').append(
                    '<tr>' +
                        '<td>' + i + '</td>' +
                        '<td>' + v.ppcare + '</td>' +
                        '<td>' + v.gravida + '</td>' +
                        '<td>[' + v.ppplace_code + '] ' + v.ppplace_name + '</td>' +
                        '<td>' + result + '</td>' +
                        '<td><div class="btn-group">' + is_appoint + '</div></td>' +
                        '</tr>'
                );
            });

            app.set_runtime();
        }
        else {
            $('#tbl_visit_list > tbody').append('<tr><td colspan="6">ไม่พบข้อมูล</td></td></tr>');
        }
    };

    $(document).on('click', 'a[data-name="btn_get_appointment"]', function(e) {
        e.preventDefault();

        var seq = $(this).data('seq'),
            pid = $(this).data('pid'),
            hospcode = $(this).data('hospcode');

        mch.ajax.get_appointment(pid, hospcode, seq, function(e, v) {
            if(e) {
                app.alert(e);
            } else {
                mch.set_appoint(v);
                mch.modal.show_appoint();
            }
        });
    });

    mch.set_appoint = function(rs) {

        $('#tbl_appoint_list > tbody').empty();

        if($(rs).size()) {
            $.each(rs, function(i, v) {

                i++;

                $('#tbl_appoint_list > tbody').append(
                    '<tr>' +
                        '<td>' + i + '</td>' +
                        '<td>' + v.apdate + '</td>' +
                        '<td>' + v.aptype + '</td>' +
                        '<td>[' + v.apdiag_code + '] ' + v.apdiag_name + '</td>' +
                        '</tr>'
                );
            });
        }
        else {
            $('#tbl_appoint_list > tbody').append('<tr><td colspan="4">ไม่พบข้อมูล</td></td></tr>');
        }
    };

    mch.get_list();

});