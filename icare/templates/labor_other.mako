<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">คนในเขตไปคลอดที่หน่วยบริการอื่น</li>
</ul>

<form action="#" class="well well-sm form-inline">
    <label for="txt_query">เลขบัตรประชาชน</label>
    <input type="text" id="txt_query" class="form-control" style="width: 240px;" placeholder="ระบุเลขบัตรประชาชน" />
    <button type="button" class="btn btn-primary" id="btn_search">
        <i class="icon-search"></i> ค้นหา
    </button>
    <button type="button" id="btn_total" class="btn btn-primary pull-right" rel="tooltip" title="จำนวนทั้งหมด">
            <i class="icon-th-list"></i> จำนวนทั้งหมด <span id="spn_total"><strong>0</strong></span> คน
        </button>
</form>

<table class="table table-striped" id="tbl_list">
    <thead>
    <tr>
        <th>เลขบัตรประชาขน</th>
        <th>ชื่อ - สกุล</th>
        <th>อายุ (ปี)</th>
        <th>ที่อยู่</th>
        <th>คลอดที่</th>
        <th>#</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td colspan="6">...</td>
    </tr>
    </tbody>
</table>

<ul class="pagination" id="paging"></ul>


<div class="modal fade" id="mdl_anc_survey">
  <div class="modal-dialog" style="width: 788px;">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title">แบบฟอร์มประเมินความเสี่ยงหญิงตั้งครรภ์</h4>
      </div>
      <div class="modal-body">
          <form action="#">
              <input type="hidden" id="txt_ans_pid" value="" />
              <input type="hidden" id="txt_ans_gravida" value="" />
              <ul class="nav nav-tabs">
                  <li class="active"><a href="#tab_ans_history" data-toggle="tab"><i class="icon-time"></i> ประวัติอดีต</a></li>
                  <li><a href="#tab_ans_current" data-toggle="tab"><i class="icon-th-large"></i> ประวัติครรภ์ปัจจุบัน</a></li>
                  <li><a href="#tab_ans_ill" data-toggle="tab"><i class="icon-user-md"></i> ประวัติทางอายุรกรรม</a></li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane active" id="tab_ans_history">
                    <br>
                    <table class="table table-bordered">
                      <thead>
                      <tr>
                          <th>รายการความเสี่ยง</th>
                          <th>ผลประเมิน</th>
                      </tr>
                      </thead>
                      <tbody>
                      <tr>
                          <td>1. เคยมีทารกตายในครรภ์ หรือเสียชีวิตแรกเกิด (1 เดือนแรก)</td>
                          <td>
                              <select class="form-control" id="sl1" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>2. เคยแท้งเอง 3 ครั้ง หรือมากกว่า <strong>ติดต่อกัน</strong></td>
                          <td>
                              <select class="form-control" id="sl2" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>3. เคยคลอดบุตรน้ำหนักน้อยกว่า 2,500 กรัม</td>
                          <td>
                              <select class="form-control" id="sl3" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>4. เคยคลอดบุตรน้ำหนักมากกว่า 4,000 กรัม</td>
                          <td>
                              <select class="form-control" id="sl4" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>5. เคยเข้ารับการรักษาพยาบาลเพราะความดันโลหิตสูง <br /> ระหว่างตั้งครรภ์ หรือครรภ์เป็นพิษ</td>
                          <td>
                              <select class="form-control" id="sl5" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>6. เคยผ่าตัดอวัยวะในระบบสืบพันธุ์ เช่น เนื้องอกมดลูก <br /> ผ่าตัดปากมดลูก ผูกปากมดลูก ฯลฯ</td>
                          <td>
                              <select class="form-control" id="sl6" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      </tbody>
                  </table>
                </div>
                <div class="tab-pane" id="tab_ans_current">
                    <br>
                    <table class="table table-bordered">
                      <thead>
                      <tr>
                          <th>รายการความเสี่ยง</th>
                          <th>ผลประเมิน</th>
                      </tr>
                      </thead>
                      <tbody>
                      <tr>
                          <td>7. ครรภ์แฝด</td>
                          <td>
                              <select class="form-control" id="sl7" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>8. อายุ < 15 ปี (นับ EDC)</td>
                          <td>
                              <select class="form-control" id="sl8" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>9. อายุ >= 35 ปี (นับ EDC)</td>
                          <td>
                              <select class="form-control" id="sl9" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>10. Rh Negative</td>
                          <td>
                              <select class="form-control" id="sl10" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>11. เลือดออกทางช่องคลอด</td>
                          <td>
                              <select class="form-control" id="sl11" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>12. มีก้อนในอุ้งเชิงกราน</td>
                          <td>
                              <select class="form-control" id="sl12" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>13. มีความดันโลหิต Diastolic >= 90 mm/Hg</td>
                          <td>
                              <select class="form-control" id="sl13" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      </tbody>
                  </table>
                </div>
                <div class="tab-pane" id="tab_ans_ill">
                    <br>
                    <table class="table table-bordered">
                      <thead>
                      <tr>
                          <th>รายการความเสี่ยง</th>
                          <th>ผลประเมิน</th>
                      </tr>
                      </thead>
                      <tbody>
                      <tr>
                          <td>14. เบาหวาน</td>
                          <td>
                              <select class="form-control" id="sl14" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>15. โรคไต</td>
                          <td>
                              <select class="form-control" id="sl15" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>16. โรคหัวใจ</td>
                          <td>
                              <select class="form-control" id="sl16" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>17. ติดยาเสพติด, ติดสุรา</td>
                          <td>
                              <select class="form-control" id="sl17" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>18. โรคอายุรกรรมอื่นๆ เช่น ความดันโลหิตสูง, โลหิตจาง <br />
                          ไทรอยด์, SLE ฯลฯ (โปรดระบุ)</td>
                          <td>
                              <select class="form-control" id="sl18" disabled>
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td colspan="2"><input type="text" class="form-control" id="txt_ans_other_ill" disabled /></td>
                      </tr>
                      </tbody>
                  </table>
                </div>
              </div>
          </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-dismiss="modal"><i class="icon-remove"></i> ปิดหน้าต่าง</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->

<div class="modal fade" id="mdl_anc_history">
  <div class="modal-dialog" style="width: 788px;">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title"><i class="icon-calendar"></i> ประวัติการรับบริการฝากครรภ์</h4>
      </div>
      <div class="modal-body">
        <table class="table table-striped" id="tbl_anc_history">
            <thead>
            <tr>
                <th>หน่วยบริการ</th>
                <th>วันที่</th>
                <th>ครรภ์ที่</th>
                <th>ช่วง</th>
                <th>อายุครรภ์</th>
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
        <button type="button" class="btn btn-danger" data-dismiss="modal"><i class="icon-remove"></i> ปิดหน้าต่าง</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->


<script src="/static/js/apps/labor_other.js"></script>