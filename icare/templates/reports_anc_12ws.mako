<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ฝากครรภ์เมื่ออายุครรภ์ <= 12 สัปดาห์</li>
</ul>
<div class="alert alert-info alert-dismissable">
  <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
  <strong>หมายเหตุ!</strong> เฉพาะ Typearea 1 และ 3</div>
<form class="form-inline well well-sm" action="#">
    <button type="button" id="btn_do_process" class="btn btn-danger" rel="tooltip" title="ประมวลผลข้อมูล">
        <i class="icon-refresh"></i> ประมวลผลข้อมูลใหม่
    </button>
    <button type="button" id="btn_list_total" class="btn btn-primary disabled" rel="tooltip" title="จำนวนทั้งหมด">
        <i class="icon-th-list"></i> จำนวนทั้งหมด <span id="spn_total"><strong>0</strong></span> คน
    </button>
</form>
<table class="table table-striped" id="tbl_list">
    <thead>
    <tr>
        <th>เลขบัตรประชาชน</th>
        <th>ชื่อ-สกุล</th>
        <th>วันเกิด</th>
        <th>อายุ (ป-ด-ว)</th>
        <th>ที่อยู่</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td colspan="5">...</td>
    </tr>
    </tbody>
</table>

<ul class="pagination" id="paging"></ul>

<script src="/static/js/apps/reports_anc_12ws.js"></script>