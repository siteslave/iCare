<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ฝากครรภ์เมื่ออายุครรภ์ <= 12 สัปดาห์</li>
</ul>
<div class="alert alert-info alert-dismissable">
  <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
  <strong>หมายเหตุ!</strong> เฉพาะ Typearea 1 และ 3</div>
<form class="form-inline well well-sm" action="#">
    <button type="button" id="btn_do_process" class="btn btn-primary" rel="tooltip" title="ประมวลผลข้อมูล">
        <i class="fa fa-refresh"></i> ประมวลผลข้อมูลใหม่
    </button>
    <button type="button" id="btn_list_total" class="btn btn-primary disabled" rel="tooltip" title="จำนวนทั้งหมด">
        <i class="fa fa-th-list"></i> จำนวนทั้งหมด <span id="spn_total"><strong>0</strong></span> คน
    </button>
</form>
<table class="table table-bordered" id="tbl_list">
    <thead>
    <tr>
        <th>เลขบัตรประชาชน</th>
        <th>ชื่อ-สกุล</th>
        <th>วันเกิด</th>
        <th>อายุ (ป-ด-ว)</th>
        <th class="visible-lg">ที่อยู่</th>
        <th>ฝากครรภ์</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td colspan="6">...</td>
    </tr>
    </tbody>
</table>

<ul class="pagination" id="paging"></ul>

<div class="modal fade" id="mdl_visit_anc">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> ประวัติการรับบริการฝากครรภ์</h4>
      </div>
      <div class="modal-body">
        <table class="table table-bordered" id="tbl_anc_visit">
            <thead>
            <tr>
               <th>#</th>
               <th>วันที่</th>
               <th>อายุครรภ์ <br /> (สัปดาห์)</th>
               <th>บันทึกโดย</th>
               <th>สถานที่ตรวจ</th>
            </tr>
            </thead>
            <tbody></tbody>
        </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<script src="/static/js/apps/reports_anc_12ws.js"></script>