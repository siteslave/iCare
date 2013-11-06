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
app.to_string_eng_date = function(d) {
    var year = d.getFullYear();
    var month = d.getMonth() + 1;

    if(month < 10) month = '0' + month;

    var date = d.getDate();
    var new_date = year + '' + month + '' + date;

    return new_date;
};

app.ajax = function(url, params, cb) {

    app.show_loading();
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
            app.hide_loading();
        },

        error: function(xhr, status) {
            cb('[ERROR] ' + xhr.status + ': ' + xhr.statusText, null);
            app.hide_loading();
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
        prepend: false,
        autoHide: true
    });
};

app.set_first_selected = function(obj) {
    $(obj).find('option').first().prop('selected', 'selected');
};

app.show_loading = function() {
    $.blockUI({
            css: {
                border: 'none',
                padding: '15px',
                backgroundColor: '#000',
                '-webkit-border-radius': '10px',
                '-moz-border-radius': '10px',
                opacity: 1,
                color: '#fff'
            },
            message: '<h4>Loading <img src="/static/img/ajax-loader.gif" alt="loading."> </h4>'
        });
};

app.clear_null = function(v) {
    if(!v) {
        return '-';
    } else {
        return v;
    }
};

app.hide_loading = function() {
    $.unblockUI();
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
};



$(function() {

    var show_app_change_password = function () {
        $('#mdl_app_change_password').modal({
            keyboard: false,
            backdrop: 'static'
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
        if(!password) {
            app.alert('กรุณาระบุรหัสผ่านใหม่');
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

    app.set_runtime();
});


