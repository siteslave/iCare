$(function() {
    var anc_12ws = {};

    anc_12ws.ajax = {
        get_list: function (start, stop, cb) {

            app.ajax('/reports/anc_12ws/list', {
                start: start,
                stop: stop
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total: function (cb) {
            app.ajax('/reports/anc_12ws/total', {}, function (e, v) {
               e ? cb (e, null) : cb (null, v.total);
            });
        },

        do_process: function (cb) {
            app.ajax('/anc/do_process_12weeks', {}, function (e, v) {
               e ? cb (e, null) : cb (null);
            });
        }
    };

    anc_12ws.set_list = function(v) {

        $('#tbl_list > tbody').empty();

        if($(v).size()) {

            $(v).each(function(i, v) {

                $('#tbl_list > tbody').append(
                    '<tr>' +
                        '<td>' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td>' + v.birth + '</td>' +
                        '<td>' + v.age.year + '-' + v.age.month + '-' + v.age.day + '</td>' +
                        '<td>' + v.address + '</td>' +
                        '</tr>'
                );
            });

            app.set_runtime();

        } else {

            $('#tbl_list > tbody').append('<tr><td colspan="5">ไม่พบรายการ</td></tr>');

        }

    };


    anc_12ws.get_list = function() {

        anc_12ws.ajax.get_total(function(e, total) {
            if (e) {
                $('#spn_total > strong').html('0');
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');

                $('#spn_total > strong').html(numeral(total).format('0,0'));

                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('rpt_anc_12ws'),
                    onSelect: function(page) {
                        app.set_cookie('rpt_anc_12ws', page);

                        anc_12ws.ajax.get_list(this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="5">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                anc_12ws.set_list(rs);
                            }
                        });

                    },
                    onFormat: function(type){
                        switch (type) {

                            case 'block':

                                if (!this.active)
                                    return '<li class="disabled"><a href="#">' + this.value + '</a></li>';
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
                                return '<li class="disabled"><a href="#">&raquo;</a></li>';

                            case 'prev':

                                if (this.active) {
                                    return '<li><a href="#' + this.value + '">&laquo;</a></li>';
                                }
                                return '<li class="disabled"><a href="#">&laquo;</a></li>';

                            case 'first':

                                if (this.active) {
                                    return '<li><a href="#' + this.value + '">&lt;</a></li>';
                                }
                                return '<li class="disabled"><a href="#">&lt;</a></li>';

                            case 'last':

                                if (this.active) {
                                    return '<li><a href="#' + this.value + '">&gt;</a></li>';
                                }
                                return '<li class="disabled"><a href="#">&gt;</a></li>';

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

    //process
    $('#btn_do_process').on('click', function(e) {
        e.preventDefault();

        if(confirm('คุณต้องการประมวลผลข้อมูลใหม่ใช่หรือไม่')) {
            anc_12ws.ajax.do_process(function(e) {
                if(e) {
                    app.alert(e);
                } else {
                    anc_12ws.get_list();
                }
            });
        }
    })

    anc_12ws.get_list();

});