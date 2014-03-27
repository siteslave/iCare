<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ผู้มีภาวะเสี่ยงในการฝากครรภ์</li>
</ul>

<ul class="nav nav-tabs">
    <li class="active">
        <a href="#home" data-toggle="tab"><i class="fa fa-th-list"></i> รายชื่อทั้งหมด</a>
    </li>
    <li>
        <a href="#bygroup" data-toggle="tab"><i class="fa fa-sort-alpha-desc"></i> แยกตามกลุ่มเสี่ยง</a>
    </li>
</ul>

<div class="tab-content">
    <div class="tab-pane active" id="home">
        <br/>
        <form action="#" class="well well-sm form-inline">
            <label for="txt_query">เลขบัตรประชาชน</label>
            <input type="text" id="txt_query" class="form-control" style="width: 240px;" placeholder="ระบุเลขบัตรประชาชน" />
            <button type="button" class="btn btn-primary" id="btn_search">
                <i class="fa fa-search"></i> ค้นหา
            </button> |
            <div class="btn-group">
                <button type="button" data-name="btn_filter" class="btn btn-primary" data-value="Y">
                    <i class="fa fa-fire"></i> มีภาวะเสี่ยง
                </button>
                <button type="button" data-name="btn_filter" class="btn btn-success" data-value="N">
                    <i class="fa fa-check-circle-o"></i> ปกติ
                </button>
                <button type="button" data-name="btn_filter" class="btn btn-default" data-value="0">
                    <i class="fa fa-refresh"></i> ทั้งหมด
                </button>
            </div>

            <button type="button" id="btn_total" class="btn btn-primary pull-right" rel="tooltip" title="จำนวนทั้งหมด">
                    <i class="fa fa-th-list"></i> จำนวนทั้งหมด <span id="spn_total"><strong>0</strong></span> คน
                </button>
        </form>

        <table class="table table-bordered" id="tbl_list">
            <thead>
            <tr>
                <th>เลขบัตรประชาขน</th>
                <th>ชื่อ - สกุล</th>
                <th>วันเกิด</th>
                <th>อายุ (ปี)</th>
                <th>ที่อยู่</th>
                <th>เสี่ยง</th>
                <th>ฝากครรภ์</th>
                <th>#</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td colspan="8">...</td>
            </tr>
            </tbody>
        </table>

        <ul class="pagination" id="paging"></ul>
    </div>

    <div class="tab-pane" id="bygroup">
        <br/>

        <form action="#" class="well well-sm form-horizontal">
           <div class="row">
              <div class="col-sm-2">
                  <div class="form-group">
                      <label for="txt_start_date" class="col-sm-3 control-label">ตั้งแต่</label>
                      <div class="input-group date col-sm-9" data-type="date-picker">
                          <input type="text" id="txt_start_date"  class="form-control" placeholder="วว/ดด/ปปปป"/>
                          <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                      </div>
                  </div>
              </div>
              <div class="col-sm-2">
                  <div class="form-group">
                      <label for="txt_end_date" class="col-sm-2 control-label"> - </label>
                      <div class="input-group date col-sm-9" data-type="date-picker">
                          <input type="text" id="txt_end_date"  class="form-control" placeholder="วว/ดด/ปปปป"/>
                          <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                      </div>
                  </div>
              </div>
              <div class="col-sm-3">
                  <div class="btn-group">
                      <button type="button" id="btn_filter_by_group" class="btn btn-default" rel="tooltip" title="แสดงตามเงื่อนไข">
                          <i class="fa fa-search"></i> แสดงข้อมูล
                      </button>
                      <button type="button" id="btn_clear_filter_by_group" class="btn btn-primary" rel="tooltip" title="ล้างข้อมูลใหม่">
                          <i class="fa fa-refresh"></i> ล้างข้อมูล
                      </button>
                  </div>
              </div>
          </div>
        </form>
        <table class="table table-bordered">
                    <thead>
                    <tr>
                        <th>ประเภทความเสี่ยง</th>
                        <th>จำนวน</th>
                        <th>#</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>1. เคยมีทารกตายในครรภ์ หรือเสียชีวิตแรกเกิด (1 เดือนแรก)</td>
                        <td class="text-center"><span id="spn_ch01"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch1"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>2. เคยแท้งเอง 3 ครั้ง หรือมากกว่า ติดต่อกัน</td>
                        <td class="text-center"><span id="spn_ch02"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch2"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>3. เคยคลอดบุตรน้ำหนักน้อยกว่า 2,500 กรัม</td>
                        <td class="text-center"><span id="spn_ch03"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch3"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>4. เคยคลอดบุตรน้ำหนักมากกว่า 4,000 กรัม</td>
                        <td class="text-center"><span id="spn_ch04"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch4"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>5. เคยเข้ารับการรักษาพยาบาลเพราะความดันโลหิตสูง
