<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">คนในเขตไปคลอดที่หน่วยบริการอื่น</li>
</ul>

<ul class="nav nav-tabs">
    <li class="active">
        <a href="#main" data-toggle="tab"><i class="fa fa-th-list"></i> รายการทั้งหมด</a>
    </li>
    <li>
        <a href="#search" data-toggle="tab"><i class="fa fa-search"></i> ค้นหารายการ</a>
    </li>
</ul>

<div class="tab-content">
    <div class="tab-pane active" id="main">
        <br/>
        <form action="#" class="form-horizontal well well-sm" role="form">
            <div class="row">
              <div class="col-sm-3">
                  <div class="form-group">
                      <label for="txt_start_date" class="col-sm-4 control-label">คลอดตั้งแต่</label>
                      <div class="input-group date col-sm-7" data-type="date-picker">
                          <input type="text" id="txt_start_date"  class="form-control" placeholder="วว/ดด/ปปปป"/>
                          <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                      </div>
                  </div>
              </div>
              <div class="col-sm-2">
                  <div class="form-group">
                      <label for="txt_end_date" class="col-sm-1 control-label"> - </label>
                      <div class="input-group date col-sm-10" data-type="date-picker">
                          <input type="text" id="txt_end_date"  class="form-control" placeholder="วว/ดด/ปปปป"/>
                          <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                      </div>
                  </div>
              </div>
              <div class="col-sm-2">
                  <div class="btn-group">
                      <button type="button" id="btn_filter" class="btn btn-default" rel="tooltip" title="แสดงตามเงื่อนไข">
                          <i class="fa fa-search"></i> แสดงข้อมูล
                      </button>
                  </div>
              </div>
            </div>

         </form>

        <table class="table table-bordered" id="tbl_list">
            <thead>
            <tr>
                <th>เลขบัตรประชาขน</th>
                <th>ชื่อ - สกุล</th>
                <th>อายุ (ปี)</th>
                <th>ที่อยู่</th>
                <th>ประเภทการคลอด</th>
                <th>สถานที่คลอด</th>
                <th>หน่วยบริการที่บันทึก</th>
                <th>#</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td colspan="8">...</td>
            </tr>
            </tbody>
        </table>

        <ul class="pagination" id="paging"></ul>

    </div>
    <div class="tab-pane" id="search">
        <br/>
        <form action="#" class="well well-sm form-inline">
            <label for="txt_query">เลขบัตรประชาชน</label>
            <input type="text" id="txt_query" class="form-control" style="width: 240px;" placeholder="ระบุเลขบัตรประชาชน" />
            <button type="button" class="btn btn-default" id="btn_search">
                <i class="fa fa-search"></i> ค้นหา
            </button>
            <button type="button" id="btn_total" class="btn btn-primary pull-right" rel="tooltip" title="จำนวนทั้งหมด">
                <i class="fa fa-th-list"></i> จำนวนทั้งหมด <span id="spn_total"><strong>0</strong></span> คน
            </button>
        </form>

        <table class="table table-bordered" id="tbl_list">
            <thead>
            <tr>
                <th>เลขบัตรประชาขน</th>
                <th>ชื่อ - สกุล</th>
                <th>อายุ (ปี)</th>
                <th>ที่อยู่</th>
                <th>คลอดที่</th>
                <th>#</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td colspan="6">...</td>
            </tr>
            </tbody>
        </table>

        <ul class="pagination" id="paging"></ul>
    </div>
</div>

<script src="/static/js/apps/labor_other.js"></script>