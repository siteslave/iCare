$(function(){
    var ncdscreen = {};

    ncdscreen.modal = {
        show_result: function() {
            $('#mdl_result').modal({
                keyboard: false,
                backdrop: 'static'
            });
        }
    };

    ncdscreen.ajax = {
        get_total: function (start, end, cb) {
            app.ajax('/ncdscreen/get_total', {
                start_date: start,
                end_date: end
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        get_history_total: function (cid, cb) {
            app.ajax('/ncdscreen/get_history_total', {
                cid: cid
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        get_list: function (start_date, end_date, s, t, cb) {
            app.ajax('/ncdscreen/get_list', {
                start_date: start_date,
                end_date: end_date,
                start: s,
                stop: t
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_history: function (cid, s, t, cb) {
            app.ajax('/ncdscreen/get_history', {
                cid: cid,
                start: s,
                stop: t
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_list_by_vid: function (vid, start_date, end_date, s, t, cb) {
            app.ajax('/ncdscreen/get_list_by_vid', {
                start_date: start_date,
                end_date: end_date,
                start: s,
                stop: t,
                vid: vid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total_by_vid: function (vid, start, end, cb) {
            app.ajax('/ncdscreen/get_total_by_vid', {
                start_date: start,
                end_date: end,
                vid: vid
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        get_screen: function (hospcode, date_serv, pid, cb) {
            app.ajax('/ncdscreen/get_screen', {
                hospcode: hospcode,
                date_serv: date_serv,
                pid: pid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        }
    };

    $('#btn_result').on('click', function(e) {
        e.preventDefault();

        var s = $('#txt_start_date').val(),
            e = $('#txt_end_date').val(),
            village_id = $('#sl_villages').val();

        if(!s) {
            app.alert('กรุณาระบุวันที่เริ่มต้นคัดกรอง');
        } else if(!e) {
            app.alert('กรุณาระบุวันที่สิ้นสุดการคัดกรอง');
        } else {
            if(village_id) {
                ncdscreen.get_list_by_vid(village_id, s, e);
            } else {
                ncdscreen.get_list(s, e);
            }
        }
    });

    ncdscreen.set_list = function(rs) {

        $('#tbl_list > tbody').empty();

        if($(rs).size()) {
            $.each(rs, function(i, v) {

                var sex = v.sex == '1' ? 'ชาย' : 'หญิง';
                var result = v.date_serv ? '<a href="javascript:void(0);" class="btn btn-success" ' +
                    'data-name="btn_result" data-date_serv="'+ v.date_serv +'" data-date_serv_th="'+ v.date_serv_th +'"' +
                        'data-pid="'+ v.pid +'" data-cid="'+ v.cid +'" data-birth="'+ v.birth +'" data-hospcode="'+ v.hospcode +'" ' +
                    'data-fullname="'+ v.fullname +'" data-age_y="'+ v.age.year +'" data-age_m="'+ v.age.month +'" data-age_d="'+ v.age.day+'">' +
                                '<i class="icon-bar-chart"></i></a>' :
                    '<p class="text-muted"><i class="icon-check-empty"></i></p>';

                $('#tbl_list > tbody').append(
                    '<tr>' +
                        '<td>' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td class="hidden-md hidden-sm">' + v.birth + '</td>' +
                        '<td class="hidden-md hidden-sm">' + v.age.year +'-' + v.age.month + '-' + v.age.day + '</td>' +
                        '<td>' + sex + '</td>' +
                        '<td class="hidden-md hidden-sm">' + v.address + '</td>' +
                        '<td>' + v.typearea + '</td>' +
                        '<td>' + v.date_serv_th + '</td>' +
                        '<td>' + result + '</td>' +
                        '<td>' +
                        '<a href="javascript:void(0);" class="btn btn-default" data-name="btn_get_history" ' +
                        'data-cid="'+ v.cid +'" title="ดูประวัติการรับบริการคัดกรองทั้งหมด" rel="tooltip">' +
                        '<i class="icon-time"></i></a>' +
                        '</td>' +
                        '</tr>'
                );
            });

            app.set_runtime();
        }
        else {
            $('#tbl_list > tbody').append('<tr><td colspan="10">ไม่พบข้อมูล</td></td></tr>');
        }
    };

    ncdscreen.set_visit_history = function(rs) {

        $('#tbl_visit_list > tbody').empty();

        if($(rs).size()) {

            $.each(rs, function(i, v) {

                $('#tbl_visit_list > tbody').append(
                    '<tr>' +
                        '<td>' + v.date_serv_th + '</td>' +
                        '<td>[' + v.hospcode + '] '+ v.hospname +'</td>' +
                        '<td>' + v.weight + '</td>' +
                        '<td>' + v.height + '</td>' +
                        '<td>' + v.sbp_1 + '/' + v.dbp_1 + '</td>' +
                        '<td>' + v.bslevel + '</td>' +
                        '<td>' +
                        '<a href="javascript:void(0);" class="btn btn-success" ' +
                        'data-name="btn_result" data-date_serv="'+ v.date_serv +'" data-date_serv_th="'+ v.date_serv_th +'"' +
                        'data-pid="'+ v.pid +'" data-cid="'+ v.cid +'" data-birth="'+ v.birth +'" data-hospcode="'+ v.hospcode +'" ' +
                        'data-fullname="'+ v.fullname +'" data-age_y="'+ v.age.year +'" data-age_m="'+ v.age.month +'" data-age_d="'+ v.age.day+'">' +
                                '<i class="icon-bar-chart"></i></a>' +
                        '</td>' +
                        '</tr>'
                );
            });

            app.set_runtime();
        }
        else {
            $('#tbl_visit_list > tbody').append('<tr><td colspan="7">ไม่พบข้อมูล</td></td></tr>');
        }
    };

    ncdscreen.get_list = function(start_date, end_date) {
        ncdscreen.ajax.get_total(start_date, end_date, function(e, total) {
            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');

                $('#spn_total').html(numeral(total).format('0,0'));

                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('ncdscreen_paging'),
                    onSelect: function(page) {
                        app.set_cookie('ncdscreen_paging', page);

                        ncdscreen.ajax.get_list(start_date, end_date, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="9">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                ncdscreen.set_list(rs);
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

    ncdscreen.get_list_by_vid = function(vid, start_date, end_date) {
        ncdscreen.ajax.get_total_by_vid(vid, start_date, end_date, function(e, total) {
            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');

                $('#spn_total').html(numeral(total).format('0,0'));

                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('ncdscreen_by_vid_paging'),
                    onSelect: function(page) {
                        app.set_cookie('ncdscreen_by_vid_paging', page);

                        ncdscreen.ajax.get_list_by_vid(vid, start_date, end_date, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="9">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                ncdscreen.set_list(rs);
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

    $(document).on('click', 'a[data-name="btn_result"]', function(e) {

        e.preventDefault();

        var pid = $(this).data('pid'),
            cid = $(this).data('cid'),
            hospcode = $(this).data('hospcode'),
            date_serv = $(this).data('date_serv'),
            date_serv_th = $(this).data('date_serv_th'),
            fullname = $(this).data('fullname'),
            birth = $(this).data('birth'),
            age_y = $(this).data('age_y'),
            age_m = $(this).data('age_m'),
            age_d = $(this).data('age_d');

        $('#txt_screen_fullname').val(fullname);
        $('#txt_screen_birth').val(birth);
        $('#txt_screen_date_serv').val(date_serv_th);
        //$('#txt_screen_cid').val(cid);
        $('#txt_age').val(age_y + ' ปี ' + age_m + ' เดือน ' + age_d + ' วัน');

        ncdscreen.set_screen(hospcode, pid, date_serv);
    });

    ncdscreen.set_screen = function(hospcode, pid, date_serv) {

        ncdscreen.ajax.get_screen(hospcode, date_serv, pid, function(e, v) {
            if(e) {
                app.alert(e);
            } else {

                var servplace = v[0].servplace == '1' ? 'ในสถานบริการ' : 'นอกสถานบริการ';
                var bstest = v[0].bstest == '1' ? 'ตรวจน้ำตาลในเลือกจากหลอดเลือดดำ หลังอดอาหาร' :
                    v[0].bstest == '2' ? 'ตรวจน้ำตาลในเลือกจากหลอดเลือดดำ โดยไม่อดอาหาร' :
                        v[0].bstest == '3' ? 'ตรวจน้ำตาลในเลือดจากเส้นเลืออฝอย หลังงดอาหาร' :
                            v[0].bstest == '4' ? 'ตรวจน้ำตาลในเลือดจากเส้นเลือดฝอย โดยไม่อดอาหาร' : '-';
                var smoke = v[0].smoke == '1' ? 'ไม่สูบ' :
                    v[0].smoke == '2' ? 'สูบนานๆ ครั้ง' :
                        v[0].smoke == '3' ? 'สูบเป็นครั้งคราว' :
                            v[0].smoke == '4' ? 'สูบเป็นประจำ' :
                                v[0].smoke == '9' ? 'ไม่ทราบ' : '-';
                var alcohol = v[0].alcohol == '1' ? 'ไม่ดื่ม' :
                    v[0].alcohol == '2' ? 'ดื่มนานๆ ครั้ง' :
                        v[0].alcohol == '3' ? 'ดื่มเป็นครั้งคราว' :
                            v[0].alcohol == '4' ? 'ดื่มเป็นประจำ' :
                                v[0].alcohol == '9' ? 'ไม่ทราบ' : '-';
                var dmfamily = v[0].dmfamily == '1' ? 'มีประวัติเบาหวานในญาติสายตรง' :
                    v[0].dmfamily == '2' ? 'ไม่มี' :
                        v[0].dmfamily == '9' ? 'ไม่ทราบ' : '-';
                var htfamily = v[0].htfamily == '1' ? 'มีประวัติความดันในญาติสายตรง' :
                    v[0].htfamily == '2' ? 'ไม่มี' :
                        v[0].htfamily == '9' ? 'ไม่ทราบ' : '-';


                $('#spn_date_serv').html(v[0].date_serv);
                $('#spn_servplace').html(servplace);
                $('#spn_bslevel').html(v[0].bslevel);
                $('#spn_bstest').html(bstest);
                $('#spn_smoke').html(smoke);
                $('#spn_alcohol').html(alcohol);
                $('#spn_dmfamily').html(dmfamily);
                $('#spn_htfamily').html(htfamily);
                $('#spn_weight').html(v[0].weight);
                $('#spn_height').html(v[0].height);
                $('#spn_waist_cm').html(v[0].waist_cm);
                $('#spn_sbp1').html(v[0].sbp_1);
                $('#spn_sbp2').html(v[0].sbp_2);
                $('#spn_dbp1').html(v[0].dbp_1);
                $('#spn_dbp2').html(v[0].dbp_2);


                ncdscreen.modal.show_result();
            }
        });
    };

    $(document).on('click', 'a[data-name="btn_get_history"]', function(e) {
        e.preventDefault();

        cid = $(this).data('cid');
        if(cid) {
            $('#txt_query_visit').val(cid);

            ncdscreen.search_visit(cid);

            $('a[href="#profile"]').tab('show');
        } else {
            app.alert('กรุณาระบุเลขบัตรประชาชน');
        }
    });

    ncdscreen.search_visit = function(cid) {
        ncdscreen.ajax.get_history_total(cid, function(err, total) {
            if (err) {
                app.alert(err);
            } else {
                $('#paging_visit').fadeIn('slow');
                $('#paging_visit').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('ncdscreen_paging_visit'),
                    onSelect: function(page) {
                        app.set_cookie('ncdscreen_paging_visit', page);

                        ncdscreen.ajax.get_history(cid, this.slice[0], this.slice[1], function(err, rs){

                            $('#tbl_visit_list > tbody').empty();

                            if(err) {
                                app.alert(err);
                                $('#tbl_visit_list > tbody').append('<tr><td colspan="7">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                ncdscreen.set_visit_history(rs);
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
});