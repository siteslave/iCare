<%inherit file="layout/default.mako" />
<%! import datetime %>
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">การดูแลแม่หลังคลอด</li>
</ul>

<ul class="nav nav-tabs">
  <li class="active"><a href="#home" data-toggle="tab"><i class="fa fa-windows"></i> ทะเบียนแม่หลังคลอด <span class="badge" id="spn_mch_total">0</span></a></li>
  <li><a href="#profile" data-toggle="tab"><i class="fa fa-briefcase"></i> ประวัติการรับบริการ</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="home">
      <br>
      <!-- <div class="navbar navbar-default"> -->
          <form class="form-inline well well-sm" action="#">
              <div class="row">
                  <div class="col-sm-3" style="width: 220px;">
                      <div class="form-group">
                          <label class="col-sm-3 control-label" for="txt_start_date">คลอดตั้งแต่</label>
                          <div data-type="date-picker" class="input-group date col-sm-9">
                              <input type="text" placeholder="วว/ดด/ปปปป" class="form-control" id="txt_start_date">
                              <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                          </div>
                      </div>
                  </div>
                  <div class="col-sm-2" style="width: 220px;">
                      <div class="form-group">
                          <label class="col-sm-2 control-label" for="txt_end_date"> ถึง </label>
                          <div data-type="date-picker" class="input-group date col-sm-9">
                              <input type="text" placeholder="วว/ดด/ปปปป" class="form-control" id="txt_end_date">
                              <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                          </div>
                      </div>
                  </div>
                  <div class="col-sm-2">
                      <div class="btn-group">
                          <button class="btn btn-primary" id="btn_search_by_birth" rel="tooltip" title="search">
                              <i class="fa fa-search"></i>
                          </button>
                          <button id="btn_refresh" class="btn btn-default" type="button"
                                  rel="tooltip" title="refresh">
                              <i class="fa fa-refresh"></i>
                          </button>
                      </div>

                  </div>
                  <div class="col-sm-5 visible-lg">
                      <div class="input-group">
                          <input type="text" title="" rel="tooltip" id="txt_query" placeholder="ระบุเลขบัตรประชาชน" class="form-control" data-original-title="ระบุคำค้นหา เช่น เลขบัตรประชาชน เป็นต้น">
                          <span class="input-group-btn">
                              <button id="btn_search" class="btn btn-primary" type="button">
                                  <i class="fa fa-search"></i> ค้นหา
                              </button>
                          </span>
                      </div>
                  </div>
              </div>

          </form>
      <!-- </div> -->

      <table class="table table-bordered" id="tbl_list">
          <thead>
          <tr>
              <th>เลขบัตรประชาชน</th>
              <th>ชื่อ - สกุล</th>
              <th>วันเกิด</th>
              <th class="visible-lg">อายุ (ป-ด-ว)</th>
              <th class="visible-lg">T</th>
              <th>ครรภ์ที่</th>
              <th class="visible-lg">วันที่คลอด</th>
              <th class="visible-lg">สถานบริการ</th>
              <th class="visible-lg">วิธีคลอด</th>
              <th>เยี่ยม (ครั้ง)</th>
              <th>#</th>
          </tr>
          </thead>
          <tbody>
          <tr>
             <td colspan="11">ไม่พบรายการ</td>
          </tr>
          </tbody>
      </table>
      <ul class="pagination" id="paging"></ul>

  </div>

    <div class="tab-pane" id="profile">
      <br>
      <!-- <div class="navbar navbar-default"> -->
          <form action="#" class="form-inline well well-sm">
              <input type="text" class="form-control" style="width: 250px;"
                     placeholder="ระบุเลขบัตรประชาชน" id="txt_query_visit"
                      rel="tooltip" title="ระบุเลขบัตรประชาชน 13 หลัก"/>
              <label for="">ครรภ์ที่</label>
              <input type="text" class="form-control" style="width: 100px;"
                     placeholder="1" id="txt_gravida" />
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
              <th>ครรภ์ที่</th>
              <th>สถานที่</th>
              <th>ผลตรวจ</th>
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

