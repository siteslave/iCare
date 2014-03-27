<%inherit file="layout/admin.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ข้อมูลผู้ใช้งาน</li>
</ul>
<button class="btn btn-success" id="btn_new">
    <i class="icon-plus-sign"></i> เพิ่มผู้ใช้งาน
</button>
<button class="btn btn-primary">
    <i class="icon-refresh"></i> รีเฟรช
</button>

<table class="table table-bordered" id="tbl_list">
    <thead>
    <tr>
        <th>เลขบัตรประชาชน</th>
        <th>ชื่อเข้าใช้งาน</th>
        <th>ชื่อ - สกุล</th>
        <th>ตำแหน่ง</th>
        <th>หน่วยงาน</th>
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

<div class="modal fade" id="mdl_new_users">
  <div class="modal-dialog" style="width: 780px;">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title"><i class="icon-edit"></i> ข้อมูลผู้ใช้งาน</h4>
      </div>
      <div class="modal-body">
          <form action="#">
              <input type="hidden" id="txt_id" value="" />
              <div class="row">
                  <div class="col-md-6">
                    <label for="txt_username">ชื่อผู้ใช้งาน (ภาษาอังกฤษ) *</label>
                    <input type="text" id="txt_username" class="form-control" />
                  </div>
                  <div class="col-md-6">
                      <label for="txt_password">รหัสผ่าน *</label>
                      <input type="password" id="txt_password" class="form-control" />
                  </div>
              </div>
              <div class="row">
                  <div class="col-md-6">
                    <label for="txt_cid">เลขบัตรประชาชน *</label>
                    <input type="text" id="txt_cid" class="form-control" />
                  </div>

                  <div class="col-md-6">
                    <label for="txt_fullname">ชื่อ - สกุล *</label>
                    <input type="text" id="txt_fullname" class="form-control" />
                  </div>
              </div>

              <div class="row">
                  <div class="col-md-6">
                    <label for="txt_position">ตำแหน่ง</label>
                    <input type="text" id="txt_position" class="form-control" />
                  </div>
                  <div class="col-md-6">
                    <label for="sl_department">หน่วยงาน</label>
                      <select name="sl_department" id="sl_department" class="form-control">
                          <option value="">*</option>
                          % for v in hospitals:
                            <option value="${v['hospcode']}">${v['hospname']}</option>
                          % endfor
                      </select>
                  </div>
              </div>
              <div class="row">
                  <div class="col-md-3">
                      <label for="sl_user_type">ประเภท</label>
                      <select name="sl_user_type" id="sl_user_type" class="form-control">
                          <option value="0">ผู้ใช้งานทั่วไป</option>
                          <option value="1">Admin</option>
                      </select>
                  </div>
                  <div class="col-md-3">
                      <label for="sl_user_status">สถานะ</label>
                      <select name="sl_user_status" id="sl_user_status" class="form-control">
                          <option value="0">ระงับการใช้งาน</option>
                          <option value="1">เปิดใช้งาน</option>
                      </select>
                  </div>
              </div>
          </form>
      </div>
      <div class="modal-footer">
          <button type="button" class="btn btn-default" id="btn_save">
              <i class="icon-save"></i> บันทึก
          </button>
        <button type="button" class="btn btn-primary" data-dismiss="modal">
            <i class="icon-remove"></i> ปิดหน้าต่าง
        </button>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="mdl_change_password">
  <div class="modal-dialog" style="width: 460px;">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title"><i class="icon-edit"></i> เปลี่ยนรหัสผ่าน</h4>
      </div>
      <div class="modal-body">
          <form action="#">
              <label for="txt_chw_new">รหัสผ่านใหม่</label>
              <input type="text" class="form-control" id="txt_chw_new"/>

              <input type="hidden" id="txt_chw_id" value="" />
          </form>
      </div>
      <div class="modal-footer">
          <button type="button" class="btn btn-default" id="btn_do_change_password">
              <i class="icon-save"></i> เปลี่ยนรหัสผ่าน
          </button>
        <button type="button" class="btn btn-primary" data-dismiss="modal">
            <i class="icon-remove"></i> ปิดหน้าต่าง
        </button>
      </div>
    </div>
  </div>
</div>

<script src="/static/js/apps/admins.users.js"></script>