ระหว่างตั้งครรภ์ หรือครรภ์เป็นพิษ</td>
                        <td class="text-center"><span id="spn_ch05"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch5"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>6. เคยผ่าตัดอวัยวะในระบบสืบพันธุ์ เช่น เนื้องอกมดลูก
ผ่าตัดปากมดลูก ผูกปากมดลูก ฯลฯ</td>
                        <td class="text-center"><span id="spn_ch06"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch6"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>7. ครรภ์แฝด</td>
                        <td class="text-center"><span id="spn_ch07"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch7"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>8. อายุ < 15 ปี (นับ EDC)</td>
                        <td class="text-center"><span id="spn_ch08"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch8"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>9. อายุ >= 35 ปี (นับ EDC)</td>
                        <td class="text-center"><span id="spn_ch09"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch9"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>10. Rh Negative</td>
                        <td class="text-center"><span id="spn_ch10"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch10"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>11. เลือดออกทางช่องคลอด</td>
                        <td class="text-center"><span id="spn_ch11"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch11"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>12. มีก้อนในอุ้งเชิงกราน</td>
                        <td class="text-center"><span id="spn_ch12"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch12"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>13. มีความดันโลหิต Diastolic >= 90 mm/Hg</td>
                        <td class="text-center"><span id="spn_ch13"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch13"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>14. เบาหวาน</td>
                        <td class="text-center"><span id="spn_ch14"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch14"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>15. โรคไต</td>
                        <td class="text-center"><span id="spn_ch15"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch15"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>16. โรคหัวใจ</td>
                        <td class="text-center"><span id="spn_ch16"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch16"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>17. ติดยาเสพติด, ติดสุรา</td>
                        <td class="text-center"><span id="spn_ch17"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch17"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    <tr>
                        <td>18. โรคอายุรกรรมอื่นๆ เช่น ความดันโลหิตสูง, โลหิตจาง
ไทรอยด์, SLE ฯลฯ</td>
                        <td class="text-center"><span id="spn_ch18"></span></td>
                        <td class="text-center">
                            <a href="#" class="btn btn-default" data-name="btn_get_risk_list" data-choice="ch18"><i class="fa fa-sign-out"></i></a>
                        </td>
                    </tr>
                    </tbody>
                </table>
    </div>
</div>

<div class="modal fade" id="mdl_anc_survey">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-check-circle-o"></i> แบบฟอร์มประเมินความเสี่ยงหญิงตั้งครรภ์</h4>
      </div>
      <div class="modal-body">
          <form action="#">
              <input type="hidden" id="txt_ans_pid" value="" />
              <input type="hidden" id="txt_ans_gravida" value="" />
              <ul class="nav nav-tabs">
                  <li class="active"><a href="#tab_ans_history" data-toggle="tab"><i class="fa fa-calendar"></i> ประวัติอดีต</a></li>
                  <li><a href="#tab_ans_current" data-toggle="tab"><i class="fa fa-th-large"></i> ประวัติครรภ์ปัจจุบัน</a></li>
                  <li><a href="#tab_ans_ill" data-toggle="tab"><i class="fa fa-user-md"></i> ประวัติทางอายุรกรรม</a></li>
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
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="mdl_anc_history">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-calendar"></i> ประวัติการรับบริการฝากครรภ์</h4>
      </div>
      <div class="modal-body">
        <table class="table table-bordered" id="tbl_anc_history">
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
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="mdl_risk_list">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-calendar"></i> รายชื่อผู้มีภาวะเสี่ยงในการฝากครรภ์</h4>
      </div>
      <div class="modal-body">

        <table class="table table-bordered" id="tbl_risk_list_by_type">
            <thead>
            <tr>
                <th>เลขบัตรประชาชน</th>
                <th>ชื่อสกุล</th>
                <th>วันเกิด</th>
                <th>อายุ (ปี)</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td colspan="4">...</td>
            </tr>
            </tbody>
        </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<script src="/static/js/apps/reports_anc_risk.js"></script>