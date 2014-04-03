<%inherit file="layout/default.mako" />
<%! import datetime %>
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ข้อมูลการฝากครรภ์</li>
</ul>

<ul class="nav nav-tabs">
  <li class="active"><a href="#home" data-toggle="tab"><i class="fa fa-windows"></i> ทะเบียนฝากครรภ์ <span class="badge" id="spn_anc_total">0</span></a></li>
  <li><a href="#profile" data-toggle="tab"><i class="fa fa-briefcase"></i> ประวัติการรับบริการ (ในเขต/นอกเขต)</a></li>
</ul>

<div class="tab-content">
  <div class="tab-pane active" id="home">
      <br>
      <!-- <div class="navbar navbar-default"> -->
          <form action="#" class="form-inline well well-sm">
              <div class="row">
                  <div class="col-md-4">
                      <div class="input-group">
                          <input type="text" class="form-control"
                             placeholder="ระบุเลขบัตรประชาชน" id="txt_query"
                              rel="tooltip" title="ระบุคำค้นหา เช่น เลขบัตรประชาชน เป็นต้น"/>
                          <span class="input-group-btn">
                              <button type="button" class="btn btn-primary" id="btn_search_anc">
                                  <i class="fa fa-search"></i> ค้นหา
                              </button>
                          </span>
                      </div>
                  </div>
                  <div class="col-md-3 col-md-offset-5">
                      <div class="btn-group">
                          <button type="button" class="btn btn-default" id="btn_refresh">
                              <i class="fa fa-refresh"></i> รีเฟรช
                          </button>
                          <button type="button" class="btn btn-primary pull-right" id="btn_process">
                              <i class="fa fa-refresh"></i> ประมวลผล
                          </button>

                      </div>
                  </div>
              </div>
          </form>
      <!-- </div> -->
      <table class="table table-bordered" id="tbl_list">
          <thead>
          <tr>
              <th>เลขบัตรประชาชน</th>
              <th>ชื่อ - สกุล</th>
              <th>วันเกิด</th>
              <th class="hidden-md">อายุ (ป-ด-ว)</th>
              <th class="hidden-md">ครั้งแรก</th>
##              <th class="hidden-md">ล่าสุด</th>
              <th>ครรภ์ที่</th>
              <th class="hidden-md">ครั้ง</th>
<%doc>              <th class="hidden-md">EDC</th>
              <th class="hidden-md">LMP</th></%doc>
              <th>คลอด</th>
              <th>ประเมิน</th>
              <th></th>
          </tr>
          </thead>
          <tbody>
          <tr>
             <td colspan="9">ไม่พบรายการ</td>
          </tr>
          </tbody>
      </table>
      <ul class="pagination" id="paging"></ul>

  </div>
  <div class="tab-pane" id="profile">
      <br>
      <!-- <div class="navbar navbar-default"> -->
          <form action="#" class="form-inline well well-sm">
              <div class="row">
                  <div class="col-md-4">
                      <div class="input-group">
                          <input type="text" class="form-control"
                             placeholder="ระบุเลขบัตรประชาชน" id="txt_query_visit"
                              rel="tooltip" title="ระบุเลขบัตรประชาชน 13 หลัก"/>
                          <span class="input-group-btn">
                              <button type="button" class="btn btn-primary" id="btn_search_visit">
                                  <i class="fa fa-search"></i> ค้นหา
                              </button>
                          </span>
                      </div>

                  </div>
              </div>
          </form>
      <!-- </div> -->
      <table class="table table-bordered" id="tbl_visit_list">
          <thead>
          <tr>
              <th>วันที่</th>
              <th>สถานที่ตรวจ</th>
              <th>ครรภ์ที่</th>
              <th>ช่วงที่</th>
              <th>อายุครรภ์</th>
              <th>ผลตรวจ</th>
              <th>คลอด</th>
              <th>สำรวจ</th>
              <th>นัด</th>
              <th>#</th>
          </tr>
          </thead>
          <tbody>
          <tr>
             <td colspan="10">ไม่พบรายการ</td>
          </tr>
          </tbody>
      </table>
      <ul class="pagination" id="visit_paging"></ul>
  </div>
</div>

