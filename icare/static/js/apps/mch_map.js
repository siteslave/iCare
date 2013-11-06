// create namespace for mch map
var mm = {};
// base icon url
mm.iconBase = '/static/img/markers/';
// latitude
mm.latitude = 16.1817729;
// longitude
mm.longitude = 103.29929419999999;
// enable/disable mark map
mm.ready_for_mark = false;
// makers
mm.markers = [];
// Patients Latitude and Longitude
mm.patientLatLng = {};
// Patients
mm.patient = [];

//Direction
mm.directionsDisplay = new google.maps.DirectionsRenderer();

// check browser support Geolocation
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(
      function(position) {
        mm.latitude = position.coords.latitude;
        mm.longitude = position.coords.longitude;
  }, 
      function(msg) {
        //alert(msg);
  });
    
};

// Current LatLng
mm.latLng = new google.maps.LatLng(
    mm.latitude, mm.longitude
);
// Set map object
var mapId = document.getElementById('map');
// Map options
var options = {
    center: mm.latLng,
    zoom: 14,
    mapTypeId: google.maps.MapTypeId.HYBRID
};

//create map
mm.map = new google.maps.Map(mapId, options);
//create owner position
mm.mgr_owner = new google.maps.Marker({
    position: mm.latLng,
    map: mm.map,
    icon: mm.iconBase + 'offices/apartment-3.png',
    title: 'คุณอยู่ที่นี่'
});

