$(function() {

    var equipment = {};

    equipment.modal = {

        showRegister: function() {
            $('#mdlNewEquipment').modal({
                keyboard: false,
                backdrop: false
            });
        },

        hideRegister: function() {
            $('#mdlNewEquipment').modal('hide');
        }
    };

    equipment.ajax = {
        save: function (data, cb) {
            app.ajax('/equipment/save', {
                id: data.id,
                name: data.name,
                serial: data.serial,
                durableGoods: data.durableGoods,
                purchaseDate: data.purchaseDate,
                status: data.status
            }, function(e) {
                e ? cb (e, null) : cb (null);
            });
        },

        remove: function (id, cb) {
            app.ajax('/equipment/remove', { id: id }, function(e, v) {
                e ? cb (e, null) : cb (null);
            });
        },

        get_total: function (cb) {
            app.ajax('/equipment/get_total', {}, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        get_list: function (start, stop, cb) {
            app.ajax('/equipment/get_list', {
            	start: start,
				stop: stop
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        }
,

        search: function (query, cb) {
            app.ajax('/equipment/search', {
            	query: query
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        }

    };

    $('#mdlNewEquipment').on('hidden.bs.modal', function() {
        equipment.clear_form();
    });

    //clear form
    equipment.clear_form = function() {
        $('#txtId').val('');
        $('#txtName').val('');
        $('#txtSerialNumber').val('');
        $('#txtDurableGoodsNumber').val('');
        $('#txtPurchaseDate').val('');
        app.set_first_selected($('#slStatus'));
    }

   $('#btnNewEquipment').on('click', function(e) {
       e.preventDefault();
       //equipment.clear_form();
       equipment.modal.showRegister();
   });

    $('#btnSave').on('click', function(e) {
        e.preventDefault();

        var items = {};

        items.id = $('#txtId').val();
        items.name = $('#txtName').val();
        items.serial = $('#txtSerialNumber').val();
        items.durableGoods = $('#txtDurableGoodsNumber').val();
        items.purchaseDate = $('#txtPurchaseDate').val();
        items.status = $('#slStatus').val();

        if(!items.name)
        {
            app.alert('กรุณาระบุชื่อครุภัณฑ์');
        }
        else
        {
            equipment.ajax.save(items, function(e) {
               if(e)
               {
                   app.alert(e);
               }
               else
               {
                   app.alert('บันทึกข้อมูลเสร็จเรียบร้อยแล้ว');
                   equipment.modal.hideRegister();
                   equipment.get_list();
               }
            });
        }
    });

    $('#btnRefresh').on('click', function(e) {
        e.preventDefault();
        equipment.get_list();
    });

    equipment.get_list = function() {
        equipment.ajax.get_total(function(e, total) {
            if (e) {
				equipment.set_table_empty();
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');
                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('emp_paging'),
                    onSelect: function(page) {
                        app.set_cookie('emp_paging', page);

                        equipment.ajax.get_list(this.slice[0], this.slice[1], function(e, rs){
                            if(e) {
                                app.alert(e);
                                equipment.set_table_empty();
                            } else {
                                equipment.set_list(rs);
                            }
                        });

                    },
                    onFormat: app.setPagingFormat
                });
            }
        });
	};

    equipment.set_list = function(data) {
		$('#tbl_list > tbody').empty();
        if(data.length) {
            $.each(data, function(i, v) {
                var status = v.status == '1' ? 'พร้อมใช้' : v.status == '2' ? 'อยู่ระหว่างซ่อมแซม' : 'แทงจำหน่าย';

                $('#tbl_list > tbody').append(
                    '<tr>' +
                    '<td>' + v.name + '</td>' +
                    '<td>' + v.serial + '</td>' +
                    '<td>' + v.durable_goods_number + '</td>' +
                    '<td>' + v.purchase_date + '</td>' +
                    '<td>' + status + '</td>' +
                    '<td class="text-center"><div class="btn-group">' +
                    '<a href="javascript:void(0);" class="btn btn-default" ' +
                        'data-id="' + v.id + '" data-vname="' + v.name + '" data-serial="' + v.serial + '" ' +
                        'data-durable_goods_number="' + v.durable_goods_number + '" ' +
                        'data-purchase_date=" ' + v.purchase_date + '" data-name="btn_edit" rel="tooltip" title="แก้ไข">' +
                        '<i class="fa fa-edit"></i></a>' +
                    '<a href="/equipment/services/' + v.id + ' " class="btn btn-success" ' +
                        'data-id="' + v.id + '" data-name="btn_service_history" rel="tooltip" title="ข้อมูล/ประวัติการซ่อมบำรุง">' +
                        '<i class="fa fa-clipboard"></i></a>' +
                    '<a href="javascript:void(0);" class="btn btn-primary" ' +
                        'data-id="' + v.id + '" data-name="btn_remove" rel="tooltip" title="ลบรายการ">' +
                        '<i class="fa fa-trash-o"></i></a>' +
                    '</div></td>' +
                    '</tr>'
                );
            });
        } else {
            $('#tbl_list > tbody').append('<tr><td colspan="6">ไม่พบรายการ</td></tr>');
            $('#paging').fadeOut('slow');
        }
	};

    //remove
    $(document).on('click', 'a[data-name="btn_remove"]', function() {
        if(confirm('คุณต้องการลบรายการนี้ใช่หรือไม่?')) {
            var id = $(this).data('id');

            equipment.ajax.remove(id, function(err) {
               if(err) {
                   app.alert(err);
                   $('#tbl_list > tbody').empty();
                   $('#tbl_list > tbody').append('<tr><td colspan="6">ไม่พบรายการ</td></tr>');
                   $('#paging').fadeOut('slow');

               } else {
                   app.alert('ลบรายการเสร็จเรียบร้อยแล้ว');
                   equipment.get_list();
               }
            });

        }
    });

    //edit
    $(document).on('click', 'a[data-name="btn_edit"]', function() {
        var name = $(this).data('vname'),
            durable_goods_number = $(this).data('durable_goods_number'),
            purchase_date = $(this).data('purchase_date'),
            serial = $(this).data('serial'),
            status = $(this).data('status'),
            id = $(this).data('id');

        $('#txtId').val(id);
        $('#txtName').val(name);
        $('#txtSerialNumber').val(serial);
        $('#txtDurableGoodsNumber').val(durable_goods_number);
        $('#txtPurchaseDate').val(purchase_date);
        $('#slStatus').val(status);

        equipment.modal.showRegister();
    });

	equipment.set_table_empty = function() {
		$('#tbl_list > tbody').empty();
		$('#tbl_list > tbody').append('<tr><td colspan="6">ไม่พบรายการ<td></tr>');
	};

    //search
    $('#btnDoSearch').on('click', function(e) {

        e.preventDefault();

       var query = $('#txtQuery').val();

        if(!query)
        {
            app.alert('กรุณาระบุคำค้นหา');
        }
        else
        {
            equipment.ajax.search(query, function(err, data) {
                if(_.size(data))
                {
                    equipment.set_list(data);
                    $('#paging').fadeOut('slow');
                }
                else
                {
                    equipment.set_table_empty();
                }

            });

        }
    });

    equipment.get_list();
});