<div class="modal fade" id="mdl_anc_survey">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> แบบฟอร์มประเมินความเสี่ยงหญิงตั้งครรภ์</h4>
      </div>
      <div class="modal-body">
          <form action="#">
              <input type="hidden" id="txt_ans_pid" value="" />
              <input type="hidden" id="txt_ans_gravida" value="" />
              <ul class="nav nav-tabs">
                  <li class="active"><a href="#tab_ans_history" data-toggle="tab"><i class="fa fa-times"></i> ประวัติอดีต</a></li>
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
                              <select class="form-control" id="sl1">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>2. เคยแท้งเอง 3 ครั้ง หรือมากกว่า <strong>ติดต่อกัน</strong></td>
                          <td>
                              <select class="form-control" id="sl2">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>3. เคยคลอดบุตรน้ำหนักน้อยกว่า 2,500 กรัม</td>
                          <td>
                              <select class="form-control" id="sl3">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>4. เคยคลอดบุตรน้ำหนักมากกว่า 4,000 กรัม</td>
                          <td>
                              <select class="form-control" id="sl4">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>5. เคยเข้ารับการรักษาพยาบาลเพราะความดันโลหิตสูง <br /> ระหว่างตั้งครรภ์ หรือครรภ์เป็นพิษ</td>
                          <td>
                              <select class="form-control" id="sl5">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>6. เคยผ่าตัดอวัยวะในระบบสืบพันธุ์ เช่น เนื้องอกมดลูก <br /> ผ่าตัดปากมดลูก ผูกปากมดลูก ฯลฯ</td>
                          <td>
                              <select class="form-control" id="sl6">
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
                              <select class="form-control" id="sl7">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>8. อายุ < 15 ปี (นับ EDC)</td>
                          <td>
                              <select class="form-control" id="sl8">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>9. อายุ >= 35 ปี (นับ EDC)</td>
                          <td>
                              <select class="form-control" id="sl9">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>10. Rh Negative</td>
                          <td>
                              <select class="form-control" id="sl10">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>11. เลือดออกทางช่องคลอด</td>
                          <td>
                              <select class="form-control" id="sl11">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>12. มีก้อนในอุ้งเชิงกราน</td>
                          <td>
                              <select class="form-control" id="sl12">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>13. มีความดันโลหิต Diastolic >= 90 mm/Hg</td>
                          <td>
                              <select class="form-control" id="sl13">
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
                              <select class="form-control" id="sl14">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>15. โรคไต</td>
                          <td>
                              <select class="form-control" id="sl15">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>16. โรคหัวใจ</td>
                          <td>
                              <select class="form-control" id="sl16">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>17. ติดยาเสพติด, ติดสุรา</td>
                          <td>
                              <select class="form-control" id="sl17">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td>18. โรคอายุรกรรมอื่นๆ เช่น ความดันโลหิตสูง, โลหิตจาง <br />
                          ไทรอยด์, SLE ฯลฯ (โปรดระบุ)</td>
                          <td>
                              <select class="form-control" id="sl18">
                                  <option value="0">ไม่มี</option>
                                  <option value="1">มี</option>
                              </select>
                          </td>
                      </tr>
                      <tr>
                          <td colspan="2"><input type="text" class="form-control" id="txt_ans_other_ill" /></td>
                      </tr>
                      </tbody>
                  </table>
                </div>
              </div>
          </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" id="btn_save_survey"><i class="fa fa-save"></i> บันทึกข้อมูล</button>
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->

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

