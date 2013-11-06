<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">สถานะอัปโหลด</li>
</ul>

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title"><i class="icon-cloud-upload"></i> ผลการอัปโหลดไฟล์</h3>
  </div>
  ${request.session.pop_flash()[0]}
</div>

<a href="${request.route_url('uploads')}" class="btn btn-default">
    <i class="icon-home"></i> กลับหน้าอัปโหลดไฟล์
</a>