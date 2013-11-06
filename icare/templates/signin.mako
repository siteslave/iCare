
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Signin for iCare</title>
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <link href="/static/css/signin.css" rel="stylesheet">
  </head>

  <body>

    <div class="container">

      <form class="form-signin" action="/signin" method="post">
        <h2 class="form-signin-heading">Please sign in</h2>
          <input type="hidden" name="csrf_token" value="${request.session.get_csrf_token()}"/>
        <input type="text" name="username" class="input-block-level"
               placeholder="Username" autofocus autocomplete="off" style="width: 280px;">
        <input type="password" name="password" class="input-block-level"
               placeholder="Password" autocomplete="off" style="width: 280px;">
        <button class="btn btn-large btn-primary btn-block" type="submit">Sign in</button>
      </form>

    </div> <!-- /container -->

  </body>
</html>