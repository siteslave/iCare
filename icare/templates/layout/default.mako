
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <title>iCare : ${title}</title>

    <!-- Bootstrap core CSS -->
    <link href="/static/css/themes/simplex/bootstrap.min.css" rel="stylesheet">
    <link href="/static/css/font-awesome.min.css" rel="stylesheet">
    <link href="/static/css/freeow/freeow.css" rel="stylesheet">
    <link href="/static/css/datepicker.css" rel="stylesheet">
    <link href="/static/css/nprogress.css" rel="stylesheet">
    <link href="/static/icheck/skins/square/red.css" rel="stylesheet">
    <link href="/static/css/app.css" rel="stylesheet">

    <script src="/static/js/jquery.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
    <script src="/static/js/nprogress.js"></script>
    <script src="/static/icheck/icheck.min.js"></script>


    <script src="/static/js/bootstrap-datepicker.js"></script>
    <script src="/static/js/bootstrap-datepicker.th.js"></script>

    <!--[if lt IE 9]>

    <script src="/static/js/respond.min.js"></script>
    <script src="/static/js/html5shiv.js"></script>
    <!--[endif]-->

    <script charset="utf-8">
        var csrf_token = '${request.session.get_csrf_token()}';
    </script>

    <!-- library -->
    <script src="/static/js/jquery.paging.min.js"></script>
    <script src="/static/js/jquery.cookie.min.js"></script>
    <script src="/static/js/jquery.freeow.min.js"></script>
    <script src="/static/js/jquery.blockUI.js"></script>
    <script src="/static/js/jquery.maskedinput.min.js"></script>
    <script src="/static/js/jquery.numeric.min.js"></script>
    <script src="/static/js/numeral.js"></script>
    <script src="/static/js/moment.min.js"></script>
    <script src="/static/js/underscore-min.js"></script>

    <script src="/static/js/app.js" charset="utf-8"></script>
  </head>

  <body>
    <div id="freeow" class="freeow freeow-bottom-right"></div>
    <!-- Fixed navbar -->
    <div class="navbar navbar-default" role="navigation">
      <div class="container">
        <button type="button" class="navbar-toggle" data-toggle="collapse"
                data-target=".navbar-ex1-collapse">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
       <a class="navbar-brand" href="${request.application_url}"><i class="fa fa-windows"></i> iCare</a>
        <div class="collapse navbar-collapse navbar-ex1-collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                  <span class="fa fa-list"></span> งานแม่และเด็ก <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li class="dropdown-header">MOTHER & CHILD</li>
                <li><a href="${request.route_url('anc_index')}"><i class="fa fa-calendar fa-fw"></i> ข้อมูลการฝากครรภ์</a></li>
                <li><a href="${request.route_url('mch_index')}"><i class="fa fa-user-md fa-fw"></i> ทะเบียนหญิงคลอด/ดูแลหลังคลอด</a></li>
                <li><a href="${request.route_url('babies_index')}"><i class="fa fa-suitcase fa-fw"></i> ทะเบียนเด็กแรกเกิด/ดูแลหลังคลอด</a></li>
                <li class="divider"></li>
                <li><a href="${request.route_url('labor_other_index')}"><i class="fa fa-search fa-fw"></i> ตรวจสอบข้อมูลการคลอดจากโรงพยาบาล</a></li>