<div class="modal fade" id="mdl_prenatal">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> รายละเอียดเกี่ยวกับการตั้งครรภ์</h4>
      </div>
      <div class="modal-body">
        <!-- <div class="navbar navbar-default"> -->
            <form action="#" class="well well-sm form-inline">
                ชื่อ - สกุล <input type="text" disabled class="form-control" id="txt_prenatal_fullname" style="width: 250px;"/>
             <%doc>   วันเกิด <input type="text" disabled class="form-control" id="txt_labor_birth" style="width: 140px;"/></%doc>
                CID <input type="text" disabled class="form-control" id="txt_prenatal_cid" style="width: 200px;"/>
                ครรภ์ที่ <input type="text" disabled class="form-control" id="txt_prenatal_gravida" style="width: 50px;"/>
            </form>
        <!-- </div> -->
           <form action="#">
                <fieldset>
                    <legend>ข้อมูลการตั้งครรภ์</legend>
                    <div class="row">
                        <div class="col-lg-3">
                             <div class="form-group">
                                <label for="txt_prenatal_edc">EDC</label>
                                <input type="text" disabled class="form-control" id="txt_prenatal_edc"/>
                            </div>
                        </div>
                        <div class="col-lg-3">
                             <div class="form-group">
                                <label for="txt_prenatal_lmp">LMP</label>
                                <input type="text" disabled class="form-control" id="txt_prenatal_lmp"/>
                            </div>
                        </div>
                        <div class="col-lg-3">
                             <div class="form-group">
                                <label for="sl_prenatal_vdrl_result">VDRL</label>
                                 <select id="sl_prenatal_vdrl_result" class="form-control" disabled>
                                     <option value="1">ปกติ</option>
                                     <option value="2">ผิดปกติ</option>
                                     <option value="3">ไม่ตรวจ</option>
                                     <option value="4">รอผลตรวจ</option>
                                     <option value="9">ไม่ทราบ</option>
                                 </select>
                            </div>
                        </div>
                         <div class="col-lg-3">
                             <div class="form-group">
                                <label for="sl_prenatal_hb_result">HB</label>
                                 <select id="sl_prenatal_hb_result" class="form-control" disabled>
                                     <option value="1">ปกติ</option>
                                     <option value="2">ผิดปกติ</option>
                                     <option value="3">ไม่ตรวจ</option>
                                     <option value="4">รอผลตรวจ</option>
                                     <option value="9">ไม่ทราบ</option>
                                 </select>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-lg-3">
                             <div class="form-group">
                                <label for="sl_prenatal_date_hct">วันที่ตรวจ HCT</label>
                                <input type="text" disabled class="form-control" id="sl_prenatal_date_hct"/>
                            </div>
                        </div>
                        <div class="col-lg-3">
                             <div class="form-group">
                                <label for="sl_prenatal_hct_result">HCT</label>
                                 <select id="sl_prenatal_hct_result" class="form-control" disabled>
                                     <option value="1">ปกติ</option>
                                     <option value="2">ผิดปกติ</option>
                                     <option value="3">ไม่ตรวจ</option>
                                     <option value="4">รอผลตรวจ</option>
                                     <option value="9">ไม่ทราบ</option>
                                 </select>
                            </div>
                        </div>

                        <div class="col-lg-3">
                             <div class="form-group">
                                <label for="sl_prenatal_hiv_result">HIV</label>
                                 <select id="sl_prenatal_hiv_result" class="form-control" disabled>
                                     <option value="1">ปกติ</option>
                                     <option value="2">ผิดปกติ</option>
                                     <option value="3">ไม่ตรวจ</option>
                                     <option value="4">รอผลตรวจ</option>
                                     <option value="9">ไม่ทราบ</option>
                                 </select>
                            </div>
                        </div>
                        <div class="col-lg-3">
                             <div class="form-group">
                                <label for="sl_prenatal_thalassemia">ธาลัสซีเมีย</label>
                                 <select id="sl_prenatal_thalassemia" class="form-control" disabled>
                                     <option value="1">ปกติ</option>
                                     <option value="2">ผิดปกติ</option>
                                     <option value="3">ไม่ตรวจ</option>
                                     <option value="4">รอผลตรวจ</option>
                                     <option value="9">ไม่ทราบ</option>
                                 </select>
                            </div>
                        </div>
                    </div>

                </fieldset>
            </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>


<div class="modal fade" id="mdl_appointment">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> ข้อมูลการนัดครั้งต่อไป</h4>
      </div>
      <div class="modal-body">
        <table class="table table-bordered" id="tbl_appoint_list">
            <thead>
            <tr>
               <th>#</th>
               <th>วันที่</th>
               <th>กิจกรรมที่นัด</th>
               <th>รหัสโรคที่นัด</th>
            </tr>
            </thead>
            <tbody></tbody>
        </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i> ปิดหน้าต่าง</button>
      </div>
    </div>
  </div>
</div>

<script src="/static/js/apps/anc.js"></script>
