<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li><a href="/equipment">รายการครุภัณฑ์ทางการแพทย์</a></li>
  <li class="active">ข้อมูลการซ่อมบำรุง</li>
</ul>

<input type="hidden" id="txtId" value="${request.matchdict['id']}"/>

##<div class="navbar navbar-default">
    <form class="well well-sm form-inline" action="#">
        <div class="row">
            <div class="col-sm-4">
                <label for="">ชื่อครุภัณฑ์</label>
                <input id="txtEquipmentName" class="form-control" disabled style="width: 250px;" type="text"/>
            </div>
            <div class="col-sm-3">
                <label for="">เลขครุภัณฑ์</label>
                <input id="txtEquipmentDurableGoodsNumber" disabled class="form-control" type="text" />
            </div>
            <div class="col-sm-3">
                <label for="">Serial No.</label>
                <input id="txtEquipmentSerial" disabled class="form-control" type="text" />
            </div>
            <div class="col-sm-2">
                <button class="btn btn-success" type="button" id="btnNewService">
                    <i class="fa fa-plus-circle"></i> บันทึกส่งซ่อม
                </button>
            </div>
        </div>
    </form>
##</div>

<table class="table table-bordered" id="tbl_list">
    <thead>
    <tr>
        <th>วันที่ส่งซ่อม</th>
        <th>วันที่รับคืน</th>
        <th>บริษัทที่รับซ่อม</th>
        <th>ชื่อผู้ติดต่อ</th>
        <th>สถานะ</th>
        <th>ประเภทบริการ</th>
        <th>#</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>..</td>
        <td>..</td>
        <td>..</td>
        <td>..</td>
        <td>..</td>
        <td>..</td>
        <td>..</td>
    </tr>
    </tbody>
</table>

<ul class="pagination" id="paging"></ul>

<div class="modal fade" id="mdlNewEquipmentService">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-file-text-o"></i> เพิ่ม/แก้ไขข้อมูล</h4>
      </div>
      <div class="modal-body">
          <form action="#">
              <input type="hidden" id="txtServiceId" value=""/>
              <div class="row">
                  <div class="col-sm-6">
                    <label for="">วันที่ส่งซ่อม</label>
                    <div class="input-group date" data-type="date-picker">
                      <input type="text" id="txtServiceDate"  class="form-control"/>
                      <span class="input-group-addon"><i class="fa fa-th-list"></i></span>
                    </div>
                  </div>
                  <div class="col-sm-6">
                      <label for="">ประเภทส่งซ่อม</label>
                      <select class="form-control" id="slServiceType" required >
                          <option value="1">ซ่อมเอง</option>
                          <option value="2">Out Source</option>
                      </select>
                  </div>
              </div>

              <div class="row">
                  <div class="col-sm-6">
                      <label for="">สถานที่ส่งซ่อม</label>
                      <input type="text" class="form-control" id="txtCompany" required />
                  </div>
                  <div class="col-sm-6">
                      <label for="">ชื่อผู้ติดต่อ</label>
                      <input type="text" class="form-control" id="txtContactName" required />
                  </div>

              </div>

              <div class="row">
                  <div class="col-sm-6">
                      <label for="">โทรศัพท์</label>
                      <input type="tel" class="form-control" id="txtTelephone"/>
                  </div>
                  <div class="col-sm-6">
                      <label for="">อีเมล์</label>
                      <input type="email" class="form-control" id="txtEmail" />
                  </div>
              </div>

              <div class="row">
                  <div class="col-sm-6">
                      <label for="">สถานะซ่อม</label>
                      <select class="form-control" id="slServiceStatus" required >
                          <option value="1">ซ่อมเสร็จแล้ว</option>
                          <option value="2">อยู่ระหว่างการซ่อม</option>
                          <option value="2">ยกเลิกการซ่อม/แทงจำหน่าย</option>
                      </select>
                  </div>
                  <div class="col-sm-6">
                      <label for="">วันที่รับกลับ</label>
                      <div class="input-group date" data-type="date-picker">
                        <input type="text" id="txtReturnDate"  class="form-control"/>
                        <span class="input-group-addon"><i class="fa fa-th-list"></i></span>
                      </div>
                  </div>
              </div>
          </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" id="btnSave"><i class="fa fa-save"></i> บันทึกข้อมูล</button>
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<script src="/static/js/apps/equipment_service.js"></script>


