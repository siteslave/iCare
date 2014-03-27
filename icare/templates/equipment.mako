<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">รายการครุภัณฑ์ทางการแพทย์</li>
</ul>
<!-- <div class="navbar navbar-default"> -->
    <form action="#" class="well well-sm">
        <div class="row">
            <div class="col-sm-4">
                <div class="input-group">
                    <input type="text" class="form-control" id="txtQuery" placeholder="ค้นหารายการ...">
                    <span class="input-group-btn">
                        <button class="btn btn-primary" id="btnDoSearch" type="button"><i class="fa fa-search"></i> ค้นหา</button>
                    </span>
                </div>
            </div>
            <div class="col-sm-8">
                <div class="btn-group pull-right">
                    <button class="btn btn-success" type="button" id="btnNewEquipment">
                        <i class="fa fa-plus-circle"></i> ลงทะเบียน
                    </button>
                    <button class="btn btn-default" type="button" id="btnRefresh">
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
        <th>ชื่อครุภัณฑ์</th>
        <th>Serial No.</th>
        <th>เลขครุภัณฑ์</th>
        <th>วันที่ซื้อ</th>
        <th>สถานะ</th>
        <th>#</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    </tr>
    </tbody>
</table>

<ul class="pagination" id="paging"></ul>

<div class="modal fade" id="mdlNewEquipment">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white">เพิ่ม/แก้ไขข้อมูล</h4>
      </div>
      <div class="modal-body">
          <form action="#">
              <fieldset>
                <input type="hidden" id="txtId" value=""/>
              <label for="">ชื่อครุภัณฑณ์</label>
              <input type="text" class="form-control" id="txtName" required />
              <label for="">Serial Number</label>
              <input type="text" class="form-control" id="txtSerialNumber"/>
              <label for="">รหัสครุภัณฑณ์</label>
              <input type="text" class="form-control" id="txtDurableGoodsNumber" required />
              <label for="">วันที่ซื้อ</label>
              <div class="input-group date" data-type="date-picker">
                <input type="text" id="txtPurchaseDate"  class="form-control"/>
                <span class="input-group-addon"><i class="fa fa-th-list"></i></span>
              </div>
              <label for="">สถานะปัจจุบัน</label>
              <select class="form-control" name="slStatus" id="slStatus" required >
                  <option value="1">พร้อมใช้งาน</option>
                  <option value="2">อยู่ระหว่างซ่อมแซม</option>
                  <option value="3">แทงจำหน่าย</option>
              </select>
              </fieldset>
          </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" id="btnSave"><i class="fa fa-save"></i> บันทึกข้อมูล</button>
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<script src="/static/js/apps/equipment.js"></script>