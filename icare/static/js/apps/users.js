$(function() {
    var users = {};

    users.ajax = {
        get_list: function(start, stop, cb) {
            app.ajax('/uadm/list', {
                start: start,
                stop: stop
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        search: function(query, cb) {
            app.ajax('/uadm/search', {
                query: query
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total: function(cb) {
            app.ajax('/uadm/total', {}, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        remove: function(id, cb) {
            app.ajax('/uadm/remove', {
                id: id
            }, function(e) {
                e ? cb (e, null) : cb (null);
            });
        },

        change_pass: function(id, pw, cb) {
            app.ajax('/uadm/chwpass', {
                id: id,
                pw: pw
            }, function(e) {
                e ? cb (e, null) : cb (null);
            });
        },

        save: function(i, cb) {
            app.ajax('/uadm/save', {
                username: i.username,
                password: i.password,
                cid: i.cid,
                fullname: i.fullname,
                position: i.position,
                hospcode: i.hospcode,
                is_active: i.is_active,
                id: i.id
            }, function(e) {
                e ? cb (e, null) : cb (null);
            });
        }
    };

    //modal

    users.modal = {
        show_new: function() {
            $('#mdl_new').modal({
                keyboard: false,
                backdrop: 'static'
            });
        },

        hide_new: function() {
            $('#mdl_new').modal('hide');
        },

        show_change_pass: function() {
            $('#mdl_changepass').modal({
                keyboard: false,
                backdrop: 'static'
            });
        },

        hide_change_pass: function() {
            $('#mdl_changepass').modal('hide');
        }
    };

    //set list
    users.set_list = function(rs) {
        $('#tbl_list > tbody').empty();

        if($(rs).size()) {

            $(rs).each(function(i, v) {
                var tr_active = v.is_active == 'N' ? 'class="warning"' : '';
                var is_active = v.is_active == 'Y' ? '<i class="fa fa-check"></i>' : '<i class="fa fa-ban"></i>';
                $('#tbl_list > tbody').append(
                    '<tr ' + tr_active + '>' +
                        '<td>' + v.username + '</td>' +
                        '<td class="text-center">' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td>['+ v.hospcode + '] ' + v.hospname + '</td>' +
                        '<td>' + v.position + '</td>' +
                        '<td class="text-center">' + is_active + '</td>' +
                        '<td class="text-center"><div class="btn-group">' +
                        '<a href="javascript:void(0);" class="btn btn-default" data-name="btn_show_change_pass" ' +
                        'data-username="' + v.username + '" data-id="' + v.id + '" ' +
                        'title="เปลี่ยนรหัสผ่าน" rel="tooltip">' +
                        '<i class="fa fa-key"></i>' +
                        '</a>' +
                        '<a href="javascript:void(0);" class="btn btn-default" data-name="btn_show_edit" data-id="' + v.id + '" ' +
                        'data-username="' + v.username + '" data-cid="' + v.cid + '" data-fullname="' + v.fullname + '" ' +
                        'data-hospcode="' + v.hospcode + '" data-position="' + v.position + '" data-is_active="' + v.is_active + '" ' +
                        'title="แก้ไขข้อมูล" rel="tooltip">' +
                        '<i class="fa fa-edit"></i>' +
                        '</a>' +
                        '<a href="javascript:void(0);" class="btn btn-primary" title="ลบผู้ใช้งาน" rel="tooltip" '+
                        'data-name="btn_remove_user" data-id="' + v.id + '"><i class="fa fa-times"></i>' +
                        '</a>' +
                        '</div></td>' +
                        '</tr>'
                );
            });

            app.set_runtime();

        } else {
            $('#tbl_list > tbody').append('<tr><td colspan="7">ไม่พบรายการ</td></tr>');
        }
    };

    //show edit
    $(document).on('click', 'a[data-name="btn_show_edit"]', function(e) {
        e.preventDefault();

        var items = {};

        items.id = $(this).data('id');
        items.username = $(this).data('username');
        items.cid = $(this).data('cid');
        items.fullname = $(this).data('fullname');
        items.hospcode = $(this).data('hospcode');
        items.position = $(this).data('position');
        items.is_active = $(this).data('is_active');

        users.set_detail(items);

    });

    users.set_detail = function(rs) {

        users.clear_form();

        $('#txt_username').val(rs.username).prop('disabled', true).css('background-color', 'white');
        $('#txt_cid').val(rs.cid);
        $('#txt_password').val('******').prop('disabled', true).css('background-color', 'white');
        $('#txt_fullname').val(rs.fullname);
        $('#txt_position').val(rs.position);
        $('#sl_hospcode').val(rs.hospcode);

        rs.is_active == 'Y' ? $('#chk_is_active').iCheck('check') : $('#chk_is_active').iCheck('uncheck');
//        if(rs.is_active == 'Y') {
//            $('#chk_is_active').prop('checked', true);
//        } else {
//            $('#chk_is_active').prop('checked', false);
//        }

        $('#txt_id').val(rs.id);

        users.modal.show_new();
    };

    users.get_list = function() {

        users.ajax.get_total(function(e, total) {

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

                        users.ajax.get_list(this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="7">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                users.set_list(rs);
                            }
                        });

                    },
                    onFormat: app.setPagingFormat
                });
            }
        });
    };

    users.search = function(query) {

        $('#tbl_list > tbody').empty();

        users.ajax.search(query, function(e, data) {
            if(e) {
                app.alert(e);
                $('#tbl_list > tbody').append('<tr><td colspan="7">ไม่พบข้อมูล</td></td></tr>');
            } else {
                $('#paging').fadeOut('slow');
                users.set_list(data);
            }
        });
    };


    $('#btn_search').on('click', function(e) {
        e.preventDefault();

        var query = $('#txt_query').val();

        if(!query) {
            users.get_list();
        } else {
            //do search
            users.search(query);
        }
    });

    //show new
    $('#btn_show_new').on('click', function(e) {
        e.preventDefault();

        users.clear_form();
        users.modal.show_new();
    });

    users.clear_form = function() {
        $('#txt_username').val('').prop('disabled', false);
        $('#txt_password').val('').prop('disabled', false);
        $('#txt_cid').val('');
        $('#txt_fullname').val('');
        $('#txt_position').val('');
        $('#sl_hospcode').val('');
        $('#chk_is_active').iCheck('uncheck');
        $('#txt_id').val('');
    };
    //save
    $('#btn_save').on('click', function(e) {
        e.preventDefault();

        var items = {};

        items.username  = $('#txt_username').val();
        items.password  = $('#txt_password').val();
        items.cid       = $('#txt_cid').val();
        items.fullname  = $('#txt_fullname').val();
        items.position  = $('#txt_position').val();
        items.hospcode  = $('#sl_hospcode').val();
        items.is_active = $('#chk_is_active').is(':checked') ? 'Y' : 'N';

        items.id        = $('#txt_id').val();

        if(!items.username) {
            app.alert('กรุณาระบุชื่อผู้ใช้งาน (เป็นภาษาอังกฤษเท่านั้น)');
        } else if(!items.password){
            app.alert('กรุณาระบุรหัสผ่าน');
        } else if(!items.cid) {
            app.alert('กรุณาระบุเลขบัตรประชาชน');
        } else if(!items.fullname) {
            app.alert('กรุณาระบุชื่อ - สกุล');
        } else if(!items.position) {
            app.alert('กรุณาระบุตำแหน่ง');
        } else if(!items.hospcode) {
            app.alert('กรุณาระบุหน่วยงานต้นสังกัด');
        } else {
            //save
            users.ajax.save(items, function(e) {
                if(e) {
                    app.alert(e);
                } else {
                    app.alert('บันทึกข้อมูลเสร็จเรียบร้อยแล้ว');
                    users.get_list();
                    users.clear_form();
                    users.modal.hide_new();
                }
            })
        }
    });

    //remove user
    $(document).on('click', 'a[data-name="btn_remove_user"]', function(e) {
        e.preventDefault();

        var id = $(this).data('id');

        if(confirm('คุณต้องการลบรายการนี้ ใช่หรือไม่?')) {
            users.ajax.remove(id, function(e) {
                if(e) {
                    app.alert(e);
                } else {
                    app.alert('ลบรายการเสร็จเรียบร้อยแล้ว');
                    users.get_list();
                }
            });
        }
    });

    //change password
    $(document).on('click', 'a[data-name="btn_show_change_pass"]', function(e) {
        e.preventDefault();

        var id = $(this).data('id')
            , username = $(this).data('username')
        ;

        $('#txt_chw_id').val(id);
        $('#txt_chw_password1').val('');
        $('#txt_chw_password2').val('');
        $('#txt_chw_username').val(username);

        users.modal.show_change_pass();
    });

    //do change password
    $('#btn_chw_dochange').on('click', function(e) {
        e.preventDefault();

        var pw1 = $('#txt_chw_password1').val()
            , pw2 = $('#txt_chw_password2').val()
            , id = $('#txt_chw_id').val()
        ;

        if(!pw1) {
            app.alert('กรุณาระบุรหัสผ่านใหม่');
        } else if(!pw2) {
            app.alert('กรุณาระบุรหัสผ่านใหม่อีกครั้ง');
        } else if(pw1 != pw2) {
            console.log(pw1);
            console.log(pw2);
            app.alert('รหัสผ่านทั้งสองช่องไม่ตรงกัน กรุณาตรวจสอบใหม่อีกครั้ง');
        } else {
            //do change
            users.ajax.change_pass(id, pw1, function(e) {
                if(e){
                    app.alert(e);
                } else {
                    app.alert('เปลี่ยนรหัสผ่านเสร็จเรียบร้อยแล้ว');
                    users.modal.hide_change_pass();
                }
            });
        }
    });

    users.get_list();
});