$(function() {
    var anc_coverages = {};

    anc_coverages.ajax = {
        get_list: function (t, start, stop, cb) {

            app.ajax('/reports/anc_coverages/list', {
                start: start,
                stop: stop,
                t: t
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },

        get_total: function (t, cb) {
            app.ajax('/reports/anc_coverages/total', {
                t: t
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.total);
            });
        },

        search: function (cid, cb) {
            app.ajax('/reports/anc_coverages/search', {}, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        }
    };

    anc_coverages.set_list = function(v) {

        $('#tbl_list > tbody').empty();

        if($(v).size()) {

            $(v).each(function(i, v) {

                $('#tbl_list > tbody').append(
                    '<tr>' +
                        '<td class="text-center">' + v.cid + '</td>' +
                        '<td>' + v.fullname + '</td>' +
                        '<td class="text-center">' + v.birth + '</td>' +
                        '<td class="text-center">' + v.age.year + '-' + v.age.month + '-' + v.age.day + '</td>' +
                        '<td class="text-center">' + numeral(v.total).format('0, 0') + '</td>' +
                        '<td>' + v.address + '</td>' +
                        '</tr>'
                );
            });

            app.set_runtime();

        } else {

            $('#tbl_list > tbody').append('<tr><td colspan="6">ไม่พบรายการ</td></tr>');

        }

    };

    anc_coverages.get_filter = function() {
        $('label[data-name="chk_filter"]').each(function() {
            if($(this).hasClass('active')) return $(this).data('id');
        });
    };


    anc_coverages.get_list = function(t) {


        //var t = t || $('label[data-name="btn_filter"]').hasClass('active') ? $();
        var t = t || anc_coverages.get_filter();

        anc_coverages.ajax.get_total(t, function(e, total) {

            $('#spn_total > strong').html(numeral(total).format('0,0'));

            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');
                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: app.record_per_page,
                    lapping: 1,
                    page: app.get_cookie('rpt_anc_coverages'),
                    onSelect: function(page) {
                        app.set_cookie('rpt_anc_coverages', page);

                        anc_coverages.ajax.get_list(t, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_list > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_list > tbody').append('<tr><td colspan="6">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                anc_coverages.set_list(rs);
                            }
                        });

                    },
                    onFormat: app.setPagingFormat
                });
            }
        });

    };

    $('label[data-name="chk_filter"]').on('click', function(e) {
        e.preventDefault();

        var id = $(this).data('id');

        anc_coverages.get_list(id);
    });

    anc_coverages.get_list('1');

});