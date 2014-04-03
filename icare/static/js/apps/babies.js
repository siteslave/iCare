$(function() {

    var babies = {};

    babies.modal = {
        show_care: function() {
            $('#mdl_care').modal({
                keyboard: false,
                backdrop: false
            });
        },

        show_newborn: function() {
            $('#mdl_newborn').modal({
                keyboard: false,
                backdrop: false
            });
        },

        show_appoint: function() {
            $('#mdl_appointment').modal({
                keyboard: false,
                backdrop: false
            });
        }
    };

    babies.ajax = {
        get_total: function (cb) {
            app.ajax('/babies/get_total', {}, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        get_total_by_birth: function (start_date, end_date, cb) {
            app.ajax('/babies/get_total_by_birth', {
                start_date: start_date,
                end_date: end_date
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        get_list: function (s, t, cb) {
            app.ajax('/babies/get_list', { start: s, stop: t }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_list_by_birth: function (start_date, end_date, s, t, cb) {
            app.ajax('/babies/get_list_by_birth', {
                start: s,
                stop: t,
                start_date: start_date,
                end_date: end_date
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        search: function (cid, cb) {
            app.ajax('/babies/search', { cid: cid }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_care: function (hospcode, pid, cb) {
            app.ajax('/babies/get_care', {
                'hospcode': hospcode,
                'pid': pid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_care_all: function (cid, cb) {
            app.ajax('/babies/get_care_all', {
                'cid': cid
            }, function (e, v) {
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

    $('#btn_search_by_birth').on('click', function(e) {
        e.preventDefault();

        var start_date = $('#txt_start_date').val(),
            end_date = $('#txt_end_date').val();

        if(!start_date) {
            app.alert('กรุณาระบุวันที่เริ่มต้น');
        } else if(!end_date) {
            app.alert('กรุณาระบุวันที่สิ้นสุด');
        } else {
            babies.get_list_by_birth(start_date, end_date);
        }
    });


    babies.get_list_by_birth = function(start_date, end_date) {

        babies.ajax.get_total_by_birth(start_date, end_date, function(e, total) {
            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');
                $('#spn_babies_total').html(total.toFixed());
                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('babies_paging_birth'),
                    onSelect: function(page) {
                        app.set_cookie('babies_paging_birth', page);

                        babies.ajax.get_list_by_birth(start_date, end_date, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="10">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                babies.set_list(rs);
                            }
                        });

                    },
                    onFormat: app.setPagingFormat
                });
            }
        });
    };

    babies.set_list = function(rs) {

        $('#tbl_list > tbody').empty();

        if($(rs).size()) {
            $.each(rs, function(i, v) {

                var btype = v.btype == '1' ? 'NORMAL' :
                    v.btype == '2' ? 'CESAREAN' :
                        v.btype == '3' ? 'VACUUM' :
                            v.btype == '4' ? 'FORCEPS' :
                                v.btype == '5' ? 'ท่ากัน' :
                                    v.btype == '6' ? 'ABORTION' : '-';
                var tr_class = v.care == 3 ? 'class="success"' :
                    v.care == '1' ? 'class="warning"' :
                        v.care == '0' ? 'class="danger"' : '';
                var sex = v.sex == '1' ? 'ชาย' : 'หญิง';

                $('#tbl_list > tbody').append(
                    '<tr ' + tr_class + '>' +
                        '<td class="text-center">' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td class="text-center">' + v.birth + '</td>' +
                        '<td class="text-center" title="อายุ ณ วันที่คลอด">' + v.age.year +'-' + v.age.month + '-' + v.age.day + '</td>' +
                        '<td class="text-center">' + sex + '</td>' +
                        '<td class="text-center">' + v.bweight + '</td>' +
                        '<td>' + v.mother.fullname + '</td>' +
                        '<td class="text-center">' + v.gravida + '</td>' +
                        '<td class="text-center">' + v.care + '</td>' +
                        '<td class="text-center"><div class="btn-group">' +
                        '<a href="javascript:void(0);" class="btn btn-default btn-small" data-name="btn_newborn" ' +
                        'data-pid="' + v.pid + '" data-hospcode="' + v.hospcode + '" data-fullname="'+ v.fullname + '" ' +
                        'data-cid="' + v.cid + '" data-gravida="' + v.gravida + '" rel="tooltip" title="ข้อมูลการคลอด">' +
                        '<i class="fa fa-file-text"></i></a>' +
                        '<a href="javascript:void(0);" class="btn btn-default btn-small" data-name="btn_get_care" ' +
                        'data-pid="' + v.pid + '" data-hospcode="' + v.hospcode + '" data-care="'+ v.care +'" rel="tooltip" title="ข้อมูลเยี่ยมหลังคลอด">' +
                        '<i class="fa fa-edit"></i></a>' +
                        '<a href="javascript:void(0);" class="btn btn-default btn-small" data-name="btn_all_care" ' +
                        'data-cid="'+ v.cid +'" rel="tooltip" title="ข้อมูลเยี่ยมหลังคลอดทั้งหมด">' +
                        '<i class="fa fa-share"></i></a>' +
                        '</div></td>' +
                        '</tr>'
                );
            });

            app.set_runtime();
        }
        else {
            $('#tbl_list > tbody').append('<tr><td colspan="10">ไม่พบข้อมูล</td></td></tr>');
        }
    };

    $('#btn_search').on('click', function(e) {
        e.preventDefault();

        var cid = $('#txt_query').val();

        if(!cid) {
            app.alert('กรุณาระบุเลขบัตรประชาชนเด็ก ที่ต้องการค้นหา');
        } else {
            babies.search(cid);
        }
    });

    babies.search = function(cid) {
        $('#paging').fadeOut('slow');
        babies.ajax.search(cid, function(e, v) {
           if(e) {
               app.alert(e);
           } else {
               babies.set_list(v);
           }
        });
    };

    babies.get_list = function() {

        babies.ajax.get_total(function(e, total) {
            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');
                $('#spn_babies_total').html(total.toFixed());
                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('babies_paging'),
                    onSelect: function(page) {
                        app.set_cookie('babies_paging', page);

                        babies.ajax.get_list(this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="10">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                babies.set_list(rs);
                            }
                        });

                    },
                    onFormat: app.setPagingFormat
                });
            }
        });
    };

    $(document).on('click', 'a[data-name="btn_get_care"]', function(e) {

        e.preventDefault();

        var pid = $(this).data('pid'),
            hospcode = $(this).data('hospcode'),
            care = $(this).data('care');

        if(care > 0) {
            babies.ajax.get_care(hospcode, pid, function(e, v) {
                if(e) {
                    app.alert(e);
                } else {
                    babies.set_care(v);
                    babies.modal.show_care();
                }
            });
        } else {
            app.alert('ไม่พบข้อมูลการเยี่ยมหลังคลอด');
        }

    });

    babies.set_care = function(v) {

        $('#tbl_care_list > tbody').empty();

        if($(v).size() > 0) {
            $.each(v, function(i, v) {
                i++;
                var result = v.result == '1' ? 'ปกติ' :
                    v.result == '2' ? 'ผิดปกติ' : 'ไม่ทราบ';
                var food = v.food == '1' ? 'นมแม่อย่างเดียว' :
                    v.food == '2' ? 'นมแม่และน้ำ' :
                        v.food == '3' ? 'นมแม่และนมผสม' :
                            v.food == '4' ? 'นมผสมอย่างเดียว' : '-';

                $('#tbl_care_list > tbody').append(
                    '<tr>' +
                        '<td class="text-center">'+ i +'</td>' +
                        '<td class="text-center">'+ v.bcare +'</td>' +
                        '<td>['+ v.bcplace_code +'] ' + v.bcplace_name + '</td>' +
                        '<td>'+ result +'</td>' +
                        '<td>'+ food +'</td>' +
                        '</tr>'
                );
            });
        } else {
            $('#tbl_care_list > tbody').append('<tr><td colspan="5"></td></tr>');
        }

    };

    $(document).on('click', 'a[data-name="btn_newborn"]', function(e) {
        e.preventDefault();
        var fullname = $(this).data('fullname'),
            cid = $(this).data('cid'),
            pid = $(this).data('pid'),
            hospcode = $(this).data('hospcode'),
            gravida = $(this).data('gravida');

        babies.ajax.get_newborn(hospcode, pid, function(e, v) {
            if(e) {
                app.alert(e);
            } else {
                $('#txt_fullname').val(fullname);
                $('#txt_cid').val(cid);
                $('#txt_gravida').val(gravida);

                babies.clear_newborn_form();
                babies.set_newborn(v[0]);

                babies.modal.show_newborn();

            }
        });
    });

    babies.clear_newborn_form = function() {
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

    babies.set_newborn = function(v) {
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

    $(document).on('click', 'a[data-name="btn_all_care"]', function(e) {
        e.preventDefault();

        var cid = $(this).data('cid');
        $('#txt_query_visit').val(cid);
        $('#btn_search_visit').trigger('click');

    });

    $('#btn_search_visit').on('click', function(e) {
        e.preventDefault();

        var cid = $('#txt_query_visit').val();

        if(cid) {
            babies.get_care_all(cid);
            $('a[href="#profile"]').tab('show');
        } else {
            app.alert('กรุณาระบุเลขบัตรประชาชน');
        }
    });

    babies.get_care_all = function(cid) {
        babies.ajax.get_care_all(cid, function(e, v) {
            if(e) {
                app.alert(e);
            } else {
                babies.set_care_all(v);
            }
        });
    };

    babies.set_care_all = function(v) {

        $('#tbl_visit_list > tbody').empty();

        if($(v).size) {
            $.each(v, function(i, v) {

                var result = v.result == '1' ? 'ปกติ' :
                    v.result == '2' ? 'ผิดปกติ' : 'ไม่ทราบ';
                var food = v.food == '1' ? 'นมแม่อย่างเดียว' :
                    v.food == '2' ? 'นมแม่และน้ำ' :
                        v.food == '3' ? 'นมแม่และนมผสม' :
                            v.food == '4' ? 'นมผสมอย่างเดียว' : '-';

                var is_appoint = v.appoint ? '<a href="javascript:void(0);" data-name="btn_get_appointment" ' +
                    'class="btn btn-default" title="ข้อมูลนัดครั้งต่อไป" rel="tooltip"' +
                        'data-seq="'+ v.seq +'" data-pid="'+ v.pid +'" data-hospcode="' + v.hospcode + '">' +
                        '<i class="fa fa-calendar"></i></a>' : '<p class="text-muted"><i class="fa fa-check-empty"></i></p>';

                i++;

               $('#tbl_visit_list > tbody').append(
                   '<tr>' +
                       '<td class="text-center">' + i + '</td>' +
                       '<td class="text-center">' + v.bcare + '</td>' +
                       '<td>[' + v.bcplace_code + '] ' + v.bcplace_name + '</td>' +
                       '<td>' + result + '</td>' +
                       '<td>' + food + '</td>' +
                       '<td class="text-center">' + is_appoint + '</td>' +
                       '</tr>'
               );
            });
        } else {
            $('#tbl_visit_list > tbody').append('<tr><td colspan="6">ไม่พบรายการ</td></tr>');
        }

    };


    $(document).on('click', 'a[data-name="btn_get_appointment"]', function(e) {
        e.preventDefault();

        var seq = $(this).data('seq'),
            pid = $(this).data('pid'),
            hospcode = $(this).data('hospcode');

        babies.ajax.get_appointment(pid, hospcode, seq, function(e, v) {
            if(e) {
                app.alert(e);
            } else {
                babies.set_appoint(v);
                babies.modal.show_appoint();
            }
        });
    });

    babies.set_appoint = function(rs) {

        $('#tbl_appoint_list > tbody').empty();

        if($(rs).size()) {
            $.each(rs, function(i, v) {

                i++;

                $('#tbl_appoint_list > tbody').append(
                    '<tr>' +
                        '<td class="text-center">' + i + '</td>' +
                        '<td class="text-center">' + v.apdate + '</td>' +
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

    $('#btn_refresh').on('click', function(e) {
        e.preventDefault();
        babies.get_list();
    });

    babies.get_list();

});