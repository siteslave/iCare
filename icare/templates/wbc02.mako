<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ทะเบียนเด็ก 0-2 ปี</li>
</ul>

<ul class="nav nav-tabs">
  <li class="active"><a href="#home" data-toggle="tab"><i class="fa fa-windows"></i> ทะเบียนเด็ก 0-2 ปี <span class="badge" id="spn_total">0</span></a></li>
  <li><a href="#profile" data-toggle="tab"><i class="fa fa-briefcase"></i> ประวัติการรับวัคซีน</a></li>
</ul>
<div class="tab-content">
    <div class="tab-pane active" id="home">
        <br>
        <!-- <div class="navbar navbar-default"> -->
      <form action="#" class="form-horizontal well well-sm" role="form">
        <div class="row">
          <div class="col-sm-2">
              <div class="form-group">
                  <label for="txt_start_date" class="col-sm-3 control-label">เกิด</label>
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
          <div class="col-sm-4">
                <select id="sl_villages" class="form-control">
                    <option value="">ทุกหมู่บ้านในเขตรับผิดชอบ</option>
                    % for v in villages:
                            <option value="${v['vid']}">หมู่ ${v['vid'][6:8]} ${v['name']}</option>
                    % endfor
                </select>
                
          </div>
          <div class="col-sm-2">
              <div class="btn-group">
                  <button type="button" id="btn_filter" class="btn btn-primary" rel="tooltip" title="แสดงตามเงื่อนไข">
                      <i class="fa fa-search"></i> แสดง
                  </button>
                  <button type="button" id="btn_refresh" class="btn btn-default" rel="tooltip" title="แสดงทั้งหมด">
                      <i class="fa fa-refresh"></i> รีเฟรช
                  </button>
              </div>
          </div>
        </div>
            
      </form>
        <!-- </div> -->
        <table class="table table-bordered" id="tbl_list">
            <thead>
            <tr>
                <th>เลขบัตรประชาชน</th>
                <th>ชื่อ-สกุล</th>
                <th class="hidden-md hidden-sm">วันเกิด</th>
                <th>อายุ (ป-ด-ว)</th>
                <th>เพศ</th>
                <th class="hidden-md hidden-sm">ที่อยู่</th>
                <th>พัฒนาการ</th>
                <th>% วัคซีน</th>
                <th></th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td colspan="9">กรุณากำหนดเงื่อนไข</td>
            </tr>
            </tbody>
        </table>

         <ul class="pagination" id="paging"></ul>

        <div class="alert alert-warning">
          <button type="button" class="close" data-dismiss="alert">&times;</button>
          <strong>หมายเหตุ!</strong> ข้อมูลอ้างอิงจาก Typearea เท่ากับ 1 และ 3 เท่านั้น
        </div>

    </div>
    <div class="tab-pane" id="profile">
         <br>
      <!-- <div class="navbar navbar-default"> -->
          <form action="#" class="form-inline well well-sm">
              <input type="text" class="form-control" style="width: 250px;"
                     placeholder="ระบุเลขบัตรประชาชน" id="txt_query_visit"
                      rel="tooltip" title="ระบุเลขบัตรประชาชน 13 หลัก"/>
              <button type="button" class="btn btn-primary" id="btn_search_visit">
                  <i class="fa fa-search"></i> ค้นหา
              </button>
          </form>
      <!-- </div> -->
      <table class="table table-bordered" id="tbl_visit_list">
          <thead>
          <tr>
              <th>#</th>
              <th>วันที่</th>
              <th>ชื่อวัคซีน</th>
              <th>สถานที่ฉีด</th>
              <th>นัดครั้งต่อไป</th>
          </tr>
          </thead>
          <tbody>
          <tr>
             <td colspan="5">ไม่พบรายการ</td>
          </tr>
          </tbody>
      </table>
    </div>
</div>

<div class="modal fade" id="mdl_vaccines">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> ประวัติการได้รับวัคซีน</h4>
      </div>
      <div class="modal-body">
        <table class="table table-bordered" id="tbl_vaccines_list">
            <thead>
            <tr>
               <th>ชื่อวัคซีน</th>
               <th>วันที่ฉีด</th>
               <th>สถานที่ฉีด</th>
            </tr>
            </thead>
            <tbody> </tbody>
        </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="mdl_nutrition">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> ประวัติการตรวจพัฒนาการ</h4>
      </div>
      <div class="modal-body">
        <table class="table table-bordered" id="tbl_nutrition">
            <thead>
            <tr>
               <th>#</th>
               <th>วันที่</th>
               <th>สถานที่ตรวจ</th>
               <th>น้ำหนัก (กก.)</th>
               <th>ส่วนสูง (ซม.)</th>
               <th>พัฒนาการ</th>
               <th>อาหาร</th>
            </tr>
            </thead>
            <tbody></tbody>
        </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="mdl_appointment">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> ข้อมูลการนัดครั้งต่อไป</h4>
      </div>
      <div class="modal-body">
        <table class="table table-bordered" id="tbl_appoint_list">
            <thead>
            <tr>
               <th>#</th>
               <th>วันที่</th>
               <th>กิจกรรมที่นัด</th>
               <th>รหัสโรคที่นัด</th>
            </tr>
            </thead>
            <tbody></tbody>
        </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<script src="/static/js/apps/wbc02.js"></script>