$(function() {
    var anc = {};

    anc.modal = {
        show_survey: function() {
            $('#mdl_anc_survey').modal({
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

        show_prenatal: function() {
            $('#mdl_prenatal').modal({
                keyboard: false,
                backdrop: 'static'
            });
        },

        show_appoint: function() {
            $('#mdl_appointment').modal({
                keyboard: false,
                backdrop: 'static'
            });
        },

        hide_survey: function() {
            $('#mdl_anc_survey').modal('hide');
        },

        hide_labor: function() {
            $('#mdl_labor').modal('hide');
        }
    };

    anc.ajax = {
        get_total: function (cb) {
            app.ajax('/anc/get_total', {}, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        get_list: function (s, t, cb) {
            app.ajax('/anc/get_list', { start: s, stop: t }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_visit: function (query, s, t, cb) {
            app.ajax('/anc/get_visit', {
                query: query,
                start: s,
                stop: t
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_visit_total: function (query, cb) {
            app.ajax('/anc/get_visit_total', { query: query}, function (e, v) {
               e ? cb (e, null) : cb (null, v.total);
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

        get_prenatal: function (pid, gravida, cb) {
            app.ajax('/anc/get_prenatal', {
                pid: pid,
                gravida: gravida
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_prenatal_by_hospcode: function (pid, gravida, hospcode, cb) {
            app.ajax('/anc/get_prenatal', {
                pid: pid,
                gravida: gravida,
                hospcode: hospcode
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_survey: function (pid, gravida, cb) {
            app.ajax('/anc/get_survey', {
                pid: pid,
                gravida: gravida
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_survey_by_hospcode: function (pid, gravida, hospcode, cb) {
            app.ajax('/anc/get_survey', {
                pid: pid,
                gravida: gravida,
                hospcode: hospcode
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        search: function (query, cb) {
            app.ajax('/anc/search', {
                query: query
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        save_survey: function (i, cb) {
            app.ajax('/anc/save_survey', {
                ch1: i.ch1,
                ch2: i.ch2,
                ch3: i.ch3,
                ch4: i.ch4,
                ch5: i.ch5,
                ch6: i.ch6,
                ch7: i.ch7,
                ch8: i.ch8,
                ch9: i.ch9,
                ch10: i.ch10,
                ch11: i.ch11,
                ch12: i.ch12,
                ch13: i.ch13,
                ch14: i.ch14,
                ch15: i.ch15,
                ch16: i.ch16,
                ch17: i.ch17,
                ch18: i.ch18,
                pid: i.pid,
                gravida: i.gravida,
                other_ill: i.other_ill
            }, function (e) {
               e ? cb (e) : cb (null);
            });
        },

        do_process: function (cb) {
            app.ajax('/anc/do_process', {}, function (e) {
               e ? cb (e, null) : cb (null);
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


    anc.set_visit = function(rs) {

        if($(rs).size()) {
            $.each(rs, function(i, v) {

                var result = v.ancresult == '1' ?
                    '<p class="text-success"><strong>ปกติ</strong></p>' :
                    v.ancresult == '2' ?
                    '<p class="text-danger"><strong>ผิดปกติ</strong></p>' :
                    '<p class="text-muted"><strong>ไม่ได้ตรวจ</strong></p>';

                var is_survey = v.is_survey ? '<a href="javascript:void(0);" class="btn btn-success btn-sm" ' +
                    'data-pid="' + v.pid + '" data-gravida="' + v.gravida + '" data-hospcode="' + v.hospcode + '"' +
                    'title="ดูข้อมูล" rel="tooltip" data-name="btn_get_survey_by_hospcode">' +
                    '<i class="icon-check"></i></a>' :
                    '<p class="text-muted"><span class="icon-check-empty"></span></p>';

                var is_labor = v.is_labor ? '<a href="javascript:void(0);" class="btn btn-success btn-sm" ' +
                    'data-gravida="'+ v.gravida +'" data-cid="' + v.cid + '" data-name="btn_get_labor" >' +
                    '<span class="icon-check"></span></a>' : '<p class="text-muted"><span class="icon-check-empty"></span></p>';

                var is_appoint = v.appoint ? '<a href="javascript:void(0);" data-name="btn_get_appointment" class="btn btn-default btn-sm" title="ข้อมูลนัดครั้งต่อไป" rel="tooltip"' +
                        'data-seq="'+ v.seq +'" data-pid="'+ v.pid +'" data-hospcode="' + v.hospcode + '">' +
                        '<i class="icon-calendar"></i></a>' : '<p class="text-muted"><i class="icon-minus"></i></p>';

                $('#tbl_visit_list > tbody').append(
                    '<tr>' +
                        '<td>' + v.date_serv + '</td>' +
                        '<td>' + v.hospcode + ' ' + v.hospname + '</td>' +
                        '<td>' + v.gravida + '</td>' +
                        '<td>' + v.ancno + '</td>' +
                        '<td>' + v.ga + '</td>' +
                        '<td>' + result + '</td>' +
                        '<td>' + is_labor + '</td>' +
                        '<td>' + is_survey + '</td>' +
                        '<td>'+ is_appoint +'</td>' +
                        '<td><div class="btn-group">' +
                        '<a href="javascript:void(0);" data-name="btn_get_prenatal_by_hospcode" class="btn btn-default btn-sm" title="ข้อมูลการตั้งครรภ์" rel="tooltip"' +
                        'data-gravida="'+ v.gravida +'" data-pid="'+ v.pid +'" data-hospcode="' + v.hospcode + '">' +
                        '<i class="icon-file-text"></i></a>' +
                        '</div></td>' +
                        '</tr>'
                );
            });

            app.set_runtime();
        }
        else {
            $('#tbl_visit_list > tbody').append('<tr><td colspan="10">ไม่พบข้อมูล</td></td></tr>');
        }
    };

        $(document).on('click', 'a[data-name="btn_get_appointment"]', function(e) {
        e.preventDefault();

        var seq = $(this).data('seq'),
            pid = $(this).data('pid'),
            hospcode = $(this).data('hospcode');

        anc.ajax.get_appointment(pid, hospcode, seq, function(e, v) {
            if(e) {
                app.alert(e);
            } else {
                anc.set_appoint(v);
                anc.modal.show_appoint();
            }
        });
    });

    anc.set_appoint = function(rs) {

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

    $(document).on('click', 'a[data-name="btn_survey"]', function(e) {
        e.preventDefault();

        var pid = $(this).data('pid'),
            gravida = $(this).data('gravida');

        anc.clear_survey_form();

        anc.ajax.get_survey(pid, gravida, function(err, v) {
            if(err) {
                app.alert(err);
            } else {
                anc.set_survey(v);
            }
        });

        $('#txt_ans_pid').val(pid);
        $('#txt_ans_gravida').val(gravida);

        $('a[href="#tab_ans_history"]').tab('show');

        anc.modal.show_survey();
    });

    $(document).on('click', 'a[data-name="btn_get_survey_by_hospcode"]', function(e) {
        e.preventDefault();

        var pid = $(this).data('pid'),
            gravida = $(this).data('gravida'),
            hospcode = $(this).data('hospcode');

        anc.clear_survey_form();

        anc.ajax.get_survey_by_hospcode(pid, gravida, hospcode, function(err, v) {
            if(err) {
                app.alert(err);
            } else {
                anc.set_survey(v);
            }
        });

        $('#txt_ans_pid').val(pid);
        $('#txt_ans_gravida').val(gravida);

        anc.set_disabled_survey_form();

        $('a[href="#tab_ans_history"]').tab('show');

        anc.modal.show_survey();
    });

    anc.set_survey = function(v) {
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
    };

    anc.set_disabled_survey_form = function() {
        $('#sl1').prop('disabled', true).css('background-color', 'white');
        $('#sl2').prop('disabled', true).css('background-color', 'white');
        $('#sl3').prop('disabled', true).css('background-color', 'white');
        $('#sl4').prop('disabled', true).css('background-color', 'white');
        $('#sl5').prop('disabled', true).css('background-color', 'white');
        $('#sl6').prop('disabled', true).css('background-color', 'white');
        $('#sl7').prop('disabled', true).css('background-color', 'white');
        $('#sl8').prop('disabled', true).css('background-color', 'white');
        $('#sl9').prop('disabled', true).css('background-color', 'white');
        $('#sl10').prop('disabled', true).css('background-color', 'white');
        $('#sl11').prop('disabled', true).css('background-color', 'white');
        $('#sl12').prop('disabled', true).css('background-color', 'white');
        $('#sl13').prop('disabled', true).css('background-color', 'white');
        $('#sl14').prop('disabled', true).css('background-color', 'white');
        $('#sl15').prop('disabled', true).css('background-color', 'white');
        $('#sl16').prop('disabled', true).css('background-color', 'white');
        $('#sl17').prop('disabled', true).css('background-color', 'white');
        $('#sl18').prop('disabled', true).css('background-color', 'white');

        $('#txt_ans_other_ill').prop('disabled', true).css('background-color', 'white');
        $('#btn_save_survey').fadeOut('slow');
    };

    anc.set_list = function(rs) {

        $('#tbl_list > tbody').empty();

        if($(rs).size()) {
            $.each(rs, function(i, v) {

                var is_labor = '';

                var is_survey = v.is_survey ? '<a href="javascript:void(0);" class="btn btn-success btn-sm" ' +
                    'data-pid="' + v.pid + '" data-gravida="' + v.gravida + '" data-hospcode="' + v.hospcode + '"' +
                    'title="ดูข้อมูล" rel="tooltip" data-name="btn_get_survey_by_hospcode">' +
                    '<i class="icon-check"></i></a>' :
                    '<p class="text-muted"><span class="icon-check-empty"></span></p>';

                if (v.bdate != '-') {
                    is_labor = '<a href="javascript:void(0);" class="btn btn-success btn-sm" data-name="btn_get_labor" ' +
                        'data-cid="'+ v.cid +'" data-gravida="'+ v.gravida +'">' +
                        '<span class="icon-check"></span></a>';
                } else {
                    is_labor = '<p class="text-muted"><span class="icon-check-empty"></span></p>';
                }

                var tr_class = v.anc_count >= 5 ? 'class="success"' : '';

                $('#tbl_list > tbody').append(
                    '<tr '+ tr_class +'>' +
                        '<td>' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td>' + v.birth + '</td>' +
                        '<td title="อายุ ณ วันฝากครรภ์ครั้งแรก" class="hidden-md">' + v.age.year +'-' + v.age.month + '-' + v.age.day + '</td>' +
                        '<td class="hidden-md">' + v.first_visit + '</td>' +
                        //'<td class="hidden-md">' + v.last_visit + '</td>' +
                        '<td>' + v.gravida + '</td>' +
                        //'<td class="hidden-md">' + v.edc + '</td>' +
                        '<td class="hidden-md">' + v.anc_count + '</td>' +
                        '<td>' + is_labor + '</td>' +
                        '<td>' + is_survey + '</td>' +
                        '<td><div class="btn-group">' +
                        '<a href="javascript:void(0);" class="btn btn-default btn-sm" data-name="btn_prenatal" ' +
                        'data-pid="' + v.pid + '" data-gravida="' + v.gravida + '" rel="tooltip" title="ข้อมูลการตั้งครรภ์">' +
                        '<i class="icon-file-text"></i></a>' +
                        '<a href="javascript:void(0);" class="btn btn-default btn-sm" data-name="btn_survey" ' +
                        'data-pid="' + v.pid + '" data-gravida="' + v.gravida + '" data-hospcode="'+ v.hospcode +'" rel="tooltip" title="บันทึกข้อมูลการคัดกรอง">' +
                        '<i class="icon-edit"></i></a>' +
                        '<a href="javascript:void(0);" class="btn btn-default btn-sm" data-name="btn_get_visit" ' +
                        'data-cid="' + v.cid + '" rel="tooltip" title="ข้อมูลการรับบริการ">' +
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

    anc.get_list = function() {
        anc.ajax.get_total(function(e, total) {
            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');
                $('#spn_anc_total').html(total.toFixed());

                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('death_paging'),
                    onSelect: function(page) {
                        app.set_cookie('death_paging', page);

                        anc.ajax.get_list(this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="10">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                anc.set_list(rs);
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


    anc.get_visit = function(query) {
        anc.ajax.get_visit_total(query, function(e, total) {
            if (e) {
                app.alert(e);
            } else {
                $('#visit_paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('visit_list'),
                    onSelect: function(page) {
                        app.set_cookie('visit_list', page);

                        anc.ajax.get_visit(query, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_visit_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_visit_list > tbody').append('<tr><td colspan="9">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                anc.set_visit(rs);
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

    $(document).on('click', 'a[data-name="btn_get_visit"]', function(e) {
        e.preventDefault();

        var cid = $(this).data('cid');
        $('#txt_query_visit').val(cid);

        $('#btn_search_visit').trigger('click');

        $('a[href="#profile"]').tab('show');

    });

    //get visit list
    $('#btn_search_visit').on('click', function(e) {
        e.preventDefault();

        var query = $('#txt_query_visit').val();
        if(!query) {
            app.alert('กรณาระบุคำค้นหา');
        } else {
            anc.get_visit(query);
        }
    });

    anc.clear_survey_form = function() {
        $('#sl1').removeProp('disabled');
        $('#sl2').removeProp('disabled');
        $('#sl3').removeProp('disabled');
        $('#sl4').removeProp('disabled');
        $('#sl5').removeProp('disabled');
        $('#sl6').removeProp('disabled');
        $('#sl7').removeProp('disabled');
        $('#sl8').removeProp('disabled');
        $('#sl9').removeProp('disabled');
        $('#sl10').removeProp('disabled');
        $('#sl11').removeProp('disabled');
        $('#sl12').removeProp('disabled');
        $('#sl13').removeProp('disabled');
        $('#sl14').removeProp('disabled');
        $('#sl15').removeProp('disabled');
        $('#sl16').removeProp('disabled');
        $('#sl17').removeProp('disabled');
        $('#sl18').removeProp('disabled');

        $('#txt_ans_other_ill').removeProp('disabled');
        $('#btn_save_survey').fadeIn('slow');

        app.set_first_selected($('#sl1'));
        app.set_first_selected($('#sl2'));
        app.set_first_selected($('#sl3'));
        app.set_first_selected($('#sl4'));
        app.set_first_selected($('#sl5'));
        app.set_first_selected($('#sl6'));
        app.set_first_selected($('#sl7'));
        app.set_first_selected($('#sl8'));
        app.set_first_selected($('#sl9'));
        app.set_first_selected($('#sl10'));
        app.set_first_selected($('#sl11'));
        app.set_first_selected($('#sl12'));
        app.set_first_selected($('#sl13'));
        app.set_first_selected($('#sl14'));
        app.set_first_selected($('#sl15'));
        app.set_first_selected($('#sl16'));
        app.set_first_selected($('#sl17'));
        app.set_first_selected($('#sl18'));

        $('#txt_ans_other_ill').val('');
        $('#txt_ans_pid').val('');
        $('#txt_ans_gravida').val('');
    };

    $('#mdl_anc_survey').on('hidden.bs.modal', function () {
        anc.clear_survey_form();
    });

    $('#btn_save_survey').on('click', function(e) {
        e.preventDefault();

        var items = {};

        items.ch1 = $('#sl1').val();
        items.ch2 = $('#sl2').val();
        items.ch3 = $('#sl3').val();
        items.ch4 = $('#sl4').val();
        items.ch5 = $('#sl5').val();
        items.ch6 = $('#sl6').val();
        items.ch7 = $('#sl7').val();
        items.ch8 = $('#sl8').val();
        items.ch9 = $('#sl9').val();
        items.ch10 = $('#sl10').val();
        items.ch11 = $('#sl11').val();
        items.ch12 = $('#sl12').val();
        items.ch13 = $('#sl13').val();
        items.ch14 = $('#sl14').val();
        items.ch15 = $('#sl15').val();
        items.ch16 = $('#sl16').val();
        items.ch17 = $('#sl17').val();
        items.ch18 = $('#sl18').val();
        items.other_ill = $('#txt_ans_other_ill').val()

        items.pid = $('#txt_ans_pid').val();
        items.gravida = $('#txt_ans_gravida').val();

        if(confirm('คุณต้องการบันทึกข้อมูล ใช่หรือไม่?')) {

            anc.ajax.save_survey(items, function(e) {

                if(e) {
                    app.alert(e);
                } else {

                    app.alert('บันทึกรายการเสร็จเรียบร้อยแล้ว');
                    anc.get_list();
                    anc.clear_survey_form();

                    anc.modal.hide_survey();
                }
            });
        }
    });

    $('#btn_process').on('click', function(e) {
        e.preventDefault();

        if(confirm('คุณต้องการประมวลผลข้อมูลใหม่ ใช่หรือไม่?')) {
            app.show_loading();
            anc.ajax.do_process(function(e) {
                if(e) {
                    app.alert(e);
                } else {
                    app.alert('ประมวลผลเสร็จเรียบร้อยแล้ว');
                    anc.get_list()
                }
            });
            app.hide_loading();
        }
    });

    anc.set_labor = function(v) {

    };

    $(document).on('click', 'a[data-name="btn_get_labor"]', function(e) {
        e.preventDefault();

        var cid = $(this).data('cid'),
            gravida = $(this).data('gravida');

        anc.ajax.get_labor(cid, gravida, function(err, v) {
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
                anc.modal.show_labor()
            }
        });
    });

    $(document).on('click', 'a[data-name="btn_prenatal"]', function(e) {
        e.preventDefault();
        var pid = $(this).data('pid'),
            gravida = $(this).data('gravida');

        anc.ajax.get_prenatal(pid, gravida, function(err, v) {
            if(err) {
                app.alert('เกิดข้อผิดพลาด/ไม่พบข้อมูล');
            } else if( !$(v).size() ) {
                app.alert('ไม่พบข้อมูล');
            } else {
                $('#txt_prenatal_edc').val(v[0]['edc']);
                $('#txt_prenatal_lmp').val(v[0]['lmp']);
                $('#sl_prenatal_vdrl_result').val(v[0]['vdrl_result']);
                $('#sl_prenatal_hb_result').val(v[0]['hb_result']);
                $('#sl_prenatal_date_hct').val(v[0]['date_hct']);
                $('#sl_prenatal_hct_result').val(v[0]['hct_result']);
                $('#sl_prenatal_thalassemia').val(v[0]['thalassemia']);
                $('#sl_prenatal_hiv_result').val(v[0]['hiv_result']);

                $('#txt_prenatal_fullname').val(v[0]['fullname']);
                $('#txt_prenatal_cid').val(v[0]['cid']);
                $('#txt_prenatal_gravida').val(v[0]['gravida']);

                anc.modal.show_prenatal();
            }

        });
    });

    $(document).on('click', 'a[data-name="btn_get_prenatal_by_hospcode"]', function(e) {
        e.preventDefault();
        var pid = $(this).data('pid'),
            gravida = $(this).data('gravida'),
            hospcode= $(this).data('hospcode');

        anc.ajax.get_prenatal_by_hospcode(pid, gravida, hospcode, function(err, v) {
            if(err) {
                app.alert('เกิดข้อผิดพลาด/ไม่พบข้อมูล');
            } else if( !$(v).size() ) {
                app.alert('ไม่พบข้อมูล');
            } else {
                $('#txt_prenatal_edc').val(v[0]['edc']);
                $('#txt_prenatal_lmp').val(v[0]['lmp']);
                $('#sl_prenatal_vdrl_result').val(v[0]['vdrl_result']);
                $('#sl_prenatal_hb_result').val(v[0]['hb_result']);
                $('#sl_prenatal_date_hct').val(v[0]['date_hct']);
                $('#sl_prenatal_hct_result').val(v[0]['hct_result']);
                $('#sl_prenatal_thalassemia').val(v[0]['thalassemia']);
                $('#sl_prenatal_hiv_result').val(v[0]['hiv_result']);

                $('#txt_prenatal_fullname').val(v[0]['fullname']);
                $('#txt_prenatal_cid').val(v[0]['cid']);
                $('#txt_prenatal_gravida').val(v[0]['gravida']);

                anc.modal.show_prenatal();
            }

        });
    });

    $('#btn_refresh').on('click', function(e) {
        e.preventDefault();
        anc.get_list();
    });

    $('#btn_search_anc').on('click', function(e) {
        e.preventDefault();

        var query = $('#txt_query').val();
        if(query) {
            anc.ajax.search(query, function(err, v) {
                if(err) {
                    app.alert(err);
                } else {
                    $('#paging').fadeOut('slow');
                    anc.set_list(v);
                }
            });

        } else {
            app.alert('กรุณาระบุคำค้นหา');
        }
    });

    anc.get_list();

});