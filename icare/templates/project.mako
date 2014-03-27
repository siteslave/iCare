<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">โครงการ</li>
</ul>

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
                    <button class="btn btn-success" type="button" id="btnNewProject">
                        <i class="fa fa-plus-circle"></i> ลงทะเบียน
                    </button>
                    <button class="btn btn-default" type="button" id="btnRefresh">
                        <i class="fa fa-refresh"></i> รีเฟรช
                    </button>
                </div>
            </div>
        </div>
    </form>

<table class="table table-bordered" id="tbl_list">
    <thead>
    <tr>
        <th>ชื่อโครงการ</th>
        <th>วันที่เริ่ม</th>
        <th>วันที่สิ้นสุด</th>
        <th>งบประมาณ</th>
        <th>จำนวน (บาท)</th>
        <th>ผู้รับผิดชอบ</th>
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
        <td>...</td>
    </tr>
    </tbody>
</table>

<ul class="pagination" id="paging"></ul>

<div class="modal fade" id="mdlNewProject">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-file-text-o"></i> เพิ่ม/แก้ไขข้อมูล</h4>
      </div>
      <div class="modal-body">
          <div class="panel panel-default">
            <div class="panel-heading">ข้อมูลโครงการ</div>
            <div class="panel-body">
              <form action="#">
                <input type="hidden" id="txtId" value=""/>
                <label for="">ชื่อโครงการ</label>
                <input type="text" class="form-control" id="txtName" required />
                <div class="row">
                    <div class="col-sm-6">
                        <label for="">ประเภทโครงการ</label>
                        <select class="form-control" id="slClassify">
                            <option value="1">โครงการทั่วไป</option>
                            <option value="2">โครงการพิเศษ</option>
                        </select>
                    </div>
                    <div class="col-sm-3">
                        <label for="">วันที่เริ่ม</label>
                        <div class="input-group date" data-type="date-picker">
                          <input type="text" id="txtStartDate"  class="form-control"/>
                          <span class="input-group-addon"><i class="fa fa-th-list"></i></span>
                        </div>
                    </div>
                    <div class="col-sm-3">
                        <label for="">วันที่สิ้นสุด</label>
                        <div class="input-group date" data-type="date-picker">
                          <input type="text" id="txtEndDate"  class="form-control"/>
                          <span class="input-group-addon"><i class="fa fa-th-list"></i></span>
                        </div>
                    </div>
                </div>
                  <div class="row">
                      <div class="col-sm-6">
                          <label for="">แผนการปฏิบัติงาน</label>
                          <textarea id="txtPlan" rows="4" class="form-control"></textarea>
                      </div>
                      <div class="col-sm-6">
                          <label for="">ตัวชี้วัด</label>
                          <textarea id="txtIndicators" rows="4" class="form-control"></textarea>
                      </div>
                  </div>
                <div class="row">
                    <div class="col-sm-8">
                        <label for="">แหล่งงบประมาณ</label>
                        <input type="text" class="form-control" id="txtBudgetsSource" />
                    </div>
                    <div class="col-sm-4">
                        <label for="">จำนวน (บาท)</label>
                        <input type="text" class="form-control" data-type="number" id="txtBudgetsAmount" />
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-12">
                        <label for="">ผู้รับผิดชอบโครงการ</label>
                        <input type="text" class="form-control" id="txtProjectManager" required/>
                    </div>
                </div>
            </form>
          </div>
            <div class="panel-footer">
                <button type="button" class="btn btn-primary" id="btnSave"><i class="fa fa-save"></i> บันทึกข้อมูล</button>
                <button type="button" class="btn btn-default" data-dismiss="modal"><i class="fa fa-times"></i> ยกเลิก</button>
            </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="mdlProblemReport">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-file-text-o"></i> รายงานปัญหาการการปฏิบัติงาน</h4>
      </div>
      <div class="modal-body">
          <div class="panel panel-default">
            <div class="panel-heading">ข้อมูล</div>
            <div class="panel-body">
              <form action="#">
                <input type="hidden" id="txtReportId" />
                <input type="hidden" id="txtProjectId" />
                <div class="row">
                    <div class="col-sm-6">
                        <label for="">ประเภทของปัญหา</label>
                        <select class="form-control" id="slReportClassify">
                            <option value="1">ด้านงบประมาณ</option>
                            <option value="2">ศักยภาพในการปฏิบัติงาน</option>
                            <option value="3">ความพร้อมของบุคลากร</option>
                        </select>
                    </div>
                    <div class="col-sm-3">
                        <label for="">วันที่รายงาน</label>
                        <div class="input-group date" data-type="date-picker">
                          <input type="text" id="txtReportDate"  class="form-control"/>
                          <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                        </div>
                    </div>
                    <div class="col-sm-3">
                        <label for="">วันที่แก้ไข</label>
                        <div class="input-group date" data-type="date-picker">
                          <input type="text" id="txtReportResolveDate"  class="form-control"/>
                          <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-sm-12">
                        <label for="">รายละเอียด</label>
                        <textarea id="txtReportDesc" rows="4" class="form-control"></textarea>
                    </div>
                </div>
            </form>
          </div>
            <div class="panel-footer">
                <button type="button" class="btn btn-primary" id="btnSaveReport"><i class="fa fa-save"></i> บันทึกข้อมูล</button>
                <button type="button" class="btn btn-default" data-dismiss="modal"><i class="fa fa-times"></i> ยกเลิก</button>
            </div>
        </div>
      </div>
    </div>
  </div>
</div>

<script src="/static/js/apps/projects.js"></script>