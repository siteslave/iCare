<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">เด็กดื่มนมแม่อย่างเดียว 6 เดียว</li>
</ul>
<div class="alert alert-warning alert-dismissable">
  <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
  <strong>หมายเหตุ!</strong> การคำนวณ ใช้วิธีการนับจำนวนครั้งที่สำรวจว่าดื่มนมแม่อย่างเดียว มากกว่า 2 ครั้งขึ้นไป (จากแฟ้ม NEWBORNCARE)
</div>

<form action="#" class="well well-sm">
    <div class="btn-group">
        <button type="button" id="btn_refresh" class="btn btn-success" rel="tooltip" title="Refresh">
            <i class="fa fa-refresh"></i> รีเฟรช
        </button>

        <button type="button" id="btn_process" class="btn btn-primary" rel="tooltip" title="ประมวลผลข้อมูล">
            <i class="fa fa-cogs"></i> ประมวลผล
        </button>

    </div>

    <button type="button" id="btn_total" class="btn btn-primary pull-right" rel="tooltip" title="จำนวนทั้งหมด">
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
        <th>ดื่มนำแม่อย่างเดียว (ครั้ง)</th>
        <th>ที่อยู่</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td colspan="6">...</td>
    </tr>
    </tbody>
</table>

<ul class="pagination" id="paging"></ul>

<script src="/static/js/apps/reports_milk.js"></script>