
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
    <link href="/static/css/font-awesome.min.css" rel="stylesheet">
    <link href="/static/css/font-awesome-ie7.min.css" rel="stylesheet">
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
                  <span class="icon-cogs"></span> จัดการข้อมูล <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li class="dropdown-header">SETTINGS</li>
                <li><a href="${request.route_url('admin_users')}"><i class="icon-calendar"></i> ทะเบียนผู้ใช้งาน</a></li>
                <!-- <li><a href="${request.route_url('mch_index')}"><i class="icon-user-md"></i> ทะเบียนบุคลากร</a></li> -->
                  <!-- <li class="divider"></li> -->
              </ul>
            </li>
          </ul>
          <ul class="nav navbar-nav pull-right">
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                    <span class="icon-cogs"></span> ตั้งค่า<b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li class="dropdown-header">${request.session['fullname']} [${request.session['hospcode']}]</li>
                <li><a href="#"><i class="icon-user"></i> ข้อมูลผู้ใช้งาน</a></li>
                <li><a href="#"><i class="icon-key"></i> เปลี่ยนรหัสผ่าน</a></li>
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

  </body>
</html>