<li class="divider"></li>
                  <li class="dropdown-header">VACCINES SERVICES</li>
                  <li><a href="${request.route_url('wbc02_index')}"><i class="fa fa-check fa-fw"></i> วัคซีนและโภชนาการเด็ก 0-2 ปี</a></li>
                  <li><a href="${request.route_url('wbc35_index')}"><i class="fa fa-check fa-fw"></i> วัคซีนและโภชนาการเด็ก 3-5 ปี</a></li>
                  <li><a href="${request.route_url('wbc612_index')}"><i class="fa fa-check fa-fw"></i> วัคซีนและโภชนาการเด็ก 6-12 ปี</a></li>

              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                  <span class="fa fa-sitemap"></span> ระบบงานอื่นๆ <b class="caret"></b></a>
              <ul class="dropdown-menu">
                    <li class="dropdown-header">OTHER SERVICES</li>
				    <li><a href="${request.route_url('employers_index')}"><i class="fa fa-group fa-fw"></i> ทะเบียนบุคลากร</a></li>
                    <li><a href="${request.route_url('users_admin_index')}"><i class="fa fa-user-md fa-fw"></i> ทะเบียนผู้ใช้งาน (Users Management)</a></li>
                    <li class="divider"></li>

                    <li><a href="${request.route_url('project_index')}"><i class="fa fa-shopping-cart fa-fw"></i> รายละเอียดโครงการ</a></li>
                    <li><a href="${request.route_url('equipment_index')}"><i class="fa fa-briefcase fa-fw"></i> รายการครุภัณฑ์ทางการแพทย์</a></li>
    ##                <li><a href="${request.route_url('ncdscreen_index')}"><i class="icon-calendar"></i> คัดกรองความเสี่ยง</a></li>
    ##                <li><a href="#"><i class="icon-user-md"></i> ปรับเปลี่ยนพฤติกรรม</a></li>
    ##                <li class="divider"></li>
    ##                <li><a href="#"><i class="icon-food"></i> ทะเบียนผู้ป่วยเบาหวานความดัน</a></li>
    ##                <li><a href="#"><i class="icon-female"></i> ทะเบียนผู้พิการ</a></li>
    ##                <li><a href="#"><i class="icon-suitcase"></i> ทะเบียนผู้เสียชีวิต</a></li>
    ##                <li><a href="#"><i class="icon-user"></i> ทะเบียนผู้สูงอายุ</a></li>
                    <li class="divider"></li>
                    <li class="dropdown-header">GIS/MAP</li>
                    <li><a href="${request.route_url('mch_map')}"><i class="fa fa-map-marker fa-fw"></i> แผนที่ระบบงานแม่และเด็ก</a></li>
                  <li><a href="${request.route_url('labor_other_index')}"><i class="fa fa-search fa-fw"></i> ตรวจสอบคนในเขตที่ไปคลอดนอกเขต</a></li>

              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                  <span class="fa fa-list-alt"></span> ข้อมูล <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li class="dropdown-header">FILE MANAGEMENT</li>
                <li><a href="${request.route_url('uploads')}"><i class="fa fa-cloud-upload"></i> นำเข้าข้อมูล 43 แฟ้ม</a></li>
              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"> 
                  <span class="fa fa-print"></span> รายงาน <b class="caret"></b></a>
                <ul class="dropdown-menu">
                    <li class="dropdown-header">REPORTS SYSTEMS</li>
                    <li>
                        <a href="${request.route_url('reports_anc_12weeks_index')}">
                        <i class="fa fa-print fa-fw"></i> ฝากครรภ์ครั้งแรกเมื่ออายุครรภ์ <= 12 สัปดาห์
                        </a>
                    </li>
                    <li>
                        <a href="${request.route_url('reports_anc_coverages_index')}">
                        <i class="fa fa-print fa-fw"></i> ฝากครรภ์ครบ/ไม่ครบ 5 ครั้งคุณภาพ
                        </a>
                    </li>
                    <li>
                        <a href="${request.route_url('reports_anc_risk')}">
                        <i class="fa fa-print fa-fw"></i> ผู้มีภาวะเสี่ยงในการฝากครรภ์
                        </a>
                    </li>
                    <li class="divider"></li>
                    <li>
                        <a href="${request.route_url('report_anc')}">
                        <i class="fa fa-print fa-fw"></i> รายชื่อหญิงครบกำหนดฝากครรภ์
                        </a>
                    </li>
                    <li>
                        <a href="${request.route_url('reports_mch_index')}">
                        <i class="fa fa-print fa-fw"></i> รายชื่อมารดาที่ต้องได้รับการเยี่ยมในเวลาที่กำหนด
                        </a>
                    </li>
                    <li class="divider"></li>
                    <li>
                        <a href="${request.route_url('reports_newborn_wlt2500')}">
                        <i class="fa fa-print fa-fw"></i> ทารกแรกเกิดน้ำหนักน้อยกว่า 2,500 กรัม
                        </a>
                    </li>
                    <li>
                        <a href="${request.route_url('reports_milk_index')}">
                        <i class="fa fa-print fa-fw"></i> เด็กดื่มนมแม่อย่างเดียว 6 เดือน
                        </a>
                    </li>
                    <li class="disabled">
                        <a href="${request.route_url('reports_anc_risk')}">
                        <i class="fa fa-print fa-fw"></i> ข้อมูลการตรวจภาวะโภชนาการเด็ก
                        </a>
                    </li>
                </ul>
            </li>
          </ul>
          <ul class="nav navbar-nav navbar-right">
