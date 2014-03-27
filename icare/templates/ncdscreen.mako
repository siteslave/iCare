<%inherit file="layout/default.mako" />
<%! import datetime %>
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">คัดกรองเบาหวาน-ความดัน</li>
</ul>

<ul class="nav nav-tabs">
  <li class="active"><a href="#home" data-toggle="tab"><i class="icon-windows"></i> ทะเบียนคัดกรอง <span class="badge" id="spn_total">0</span></a></li>
  <li><a href="#profile" data-toggle="tab"><i class="icon-briefcase"></i> ประวัติการรับบริการ</a></li>
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="home">
      <br>
      <div class="navbar navbar-default">
          <form action="#" class="form-inline navbar-form">
              <label for="">คัดกรองระหว่างวันที่</label>
              <input type="text" class="form-control" style="width: 100px;" data-type="date"
                      placeholder="วว/ดด/ปปปป" title="ระบุวันที่ วว/ดด/ปปปป" rel="tooltip" id="txt_start_date" />
              <label for="">ถึง</label>
              <input type="text" class="form-control" style="width: 100px;" data-type="date"
                      placeholder="วว/ดด/ปปปป" title="ระบุวันที่ วว/ดด/ปปปป" rel="tooltip" id="txt_end_date" />
              <select id="sl_villages" class="form-control" style="width: 250px;">
                    <option value="">ทุกหมู่บ้านในเขตรับผิดชอบ</option>
                    % for v in villages:
                            <option value="${v['vid']}">หมู่ ${v['vid'][6:8]} ${v['name']}</option>
                    % endfor
                </select>
              <button type="button" class="btn btn-primary" id="btn_result">
                  <i class="icon-search"></i> แสดง
              </button>
              <div class="btn-group pull-right">
                  <button type="button" class="btn btn-success" id="btn_refresh">
                  <i class="icon-refresh"></i> รีเฟรช
              </button>
              <button type="button" class="btn btn-default" id="btn_search">
                  <i class="icon-search"></i> ค้นหา
              </button>
              </div>

          </form>
      </div>

      <table class="table table-bordered" id="tbl_list">
          <thead>
          <tr>
              <th>เลขบัตรประชาชน</th>
              <th>ชื่อ - สกุล</th>
              <th>วันเกิด</th>
              <th class="hidden-md">อายุ (ป-ด-ว)</th>
              <th>เพศ</th>
              <th class="hidden-md">ที่อยู่</th>
              <th title="Type area">T</th>
              <th>วันที่คัดกรอง</th>
              <th>ผล</th>
              <th>ประวัติ</th>
          </tr>
          </thead>
          <tbody>
          <tr>
             <td colspan="10">ไม่พบรายการ</td>
          </tr>
          </tbody>
      </table>
      <ul class="pagination" id="paging"></ul>

  </div>

    <div class="tab-pane" id="profile">
      <br>
      <div class="navbar navbar-default">
          <form action="#" class="form-inline navbar-form">
              <label for="">เลขบัตรประชาชน</label>
              <input type="text" class="form-control" style="width: 250px;"
                     placeholder="ระบุเลขบัตรประชาชน" id="txt_query_visit"
                      rel="tooltip" title="ระบุเลขบัตรประชาชน 13 หลัก"/>
              <button type="button" class="btn btn-primary" id="btn_search_visit">
                  <i class="icon-search"></i> ค้นหา
              </button>
          </form>
      </div>
      <table class="table table-bordered" id="tbl_visit_list">
          <thead>
          <tr>
              <th>วันที่</th>
              <th>สถานที่</th>
              <th>น้ำหนัก (กก.)</th>
              <th>ส่วนสูง (ซม.)</th>
              <th>ความดันโลหิต</th>
              <th>ระดับน้ำตาล</th>
              <th>ผลคัดกรอง</th>
          </tr>
          </thead>
          <tbody>
          <tr>
             <td colspan="7">ไม่พบรายการ</td>
          </tr>
          </tbody>
      </table>

        <ul class="pagination" id="paging_visit"></ul>

  </div>
</div>

<div class="modal fade" id="mdl_result">
  <div class="modal-dialog" style="width: 780px;">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title"><i class="icon-edit"></i> ข้อมูลการคัดกรองความเสี่ยงเบาหวาน-ความดัน</h4>
      </div>
      <div class="modal-body">
        <div class="navbar navbar-default">
            <form action="#" class="navbar-form">
                ชื่อ - สกุล <input type="text" disabled class="form-control" id="txt_screen_fullname" style="width: 220px;"/>
                วันเกิด <input type="text" disabled class="form-control" id="txt_screen_birth" style="width: 110px;"/>
                อายุ <input type="text" disabled class="form-control" id="txt_age" style="width: 200px; "/>
##                วันที่ <input type="text" disabled class="form-control" id="txt_date_serve" style="width: 100px;"/>
            </form>
        </div>
        <table class="table table-bordered" id="tbl_result">
            <thead>
            <tr>
               <th>รายการคัดกรอง</th>
               <th>ผลคัดกรอง</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td>วันที่ตรวจ</td>
                <td><span id="spn_date_serv"></span></td>
            </tr>
            <tr>
                <td>ประเภทบริการ</td>
                <td><span id="spn_servplace"></span></td>
            </tr>
            <tr>
                <td>ระดับน้ำตาลในเลือด (มก./ดล)</td>
                <td><span id="spn_bslevel"></span></td>
            </tr>
            <tr>
                <td>วิธีตรวจระดับน้ำตาล</td>
                <td><span id="spn_bstest"></span></td>
            </tr>
            <tr>
                <td>ประวัติสูบบุหรี่</td>
                <td><span id="spn_smoke"></span></td>
            </tr>
            <tr>
                <td>ดื่มแอลกอฮอลล์</td>
                <td><span id="spn_alcohol"></span></td>
            </tr>
            <tr>
                <td>ประวัติเบาหวานในญาติสายตรง</td>
                <td><span id="spn_dmfamily"></span></td>
            </tr>
            <tr>
                <td>ประวัติความดันในญาติสายตรง</td>
                <td><span id="spn_htfamily"></span></td>
            </tr>
            <tr>
                <td>น้ำหนัก</td>
                <td><span id="spn_weight"></span></td>
            </tr>
            <tr>
                <td>ส่วนสูง</td>
                <td><span id="spn_height"></span></td>
            </tr>
            <tr>
                <td>เส้นรอบเอว (ซ.ม.)</td>
                <td><span id="spn_waist_cm"></span></td>
            </tr>
            <tr>
                <td>ความดันซิสโตลิก ครั้งที่ 1</td>
                <td><span id="spn_sbp1"></span></td>
            </tr>
            <tr>
                <td>ความดันไดแอสโตลิก ครั้งที่ 1</td>
                <td><span id="spn_dbp1"></span></td>
            </tr>
            <tr>
                <td>ความดันซิสโตลิก ครั้งที่ 2</td>
                <td><span id="spn_sbp2"></span></td>
            </tr>
            <tr>
                <td>ความดันไดแอสโตลิก ครั้งที่ 2</td>
                <td><span id="spn_dbp2"></span></td>
            </tr>
            </tbody>
        </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="icon-remove"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<script src="/static/js/apps/ncdscreen.js"></script>