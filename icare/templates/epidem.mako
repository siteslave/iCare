<%inherit file="layout/default.mako" />

<%! import datetime %>
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ข้อมูลระบาดวิทยา</li>
</ul>

<ul class="nav nav-tabs">
  <li class="active"><a href="#home" data-toggle="tab"><i class="icon-windows"></i> ทะเบียนผู้ป่วย <span class="badge" id="spn_total">0</span></a></li>
  <li><a href="#profile" data-toggle="tab"><i class="icon-map-marker"></i> ระบบ GIS</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="home">
      <br>
      <div class="navbar navbar-default">
          <form action="#" class="form-inline navbar-form">
              <label for="">วันที่ป่วย</label>
              <input type="text" class="form-control" style="width: 100px;" data-type="date"
                      placeholder="วว/ดด/ปปปป" title="ระบุวันที่ วว/ดด/ปปปป" rel="tooltip" id="txt_start_date" />
              <label for="">ถึง</label>
              <input type="text" class="form-control" style="width: 100px;" data-type="date"
                      placeholder="วว/ดด/ปปปป" title="ระบุวันที่ วว/ดด/ปปปป" rel="tooltip" id="txt_end_date" />
              <select id="sl_code506" class="form-control" style="width: 250px;">
                    <option value="">กลุ่มโรค 506 [ทั้งหมด]</option>
                    % for v in code506:
                            <option value="${v['code']}">${v['code']} ${v['name']}</option>
                    % endfor
              </select>
              <select id="sl_ptstatus" class="form-control" style="width: 150px;">
                  <option value="">สถานะ [ทั้งหมด]</option>
                  <option value="1">หาย</option>
                  <option value="2">ตาย</option>
                  <option value="3">ยังรักษาอยู่</option>
                  <option value="9">ไม่ทราบ</option>
              </select>
              <button type="button" class="btn btn-primary" id="btn_result">
                  <i class="icon-search"></i> แสดง
              </button>
              <button type="button" class="btn btn-success" id="btn_search">
                  <i class="icon-search"></i> ค้นหา
              </button>

          </form>
      </div>

      <table class="table table-bordered" id="tbl_list">
          <thead>
          <tr>
              <th>วันที่ป่วย</th>
              <th>เลขบัตรประชาชน</th>
              <th>ชื่อ - สกุล</th>
              <th class="hidden-md hidden-sm">อายุ (ป-ด-ว)</th>
              <th class="hidden-md hidden-sm">เพศ</th>
              <th>ที่อยู่ขณะป่วย</th>
              <th>สภาพผู้ป่วย</th>
              <th>กลุ่มโรค 506</th>
              <th>#</th>
          </tr>
          </thead>
          <tbody>
          <tr>
             <td colspan="9">กรุณาระบุเงื่อนไข</td>
          </tr>
          </tbody>
      </table>
      <ul class="pagination" id="paging"></ul>

  </div>

    <div class="tab-pane" id="profile">
      <br>
            <div class="navbar navbar-default">
          <form action="#" class="form-inline navbar-form">
              <label for="">วันที่ป่วย</label>
              <input type="text" class="form-control" style="width: 100px;" data-type="date"
                      placeholder="วว/ดด/ปปปป" title="ระบุวันที่ วว/ดด/ปปปป" rel="tooltip" id="txt_start_date" />
              <label for="">ถึง</label>
              <input type="text" class="form-control" style="width: 100px;" data-type="date"
                      placeholder="วว/ดด/ปปปป" title="ระบุวันที่ วว/ดด/ปปปป" rel="tooltip" id="txt_end_date" />
              <select id="sl_code506" class="form-control" style="width: 250px;">
                    <option value="">กลุ่มโรค 506 [ทั้งหมด]</option>
                    % for v in code506:
                            <option value="${v['code']}">${v['code']} ${v['name']}</option>
                    % endfor
              </select>
              <select id="sl_ptstatus" class="form-control" style="width: 150px;">
                  <option value="">สถานะ [ทั้งหมด]</option>
                  <option value="1">หาย</option>
                  <option value="2">ตาย</option>
                  <option value="3">ยังรักษาอยู่</option>
                  <option value="9">ไม่ทราบ</option>
              </select>
              <button type="button" class="btn btn-primary" id="btn_result">
                  <i class="icon-search"></i> แสดง
              </button>
              <button type="button" class="btn btn-success" id="btn_search">
                  <i class="icon-search"></i> ค้นหา
              </button>

          </form>
      </div>

<%doc>      <div id="map2" style="width: 680px; height: 480px;">

      </div></%doc>

  </div>
</div>

<div class="modal fade" id="mdl_info">
  <div class="modal-dialog" style="width: 780px;">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title"><i class="icon-edit"></i> ข้อมูลระบาดวิทยา</h4>
      </div>
      <div class="modal-body">
        <div class="navbar navbar-default">
            <form action="#" class="navbar-form">
                ชื่อ - สกุล <input type="text" disabled class="form-control" id="txt_fullname" style="width: 220px;"/>
                วันเกิด <input type="text" disabled class="form-control" id="txt_birth" style="width: 110px;"/>
                อายุ <input type="text" disabled class="form-control" id="txt_age" style="width: 200px; "/>
    ##                วันที่ <input type="text" disabled class="form-control" id="txt_date_serve" style="width: 100px;"/>
            </form>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">
                ข้อมูลการให้บริการระบาดวิทยา
            </div>
            <table class="table table-bordered">
                <thead>
                <tr>
                    <th>รายการ</th>
                    <th>ผลให้บริการ</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>AN</td>
                    <td><span id="spn_an"></span></td>
                </tr>
                <tr>
                    <td>วันที่รับบริการ</td>
                    <td><span id="spn_date_serv"></span></td>
                </tr>
                <tr>
                    <td>วันที่ป่วย</td>
                    <td><span id="spn_illdate"></span></td>
                </tr>
                <tr>
                    <td>การวินิจฉัย</td>
                    <td><span id="spn_diag"></span></td>
                </tr>
                <tr>
                    <td>กลุ่มโรค 506</td>
                    <td><span id="spn_code506"></span></td>
                </tr>
                <tr>
                    <td>Complication</td>
                    <td><span id="spn_complication"></span></td>
                </tr>
                <tr>
                    <td>ที่อยู่ขณะเจ็บป่วย</td>
                    <td><span id="spn_address"></span></td>
                </tr>
                <tr>
                    <td>สภาพผู้ป่วย</td>
                    <td><span id="spn_ptstatus"></span></td>
                </tr>
                <tr>
                    <td>Latitude, Longitude</td>
                    <td><span id="spn_lat_lng"></span></td>
                </tr>
                </tbody>
            </table>
        </div>
      </div>
    </div>
  </div>
</div>

<script src="/static/js/apps/epidem.js"></script>