//set window title
mm.set_window = function(msg, map, maker) {
    var infowindow = new google.maps.InfoWindow({
        content: msg
    });
	// Create infowindows
    infowindow.open(map, maker);
};
//clear map
mm.clearMarker = function() {
    
    // Clear old direction
    mm.directionsDisplay.setMap(null);
    // Set map type to HYBRID
    mm.map.setMapTypeId(google.maps.MapTypeId.HYBRID);
    
	// Clear markers
    for (var i = 0; i < mm.markers.length; i++) {
        mm.markers[i].setMap(null);
    }
	// Clear patient LatLng
    mm.patientLatLng.latitude = '';
    mm.patientLatLng.longitude = '';
    mm.patientLatLng.cid = '';

};
// Create maker
mm.addMarkerAnc = function(lat, lng, title) {

    var mkg = new google.maps.Marker({
        position: new google.maps.LatLng(
            lat, lng
        ),
        map: mm.map,
        icon: mm.iconBase + 'health/fetalalcoholsyndrom.png',
        title: title
    });
	// Add marker to array
    mm.markers.push(mkg);
};
// Create events for owner map
google.maps.event.addListener(mm.mgr_owner, 'click', function() {
    mm.map.setZoom(18);
    mm.set_window('ที่อยู่ของคุณปัจจุบัน', mm.map, mm.mgr_owner);
});
//Add event to main map
mm.set_event = function() {
    // Create main map event
    google.maps.event.addListener(mm.map, 'click', function(e) {
        //console.log(e.latLng.nb);
        //var msg = e.latLng.mb + ', ' + e.latLng.nb;
        // mb = Latitude, nb = Longitude
        //console.log(e.latLng.lat());


        if(mm.ready_for_mark) {
            //can mark map
    /*        new google.maps.Marker({
                position: new google.maps.LatLng(
                    e.latLng.mb, e.latLng.nb
                ),
                map: mm.map,
                    icon: mm.iconBase + 'health/fetalalcoholsyndrom.png',
                    title: 'คนคลอด'
                });*/
            mm.clearMarker();
            mm.addMarkerAnc(e.latLng.lat(), e.latLng.lng(), 'หญิงตั้งครรภ์');
            mm.patientLatLng.latitude = e.latLng.lat();
            mm.patientLatLng.longitude = e.latLng.lng();

            $('#btn_save_marker').removeProp('disabled');
        }

    });  
};
// jQuery initial
$(function(){
	// Ajax module
    mm.ajax = {
		// Get patient total
        get_total: function (vid, by, cb) {
            app.ajax('/anc/get_list_map_total', {
                by: by,
                vid: vid
            }, function(e, v) {
                e ? cb (e, null) : cb (null, v.total);
            });
        },
		// Get patients list
        get_list: function (vid, b, s, t, cb) {
            app.ajax('/anc/get_list_map', {
                start: s,
                stop: t,
                by: b,
                vid: vid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },
		// Get LatLng
        get_marker: function (b, cb) {
            app.ajax('/anc/get_marker', {
                by: b
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },
		// Save LatLng
        save_latlng: function (hospcode, hid, lat, lng, cb) {
            app.ajax('/home/save_latlng', {
                hid: hid,
                hospcode: hospcode,
                lat: lat,
                lng: lng
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },
		// Get all LatLng
        get_all_latlng: function (vid, by, cb) {
            app.ajax('/anc/get_all_latlng', {
                by: by,
                vid: vid
            }, function (e, v) {
               e ? cb (e, null) : cb (null, v.rows);
            });
        },
		// Remove LatLng
        remove_latlng: function (hospcode, hid, cb) {
            app.ajax('/home/remove_latlng', {
                hospcode: hospcode,
                hid: hid
            }, function (e, v) {
               e ? cb (e, null) : cb (null);
            });
        }
    };
	// Modal modules
    mm.modal = {
        show_mark_map: function() {
            $('#mdl_mark_map').modal({
                keyboard: false,
                backdrop: 'static'
            });
        }
    };
	// Set patients list
    mm.set_list = function(rs) {
		// Clear table list
        $('#tbl_anc > tbody').empty();
		// Check isn't empty rows
        if($(rs).size()) {
            $.each(rs, function(i, v) {
                var latlng_link = v.latlng[0] && v.latlng[1] ?
                    '<li><a href="javascript:void(0);" data-name="btn_view_map" data-lat="'+ v.latlng[0] +'" data-lng="'+ v.latlng[1] +'">' +
                    '<i class="icon-map-marker"></i> ไปที่หลังคาเรือน</a></li>' :
                    '<li class="disabled"><a href="javascript:void(0);"><i class="icon-map-marker"></i> ไปที่หลังคาเรือน</a></li>';

                var direction = v.latlng[0] && v.latlng[1] ?
                    '<li><a href="javascript:void(0);" data-name="btn_get_direction" data-lat="'+ v.latlng[0] +'" data-lng="'+ v.latlng[1] +'">' +
                    '<i class="icon-ambulance"></i> ขอเส้นทาง</a></li>' :
                    '<li class="disabled"><a href="javascript:void(0);"><i class="icon-ambulance"></i> ขอเส้นทาง</a></li>';

                var fullname = v.latlng[0] && v.latlng[1] ? '<strong>'+ v.fullname +'</strong> <span class="label label-success">แผนที่</span>' : v.fullname;

                $('#tbl_anc > tbody').append(
                    '<tr>' +
                        '<td>' + v.cid + '</td>' +
                        '<td>' + fullname + '</td>' +
                        '<td>' + v.age.year + '</td>' +
                        '<td><div class="btn-group">' +
                        '<button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">' +
                        '<i class="icon-double-angle-right"></i>' +
                        '</button>' +
                        '<ul class="dropdown-menu" role="menu">' +
                        '<li role="presentation" class="dropdown-header">TOOLS</li>' +
                        latlng_link +
                        direction +
                        '<li>' +
                        '<a href="javascript:void(0);" data-name="btn_mark_map" data-cid="'+ v.cid +'" ' +
                        'data-fullname="'+ v.fullname +'" data-pid="'+ v.pid +'" data-hospcode="'+ v.hospcode +'" data-hid="' + v.hid + '"><i class="icon-screenshot"></i> ระบุพิกัดแผนที่</a>' +
                        '</li>' +
                        '<li class="divider"></li>' +
                        '<li><a href="javascript:void(0);" data-name="btn_remove_mark" data-hospcode="'+ v.hospcode +'"' +
                        'data-pid="'+ v.pid + '" data-hid="' + v.hid + '">' +
                        '<i class="icon-trash"></i> ยกเลิกพิกัด</a></li>' +
                        '</ul>' +
                        '</div></td>' +
                        '</tr>'
                );
            });

            app.set_runtime();
        }
        else {
            $('#tbl_anc > tbody').append('<tr><td colspan="3">ไม่พบข้อมูล</td></td></tr>');
        }
    };
	// Remove LatLng
    $(document).on('click', 'a[data-name="btn_remove_mark"]', function(e) {
        e.preventDefault();

        var hid = $(this).data('hid');
        var hospcode = $(this).data('hospcode');

        if(confirm('คุณต้องการลบพิกัดคนนี้ใช่หรือไม่? \n\r')) {
            mm.ajax.remove_latlng(hospcode, hid, function(err) {
                if(err) {
                    app.alert(err);
                } else {
                    mm.get_all_latlng();
                    mm.map.setCenter(mm.latLng);
                    mm.map.setZoom(14);
                }
            });
        }
    });
	// View map
    $(document).on('click', 'a[data-name="btn_view_map"]', function(e) {
        e.preventDefault();
        var lat = $(this).data('lat');
        var lng = $(this).data('lng');

        var latLng = new google.maps.LatLng(lat, lng);
        var tr = $(this).parent().parent().parent().parent().parent();
        mm.clear_tr();
        tr.addClass('success');
        mm.map.setCenter(latLng);
        mm.map.setZoom(18);

    });
	// Mark map
    $(document).on('click', 'a[data-name="btn_mark_map"]', function(){

        var cid = $(this).data('cid');
        var fullname = $(this).data('fullname');
        var hid = $(this).data('hid');
        var hospcode = $(this).data('hospcode');

        var tr = $(this).parent().parent().parent().parent().parent();
		// Clear table row color
        mm.clear_tr();
		// Clear markers
        mm.clearMarker();
		// Add .success class to tr
        tr.addClass('success');
		
		// Set patient data
        $('#txt_ptname').val(fullname);
        $('#txt_cid').val(cid);
        $('#txt_hid').val(hid);
        $('#txt_hospcode').val(hospcode);
		// Show mark map menu
        $('#div_mark_map').fadeIn('slow');
        $('#btn_save_marker').prop('disabled', true);
        //creat event to main map
        mm.set_event();
        // Set mark enable
        mm.ready_for_mark = true;
    });

	// Remove .success class of tr
    mm.clear_tr = function() {
        $('#tbl_anc tr').each(function() {
            //$(this).removeClass('success');
            if($(this).hasClass('success'))
                $(this).removeClass('success');
            console.log($(this));
        });
    };

    mm.generate_marker = function(patient) {
        /*
            var mkg = new google.maps.Marker({
        position: new google.maps.LatLng(
            lat, lng
        ),
        map: mm.map,
        icon: mm.iconBase + 'health/fetalalcoholsyndrom.png',
        title: title
    });
         */
        
        mm.map.setZoom(14);
        mm.map.setCenter(mm.latLng);
        
        $.each(patient, function(i, v) {
            //console.log(v);
            var latLng = new google.maps.LatLng(v.latlng[0], v.latlng[1]);

            var marker = new google.maps.Marker({
                position: latLng,
                map: mm.map,
                icon: mm.iconBase + 'health/fetalalcoholsyndrom.png',
                title: v.fullname,
                draggable: false,
                animation: google.maps.Animation.DROP
            });

            mm.markers.push(marker);

            google.maps.event.addListener(marker, 'click', function() {
                var html =
                '<div style="width: 400px; height: 200px;"><ul class="nav nav-tabs" id="infoTab">' +
                '<li class="active"><a href="#home" data-toggle="tab"><i class="icon-user"></i> ข้อมูลทั่วไป</a></li>' +
                '<li><a href="#profile" data-toggle="tab"><i class="icon-paste"></i> ข้อมูลการฝากครรภ์</a></li>' +
                '</ul> <br />' +
                '<div class="tab-content">' +
                '<div class="tab-pane active" id="home">' +
                    '<strong>ชื่อ-สกุล:</strong> ' + v.fullname + '<br />' +
                    '<strong>เลขบัตรประชาชน:</strong> ' + v.cid + '<br />' +
                    '<strong>วันเกิด:</strong> ' + v.birth + '<br />' +
                    '<strong>อายุ:</strong> ' + v.age.year + ' ปี ' + v.age.month + ' เดือน ' + v.age.day + ' วัน <br />' +
                '</div>' +
                '<div class="tab-pane" id="profile">';


                $.each(v.prenatal, function(ii, vv) {

                    var tha = vv.thalassemia == '1' ? 'ปกติ' :
                        vv.thalassemia == '2' ? 'ผิดปกติ' :
                            vv.thalassemia == '3' ? 'ไม่ตรวจ' :
                                vv.thalassemia == '4' ? 'รอผลตรวจ' :
                                    vv.thalassemia == '9' ? 'ไม่ทราบ' : '-';
                    var vdrl = vv.vdrl_result == '1' ? 'ปกติ' :
                        vv.vdrl_result == '2' ? 'ผิดปกติ' :
                            vv.vdrl_result == '3' ? 'ไม่ตรวจ' :
                                vv.vdrl_result == '4' ? 'รอผลตรวจ' :
                                    vv.vdrl_result == '9' ? 'ไม่ทราบ' : '-';
                    var hb = vv.hb_result == '1' ? 'ปกติ' :
                        vv.hb_result == '2' ? 'ผิดปกติ' :
                            vv.hb_result == '3' ? 'ไม่ตรวจ' :
                                vv.hb_result == '4' ? 'รอผลตรวจ' :
                                    vv.hb_result == '9' ? 'ไม่ทราบ' : '-';
                    var hiv = vv.hiv_result == '1' ? 'ปกติ' :
                        vv.hiv_result == '2' ? 'ผิดปกติ' :
                            vv.hiv_result == '3' ? 'ไม่ตรวจ' :
                                vv.hiv_result == '4' ? 'รอผลตรวจ' :
                                    vv.hiv_result == '9' ? 'ไม่ทราบ' : '-';
                    html +=
                    '<table class="table table-bordered" style="width: 350px;">' +
                        '<thead>' +
                            '<tr>' +
                                '<th colspan="2">ครรภ์ที่ : <strong>'+ vv.gravida +'</strong></th>' +
                            '</tr>' +
                            '</thead>' +
                            '<tbody>' +
                                '<tr>' +
                                    '<td>LMP</td>' +
                                    '<td>'+vv.lmp +'</td>' +
                                '</tr>' +
                                '<tr>' +
                                    '<td>EDC</td>' +
                                    '<td>'+vv.edc +'</td>' +
                                '</tr>' +
                                '<tr>' +
                                    '<td>DATE HCT</td>' +
                                    '<td>'+vv.date_hct +'</td>' +
                                '</tr>' +
                                '<tr>' +
                                    '<td>HCT RESULT</td>' +
                                    '<td>'+vv.hct_result +'</td>' +
                                '</tr>' +
                                '<tr>' +
                                    '<td>THALASSEMIA</td>' +
                                    '<td>'+ tha +'</td>' +
                                '</tr>' +
                                '<tr>' +
                                    '<td>VDRL</td>' +
                                    '<td>'+ vdrl +'</td>' +
                                '</tr>' +
                                '<tr>' +
                                    '<td>HB</td>' +
                                    '<td>'+ hb +'</td>' +
                                '</tr>' +
                                '<tr>' +
                                    '<td>HIV</td>' +
                                    '<td>'+ hiv +'</td>' +
                                '</tr>' +
                            '</tbody>' +
                    '</table>';
                });



                html += '</div></div></div>';

                var content = '';

                var infoWindow = new google.maps.InfoWindow({
                    content: html
                });

                mm.map.setZoom(18);
                mm.map.setCenter(latLng);

                infoWindow.open(mm.map, marker);
            });
        });
    };

    mm.get_all_latlng = function() {
        
        var vid = $('#sl_villages').val();
        var by = $('#sl_by').val();
        
        mm.clearMarker();

        mm.ajax.get_all_latlng(vid, by, function(err, rs) {
            if(!err) {

                var data = [];

                $.each(rs, function(i, v) {
                    //latLng.push(v.latlng);
                    //var content = 'เลขบัตรประชาชน: ' + v.cid;
                    //mm.addMarkerAnc(v.latlng[0], v.latlng[1], v.fullname, false);
                    var obj = {
                        'cid': v.cid,
                        'fullname': v.fullname,
                        'birth': v.birth,
                        'age': v.age,
                        'latlng': v.latlng,
                        'prenatal': v.prenatal
                    };
                    data.push(obj);
                    //set
                });

                mm.generate_marker(data);
            }
        });
    };

    $('#btn_get_anc_list').on('click', function(e) {
        e.preventDefault();
        
        mm.get_all_latlng();
        mm.get_list();
        
    });

    mm.get_list = function() {

        var vid = $('#sl_villages').val();
        var by = $('#sl_by').val();

        mm.ajax.get_total(vid, by, function(e, total) {
            if (e) {
                app.alert(e);
            } else {
                $('#paging').fadeIn('slow');

                $('#paging').paging(total, {
                    format: " < . (qq -) nnncnnn (- pp) . >",
                    perpage: 5,
                    lapping: 1,
                    page: app.get_cookie('mchmap_paging'),
                    onSelect: function(page) {
                        app.set_cookie('mchmap_paging', page);

                        mm.ajax.get_list(vid, by, this.slice[0], this.slice[1], function(e, rs){

                            $('#tbl_anc > tbody').empty();

                            if(e) {
                                app.alert(e);
                                $('#tbl_anc > tbody').append('<tr><td colspan="3">ไม่พบข้อมูล</td></td></tr>');
                            } else {
                                mm.set_list(rs);
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

    // clear markers
    $('#btn_clear_marker').on('click', function(e) {
        e.preventDefault();
        $('#btn_save_marker').prop('disabled', true);
        mm.clearMarker();
    });

    $('#btn_cancel_marker').on('click', function(e) {
        e.preventDefault();
        mm.clear_tr();
        mm.clearMarker();

        $('#txt_cid').val('');
        $('#txt_ptname').val('');
        $('#txt_pid').val('');
        $('#txt_hospcode').val('');

        $('#div_mark_map').fadeOut('slow');
        $('#btn_save_marker').prop('disabled', true);
        //load marker
        //mm.loadMarker();
        mm.ready_for_mark = false;
        mm.get_all_latlng();
        mm.get_list();
    });

    $(document).on('click', '#btn_save_marker', function(e) {

        e.preventDefault();

        //var cid = $('#txt_cid').val();
        var hid = $('#txt_hid').val();
        var hospcode = $('#txt_hospcode').val();

        if(mm.patientLatLng.latitude && mm.patientLatLng.longitude && hid && hospcode) {


            if(confirm('คุณต้องการบันทึกพิกัด ใช่หรือไม่?')) {
                mm.ajax.save_latlng(hospcode, hid, mm.patientLatLng.latitude, mm.patientLatLng.longitude,

                    function(err) {

                    if(err) {
                        app.alert(err);
                    } else {
                        app.alert('บันทึกพิกัดเสร็จเรียบร้อยแล้ว');
                        //set map
                        mm.ready_for_mark = false;
                        mm.get_all_latlng();
                        mm.map.setZoom(10);
                        mm.map.setCenter(mm.latLng);

                        $('#div_mark_map').fadeOut('slow');
                        mm.clear_tr();
                        mm.get_list();
                        //hide add marker form
                    }

                });
            }

        } else {
            app.alert('กรุณาระบุพิกัด');
        }

        //alert('Latitude: ' + mm.patientLatLng.latitude + ' , Longitude: ' + mm.patientLatLng.longitude);

    });

    //get direction
    $(document).on('click', 'a[data-name="btn_get_direction"]', function(e) {
        e.preventDefault();

        var tr = $(this).parent().parent().parent().parent().parent();
        mm.clear_tr();
        tr.addClass('success');

        var lat = $(this).data('lat');
        var lng = $(this).data('lng');

        var directionsService = new google.maps.DirectionsService();

        var src_latlng = new google.maps.LatLng(mm.latitude, mm.longitude);
        var dst_latlng = new google.maps.LatLng(lat, lng);

        
        //direct_map = new google.maps.Maps

        var options = {
            //center: mm.latLng,
            //zoom: 14,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        //create map
        mm.map = new google.maps.Map(mapId, options);
        // Clear old direction
        mm.directionsDisplay.setMap(null);
        //set direction
        mm.directionsDisplay.setMap(mm.map);

        var request = {
            origin: src_latlng,
            destination: dst_latlng,
            travelMode: google.maps.DirectionsTravelMode.DRIVING
        };

        directionsService.route(request, function(response, status) {
            if (status == google.maps.DirectionsStatus.OK) {
                mm.directionsDisplay.setDirections(response);
            }
        });

    });

    mm.set_event();
    
});
