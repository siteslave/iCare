//Application module

var app = {}

app.dbpop2thai_date = function(d) {
      if(!d) {
          return '-';
      } else {
          var old_date  = d.toString();
          var year      = old_date.substr(0, 4).toString(),
              month     = old_date.substr(4, 2).toString(),
              day       = old_date.substr(6, 2).toString();

          var new_year  = parseInt(year) + 543;

          var new_date  = day + '/' + month + '/' + new_year;

          return new_date;
      }
};

app.string_to_jsdate = function(d) {
      if(!d) {
          return '-';
      } else {
          var old_date  = d.toString();
          var year      = old_date.substr(0, 4).toString(),
              month     = old_date.substr(4, 2).toString(),
              day       = old_date.substr(6, 2).toString();

          var new_date  = day + '/' + month + '/' + year;

          return new_date;
      }
};
/*
Add date
x = yyyymmdd
y = integer
 */
app.add_date = function(x, y) {
    var d = moment(x, 'YYYYMMDD');
    var new_date = d.add('days', y);

    return new_date;
};
/*
Subtract date
x = yyyymmdd
y = integer
 */
app.sub_date = function(x, y) {
    var d = moment(x, 'YYYYMMDD');
    var new_date = d.subtract('days', y);

    return new_date;
};

/*
To English string date [YYYYMMDD]
var d = Date()
 */
app.get_current_jsdate = function() {
    var year = d.getFullYear();
    var month = d.getMonth() + 1;

    if(month < 10) month = '0' + month;

    var date = d.getDate();
    if(date < 10) date = '0' + date;

    var new_date = date + '/' + month + '/' + year;

    return new_date;
};

app.day_in_month = function(month, year) {
    return new Date(year, month, 0).getDate();
};

app.get_current_date_range = function() {
    var current_year = new Date().getFullYear(),
        current_month = new Date().getMonth() + 1;

    var max_date = app.day_in_month(current_month, current_year);
    if(current_month < 10) current_month = '0' + current_month;

    var return_date = {
        start_date: '01' + '/' + current_month + '/' + current_year,
        end_date: max_date + '/' + current_month + '/' + current_year
    };

    return return_date;
};

app.to_string_eng_date = function(d) {
    var year = d.getFullYear();
    var month = d.getMonth() + 1;

    if(month < 10) month = '0' + month;

    var date = d.getDate();
    var new_date = year + '' + month + '' + date;

    return new_date;
};

app.ajax = function(url, params, cb) {

    //app.show_loading();
    //NProgress.start();
    params.csrf_token = csrf_token;
    
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'json',
        data: params,

        success: function(v) {
            if (v.ok) {
               cb(null, v)
            } else {
                cb(v.msg, null);
            }
            //app.hide_loading();
        },

        error: function(xhr, status) {
            cb('[ERROR] ' + xhr.status + ': ' + xhr.statusText, null);
            //app.hide_loading();
            //NProgress.done(true);
        }
    });
};

app.set_cookie = function(k, v) {
    $.cookie(k, v);
};

app.get_cookie = function(k) {
    return $.cookie(k);
};

app.strip = function(msg, len)
{
    return msg.length > len ? msg.substr(0, len) + ' ...' : msg;
};

app.alert = function(msg, title) {
    if(!title){
        title = 'Messages';
    }

    $("#freeow").freeow(title, msg, {
        //classes: ["gray", "error"],
        classes: ["gray"],
        style: 'smokey',
        prepend: false,
        autoHide: true
    });
};

app.set_first_selected = function(obj) {
    $(obj).find('option').first().prop('selected', 'selected');
};

app.show_loading = function() {
    NProgress.start();
    // $.blockUI({
    //         css: {
    //             border: 'none',
    //             padding: '15px',
    //             backgroundColor: '#000',
    //             '-webkit-border-radius': '10px',
    //             '-moz-border-radius': '10px',
    //             opacity: 1,
    //             color: '#fff'
    //         },
    //         message: '<h4>Loading <img src="/static/img/ajax-loader.gif" alt="loading."> </h4>'
    //     });
};

app.hide_loading = function() {
    //$.unblockUI();
    NProgress.done(true);
};


app.clear_null = function(v) {
    if(!v) {
        return '-';
    } else {
        return v;
    }
};

app.record_per_page = 15;

app.set_runtime = function() {
    $('input[data-type="time"]').mask("99:99");
    $('input[data-type="date"]').mask("99/99/9999");
    $('input[data-type="year"]').mask("9999");
    $('input[data-type="number"]').numeric();
    $('select[disabled]').css('background-color', 'white');
    $('input[disabled]').css('background-color', 'white');
    $('textarea[disabled]').css('background-color', 'white');

    $('[rel="tooltip"]').tooltip();

    //icheck
    $('input[type="checkbox"]').iCheck({
        checkboxClass: 'icheckbox_square-red',
        radioClass: 'iradio_square-red'
    });

    $('[data-type="date-picker"]').datepicker({
        format: "dd/mm/yyyy",
        todayBtn: "linked",
        language: "th",
        todayHighlight: true,
        forceParse: true,
        autoclose: true
      });
};

$(function() {

    $(document).ajaxStart(function() {
        NProgress.start();
        $.blockUI({
            message: null,
            overlayCSS: {
                opacity: 0.3
            }
        });
    }).ajaxStop(function() {
        NProgress.done(true);
        $.unblockUI();
    });

    var get_labor_other_total = function(start_date, end_date, cb) {
        app.ajax('/labor/get_total', {
            start_date: start_date,
            end_date: end_date
        }, function(e, v) {
            e ? cb (e, null) : cb (null, v.total);
        });
    };

//    setInterval(function() {
//        var date_range = app.get_current_date_range();
//
//        get_labor_other_total(date_range.start_date, date_range.end_date, function(err, total) {
//            console.log(total);
//        });
//    }, 50000);

    var show_app_change_password = function () {
        $('#mdl_app_change_password').modal({
            keyboard: false,
            backdrop: false
        });
    };


    $('#btn_app_show_change_password').on('click', function(e) {
        e.preventDefault();

        show_app_change_password();
    });


    var app_do_change_pass = function(password, cb) {
        app.ajax('/admins/changepass', {
            password: password
        }, function(e) {
            e ? cb(e, null) : cb(null);
        });
    };

    $('#btn_app_change_password').on('click', function(e) {
        e.preventDefault();

        var password = $('#txt_app_chw_new').val();
        var password2 = $('#txt_app_chw_new2').val();

        if(!password || !password2) {
            app.alert('กรุณาระบุรหัสผ่านใหม่');
        } else if(password != password2) {
            app.alert('รหัสผ่านทั้งสองช่องไม่เหมือนกัน กรุณาตรวจสอบ');
        } else {
            app_do_change_pass(password, function(e) {
                if(e) {
                    app.alert(e);
                } else {
                    app.alert('เปลี่ยนรหัสผ่านเสร็จเรียบร้อยแล้ว');
                }
            });
        }
    });


    app.setPagingFormat = function(type)
    {
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
    };

    //set table header text center
    $('th').addClass('text-center');


    app.set_runtime();
});


