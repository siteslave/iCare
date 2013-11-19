<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ข้อมูลผู้ใช้งาน</li>
</ul>

<form action="#" class="well well-sm form-inline">
    <label for="txt_query">ค้นหา</label>
    <input type="text" id="txt_query" class="form-control" style="width: 240px;" placeholder="ชื่อ หรือ ชื่อผู้ใช้งาน" />
    <button type="button" class="btn btn-primary" id="btn_search">
        <i class="icon-search"></i> ค้นหา
    </button> |
    <button type="button" class="btn btn-success" id="btn_show_new">
        <i class="icon-plus-sign"></i> เพิ่มผู้ใช้งาน
    </button>
    <button type="button" id="btn_total" class="btn btn-primary pull-right" rel="tooltip" title="จำนวนทั้งหมด">
        <i class="icon-th-list"></i> จำนวนทั้งหมด <span id="spn_total"><strong>0</strong></span> คน
    </button>
</form>

<table class="table table-striped" id="tbl_list">
    <thead>
    <tr>
        <th>ชื่อผู้ใช้งาน</th>
        <th>เลขบัตรประชาขน</th>
        <th>ชื่อ - สกุล</th>
        <th>หน่วยงาน</th>
        <th>ตำแหน่ง</th>
        <th>สถานะ</th>
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


<div class="modal fade" id="mdl_new">
  <div class="modal-dialog" style="width: 788px;">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title">เพิ่มผู้ใช้งานใหม่</h4>
      </div>
      <div class="modal-body">
          <form action="#" class="form-inline">
              <input type="hidden" id="txt_id" value="" />
              <div class="row">
                  <div class="col-sm-6">
                      <label for="txt_username">ชื่อผู้ใช้งาน</label>
                      <input type="text" id="txt_username" class="form-control"/>
                  </div>
                  <div class="col-sm-6">
                      <label for="txt_username">รหัสผ่าน</label>
                      <input type="password" id="txt_password" class="form-control"/>
                  </div>
              </div>
              <div class="row">
                  <div class="col-sm-6">
                      <label for="txt_cid">เลขบัตรประชาชน</label>
                      <input type="text" id="txt_cid" class="form-control"/>
                  </div>
                  <div class="col-sm-6">
                      <label for="txt_fullname">ชื่อ-สกุล</label>
                      <input type="text" id="txt_fullname" class="form-control"/>
                  </div>
              </div>
              <div class="row">
                  <div class="col-sm-6">
                      <label for="txt_position">ตำแหน่ง</label>
                      <input type="text" id="txt_position" class="form-control"/>
                  </div>
                  <div class="col-sm-6">
                      <label for="txt_fullname">หน่วยงาน</label>
                      <select name="sl_owners" id="sl_hospcode" class="form-control">
                          <option value="">เลือกหน่วยงานสังกัด</option>
                            % for v in owners:
                                <option value="${v['hsub']}">${v['hsub']} ${v['name']}</option>
                            % endfor
                      </select>
                  </div>
              </div>
              <div class="row">
                  <div class="col-sm-4">
                      <label for="chk_is_active">ระงับใช้งาน</label>
                      <input type="checkbox" id="chk_is_active" />
                  </div>
              </div>
          </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-success" id="btn_save">
            <i class="icon-save"></i> บันทึกข้อมูล
        </button>
        <button type="button" class="btn btn-danger" data-dismiss="modal"><i class="icon-remove"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="mdl_changepass">
  <div class="modal-dialog" style="width: 480px;">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title"><i class="icon-key"></i> เปลี่ยนรหัสผ่าน</h4>
      </div>
      <div class="modal-body">
          <form action="#">
              <input type="hidden" id="txt_chw_id" value="" />
              <label for="txt_chw_username">ชื่อผู้ใช้งาน</label>
              <input type="text" class="form-control" id="txt_chw_username" disabled style="background-color: #ffffff;" />
              <label for="txt_chw_password1">รหัสผ่านใหม่</label>
              <input type="password" class="form-control" id="txt_chw_password1"/>
              <label for="txt_chw_password2">รหัสผ่านใหม่ (อีกครั้ง)</label>
              <input type="password" class="form-control" id="txt_chw_password2"/>
          </form>
      </div>
      <div class="modal-footer">
          <button type="button" class="btn btn-success" id="btn_chw_dochange">
              <i class="icon-save"></i> เปลี่ยนรหัสผ่าน
          </button>
        <button type="button" class="btn btn-danger" data-dismiss="modal"><i class="icon-remove"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>


<script src="/static/js/apps/users.js"></script>