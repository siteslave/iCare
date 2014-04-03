
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Signin for iCare</title>
    <link href="/static/css/themes/simplex/bootstrap.min.css" rel="stylesheet">
    <link href="/static/css/font-awesome.min.css" rel="stylesheet">

    <link href="/static/css/signin.css" rel="stylesheet">
    <link href="/static/icheck/skins/square/red.css" rel="stylesheet">
    <script src="/static/js/jquery.js"></script>
    <script src="/static/icheck/icheck.min.js"></script>

      <script>
        $(function() {
            $('input[type="checkbox"]').iCheck({
                checkboxClass: 'icheckbox_square-red',
                radioClass: 'iradio_square-red'
            });
        });
      </script>
  </head>

  <body>

<div class="container">
    <div class="row">
        <div class="col-sm-6 col-md-4 col-md-offset-4">
            <h1 class="text-center login-title">ลงชื่อเข้าใช้งานโปรแกรม iCare</h1>
            <div class="account-wall">
                <img class="profile-img" src="https://lh5.googleusercontent.com/-b0-k99FZlyE/AAAAAAAAAAI/AAAAAAAAAAA/eu7opA4byxI/photo.jpg?sz=120"
                    alt="">
                <form class="form-signin" action="/signin" method="post">
                    <input type="hidden" name="csrf_token" value="${request.session.get_csrf_token()}"/>
                    <input type="text" name="username" class="form-control" placeholder="Username" required autofocus>
                    <input type="password" name="password" class="form-control" placeholder="Password" required>
                    <button class="btn btn-lg btn-success btn-block" type="submit">
                        Sign in
                        <i class="fa fa-lg fa-sign-in"></i>
                    </button>

                    <br/>
                    <input type="checkbox" checked id="isProcess" name="isProcess"/> ประมวลผลข้อมูลก่อนใช้งาน
                    <a href="#" class="need-help text-right">ยังไม่มีชื่อในระบบ/ลืมรหัสผ่าน? </a><span class="clearfix"></span>
                </form>
            </div>
        </div>
    </div>
</div>


  </body>
</html>