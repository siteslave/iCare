/**
* Project Script
*
* @author       Satit Rianpit <rianpit@gmail.com>
* @module       Project
* @copyright    2014
**/

$(function() {
    var project = {};

    project.ajax = {

        save: function (data, cb) {
            app.ajax('/projects/save', {
                project_id: data.project_id,
                name: data.name,
                classify: data.classify,
                start_date: data.start_date,
                end_date: data.end_date,
                indicator: data.indicator,
                budgets_source: data.budgets_source,
                budgets_amount: data.budgets_amount,
                project_manager: data.project_manager,
                plan: data.plan
            }, function(e) {
                e ? cb (e, null) : cb (null);
            });
        },
        
        save_report: function (data, cb) {
            app.ajax('/projects/save_report', {
                reportId: data.reportId,
                projectId: data.projectId,
                classify: data.classify,
                reportDate: data.reportDate,
                resolveDate: data.resolveDate,
                desc: data.desc
            }, function(e) {
                e ? cb (e, null) : cb (null);
            });
        },
        
        remove: function (id, cb) {
            app.ajax('/projects/remove', { project_id: id }, function(e) {
                e ? cb (e, null) : cb (null);
            });
        },

        get_total: function (cb) {
            app.ajax('/projects/get_total', {}, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        get_list: function (start, stop, cb) {
            app.ajax('/projects/get_list', {
                start: start,
                stop: stop
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_detail: function (project_id, cb) {
            app.ajax('/projects/get_detail', {
                project_id: project_id
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_report: function (project_id, cb) {
            app.ajax('/projects/get_report', {
                project_id: project_id
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        search: function (query, cb) {
            app.ajax('/projects/search', {
                query: query
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        }

    };

    project.modal = {

        showRegister: function() {
            $('#mdlNewProject').modal({
                keyboard: false,
                backdrop: false
            });
        },
        showReport: function() {
            $('#mdlProblemReport').modal({
                keyboard: false,
                backdrop: false
            });
        },

        hideRegister: function() {
            $('#mdlNewProject').modal('hide');
        },

        hideReport: function() {
            $('#mdlProblemReport').modal('hide');
        }
    };

    $('#btnNewProject').on('click', function(e) {

        e.preventDefault();
        project.modal.showRegister();

    });

    $('#btnSave').on('click', function(e) {
        e.preventDefault();

        var items = {
            project_id: $('#txtId').val(),
            name: $('#txtName').val(),
            classify: $('#slClassify').val(),
            start_date: $('#txtStartDate').val(),
            end_date: $('#txtEndDate').val(),
            indicator: $('#txtIndicators').val(),
            budgets_source: $('#txtBudgetsSource').val(),
            budgets_amount: $('#txtBudgetsAmount').val(),
            project_manager: $('#txtProjectManager').val(),
            plan: $('#txtPlan').val()
        }

        if(!items.name) {
            app.alert('กรุณาระบุชื่อโครงการ');
        }
        else if(!items.start_date) {
            app.alert('กรุณาวันที่เริ่มโครงการ');
        }
        else if(!items.end_date) {
            app.alert('กรุณาระบุวันที่สิ้นสุดโครงการ');
        }
        else if(!items.budgets_source)
        {
            app.alert('กรุณาระบุแหล่งที่มาของเงิน');
        }
        else if(!items.budgets_amount)
        {
            app.alert('กรุณาระบุจำนวนเงิน');
        }
        else if(!items.plan)
        {
            app.alert('กรุณาระบุแผนการปฏิบัติงาน');
        }
        else if(!items.project_manager)
        {
            app.alert('กรุณาระบุผู้รับผิดชอบโครงการ');
        }
        else {
            project.ajax.save(items, function(err) {
                if(err) {
                    app.alert(err);
                } else {
                    app.alert('บันทึกข้อมูลเสร็จเรียบร้อยแล้ว');
                    project.modal.hideRegister();
                    project.get_list();
                }
            });
        }
    });

    project.clear_form = function() {
        $('#txtId').val('');
        $('#txtName').val('');
        app.set_first_selected($('#slClassify'));
        $('#txtStartDate').val('');
        $('#txtEndDate').val('');
        $('#txtIndicators').val('');
        $('#txtBudgetsSource').val('');
        $('#txtBudgetsAmount').val('');
        $('#txtPlan').val('');
    };

    $('#mdlNewProject').on('hidden.bs.modal', function() {
        project.clear_form();
    });

    project.set_table_empty = function() {
        $('#tbl_list > tbody').empty();
        $('#tbl_list > tbody').append('<tr><td colspan="7">ไม่พบรายการ<td></tr>')
    };

    $('#btnRefresh').on('click', function(e) {
        e.preventDefault();
        project.get_list();
    });

    project.get_list = function() {
        project.ajax.get_total(function(e, total) {
            if (e) {
                project.set_table_empty();
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

                        project.ajax.get_list(this.slice[0], this.slice[1], function(e, rs) {
                            if(e) {
                                app.alert(e);
                                project.set_table_empty();
                            } else {
                                project.set_list(rs);
                            }
                        });

                    },
                    
                    onFormat: app.setPagingFormat
                });
            }
        });
    };

    //Set project list
    project.set_list = function(data) {
        $('#tbl_list > tbody').empty();

        $.each(data, function(i, v) {
            $('#tbl_list > tbody').append(
                '<tr>' +
                '<td>' + v.name + '</td>' +
                '<td>' + v.start_date + '</td>' +
                '<td>' + v.end_date + '</td>' +
                '<td>' + v.budgets_source + '</td>' +
                '<td class="text-right">' + numeral(v.budgets_amount).format('0,0.00') + '</td>' +
                '<td>' + v.project_manager + '</td>' +
                '<td class="text-center"><div class="btn-group">' +
                '<a href="javascript:void(0);" class="btn btn-default" ' +
                    'data-id="' + v.id + '" data-name="btn_edit" rel="tooltip" title="แก้ไข">' +
                    '<i class="fa fa-edit"></i></a>' +
                '<a href="javascript:void(0);" class="btn btn-default" ' +
                    'data-id="' + v.id + '" data-name="btn_problem_report" rel="tooltip" title="รายงานปัญหาการทำโครงการ">' +
                    '<i class="fa fa-desktop"></i></a>' +
                '<a href="javascript:void(0);" class="btn btn-default" ' +
                    'data-id="' + v.id + '" data-name="btn_remove" rel="tooltip" title="ลบรายการ">' +
                    '<i class="fa fa-trash-o"></i></a>' +
                '</div></td>' +
                '</tr>'
            );
        });
    };

    //report problem
    $(document).on('click', 'a[data-name="btn_problem_report"]', function(){
        var projectId = $(this).data('id');

        $('#txtProjectId').val(projectId);
        //set report detail
        project.ajax.get_report(projectId, function(err, data) {

            if(data) {
                $('#slReportClassify').val(data.classify);
                $('#txtReportDate').val(data.report_date);
                $('#txtReportResolveDate').val(data.resolve_date);
                $('#txtReportDesc').val(data.desc); 
            }

            $('#txtProjectId').val(projectId);
            project.modal.showReport();

        });
        
    });

    //set detail
    project.set_detail = function(v) {
        $('#txtName').val(v.name);
        $('#slClassify').val(v.classify);
        $('#txtStartDate').val(v.start_date);
        $('#txtEndDate').val(v.end_date);
        $('#txtIndicators').val(v.indicator);
        $('#txtBudgetsSource').val(v.budgets_source);
        $('#txtBudgetsAmount').val(v.budgets_amount);
        $('#txtProjectManager').val(v.project_manager);
        $('#txtPlan').val(v.plan);

    };

    //edit
    $(document).on('click', 'a[data-name="btn_edit"]', function(e) {
        e.preventDefault();

        var project_id = $(this).data('id');

        project.ajax.get_detail(project_id, function(err, data) {

           if(err) {
               app.alert('ไม่พบข้อมูล');
           } else {
               $('#txtId').val(project_id);
               project.set_detail(data);
               project.modal.showRegister();
           }

        });
    });

    //Remove
    $(document).on('click', 'a[data-name="btn_remove"]', function(e) {
        e.preventDefault();

        var project_id = $(this).data('id');

        if( confirm('คุณต้องการลบรายการนี้ใช่หรือไม่?') )
        {
            project.ajax.remove(project_id, function(err) {
               if(err) {
                   app.alert(err);
               } else {
                   app.alert('ลบรายการเสร็จเรียบร้อยแล้ว');
                   project.get_list();
               }
            });
        }
    });

    //Search
    $('#btnDoSearch').on('click', function(e) { 
        var query = $('#txtQuery').val();

        if(!query) {
            app.alert('กรุณาระบุคำค้นหา');
        } else {
            project.ajax.search(query, function(err, data) {
                $('#paging').fadeOut('slow');
                project.set_list(data);
            });
        }
    });

    //save report
    $('#btnSaveReport').on('click', function(e) {
      e.preventDefault();
      
      var items = {};
      
      items.projectId = $('#txtProjectId').val(),
      items.classify = $('#slReportClassify').val(),
      items.reportDate = $('#txtReportDate').val(),
      items.resolveDate = $('#txtReportResolveDate').val(),
      items.desc = $('#txtReportDesc').val();
      
      if(!items.reportDate) {
        app.alert('กรุณาระบุวันที่รายงาน');
      } else if(!items.desc) {
        app.alert('กรุณาระบุรายละเอียด');
      } else {
        project.ajax.save_report(items, function(err) {
          if(err) {
            app.alert(err);
          } else {
            app.alert('บันทึกรายการเสร็จเรียบร้อยแล้ว');
            project.modal.hideReport();
          }
        });
      }
    });

    $('#mdlProblemReport').on('hidden.bs.modal', function() {
        project.clear_report_form();
    });

    project.clear_report_form = function() {
        $('#txtReportId').val('');
        $('#txtProjectId').val('');
        app.set_first_selected($('#slReportClassify'));
        $('#txtReportDate').val('');
        $('#txtReportResolveDate').val('');
        $('#txtReportDesc').val('');
    };
    
    //Get project list
    project.get_list();

});