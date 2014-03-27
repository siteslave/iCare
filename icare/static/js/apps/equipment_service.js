$(function() {
   var service = {};

    service.ajax = {
        save: function (data, cb) {
            app.ajax('/equipment/save_service', {
                id: data.id,
                service_id: data.service_id,
                service_date: data.service_date,
                service_type: data.service_type,
                company: data.company,
                contact_name: data.contact_name,
                telephone: data.telephone,
                email: data.email,
                service_status: data.service_status,
                return_date: data.return_date
            }, function(e) {
                e ? cb (e, null) : cb (null);
            });
        },

        remove: function (eqid, sid, cb) {
            app.ajax('/equipment/remove_service', {
                eqid: eqid,
                sid: sid
            }, function(e, v) {
                e ? cb (e, null) : cb (null);
            });
        },

        get_list: function (id, cb) {
            app.ajax('/equipment/get_service_list', {
                id: id
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_detail: function (id, cb) {
            app.ajax('/equipment/get_detail', {
                id: id
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_service_detail: function (eqid, sid, cb) {
            app.ajax('/equipment/get_service_detail', {
                eqid: eqid,
                sid: sid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        }
    };

    service.modal = {
      showRegister: function() {

            $('#mdlNewEquipmentService').modal({
                keyboard: false,
                backdrop: false
            });
        },

        hideRegister: function() {
            $('#mdlNewEquipmentService').modal('hide');
        }

    };

    $('#btnNewService').on('click', function(e) {
        e.preventDefault();

        service.modal.showRegister();
    });

    $('#btnSave').on('click', function(e) {

        e.preventDefault();

        var items = {};

        items.id = $('#txtId').val();
        items.service_id = $('#txtServiceId').val();
        items.service_date = $('#txtServiceDate').val();
        items.service_type = $('#slServiceType').val();
        items.company = $('#txtCompany').val();
        items.contact_name = $('#txtContactName').val();
        items.telephone = $('#txtTelephone').val();
        items.email = $('#txtEmail').val();
        items.service_status = $('#slServiceStatus').val();
        items.return_date = $('#txtReturnDate').val();

        if(!items.service_date) {
            app.alert('กรุณาระบุวันที่ส่งซ่อม');
        } else if(!items.company) {
            app.alert('กรุณาระบุบริษัทที่รับซ่อม');
        } else {
            //save new service
            service.ajax.save(items, function(err) {
               if(err) {
                   app.alert(err);
               } else {
                   app.alert('บันทึกข้อมูลเสร็จเรียบร้อยแล้ว');
                   service.modal.hideRegister();
                   service.get_list();
               }
            });
        }

    });

    $('#mdlNewEquipmentService').on('hidden.bs.modal', function() {
        service.clear_form();
    });

    service.clear_form = function() {
        $('#txtServiceId').val('');
        $('#txtServiceDate').val('');
        $('#slServiceType').val('');
        $('#txtCompany').val('');
        $('#txtContactName').val('');
        $('#txtTelephone').val('');
        $('#txtEmail').val('');
        $('#slServiceStatus').val('');
        $('#txtReturnDate').val('');
    };

    service.set_list = function(data) {
		$('#tbl_list > tbody').empty();

        var my_data = _.sortBy(data, function(item) {
            return item.service_date
        }).reverse();

		$.each(my_data, function(i, v) {
			var status = v.service_status == '1' ? 'ซ่อมเสร็จแล้ว' : v.status == '2' ? 'อยู่ระหว่างการซ่อม' : 'ยกเลิกการซ่อม/แทงจำหน่าย';
			var service_type = v.service_type == '1' ? 'ซ่อมเอง' : 'Out Source';

			$('#tbl_list > tbody').append(
				'<tr>' +
				'<td>' + v.service_date + '</td>' +
				'<td>' + v.return_date + '</td>' +
				'<td>' + v.company + '</td>' +
				'<td>' + v.contact_name + '</td>' +
				'<td>' + status + '</td>' +
				'<td>' + service_type + '</td>' +
				'<td><div class="btn-group">' +
                '<a href="javascript:void(0);" class="btn btn-default" ' +
                    'data-id="' + v.id + '" data-name="btn_edit" rel="tooltip" title="แก้ไข">' +
                    '<i class="fa fa-edit"></i></a>' +
                '<a href="javascript:void(0);" class="btn btn-primary" ' +
                    'data-id="' + v.id + '" data-name="btn_remove" rel="tooltip" title="ลบรายการ">' +
                    '<i class="fa fa-trash-o"></i></a>' +
                '</div></td>' +
				'</tr>'
			);
		});
	};

    //remove service
    $(document).on('click', 'a[data-name="btn_remove"]', function(e) {

        e.preventDefault();

        var service_id = $(this).data('id'),
            equipment_id = $('#txtId').val();

        if(confirm('คุณต้องการลบรายการนี้ใช่หรือไม่?')) {
            service.ajax.remove(equipment_id, service_id, function(err) {
                if(err) {
                    app.alert(err);
                } else {
                    app.alert('ลบรายการเสร็จเรียบร้อยแล้ว');
                    service.get_list();
                }
            })
        }
    })

    $(document).on('click', 'a[data-name="btn_edit"]', function(e) {

        e.preventDefault();

        var equipment_id = $('#txtId').val(),
            service_id = $(this).data('id');

        service.ajax.get_service_detail(equipment_id, service_id, function(err, v) {
            if(err) {
                app.alert('ไม่พบข้อมูลการซ่อมบำรุงของ id นี้');
            } else {

                $('#txtServiceId').val(v.id);
                $('#txtServiceDate').val(v.service_date);
                $('#slServiceType').val(v.service_type);
                $('#txtCompany').val(v.company);
                $('#txtContactName').val(v.contact_name);
                $('#txtTelephone').val(v.telephone);
                $('#txtEmail').val(v.email);
                $('#slServiceStatus').val(v.service_status);
                $('#txtReturnDate').val(v.return_date);

                service.modal.showRegister();
            }
        });

    });

    service.get_list = function() {

        var id = $('#txtId').val();

        service.ajax.get_list(id, function(e, rs) {
            if(e) {
                app.alert(e);
                service.set_table_empty();
            } else {
                service.set_list(rs);
            }
        });
    };

    service.set_table_empty = function() {
		$('#tbl_list > tbody').empty();
		$('#tbl_list > tbody').append('<tr><td colspan="7">ไม่พบรายการ<td></tr>')
	};

    service.get_detail = function() {
        var id = $('#txtId').val();

        service.ajax.get_detail(id, function(err, v) {
           if(err) {
               app.alert('ไม่พบข้อมูลครุภัณฑ์');
           } else {
               $('#txtEquipmentDurableGoodsNumber').val(v.durable_goods_number);
               $('#txtEquipmentName').val(v.name);
               $('#txtEquipmentSerial').val(v.serial);
           }
        });
    };

    service.get_detail();
    service.get_list();
});