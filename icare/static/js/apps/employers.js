$(function() {

    var emp = {};

    emp.modal = {
        show_new: function() {
            $('#mdl_new').modal({
                keyboard: false,
                backdrop: 'static'
            });
        },
        show_meeting: function() {
            $('#mdl_meeting').modal({
                keyboard: false,
                backdrop: 'static'
            });
        },
		hide_new: function() {
			$('#mdl_new').modal('hide');
		}
    };

    emp.ajax = {
        get_total: function (cb) {
            app.ajax('/employers/get_total', {}, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },
		
        get_list: function (start, stop, cb) {
            app.ajax('/employers/get_list', {
            	start: start,
				stop: stop
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        search: function (query, cb) {
            app.ajax('/employers/search', { query: query }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },
		//Get employer detail
		get_detail: function(id, cb) {
			app.ajax('/employers/detail', { id: id }, function(e, v) {
				e ? cb(e) : cb(null, v.rows);
			});
		},
        //Get meetings list
        get_meetings: function(cid, cb) {
            app.ajax('/employers/get_meetings', { cid: cid }, function(e, v) {
                e ? cb(e) : cb(null, v.rows);
            });
        },
		//Save new employer
        save_new: function (item, cb) {
            app.ajax('/employers/save_new', 
			{
				id: item.id,
				f: item.fullname,
				c: item.cid,
				b: item.birth,
				s: item.sex,
				p: item.position,
				pg: item.position_grade,
				d: item.department,
				e: item.email,
				t: item.telephone,
				sd: item.start_date,
				ed: item.end_date,
				st: item.status,
				pid: item.position_id
			}, function(e, v) {
                e ? cb (e, null) : cb (null);
            });
        },
        //Save meeting
        save_meeting: function(i, cb) {
            app.ajax('/employers/save_meeting', {
                cid: i.mcid,
                s: i.mstart,
                e: i.mend,
                t: i.mtitle,
                o: i.mowner,
                p: i.mplace,
                id: i.id
            }, function(e, v) {
                e ? cb(e) : cb(null);
            })
        },
        //Remove meeting
        remove_meeting: function(cid, id, cb) {
            app.ajax('/employers/remove_meeting', {
               cid: cid,
               id: id 
            }, function(e) {
                e ? cb(e) : cb(null);
            });
        }
	};// end ajax	
	
	//New employer
	$('#btn_new').on('click', function(e) {
		e.preventDefault();
		emp.clear_new_form();
		emp.modal.show_new();
	});
	//Get employer list
	emp.get_list = function() {
        emp.ajax.get_total(function(e, total) {
            if (e) {
				emp.set_table_empty();
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');
				$('#spn_total').html(numeral(total).format('0,0'));
				
                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('emp_paging'),
                    onSelect: function(page) {
                        app.set_cookie('emp_paging', page);

                        emp.ajax.get_list(this.slice[0], this.slice[1], function(e, rs){
                            if(e) {
                                app.alert(e);
                                emp.set_table_empty();
                            } else {
                                emp.set_list(rs);
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
	//Set employer list
	emp.set_list = function(data) {
		$('#tbl_list > tbody').empty();
		
		$.each(data, function(i, v) {
			var status = v.status == '1' ? 'ปกติ' : 'ไม่อยู่';
			var tr_class = v.status == '0' ? 'class="warning"' : '';
			$('#tbl_list > tbody').append(
				'<tr ' + tr_class + '>' +
				'<td>' + v.cid + '</td>' +
				'<td>' + v.fullname + '</td>' +
				'<td>' + v.position + '</td>' +
				'<td>' + v.grade + '</td>' +
				'<td>' + v.start_date + '</td>' +
				'<td>' + v.end_date + '</td>' +
				'<td>' + status + '</td>' +
				'<td><div class="btn-group">' +
                '<a href="javascript:void(0);" class="btn btn-primary" data-id="' + v.id + '" data-name="btn_edit" rel="tooltip" title="แก้ไข"><i class="icon-edit"></i></a>' +
                '<a href="javascript:void(0);" class="btn btn-default" data-id="' + v.id + '" data-name="btn_get_meeting" rel="tooltip" title="ข้อมูลการฝึกอบรม" data-cid="' + v.cid + '"><i class="icon-share"></i></a>' +
                '</div></td>' +
				'</tr>'
			);
		});
        
        app.set_runtime();
	};
    
    //Clear meeting form
    emp.clear_meeting_form = function() {
        $('#txt_mstart_date').val('');
        $('#txt_mend_date').val('');
        $('#txt_mtitle').val('');
        $('#txt_mowner').val('');
        $('#txt_mplace').val('');
        //$('#txt_mcid').val(''); 
        $('#txt_mid').val(''); 
    };
    
    //Show meeting
    $(document).on('click', 'a[data-name="btn_get_meeting"]', function(e) {
        e.preventDefault();
        //Clear meeting form
        emp.clear_meeting_form();
        //Set cid
        var cid = $(this).data('cid');
        $('#txt_mcid').val(cid);
        emp.get_meetings(cid);
        //Set main tab selected
        $('a[href="#main-meeting"]').tab('show');
        //Show modal
        emp.modal.show_meeting();
    });
	
	//Edit employer detail
	$(document).on('click', 'a[data-name="btn_edit"]', function(e) {
		
		e.preventDefault();
		var id = $(this).data('id');

		//Get detail
		emp.ajax.get_detail(id, function(err, data) {
			if(err) {
				app.alert(err);
			} else {
				//Clear form
				emp.clear_new_form();
				//Set detail
				emp.set_detail(data);
				//Show new modal
				emp.modal.show_new();
			}
		});
	});
	
	//Set employer detail
	emp.set_detail = function(v) {
		$('#txt_id').val(v.id);
		$('#txt_fullname').val(v.fullname);
		$('#txt_cid').prop('disabled', true).val(v.cid);
		$('#txt_birth').val(v.birth);
		$('#sl_sex').val(v.sex);
		$('#sl_position_grade').val(v.grade);
		$('#sl_position').val(v.position);
		$('#txt_position_id').val(v.position_id);
		$('#txt_department').val(v.department);
		$('#txt_email').val(v.email);
		$('#txt_telephone').val(v.telephone);
		$('#txt_start_date').val(v.start_date);
		$('#txt_end_date').val(v.end_date);
		v.status == '1' ? $('#chk_status').prop('checked', true) : $('#chk_status').removeProp('checked');
	};
	
	emp.set_table_empty = function() {
		$('#tbl_list > tbody').empty();
		$('#tbl_list > tbody').append('<tr><td colspan="8">ไม่พบรายการ<td></tr>')
	};
	
	emp.clear_new_form = function() {
		$('#txt_fullname').val('');
		$('#txt_cid').removeProp('disabled').val('');
		$('#txt_birth').val('');
		$('#sl_sex').val('');
		app.set_first_selected($('#sl_position_grade'));
		app.set_first_selected($('#sl_position'));
		$('#txt_position_id').val('');
		$('#txt_department').val('');
		$('#txt_email').val('');
		$('#txt_telephone').val('');
		$('#txt_start_date').val('');
		$('#txt_end_date').val('');
		$('#txt_id').val('');
		$('#chk_status').prop('checked', true);
	};
	
	$('#btn_save_new').on('click', function(e){
		e.preventDefault();
		
		var items = {};
		
		items.fullname 		= $('#txt_fullname').val();
		items.cid 			= $('#txt_cid').val();
		items.birth 		= $('#txt_birth').val();
		items.sex 			= $('#sl_sex').val();
		items.position 		= $('#sl_position').val();
		items.position_grade= $('#sl_position_grade').val();
		items.position_id   = $('#txt_position_id').val();
		items.department 	= $('#txt_department').val();
		items.email 		= $('#txt_email').val();
		items.telephone 	= $('#txt_telephone').val();
		items.start_date 	= $('#txt_start_date').val();
		items.end_date 		= $('#txt_end_date').val();
		items.id			= $('#txt_id').val();
		items.status		= $('#chk_status').prop('checked') ? '1' : '0';
		
		if(!items.fullname) {
			app.alert('กรุณาระบุชื่อ-สกุล');
		} else if(!items.cid) {
			app.alert('กรุณาระบุเลขบัตรประชาชน');
		} else if(!items.birth) {
			app.alert('กรุณาระบุวันเกิด');
		} else if(!items.sex) {
			app.alert('กรุณาระบุเพศ');
		} else if(!items.position) {
			app.alert('กรุณาระบุตำแหน่ง');
		} else if(!items.position_grade) { 
			app.alert('กรุณาระบุระดับ');
		} else if(!items.department) {
			app.alert('กรุณาระบุหน่วยงาน');
		} else {
			//do save
			emp.ajax.save_new(items, function(err) {
				if(err) {
					app.alert(err);
				} else {
					app.alert('บันทึกข้อมูลเสร็จเรียบร้อยแล้ว');
					emp.modal.hide_new();
					emp.get_list();
				}
			})
		}
	});
	
	//Search
	$('#btn_search').on('click', function(e) {
		e.preventDefault();
		
		var query = $('#txt_query').val();
		if(query) {
			emp.ajax.search(query, function(err, data) {
				if(err) {
					app.alert(err);
				} else {
	                $('#paging').fadeOut('slow');
					if(data.length == 0) {
						emp.set_table_empty();
					} else {
						//Set result
						$('#spn_total').html(numeral(data.length).format('0,0'));
						emp.set_table_empty();
						emp.set_list(data);
					}
				}
			});
		} else {
			app.alert('กรุณาระบุคำค้นหา');
		}
	});
	
	$('#btn_refresh').on('click', function(e) {
		e.preventDefault();
		emp.get_list();
	});
    
    //Get meeting list
    emp.get_meetings = function(cid) {
        emp.ajax.get_meetings(cid, function(e, data) {
            if(e) {
                app.alert(e);
                $('#tbl_mlist > tbody').empty();
                $('#tbl_mlist > tbody').append('<tr><td colspan="7">ไม่พบรายการ</td></tr>');
            } else {
                //Set meetings list
                
                emp.set_meetings(data);
            }
        });
    };
    //Set meeting list
    emp.set_meetings = function(data) {
        //Clear table list
        $('#tbl_mlist > tbody').empty();
        //Check data is empty
        if($(data).length) {
            //var cid = $('#txt_mcid').val();
            //Loop foreach row
            var x = 1;
            $.each(data, function(i, v) {
                $('#tbl_mlist > tbody').append(
                    '<tr>' +
                    '<td>' + x + '</td>' +
                    '<td>' + v.start_date + '</td>' +
                    '<td>' + v.end_date + '</td>' +
                    '<td title="' + v.title + '">' + app.strip(v.title, 25) + '</td>' +
                    '<td title="' + v.owner_name + '">' + app.strip(v.owner_name, 25) + '</td>' +
                    '<td title="' + v.place_name + '">' + app.strip(v.place_name, 25) + '</td>' +
                    '<td><div class="btn-group">' +
                    '<a href="javascript:void(0);" data-id="' + v.id + '" class="btn btn-success" data-name="btn_mshow_edit" data-start_date="' + v.start_date + '" data-end_date="' + v.end_date + '" data-title="' + v.title + '" data-owner_name="' + v.owner_name + '" data-place_name="' + v.place_name + '" rel="tooltip" title="แก้ไขรายการ"><i class="icon-edit"></i></a>' +
                    '<a href="javascript:void(0);" data-id="' + v.id + '" class="btn btn-danger" rel="tooltip" title="ลบรายการ" data-name="btn_mremove"><i class="icon-trash"></i></a>' +
                    '</div></td>' +
                    '</tr>'
                );
                x++;
            });
            
            app.set_runtime();
            
        } else {
            $('#tbl_mlist > tbody').append(
                '<tr><td colspan="7">ไม่พบรายการ</td></tr>'
            );
        }
    };
    
    //Remove meeting
    $(document).on('click', 'a[data-name="btn_mremove"]', function(e) {
        var id = $(this).data('id');
        var cid = $('#txt_mcid').val();
        
        if(confirm('คุณต้องการลบรายการนี้ ใช่หรือไม่?')) {
            //Remove meeting
            emp.ajax.remove_meeting(cid, id, function(e) {
                if(e) {
                    app.alert(e);
                } else {
                    app.alert('ลบรายการเสร็จเรียบร้อยแล้ว');
                    emp.get_meetings(cid);
                }
            });
        }
    });
    
    //Edit meeting
    $(document).on('click', 'a[data-name="btn_mshow_edit"]', function(e) {
        
        var cid = $('#txt_mcid').val();
        
        var id = $(this).data('id'),
        title = $(this).data('title'),
        start_date = $(this).data('start_date'),
        end_date = $(this).data('end_date'),
        owner_name = $(this).data('owner_name'),
        place_name = $(this).data('place_name');
        
        emp.clear_meeting_form();
        
        $('#txt_mstart_date').val(start_date);
        $('#txt_mend_date').val(end_date);
        $('#txt_mtitle').val(title);
        $('#txt_mowner').val(owner_name);
        $('#txt_mplace').val(place_name);
        $('#txt_mcid').val(cid);
        $('#txt_mid').val(id);
        
        $('a[href="#new-meeting"]').tab('show');
        
    });
    
    //Save meeting
    $('#btn_msave').on('click', function(e) {
        e.preventDefault();
        var items = {};
        
        items.mstart = $('#txt_mstart_date').val();
        items.mend = $('#txt_mend_date').val();
        items.mtitle = $('#txt_mtitle').val();
        items.mowner = $('#txt_mowner').val();
        items.mplace = $('#txt_mplace').val();
        items.mcid = $('#txt_mcid').val();
        items.id = $('#txt_mid').val();
        
        if (!items.mcid) {
            app.alert('กรุณาระบุเลขบัตรประชาชน');
        } else if(!items.mstart) {
            app.alert('กรุณาระะบุวันที่เริ่ม');
        } else if(!items.mend) {
            app.alert('กรุณาระบุวันที่สิ้นสุด');
        } else if(!items.mtitle) {
            app.alert('กรุณาระบุหัวข้อ');
        } else if(!items.mowner) {
            app.alert('กรุณาระบุหน่วยงานที่จัด');
        } else if(!items.mplace) {
            app.alert('กรุณาระบุสถานที่');
        } else {
            emp.ajax.save_meeting(items, function(e) {
                if(e) {
                    app.alert(e);
                } else {
                    app.alert('บันทึกรายการเสร็จเรียบร้อยแล้ว');
                    //Get meeting list
                    emp.get_meetings(items.mcid);
                    //Set tab selected
                    $('a[href="#main-meeting"]').tab('show');
                    emp.clear_meeting_form();
                }
            });
        }
    });
	
	emp.get_list();
    
});