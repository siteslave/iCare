<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">คุณภาพการฝากครรภ์</li>
</ul>
<div class="alert alert-info alert-dismissable">
  <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
  <strong>หมายเหตุ!</strong> เฉพาะ Typearea 1 และ 3</div>
<form action="#" class="form-inline well well-sm">
    <label for="txt_query">เลขบัตรประชาชน</label>
    <input type="text" class="form-control" style="width: 220px;" data-type="number" placeholder="เลขบัตรประชาชน"/>
    <div class="btn-group">
        <button type="button" id="btn_search" class="btn btn-primary" rel="tooltip" title="ค้นหา">
            <i class="fa fa-search"></i> ค้นหา
        </button>
    </div>
    |
    <div class="btn-group" data-toggle="buttons">
        <label class="btn btn-primary" data-name="chk_filter" data-id="2">
            <input type="radio"><i class="fa fa-check"></i> ครบ
        </label>
        <label class="btn btn-default" data-name="chk_filter" data-id="3">
            <input type="radio"><i class="fa fa-minus"></i> ไม่ครบ
        </label>
        <label class="btn btn-success" data-name="chk_filter" data-id="1">
            <input type="radio"> <i class="fa fa-refresh"></i> ทั้งหมด
        </label>
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
        <th>จำนวน (ครั้ง)</th>
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

<script src="/static/js/apps/reports_anc_coverages.js"></script>