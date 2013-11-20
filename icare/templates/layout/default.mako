
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
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">
    <link href="/static/css/freeow/freeow.css" rel="stylesheet">

    <script src="/static/js/jquery.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>

    <script src="/static/js/respond.min.js"></script>

    <!--[if lt IE 9]>
    <script src="/static/js/html5shiv.js"></script>
    <![endif]-->

    <script charset="utf-8">
        var csrf_token = '${request.session.get_csrf_token()}';
    </script>
    <style>
        body {
            padding-top: 60px;
        }
        input[type='file']{
            position:absolute;
            opacity:0;
            /* For IE8 "Keep the IE opacity settings in this order for max compatibility" */
            -ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
            /* For IE5 - 7 */
            filter: alpha(opacity=0);
        }
    </style>

    <!-- library -->
    <script src="/static/js/jquery.paging.min.js"></script>
    <script src="/static/js/jquery.cookie.min.js"></script>
    <script src="/static/js/jquery.freeow.min.js"></script>
    <script src="/static/js/jquery.blockUI.js"></script>
    <script src="/static/js/jquery.maskedinput.min.js"></script>
    <script src="/static/js/jquery.numeric.min.js"></script>
    <script src="/static/js/numeral.js"></script>
    <script src="/static/js/moment.min.js"></script>

    <script src="/static/js/app.js" charset="utf-8"></script>

  </head>

  <body>
    <div id="freeow" class="freeow freeow-bottom-right"></div>
    <!-- Fixed navbar -->
    <div class="navbar navbar-default navbar-fixed-top" role="navigation">
      <div class="container">
        <button type="button" class="navbar-toggle" data-toggle="collapse"
                data-target=".navbar-ex1-collapse">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
       <a class="navbar-brand" href="${request.application_url}"><i class="icon-windows"></i> iCare</a>
        <div class="collapse navbar-collapse navbar-ex1-collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                  <span class="icon-list"></span> งานแม่และเด็ก <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li class="dropdown-header">MOTHER & CHILD</li>
                <li><a href="${request.route_url('anc_index')}"><i class="icon-calendar"></i> ข้อมูลการฝากครรภ์</a></li>
                <li><a href="${request.route_url('mch_index')}"><i class="icon-user-md"></i> การให้บริการแม่หลังคลอด</a></li>
                <li><a href="${request.route_url('babies_index')}"><i class="icon-suitcase"></i> ทะเบียนเด็กแรกเกิด</a></li>
                  <li class="divider"></li>
                  <li class="dropdown-header">VACCINES SERVICES</li>
                  <li><a href="${request.route_url('wbc02_index')}"><i class="icon-check"></i> วัคซีนและโภชนาการเด็ก 0-2 ปี</a></li>
                  <li><a href="${request.route_url('wbc35_index')}"><i class="icon-check"></i> วัคซีนและโภชนาการเด็ก 3-5 ปี</a></li>
                  <li><a href="${request.route_url('wbc612_index')}"><i class="icon-check"></i> วัคซีนและโภชนาการเด็ก 6-12 ปี</a></li>

              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                  <span class="icon-sitemap"></span> ระบบงานอื่นๆ <b class="caret"></b></a>
              <ul class="dropdown-menu">
                    <li class="dropdown-header">OTHER SERVICES</li>
				    <li><a href="${request.route_url('employers_index')}"><i class="icon-group"></i> ทะเบียนบุคลากร</a></li>
                    <li><a href="${request.route_url('users_admin_index')}"><i class="icon-user-md"></i> ทะเบียนผู้ใช้งาน (Users Management)</a></li>
                    <li class="divider"></li>
				    <li class="disabled"><a href="#"><i class="icon-search"></i> ตรวจสอบคนในเขตที่ไปคลอดนอกเขต</a></li>
