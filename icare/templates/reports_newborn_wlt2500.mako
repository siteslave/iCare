<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">เด็กน้ำหนักน้อยกว่า 2,500 กรัม</li>
</ul>

<form action="#" class="well well-sm form-inline">
    <label for="txt_query">ค้นหา</label>
    <input type="text" id="txt_query" class="form-control" style="width: 180px;"
            placeholder="เลขบัตรประชาชน" />
    <button type="button" id="btn_search" class="btn btn-primary" rel="tooltip" title="ค้นหา">
        <i class="icon-search"></i> ค้นหา
    </button>
    |
    <button type="button" id="btn_refresh" class="btn btn-success" rel="tooltip" title="Refresh">
        <i class="icon-search"></i> รีเฟรช
    </button>

    <button type="button" id="btn_total" class="btn btn-primary pull-right" rel="tooltip" title="จำนวนทั้งหมด">
            <i class="icon-th-list"></i> จำนวนทั้งหมด <span id="spn_total"><strong>0</strong></span> คน
        </button>

</form>



<table class="table table-striped" id="tbl_list">
    <thead>
    <tr>
        <th>เลขบัตรประชาชน</th>
        <th>ชื่อ-สกุล</th>
        <th>อายุ (ป-ด-ว)</th>
        <th>วันที่คลอด</th>
        <th>น้ำหนัก (กรัม)</th>
        <th>ที่อยู่</th>
        <th>#</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td colspan="7">...</td>
    </tr>
    </tbody>
</table>

<ul class="pagination" id="paging"></ul>


<div class="modal fade" id="mdl_newborn">
  <div class="modal-dialog" style="width: 780px;">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title"><i class="icon-edit"></i> ข้อมูลการคลอด</h4>
      </div>
      <div class="modal-body">
        <div class="navbar navbar-default">
            <form action="#" class="navbar-form">
                ชื่อ - สกุล <input type="text" disabled class="form-control" id="txt_fullname" style="width: 250px;"/>
                CID <input type="text" disabled class="form-control" id="txt_cid" style="width: 200px;"/>
                ครรภ์ที่ <input type="text" disabled class="form-control" id="txt_gravida" style="width: 50px;"/>
            </form>
        </div>
          <form action="#" class="form-inline">
              <div class="row">
                  <div class="col-lg-2">
                      <label for="">วันที่คลอด</label>
                      <input type="text" class="form-control" id="txt_bdate" disabled />
                  </div>
                  <div class="col-lg-2">
                      <label for="">เวลา</label>
                      <input type="text" class="form-control" id="txt_btime" disabled />
                  </div>
                  <div class="col-lg-3">
                      <label for="">CID มารดา</label>
                      <input type="text" class="form-control" id="txt_mother_cid" disabled />
                  </div>
                  <div class="col-lg-5">
                      <label for="">ชื่อ - สกุล มารดา</label>
                      <input type="text" class="form-control" id="txt_mother_name" disabled />
                  </div>
              </div>
              <div class="row">
                  <div class="col-lg-3">
                      <label for="">สถานที่คลอด</label>
                      <select id="sl_bplace" class="form-control" disabled >
                          <option value="">-*-</option>
                          <option value="1">โรงพยาบาล</option>
                          <option value="2">สถานีอนามัย</option>
                          <option value="3">บ้าน</option>
                          <option value="4">ระหว่างทาง</option>
                          <option value="5">อื่นๆ</option>
                      </select>
                  </div>
                  <div class="col-lg-2">
                      <label for="">รหัส</label>
                      <input type="text" class="form-control" id="txt_bhosp_code" disabled />
                  </div>
                  <div class="col-lg-7">
                      <label for="">สถานพยาบาลที่ทำคลอด</label>
                      <input type="text" class="form-control" id="txt_bhosp_name" disabled />
                  </div>
              </div>
              <div class="row">
                  <div class="col-lg-3">
                      <label for="">ลำดับที่</label>
                      <select id="sl_birthno" class="form-control" disabled>
                          <option value="">-*-</option>
                          <option value="1">คลอดเดี่ยว</option>
                          <option value="2">เป็นเด็กแฝดลำดับที่ 1</option>
                          <option value="3">เป็นเด็กแฝดลำดับที่ 2</option>
                          <option value="4">เป็นเด็กแฝดลำดับที่ 3</option>
                          <option value="5">เป็นเด็กแฝดลำดับที่ 4</option>
                      </select>
                  </div>
                  <div class="col-lg-3">
                      <label for="">วิธีคลอด</label>
                      <select id="sl_btype" class="form-control" disabled>
                          <option value="">-*-</option>
                          <option value="1">NORMAL</option>
                          <option value="2">CESAREAN</option>
                          <option value="3">VACUUM</option>
                          <option value="4">FORCEPS</option>
                          <option value="5">ท่าก้น</option>
                      </select>
                  </div>
                  <div class="col-lg-3">
                      <label for="">ผู้ทำคลอด</label>
                      <select id="sl_bdoctor" class="form-control" disabled>
                          <option value="">-*-</option>
                          <option value="1">แพทย์</option>
                          <option value="2">พยาบาล</option>
                          <option value="3">จนท. สาธารณสุข</option>
                          <option value="4">ผดุงครรภ์โบราณ</option>
                          <option value="5">คลอดเอง</option>
                          <option value="5">อื่นๆ</option>
                      </select>
                  </div>
                  <div class="col-lg-3">
                      <label for="">น้ำหนัก (g)</label>
                      <input type="text" id="txt_bweight" class="form-control" disabled />
                  </div>
              </div>
              <div class="row">
                  <div class="col-lg-3">
                      <label for="">ขาดออกซิเจน</label>
                      <select id="txt_asphyxia" class="form-control" disabled >
                          <option value="">-*-</option>
                          <option value="1">ขาด</option>
                          <option value="2">ไม่ขาด</option>
                          <option value="9">ไม่ทราบ</option>
                      </select>
                  </div>
                  <div class="col-lg-3">
                      <label for="">ได้รับ VIT K</label>
                      <select id="sl_vitk" class="form-control" disabled >
                          <option value="">-*-</option>
                          <option value="1">ได้รับ</option>
                          <option value="2">ไม่ได้รับ</option>
                          <option value="9">ไม่ทราบ</option>
                      </select>
                  </div>
                  <div class="col-lg-3">
                      <label for="">ตรวจ TSH</label>
                      <select id="sl_tsh" class="form-control" disabled >
                          <option value="">-*-</option>
                          <option value="1">ได้รับการตรวจ</option>
                          <option value="2">ไม่ได้ตรวจ</option>
                          <option value="9">ไม่ทราบ</option>
                      </select>
                  </div>
                  <div class="col-lg-3">
                      <label for="">ผล TSH</label>
                      <input type="text" class="form-control" id="txt_tshresult" disabled />
                  </div>
              </div>
          </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-dismiss="modal"><i class="icon-remove"></i> ปิดหน้าต่าง</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div>

<script src="/static/js/apps/reports_newborn_wlt2500.js"></script>