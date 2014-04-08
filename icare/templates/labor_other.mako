<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">คนในเขตไปคลอดที่หน่วยบริการอื่น</li>
</ul>

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
              <div class="col-sm-3">
                      <select id="sl_hospitals" class="form-control">
                          % for v in owners:
                            <option value="${v['hospcode']}">${v['hospname']}</option>
                          % endfor
                      </select>
              </div>
              <div class="col-sm-2">
                  <div class="btn-group">
                      <button type="button" id="btn_process" class="btn btn-default" rel="tooltip" title="แสดงตามเงื่อนไข">
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
                <th>ครรภ์ที่</th>
                <th>วันที่คลอด</th>
                <th>ที่อยู่</th>
                <th>#</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td colspan="7">ระบุเงื่อนไขเพื่อค้นหา</td>
            </tr>
            </tbody>
        </table>

        <ul class="pagination" id="paging"></ul>
##
##<ul class="nav nav-tabs">
##    <li class="active">
##        <a href="#main" data-toggle="tab"><i class="fa fa-th-list"></i> รายการทั้งหมด</a>
##    </li>
##    <li>
##        <a href="#search" data-toggle="tab"><i class="fa fa-search"></i> ค้นหารายการ</a>
##    </li>
##</ul>
##
##<div class="tab-content">
##    <div class="tab-pane active" id="main">
##        <br/>
##
##
##    </div>
####    <div class="tab-pane" id="search">
####        <br/>
####        <form action="#" class="well well-sm form-inline">
####            <label for="txt_query">เลขบัตรประชาชน</label>
####            <input type="text" id="txt_anc_query" class="form-control" style="width: 240px;" placeholder="ระบุเลขบัตรประชาชน" />
####            <button type="button" class="btn btn-default" id="btn_anc_search">
####                <i class="fa fa-search"></i> ค้นหา
####            </button>
####        </form>
####
####        <table class="table table-bordered" id="tbl_anc_visit_list">
####            <thead>
####            <tr>
####                <th>วันที่</th>
####                <th>บันทึกโดย</th>
####                <th>ให้บริการโดย</th>
####                <th>ครรภ์ที่</th>
####                <th>ครั้งที่</th>
####                <th>อายุครรภ์ (สัปดาห์)</th>
####            </tr>
####            </thead>
####            <tbody>
####            <tr>
####                <td colspan="6">...</td>
####            </tr>
####            </tbody>
####        </table>
####
####        <ul class="pagination" id="paging_anc"></ul>
####    </div>
##</div>

<div class="modal fade" id="mdl_labor">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> รายละเอียดเกี่ยวกับการคลอด</h4>
      </div>
      <div class="modal-body">
        <!-- <div class="navbar navbar-default"> -->
            <form action="#" class="well well-sm form-inline">
                ชื่อ - สกุล <input type="text" disabled class="form-control" id="txt_labor_fullname" style="width: 250px;"/>
             <%doc>   วันเกิด <input type="text" disabled class="form-control" id="txt_labor_birth" style="width: 140px;"/></%doc>
                CID <input type="text" disabled class="form-control" id="txt_labor_cid" style="width: 200px;"/>
                ครรภ์ที่ <input type="text" disabled class="form-control" id="txt_labor_gravida" style="width: 50px;"/>
            </form>
        <!-- </div> -->
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
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->

<div class="modal fade" id="mdl_anc">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> ประวัติการฝากครรภ์</h4>
      </div>
      <div class="modal-body">
        <table class="table table-bordered" id="tbl_anc_visit_list">
            <thead>
            <tr>
                <th>วันที่</th>
                <th>บันทึกโดย</th>
                <th>ให้บริการโดย</th>
                <th>ครรภ์ที่</th>
##                <th>ครั้งที่</th>
                <th>อายุครรภ์ (สัปดาห์)</th>
                <th>ผลตรวจ</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td colspan="6">...</td>
            </tr>
            </tbody>
        </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->


<script src="/static/js/apps/labor_other.js"></script>