##                <li><a href="${request.route_url('epidem_index')}"><i class="icon-group"></i> ระบาดวิทยา</a></li>
##                <li><a href="${request.route_url('ncdscreen_index')}"><i class="icon-calendar"></i> คัดกรองความเสี่ยง</a></li>
##                <li><a href="#"><i class="icon-user-md"></i> ปรับเปลี่ยนพฤติกรรม</a></li>
##                <li class="divider"></li>
##                <li><a href="#"><i class="icon-food"></i> ทะเบียนผู้ป่วยเบาหวานความดัน</a></li>
##                <li><a href="#"><i class="icon-female"></i> ทะเบียนผู้พิการ</a></li>
##                <li><a href="#"><i class="icon-suitcase"></i> ทะเบียนผู้เสียชีวิต</a></li>
##                <li><a href="#"><i class="icon-user"></i> ทะเบียนผู้สูงอายุ</a></li>

##                    <li class="dropdown-header">GIS/MAP</li>
                    <li><a href="${request.route_url('mch_map')}"><i class="icon-map-marker"></i> แผนที่ระบบงานแม่และเด็ก</a></li>

              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                  <span class="icon-list-alt"></span> ข้อมูล <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li class="dropdown-header">FILE MANAGEMENT</li>
                <li><a href="${request.route_url('uploads')}"><i class="icon-cloud-upload"></i> นำเข้าข้อมูล 43 แฟ้ม</a></li>
              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"> 
                  <span class="icon-print"></span> รายงาน <b class="caret"></b></a>
                <ul class="dropdown-menu">
                    <li class="dropdown-header">REPORTS SYSTEMS</li>
                    <li>
                        <a href="${request.route_url('reports_anc_12weeks_index')}">
                        <i class="icon-print"></i> ฝากครรภ์ครั้งแรกเมื่ออายุครรภ์ <= 12 สัปดาห์
                        </a>
                    </li>
                    <li>
                        <a href="${request.route_url('reports_anc_coverages_index')}">
                        <i class="icon-print"></i> ฝากครรภ์ครบ/ไม่ครบ 5 ครั้งคุณภาพ
                        </a>
                    </li>
                    <li>
                        <a href="${request.route_url('reports_anc_risk')}">
                        <i class="icon-print"></i> ผู้มีภาวะเสี่ยงในการฝากครรภ์
                        </a>
                    </li>
                    <li class="divider"></li>
                    <li>
                        <a href="${request.route_url('report_anc')}">
                        <i class="icon-print"></i> รายชื่อหญิงครบกำหนดฝากครรภ์
                        </a>
                    </li>
                    <li>
                        <a href="${request.route_url('reports_mch_index')}">
                        <i class="icon-print"></i> รายชื่อมารดาที่ต้องได้รับการเยี่ยมในเวลาที่กำหนด
                        </a>
                    </li>
                    <li class="divider"></li>
                    <li>
                        <a href="${request.route_url('reports_newborn_wlt2500')}">
                        <i class="icon-print"></i> ทารกแรกเกิดน้ำหนักน้อยกว่า 2,500 กรัม
                        </a>
                    </li>
                    <li>
                        <a href="${request.route_url('reports_milk_index')}">
                        <i class="icon-print"></i> เด็กดื่มนมแม่อย่างเดียว 6 เดือน
                        </a>
                    </li>
                    <li class="disabled">
                        <a href="${request.route_url('reports_anc_risk')}">
                        <i class="icon-print"></i> ข้อมูลการตรวจภาวะโภชนาการเด็ก
                        </a>
                    </li>
                </ul>
            </li>
          </ul>
          <ul class="nav navbar-nav pull-right">
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                    <span class="icon-cogs"></span> Tools<b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li class="dropdown-header">${request.session['fullname']} [${request.session['hospcode']}]</li>
                <li><a href="#" id="btn_app_show_change_password"><i class="icon-key"></i> เปลี่ยนรหัสผ่าน</a></li>
                <li class="divider"></li>
                <li><a href="${request.route_url('signout')}"><i class="icon-signout"></i> ออกจากระบบ</a></li>
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
  <div class="modal-dialog" style="width: 460px;">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title"><i class="icon-edit"></i> เปลี่ยนรหัสผ่าน</h4>
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
          <button type="button" class="btn btn-success" id="btn_app_change_password">
              <i class="icon-save"></i> เปลี่ยนรหัสผ่าน
          </button>
        <button type="button" class="btn btn-danger" data-dismiss="modal">
            <i class="icon-remove"></i> ปิดหน้าต่าง
        </button>
      </div>
    </div>
  </div>
</div>

  </body>
</html>