<div class="modal fade" id="mdl_postnatal">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> รายละเอียดเกี่ยวกับการตั้งครรภ์</h4>
      </div>
      <div class="modal-body">
        <!-- <div class="navbar navbar-default"> -->
            <form action="#" class="form-inline well well-sm">
                ชื่อ - สกุล <input type="text" disabled class="form-control" id="txt_fullname" style="width: 250px;"/>
             <%doc>   วันเกิด <input type="text" disabled class="form-control" id="txt_labor_birth" style="width: 140px;"/></%doc>
                CID <input type="text" disabled class="form-control" id="txt_cid" style="width: 200px;"/>
                ครรภ์ที่ <input type="text" disabled class="form-control" id="txt_postnatal_gravida" style="width: 50px;"/>
            </form>
        <!-- </div> -->
        <table class="table table-bordered" id="tbl_postnatal_list">
            <thead>
            <tr>
               <th>วันที่</th>
               <th>สถานบริการ</th>
               <th>ผลตรวจ</th>
            </tr>
            </thead>
            <tbody></tbody>
        </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->

<div class="modal fade" id="mdl_labor">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> รายละเอียดเกี่ยวกับการคลอด</h4>
      </div>
      <div class="modal-body">
##        <div class="navbar navbar-default">
            <form action="#" class="form-inline well well-sm">
                ชื่อ - สกุล <input type="text" disabled class="form-control" id="txt_labor_fullname" style="width: 250px;"/>
             <%doc>   วันเกิด <input type="text" disabled class="form-control" id="txt_labor_birth" style="width: 140px;"/></%doc>
                CID <input type="text" disabled class="form-control" id="txt_labor_cid" style="width: 200px;"/>
                ครรภ์ที่ <input type="text" disabled class="form-control" id="txt_labor_gravida" style="width: 50px;"/>
            </form>
##        </div>
           <form action="#">
                <fieldset>
                    <legend>ข้อมูลการคลอด</legend>
                    <div class="row">
                        <div class="col-lg-2">
                             <div class="form-group">
                                <label for="txt_labor_bdate">วันที่คลอด</label>
                                <input type="text" disabled class="form-control" id="txt_labor_bdate"/>
                            </div>
                        </div>
                        <div class="col-lg-3">
                             <div class="form-group">
                                <label for="">ประเภทสถานที่</label>
                                 <select id="sl_bplace" class="form-control" disabled>
                                     <option value="1">โรงพยาบาล</option>
                                     <option value="2">สถานีอนามัย</option>
                                     <option value="3">บ้าน</option>
                                     <option value="4">ระหว่างทาง</option>
                                     <option value="5">อื่นๆ</option>
                                 </select>
                            </div>
                        </div>
                        <div class="col-lg-2">
                             <div class="form-group">
                                <label for="txt_labor_hospcode">รหัส</label>
                                <input type="text" disabled class="form-control" id="txt_labor_hospcode"/>
                            </div>
                        </div>
                        <div class="col-lg-5">
                             <div class="form-group">
                                <label for="txt_labor_hospname">สถานที่ทำคลอด</label>
                                <input type="text" disabled class="form-control" id="txt_labor_hospname"/>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-lg-2">
                             <div class="form-group">
                                <label for="">รหัส</label>
                                <input type="text" disabled class="form-control" id="txt_labor_diagcode"/>
                            </div>
                        </div>
                        <div class="col-lg-10">
                            <div class="form-group">
                                <label for="">คำอธิบายการวินิจฉัย</label>
                                <input type="text" disabled class="form-control" id="txt_labor_diagname"/>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-lg-3">
                            <label for="sl_labor_btype">วิธีการคลอด</label>
                            <select id="sl_labor_btype" class="form-control" disabled>
                                <option value="1">NORMAL</option>
                                <option value="2">CESAREAN</option>
                                <option value="3">VACUUM</option>
                                <option value="4">FORCEPS</option>
                                <option value="5">ท่ากัน</option>
                                <option value="6">ABORTION</option>
                            </select>
                        </div>
                        <div class="col-lg-3">
                            <label for="sl_labor_bdoctor">ประเภทผู้ทำคลอด</label>
                            <select id="sl_labor_bdoctor" class="form-control" disabled>
                                <option value="1">แพทย์</option>
                                <option value="2">พยาบาล</option>
                                <option value="3">จนท.สาธารณสุข</option>
                                <option value="4">ผดุงครรภ์โบราณ</option>
                                <option value="5">คลอดเอง</option>
                                <option value="6">อื่นๆ</option>
                            </select>
                        </div>
                        <div class="col-lg-3">
                            <label for="">เกิดมีชีพ</label>
                            <input type="text" class="form-control" id="txt_labor_lborn" disabled/>
                        </div>
                        <div class="col-lg-3">
                            <label for="">เกิดไร้ชีพ</label>
                            <input type="text" class="form-control" id="txt_labor_sborn" disabled/>
                        </div>
                    </div>
                </fieldset>
            </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
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
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<script src="/static/js/apps/mch.js"></script>