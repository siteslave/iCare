$(function(){
    var users = {};

    //Modal
    users.modal = {
        show_new: function () {
            $('#mdl_new_users').modal({
                keyboard: false,
                backdrop: 'static'
            });
        },

        show_change_password: function() {
            $('#mdl_change_password').modal({
                keyboard: false,
                backdrop: 'static'
            });
        },

        hide_new: function () {
            $('#mdl_new_users').modal('hide');
        },

        hide_change_password: function() {
            $('#mdl_change_password').modal('hide');
        }
    };

    //Ajax
    users.ajax = {
        get_list: function (s, t, cb) {
            app.ajax('/admins/users/list', { start: s, stop: t }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total: function (cb) {
            app.ajax('/admins/users/total', {}, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        remove: function(id, cb) {
            app.ajax('/admins/users/remove', {
                id: id
            }, function(e) {
                e ? cb(e, null) : cb(null);
            });
        },

        change_password: function(id, password, cb) {
            app.ajax('/admins/users/changepass', {
                id: id,
                password: password
            }, function(e) {
                e ? cb(e, null) : cb(null);
            });
        },

        save_user: function (i, cb) {
            app.ajax ('/admins/users/save', {
                id: i.id,
                username: i.username,
                password: i.password,
                cid: i.cid,
                fullname: i.fullname,
                position: i.position,
                department: i.department,
                user_type: i.user_type,
                user_status: i.user_status
            }, function (e) {
                e ? cb (e, null) : cb (null);
            });
        }
    };

    //show new user modal
    $('#btn_new').on('click', function (e) {
        e.preventDefault();
        users.clear();
        users.modal.show_new();
    });

    users.set_detail = function (v) {
        $('#txt_id').val(v.id);
        $('#txt_username').prop('disabled', true).css('background-color', 'white').val(v.username);
        $('#txt_password').prop('disabled', true).css('background-color', 'white').val('xxxxxx');
        $('#txt_cid').val(v.cid);
        $('#txt_fullname').val(v.fullname);
        $('#txt_position').val(v.position);
        $('#sl_department').val(v.hospcode);
        $('#sl_user_type').val(v.user_type);
        $('#sl_user_status').val(v.user_status);
    };

    users.clear = function () {
        $('#txt_id').val('');
        $('#txt_username').removeProp('disabled').val('');
        $('#txt_password').removeProp('disabled').val('');
        $('#txt_cid').val('');
        $('#txt_fullname').val('');
        $('#txt_position').val('');
        $('#sl_department').val('');
        $('#sl_user_type').val('');
        $('#sl_user_status').val('');
    };

    //save user
    $('#btn_save').on('click', function (e) {

        e.preventDefault();

        var items = {};

        items.id            = $('#txt_id').val();
        items.username      = $('#txt_username').val();
        items.password      = $('#txt_password').val();
        items.cid           = $('#txt_cid').val();
        items.fullname      = $('#txt_fullname').val();
        items.position      = $('#txt_position').val();
        items.department    = $('#sl_department').val();
        items.user_type     = $('#sl_user_type').val();
        items.user_status   = $('#sl_user_status').val();

        if ( !items.username ) {
            app.alert( 'กรุณาระบุชื่อผู้ใช้งาน' );
        } else if ( !items.password || items.password.length < 3 ) {
            app.alert( 'กรุณาระบุรหัสผ่าน และความยาวมากกว่า 3 ตัวอักษร' );
        } else if ( !items.fullname ) {
            app.alert( 'กรุณาระบุชื่อ - สกุล' );
        } else if ( !items.cid ) {
            app.alert( 'กรุณาระบุเลขบัตรประชาชน' );
        } else if ( !items.position ) {
            app.alert( 'กรุณาระบุตำแหน่ง' );
        } else if ( !items.department ) {
            app.alert( 'กรุณาระบุแผนก' );
        } else if ( !items.user_type ) {
            app.alert( 'กรุณาระบุประเภทผู้ใช้งาน' );
        } else if ( !items.user_status ) {
            app.alert( 'กรุณาระบุสถานะผู้ใช้งาน' );
        } else {
            users.ajax.save_user (items, function (e) {
                if (e) {
                    app.alert (e);
                } else {
                    app.alert ('บันทึกข้อมูลเสร็จเรียบร้อยแล้ว');
                    users.modal.hide_new();
                    users.get_list();
                }
            })
        }
    });

    $(document).on('click', 'a[data-name="btn_edit"]', function(e) {
        e.preventDefault();

        var items = {
            cid: $(this).data('cid'),
            username: $(this).data('username'),
            fullname: $(this).data('fullname'),
            hospcode: $(this).data('department'),
            position: $(this).data('position'),
            user_status: $(this).data('user_status'),
            user_type: $(this).data('user_type'),
            id: $(this).data('id')
        };

        users.clear();
        users.set_detail(items);
        users.modal.show_new();
    });

    $(document).on('click', 'a[data-name="btn_change_password"]', function(e) {
        e.preventDefault();

        var id = $(this).data('id');
        //show modal change password
    });

    $(document).on('click', 'a[data-name="btn_remove"]', function(e) {
        e.preventDefault();

        var id = $(this).data('id');

        if (confirm('คุณต้องการลบรายการใช่หรือไม่?')) {
            users.ajax.remove(id, function(e) {
                if (e) {
                    app.alert(e);
                } else {
                    app.alert('ลบรายการเสร็จเรียบร้อยแล้ว');
                    users.get_list();
                }
            });
        }
    });

    users.clear_change_password = function() {
        $('#txt_chw_id').val('');
        $('#txt_chw_new').val('');
    };

    $(document).on('click', 'a[data-name="btn_change_password"]', function(e) {
        e.preventDefault();

        var id = $(this).data('id');

        users.clear_change_password();

        $('#txt_chw_id').val(id);

        users.modal.show_change_password();
    });

    users.set_list = function (rs) {

        $('#tbl_list > tbody').empty();

        if ($(rs).size () ) {
            $.each(rs, function(i, v) {

                var status = v.user_status == '0' ? 'ระงับ' : 'ปกติ';
                $('#tbl_list > tbody').append(
                    '<tr>' +
                        '<td>' + v.cid + '</td>' +
                        '<td>' + v.username + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td>' + v.position + '</td>' +
                        '<td>' + v.hospname + '</td>' +
                        '<td>' + status + '</td>' +
                        '<td><div class="btn-group">' +
                        '<a href="javascript:void(0);" class="btn btn-default btn-small" data-name="btn_edit" ' +
                        'data-cid="' + v.cid + '" data-username="' + v.username + '" data-fullname="' + v.fullname + '" ' +
                        'data-department="' + v.hospcode + '" data-position="' + v.position + '" data-user_type="' + v.user_type + '" ' +
                        'data-user_status="' + v.user_status + '" data-id="' + v.id + '" rel="tooltip" title="แก้ไข">' +
                        '<i class="icon-file-text"></i></a>' +
                        '<a href="javascript:void(0);" class="btn btn-default btn-small" data-name="btn_change_password" ' +
                        'data-id="' + v.id + '" rel="tooltip" title="เปลี่ยนรหัสผ่าน">' +
                        '<i class="icon-edit"></i></a>' +
                        '<a href="javascript:void(0);" class="btn btn-danger btn-small" data-name="btn_remove" ' +
                        'data-id="' + v.id + '" rel="tooltip" title="ลบรายการ">' +
                        '<i class="icon-trash"></i></a>' +
                        '</div></td>' +
                        '</tr>'
                );
            });

            app.set_runtime();
        }
        else {
            $('#tbl_list > tbody').append('<tr><td colspan="7">ไม่พบข้อมูล</td></td></tr>');
        }
    };


    //change password
    $('#btn_do_change_password').on('click', function(e) {
        e.preventDefault();

        var id = $('#txt_chw_id').val();
        var password = $('#txt_chw_new').val();

        if ( !password ) {
            app.alert('กรุณาระบุรหัสผ่านใหม่');
        } else {
            users.ajax.change_password(id, password, function(e) {
                if(e) {
                    app.alert(e);
                } else {
                    app.alert('เปลี่ยนรหัสผ่านเสร็จเรียบร้อยแล้ว');
                    users.modal.hide_change_password();
                }
            })
        }
    });

    users.get_list = function() {
        users.ajax.get_total ( function (e, total) {
            if (e) {
                app.alert (e);
            } else {
                $('#paging').fadeIn('slow');

                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('users_paging'),
                    onSelect: function(page) {
                        app.set_cookie('users_paging', page);

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


    users.get_list();
});