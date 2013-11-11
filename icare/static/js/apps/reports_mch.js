$(function() {
    ///mch/process

    var rpt_mch = {};

    rpt_mch.ajax = {
        get_total: function (cb) {
            app.ajax('/reports/mch/total', {}, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },

        search: function (cid, cb) {
            app.ajax('/reports/mch/search', { cid: cid}, function(e, v) {
                e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_list: function (s, t, cb) {
            app.ajax('/reports/mch/list', { start: s, stop: t }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        process: function (cb) {
            app.ajax('/reports/mch/process', {}, function (e) {
               e ? cb (e, null) : cb (null);
            });
        }
    };

    $('#btn_process').on('click', function(e) {
        e.preventDefault();

        if (confirm('คุณต้องการประมวลผลข้อมูล ใช่หรือไม่?')) {
            rpt_mch.ajax.process(function (e) {
                if (e) {
                    app.alert(e);
                } else {
                    app.alert('ประมวลผลข้อมูลเสร็จเรียบร้อยแล้ว');
                }
            });
        }
    });
});