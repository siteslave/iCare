<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li><a href="${request.route_url('uploads')}">อัปโหลดไฟล์</a></li>
  <li class="active">สถานะอัปโหลด</li>
</ul>

<div class="panel panel-info" style="width: 480px;">
  <div class="panel-heading">
    <h3 class="panel-title"><i class="icon-cloud-upload"></i> ผลการอัปโหลดไฟล์</h3>
  </div>
    <br/><p class="text-center text-muted"><span class="icon-info"></span>
    ${request.session.pop_flash()[0]}.</p>
    <br/>
</div>

##<a href="${request.route_url('uploads')}" class="btn btn-success">
##    <span class="icon-home"></span> กลับหน้าอัปโหลดไฟล์
##</a>