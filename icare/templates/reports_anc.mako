<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">หญิงตั้งครรภ์ที่ครบกำหนดฝากครรภ์</li>
</ul>

<!-- <div class="navbar navbar-default"> -->
    <form action="#" class="well well-sm form-horizontal" role="form">
    <div class="row">
        <div class="col-sm-2">
            <div class="form-group">
                <label for="txt_start_date" class="col-sm-3 control-label">ตั้งแต่</label>
                <div class="input-group date col-sm-9" data-type="date-picker">
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
        <div class="col-sm-1">
            <div class="btn-group">
                <button type="button" id="btn_filter" class="btn btn-primary" rel="tooltip" title="แสดงตามเงื่อนไข">
                    <i class="fa fa-search"></i>
                </button>
            </div>
        </div>
        <div class="col-sm-4">
            <div class="input-group">
                <input type="text" id="txt_query" class="form-control" placeholder="เลขบัตรประชาชน" />
                <span class="input-group-btn">
                    <button type="button" id="btn_search" class="btn btn-default" rel="tooltip" title="ค้นหา">
                        <i class="fa fa-search"></i>
                    </button>
                </span>
            </div>
        </div>
        <div class="col-sm-3">
            <div class="btn-group pull-right">
                <button type="button" class="btn btn-primary" id="btn_process">
                    <i class="fa fa-refresh"></i> ประมวลผล
                </button>
                <button type="button" id="btn_refresh" class="btn btn-default" rel="tooltip" title="แสดงทั้งหมด">
                    <i class="fa fa-refresh"></i>
                </button>
            </div>
            
        </div>
    </div>

    
</form>
<!-- </div> -->

<div class="alert alert-warning alert-dismissable">
  <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
  <strong>หมายเหตุ!</strong> สีแดง หมายถึง วันที่ครบกำหนดฝากครรภ์ (โดยการคำนวณจากวันที่รับบริการ) สีเขียว หมายถึง วันที่ฝากครรภ์ในหน่วยบริการ. [เฉพาะ Typearea 1, 3]
</div>
<table class="table table-bordered" id="tbl_list">
    <thead>
    <tr>
        <th>เลขบัตรประชาชน</th>
        <th>ชื่อ-สกุล</th>
        <th>อายุ (ปี)</th>
        <th>ครั้งที่ 1</th>
        <th>ครั้งที่ 2</th>
        <th>ครั้งที่ 3</th>
        <th>ครั้งที่ 4</th>
        <th>ครั้งที่ 5</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td colspan="8">...</td>
    </tr>
    </tbody>
</table>

<ul class="pagination" id="paging"></ul>

<script src="/static/js/apps/reports_anc.js"></script>