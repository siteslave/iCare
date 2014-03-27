<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ทะเบียนเยี่ยมแม่หลังคลอด</li>
</ul>

<form action="#" class="well well-sm form-horizontal" role="form">
    <div class="row">
        <div class="col-sm-4">
            <div class="form-group">
                <label for="txt_start_date" class="col-sm-7 control-label">ครบกำหนดฝากครรภ์ ตั้งแต่</label>
                <div class="input-group date col-sm-5" data-type="date-picker">
                    <input type="text" id="txt_start_date"  class="form-control" placeholder="วว/ดด/ปปปป"/>
                    <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                </div>
            </div>
        </div>
        <div class="col-sm-2">
            <div class="form-group">
                <label for="txt_end_date" class="col-sm-2 control-label"> - </label>
                <div class="input-group date col-sm-9" data-type="date-picker">
                    <input type="text" id="txt_end_date"  class="form-control" placeholder="วว/ดด/ปปปป"/>
                    <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                </div>
            </div>
        </div>
        <div class="col-sm-3">
            <div class="btn-group">
                <button type="button" id="btn_filter" class="btn btn-default" rel="tooltip" title="แสดงตามเงื่อนไข">
                    <i class="fa fa-search"></i> แสดง
                </button>
                <button type="button" id="btn_refresh" class="btn btn-success" rel="tooltip" title="แสดงทั้งหมด">
                    <i class="fa fa-refresh"></i> รีเฟรช
                </button>
            </div>
        </div>
        <div class="col-sm-3">
                <button type="button" class="btn btn-primary pull-right" id="btn_process">
                    <i class="fa fa-refresh"></i> ประมวลผล
                </button>
        </div>
    </div>
    
##    |
##    <input type="text" id="txt_query" class="form-control" style="width: 180px;"
##            placeholder="เลขบัตรประชาชน" />
##    <button type="button" id="btn_search" class="btn btn-primary" rel="tooltip" title="ค้นหา">
##        <i class="fa fa-search"></i> ค้นหา
##    </button>

    
</form>

<div class="alert alert-warning alert-dismissable">
  <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
  <strong>หมายเหตุ!</strong> สีแดง หมายถึง วันที่ครบกำหนดเยี่ยม (โดยการคำนวณจากวันที่คลอด) สีเขียว หมายถึง วันที่เราเยี่ยม.
 [เฉพาะ Typearea 1, 3]</div>

<table class="table table-bordered" id="tbl_list">
    <thead>
    <tr>
        <th>เลขบัตรประชาชน</th>
        <th>ชื่อ-สกุล</th>
        <th>อายุ (ปี)</th>
        <th>วันที่คลอด</th>
        <th>ครั้งที่ 1</th>
        <th>ครั้งที่ 2</th>
        <th>ครั้งที่ 3</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td colspan="7">...</td>
    </tr>
    </tbody>
</table>

<ul class="pagination" id="paging"></ul>

<script src="/static/js/apps/reports_mch.js"></script>