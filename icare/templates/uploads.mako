<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">อัปโหลดไฟล์</li>
</ul>
<div class="navbar">
    <form action="/uploads" method="post" enctype="multipart/form-data" class="navbar-form" id="frm_upload">
        <input type="text" class="form-control" disabled
               style="width: 300px; background-color: white;"
                placeholder="เลือกไฟล์..." id="txt_file_name" />
        <input type="file" id="file" name="file" />
        <button type="button" class="btn btn-success" id="btn_select_file">
            <i class="icon-paper-clip"></i> เลือกไฟล์...
        </button>
        <button type="submit" class="btn btn-primary" id="btn_upload">
            <i class="icon-upload"></i> อัปโหลดไฟล์
        </button>
    </form>
</div>

<script charset="utf-8" src="/static/js/apps/uploads.js"></script>