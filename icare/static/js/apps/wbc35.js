$(function(){
    var wbc35 = {};

    wbc35.modal = {
        show_vaccines: function() {
            $('#mdl_vaccines').modal({
                keyboard: false,
                backdrop: 'static'
            });
        },
        show_nutrition: function() {
            $('#mdl_nutrition').modal({
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

    wbc35.ajax = {
        get_total: function (start, end, cb) {
            app.ajax('/wbc35/get_total', {
                start_date: start,
                end_date: end
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        get_list: function (start_date, end_date, s, t, cb) {
            app.ajax('/wbc35/get_list', {
                start_date: start_date,
                end_date: end_date,
                start: s,
                stop: t
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_vaccines: function (pid, cb) {
            app.ajax('/wbc35/get_vaccines', {
                pid: pid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total_by_vid: function (vid, start, end, cb) {
            app.ajax('/wbc35/get_total_by_vid', {
                start_date: start,
                end_date: end,
                vid: vid
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        get_list_by_vid: function (vid, start_date, end_date, s, t, cb) {
            app.ajax('/wbc35/get_list_by_vid', {
                start_date: start_date,
                end_date: end_date,
                vid: vid,
                start: s,
                stop: t
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        search_visit: function (cid, cb) {
            app.ajax('/wbc35/search_visit', {
                cid: cid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_nutrition: function (cid, cb) {
            app.ajax('/wbc35/get_nutrition', {
                cid: cid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_nutrition_owner: function (pid, hospcode, cb) {
            app.ajax('/wbc35/get_nutrition_owner', {
                pid: pid,
                hospcode: hospcode
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

    wbc35.get_list = function(start, end) {
        wbc35.ajax.get_total(start, end, function(e, total) {
            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');

                $('#spn_total').html(total.toFixed());

                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('wbc35_paging'),
                    onSelect: function(page) {
                        app.set_cookie('wbc35_paging', page);

                        wbc35.ajax.get_list(start, end, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="6">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                wbc35.set_list(rs);
                            }
                        });

                    },
                    onFormat: app.setPagingFormat
                });
            }
        });
    };

    wbc35.get_list_by_vid = function(vid, start, end) {
        wbc35.ajax.get_total_by_vid(vid, start, end, function(e, total) {
            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');

                $('#spn_total').html(total.toFixed());

                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('wbc35_vid_paging'),
                    onSelect: function(page) {
                        app.set_cookie('wbc35_vid_paging', page);

                        wbc35.ajax.get_list_by_vid(vid, start, end, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="6">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                wbc35.set_list(rs);
                            }
                        });

                    },
                    onFormat: app.setPagingFormat
                });
            }
        });
    };

     wbc35.set_list = function(rs) {

        $('#tbl_list > tbody').empty();

        if($(rs).size()) {
            $.each(rs, function(i, v) {

                var x = 0;

                $.each(v.vaccines, function(i, vcc) {
                    if(vcc) x++;
                });
                var vcc_per = (x*100)/3;

                var sex = v.sex == '1' ? 'ชาย' : 'หญิง';

                var is_nutrition = v.nutrition ? '<a href="javascript:void(0);" data-name="btn_visit_nutrition" ' +
                    'class="btn btn-success" title="การตรวจพัฒนาการที่นี่" rel="tooltip"' +
                        'data-pid="'+ v.pid +'" data-hospcode="' + v.hospcode + '">' +
                        '<i class="fa fa-bar-chart-o"></i></a>' : '<p class="text-muted"><i class="fa fa-square-o"></i></p>';


                $('#tbl_list > tbody').append(
                    '<tr>' +
                        '<td class="text-center">' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td class="text-center hidden-md hidden-sm">' + v.birth + '</td>' +
                        '<td class="text-center">' + v.age.year +'-' + v.age.month + '-' + v.age.day + '</td>' +
                        '<td class="text-center">' + sex + '</td>' +
                        '<td class="hidden-md hidden-sm">' + v.address + '</td>' +
                        '<td class="text-center">' + is_nutrition + '</td>' +
                        '<td><div class="progress progress-striped" title="'+vcc_per.toFixed(2)+'%">' +
                        '<div class="progress-bar progress-bar-info" style="width: '+vcc_per.toFixed()+'%"></div>' +
                        '</div></td>' +
                        '<td class="text-center"><div class="btn-group">' +
                        '<a href="javascript:void(0);" class="btn btn-default" data-name="btn_get_vaccines" ' +
                        'data-pid="'+ v.pid +'" title="ข้อมูลการรับวัคซีน" rel="tooltip">' +
                        '<i class="fa fa-desktop"></i></a>' +
                        '<a href="javascript:void(0);" class="btn btn-primary" data-name="btn_get_nutrition"' +
                        'data-cid="'+ v.cid +'" title="ประวัติการตรวจพัฒนาการ" rel="tooltip">' +
                        '<i class="fa fa-bar-chart-o"></i></a>' +
                        '<a href="javascript:void(0);" class="btn btn-default" data-name="btn_get_vaccines_history"' +
                        'data-cid="'+ v.cid +'" title="ประวัติการรับวัคซีน" rel="tooltip">' +
                        '<i class="fa fa-share-square-o"></i></a>' +
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

    $(document).on('click', 'a[data-name="btn_get_vaccines"]', function(e) {
        e.preventDefault();

        var pid = $(this).data('pid');

        wbc35.ajax.get_vaccines(pid, function(e, v) {
            if(e) {
                app.alert(e);
            } else {
                wbc35.set_vaccine_list(v);
                wbc35.modal.show_vaccines();
            }
        });
    });

    wbc35.set_vaccine_list = function(v) {

        $('#tbl_vaccines_list > tbody').empty();

        $.each(v, function(i, v) {
            $('#tbl_vaccines_list > tbody').append(
                '<tr>' +
                    '<td>' + v.name + '</td>' +
                    '<td>' + app.clear_null(v.date_serv) + '</td>' +
                    '<td>[' + app.clear_null(v.vaccineplace_code) + '] ' + app.clear_null(v.vaccineplace_name) +'</td>' +
                    '</tr>'
            );
        });
    };

    $('#btn_filter').on('click', function(e) {
        e.preventDefault();

        var start_date = $('#txt_start_date').val(),
            end_date = $('#txt_end_date').val(),
            vid = $('#sl_villages').val();

        if(!start_date) {
            app.alert('กรุณารุบุวันที่เริ่มต้น');
        } else if(!end_date) {
            app.alert('กรุณาระบุวันที่สิ้นสุด');
        } else {
            if(!vid) {
                wbc35.get_list(start_date, end_date);
            } else {
                wbc35.get_list_by_vid(vid, start_date, end_date);
            }
        }
    });

    $(document).on('click', 'a[data-name="btn_get_vaccines_history"]', function(e) {
        e.preventDefault();

        var cid = $(this).data('cid');

        $('#txt_query_visit').val(cid);
        $('#btn_search_visit').trigger('click');

        $('a[href="#profile"]').tab('show');
    });

    $('#btn_search_visit').on('click', function(e) {

        e.preventDefault();

        var cid = $('#txt_query_visit').val();
        if(cid) {
            wbc35.do_search_visit(cid);
        } else {
            app.alert('กรุณาระบุเลขบัตรประชาชนเพื่อค้นหา');
        }
    });

    wbc35.do_search_visit = function(cid) {
        wbc35.ajax.search_visit(cid, function(e, v) {

            $('#tbl_visit_list > tbody').empty();

            if(e) {
                $('#tbl_visit_list > tbody').append('<tr><td colspan="5">ไม่พบรายการ</td></tr>');
                app.alert(e);
            } else {
                wbc35.set_visit_history(v);
            }
        });
    };

    wbc35.set_visit_history = function(v) {
        if($(v).size()) {
            $.each(v, function(i, v) {
                i++;

                var is_appoint = v.appoint ? '<a href="javascript:void(0);" data-name="btn_get_appointment" ' +
                    'class="btn btn-default" title="ข้อมูลนัดครั้งต่อไป" rel="tooltip"' +
                        'data-seq="'+ v.seq +'" data-pid="'+ v.pid +'" data-hospcode="' + v.hospcode + '">' +
                        '<i class="fa fa-calendar"></i></a>' : '<p class="text-muted"><i class="fa fa-square-o"></i></p>';

                $('#tbl_visit_list > tbody').append(
                    '<tr>' +
                        '<td>' + i + '</td>' +
                        '<td class="text-center">' + v.date_serv + '</td>' +
                        '<td>[' + v.code + '] ' + v.name + '</td>' +
                        '<td>[' + v.hospcode + '] ' + v.hospname + '</td>' +
                        '<td class="text-center">' + is_appoint + '</td>' +
                        '</tr>'
                );
            });
        } else {
            $('#tbl_visit_list > tbody').append('<tr><td colspan="5">ไม่พบรายการ</td></tr>');
        }
    };

    $(document).on('click', 'a[data-name="btn_get_nutrition"]', function(e) {
        e.preventDefault();

        var cid = $(this).data('cid');

        wbc35.get_nutrition(cid);
    });

    wbc35.get_nutrition = function(cid) {

        $('#tbl_nutrition > tbody').empty();

        wbc35.ajax.get_nutrition(cid, function(e, v) {
            if(e) {;
                app.alert(e);
            } else {
                wbc35.set_nutrition(v);
                wbc35.modal.show_nutrition();
            }
        });
    };
    wbc35.get_nutrition_owner = function(pid, hospcode) {

        $('#tbl_nutrition > tbody').empty();

        wbc35.ajax.get_nutrition_owner(pid, hospcode, function(e, v) {
            if(e) {;
                app.alert(e);
            } else {
                wbc35.set_nutrition(v);
                wbc35.modal.show_nutrition();
            }
        });
    };

    wbc35.set_nutrition = function(v) {
        if($(v).size()) {
            $.each(v, function(i, v) {
                i++;
                var child_develop = v.childdevelop == '1' ? 'ปกติ' :
                    v.childdevelop == '2' ? 'สงสัยช้ากว่าปกติ' :
                        v.childdevelop == '3' ? 'ช้ากว่าปกติ' : '-';
                var food = v.food == '1' ? 'นมแม่อย่างเดียว' :
                    v.food == '2' ? 'นมแม่และน้ำ' :
                        v.food == '3' ? 'นมแม่และนมผสม' :
                            v.food == '4' ? 'นมผสมอย่างเดียว' : '-';

                $('#tbl_nutrition > tbody').append(
                    '<tr>' +
                        '<td>' + i + '</td>' +
                        '<td class="text-center">' + v.date_serv + '</td>' +
                        '<td>[' + v.nutritionplace_code + '] ' + v.nutritionplace_name + '</td>' +
                        '<td class="text-center">' + v.weight + '</td>' +
                        '<td class="text-center">' + v.height + '</td>' +
                        '<td class="text-center">' + child_develop + '</td>' +
                        '<td>' + food + '</td>' +
                        '</tr>'
                );
            });
        } else {
            $('#tbl_nutrition > tbody').append('<tr><td colspan="7">ไม่พบรายการ</td></tr>');
        }
    };

    $(document).on('click', 'a[data-name="btn_visit_nutrition" ]', function(e) {
        var pid = $(this).data('pid'),
            hospcode = $(this).data('hospcode');

        wbc35.get_nutrition_owner(pid, hospcode);
    });

    $(document).on('click', 'a[data-name="btn_get_appointment"]', function(e) {
        e.preventDefault();

        var seq = $(this).data('seq'),
            pid = $(this).data('pid'),
            hospcode = $(this).data('hospcode');

        wbc35.ajax.get_appointment(pid, hospcode, seq, function(e, v) {
            if(e) {
                app.alert(e);
            } else {
                wbc35.set_appoint(v);
                wbc35.modal.show_appoint();
            }
        });
    });

    wbc35.set_appoint = function(rs) {

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


});