##              <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown"><span
##                    class="fa fa-comments"></span> ข้อความ <span class="label label-primary">5</span>
##                </a>
##                    <ul class="dropdown-menu">
##                        <li><a href="#"><i class="fa fa-check"></i> [3440400677068] ศิวาพร ศรีธรรมา</a></li>
##                        <li><a href="#"><i class="fa fa-check"></i> [1100500996943] วนิดา ฟั่นปั๋น</a></li>
##                        <li><a href="#"><i class="fa fa-check"></i> [3440400678285] เบญจวรรณ บุตราช</a></li>
##                        <li class="divider"></li>
##                        <li><a href="#" class="text-center"><i class="fa fa-th-list"></i> ทั้งหมด</a></li>
##                    </ul>
##                </li>
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                    <span class="fa fa-cogs"></span> ตัวเลือก<b class="caret"></b></a>
              <ul class="dropdown-menu">
                  <li>
                  <div class="navbar-content">
                                                    <div class="row">
                                                        <div class="col-md-5">
                                                            <img src="http://lh5.googleusercontent.com/-b0-k99FZlyE/AAAAAAAAAAI/AAAAAAAAAAA/twDq00QDud4/s120-c/photo.jpg"
                                                                alt="Alternate Text" class="img-responsive" />
##                                                            <p class="text-center small">
##                                                                <a href="#">Change Photo</a></p>
                                                        </div>
                                                        <div class="col-md-7">
                                                            <span>${request.session['fullname']}</span>
                                                            <p class="text-muted small">
                                                                ${request.session['hospcode']}</p>
                                                            <div class="divider">
                                                            </div>
##                                                            <a href="#" class="btn btn-primary btn-sm">View Profile</a>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="navbar-footer">
                                                    <div class="navbar-footer-content">
                                                        <div class="row">
                                                            <div class="col-md-6">
                                                                <a href="#" id="btn_app_show_change_password" class="btn btn-default btn-sm"><i class="fa fa-key fa-fw"></i> เปลี่ยนรหัสผ่าน</a>
                                                            </div>
                                                            <div class="col-md-6">
                                                                <a href="${request.route_url('signout')}" class="btn btn-default btn-sm pull-right">ออกจากระบบ <i class="fa fa-sign-out fa-fw"></i></a>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                  </li>
##                <li class="dropdown-header">${request.session['fullname']} [${request.session['hospcode']}]</li>
##                <li><a href="#" id="btn_app_show_change_password"><i class="fa fa-key fa-fw"></i> เปลี่ยนรหัสผ่าน</a></li>
##                <li class="divider"></li>
##                <li><a href="${request.route_url('signout')}"><i class="fa fa-sign-out fa-fw"></i> ออกจากระบบ</a></li>
              </ul>
            </li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container">

      ${self.body()}

    </div>

  <div class="modal fade" id="mdl_app_change_password">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> เปลี่ยนรหัสผ่าน</h4>
      </div>
      <div class="modal-body">
          <form action="#">
              <label for="txt_app_chw_new">รหัสผ่านใหม่</label>
              <input type="password" class="form-control" id="txt_app_chw_new"/>
              <label for="txt_app_chw_new2">รหัสผ่านใหม่ (อีกครั้ง)</label>
              <input type="password" class="form-control" id="txt_app_chw_new2"/>
          </form>
      </div>
      <div class="modal-footer">
          <button type="button" class="btn btn-default" id="btn_app_change_password">
              <i class="fa fa-save"></i> เปลี่ยนรหัสผ่าน
          </button>
        <button type="button" class="btn btn-primary" data-dismiss="modal">
            <i class="fa fa-times"></i> ปิดหน้าต่าง
        </button>
      </div>
    </div>
  </div>
</div>

  </body>
</html>
