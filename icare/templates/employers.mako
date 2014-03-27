<%inherit file="layout/default.mako" />

<%! import datetime %>
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ข้อมูลบุคลากร</li>
</ul>

<ul class="nav nav-tabs">
  <li class="active"><a href="#home" data-toggle="tab"><i class="fa fa-windows"></i> ทะเบียนบุคลากร <span class="badge" id="spn_total">0</span></a></li>
  <!--<li><a href="#new" data-toggle="tab"><i class="fa fa-plus-sign"></i> เพิ่มข้อมูล</a></li> -->
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="home">
      <br>
      <!-- <div class="navbar navbar-default"> -->
          <form action="#" class="form-inline well well-sm">
              <label for="">ค้นหา</label>
              <input type="text" value="" id="txt_query" class="form-control" style="width: 220px;"
			  placeholder="ชื่อ-สกุล หรือ เลขบัตรประชาชน">
			       <div class="btn-group">
	              <button type="button" class="btn btn-primary" id="btn_search">
	                  <i class="fa fa-search"></i> ค้นหา
	              </button>
	              <button type="button" class="btn btn-default" id="btn_refresh">
	                  <i class="fa fa-refresh"></i> รีเฟรช
	              </button>
			       </div>
			  
    			  <button class="btn btn-success pull-right" type="button" id="btn_new">
    				  <i class="fa fa-plus-circle"></i> เพิ่มรายการ
    			  </button>
          </form>
      <!-- </div> -->

      <table class="table table-bordered" id="tbl_list">
          <thead>
          <tr>
              <th>เลขบัตรประชาชน</th>
              <th>ชื่อ-สกุล</th>
              <th>ตำแหน่ง</th>
			  <th>ระดับ</th>
              <th>เริ่มปฏิบัติงาน</th>
              <th>สิ้นสุดปฏิบัติงาน</th>
              <th>สถานะ</th>
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
</div>

<!-- Meeting -->
<div id="mdl_meeting" class="modal fade">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header modal-header-black">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> ประวัติการผึกอบรม</h4>
            </div>
            <div class="modal-body">
                <ul class="nav nav-tabs">
                  <li class="active"><a href="#main-meeting" data-toggle="tab"><i class="fa fa-th-list"></i> ประวัติ</a></li>
                  <li><a href="#new-meeting" data-toggle="tab"><i class="fa fa-plus"></i> เพิ่ม/แก้ไขรายการ</a></li>
                </ul>
                <div class="tab-content">
                  <div class="tab-pane active" id="main-meeting">
                      <br />
                      <!-- Main list -->
                      <table class="table table-bordered" id="tbl_mlist">
                          <thead>
                              <tr>
                                  <th>#</th>
                                  <th>ตั้งแต่วันที่</th>
                                  <th>ถึงวันที่</th>
                                  <th>หลักสูตร</th>
                                  <th>หน่วยงานที่จัด</th>
                                  <th>สถานที่</th>
                                  <th></th>
                              </tr>
                          </thead>
                          <tbody>
                              <tr>
                                  <td colspan="7">..</td>
                              </tr>
                          </tbody>
                      </table>
                      <!-- /Main list -->
                  </div>
                  <div class="tab-pane" id="new-meeting">
                      <!-- new meeting -->
                      <form action="#" role="form">
                      <input type="hidden" name="txt_mcid" value="" id="txt_mcid">
                      <input type="hidden" name="txt_mid" value="" id="txt_mid">
                      <br />
                      <div class="row">
                          <div class="col-md-3">
                              <div class="form-group">
                                <label>วันเริ่มต้น</label>
                                  <div class="input-group date" data-type="date-picker">
                                    <input type="text" id="txt_mstart_date"  class="form-control" placeholder="วว/ดด/ปปปป" />
                                    <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                                  </div>
                              </div>
                          </div>
                          <div class="col-md-3">
                              <div class="form-group">
                                  <label>วันสิ้นสุด</label>
                                  <div class="input-group date" data-type="date-picker">
                                    <input type="text" id="txt_mend_date"  class="form-control" placeholder="วว/ดด/ปปปป" />
                                    <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                                  </div>
                              </div>
                          </div>
                          <div class="col-md-3">
                            <div class="form-group">
                              <label>จำนวนชั่วโมง</label>
                              <input type="text" class="form-control" data-type="number" id="txt_mhour" placeholder="0" />
                            </div>
                          </div>
                      </div>
                          
                          <div class="form-group">
                              <label for="txt_mstart_date">ชื่อหลักสูตร</label>
                              <input type="text" name="txt_mtitle" value="" id="txt_mtitle" class="form-control" placeholder="ระบุชื่อหลักสูตร">
                          </div>
                          <div class="form-group">
                              <label for="txt_mstart_date">จัดโดย</label>
                              <input type="text" name="txt_mowner" value="" id="txt_mowner" class="form-control" placeholder="ระบุชื่อผู้จัดงาน">
                          </div>
                          <div class="form-group">
                              <label for="txt_mstart_date">สถานที่</label>
                              <input type="text" name="txt_mplace" value="" id="txt_mplace" class="form-control" placeholder="ระบุสถานที่จัด">
                          </div>
                          <button type="button" class="btn btn-success" id="btn_msave"><i class="fa fa-save"></i> บันทึกข้อมูล</button>
                      </form>
                      <!-- /new meeting -->
                  </div>
                </div>
            </div>
            <div class="modal-footer">
                
            </div>
        </div>
    </div>
</div>
<!-- /Meeting -->
<div class="modal fade" id="mdl_new">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header modal-header-black">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> ข้อมูลทั่วไปเจ้าหน้าที่ผู้ปฏิบัติงาน</h4>
      </div>
      <div class="modal-body">
        <ul class="nav nav-tabs">
          <li class="active"><a href="#info" data-toggle="tab"><i class="fa fa-group"></i> ข้อมูลทั่วไป</a></li>
          <li><a href="#work" data-toggle="tab"><i class="fa fa-desktop"></i> ข้อมูลการปฏิบติงาน</a></li>
        </ul>
        <div class="tab-content">
          <div class="tab-pane active" id="info">       
            <form class="form-horizontal" action="#">
              <input type="hidden" name="txt_id" value="" id="txt_id">
              <br />
              <div class="row">
                <div class="col-sm-6">
                  <div class="control-group">
                    <label>ชื่อ - สกุล</label>
                    <input type="text" name="txt_fullname" value="" id="txt_fullname" class="form-control"
              placeholder="ชื่อ - สกุล">
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="control-group">
                    <label>เลขบัตรประชาชน</label>
                    <input type="text" name="txt_cid" value="" id="txt_cid" class="form-control" 
                    placeholder="xxxxxxxxxxxxx">
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-3">
                  <div class="control-group">
                    <label>วันเกิด</label>
                    <div class="input-group date" data-type="date-picker">
                      <input type="text" id="txt_birth"  class="form-control" placeholder="วว/ดด/ปปปป" />
                      <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                    </div>
                  </div>
                </div>
                <div class="col-sm-3">
                  <div class="control-group">
                    <label>เพศ</label>
                    <select class="form-control" id="sl_sex">
                      <option value="2">หญิง</option>
                      <option value="1">ชาย</option>
                    </select>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-6">
                  <div class="control-group">
                    <label>ระดับการศึกษา</label>
                    <select class="form-control" id="sl_graduate">
                      <option value="1">อนุปริญญา</option>
                      <option value="2">ปริญญาตรี</option>
                      <option value="3">ปริญญาโท</option>
                      <option value="4">ปริญญาเอก</option>
                    </select>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="control-group">
                    <label>สถานศึกษา</label>
                    <input type="text" class="form-control" id="txt_graduate_place" />
                  </div>
                </div>
              </div>            
            </form>
          </div>
          <div class="tab-pane" id="work">
            <form class="form-horizontal" action="#">
            <br />

              <div class="row">
                <div class="col-sm-6">
                  <div class="control-group">
                    <label>ตำแหน่ง</label>
                    <select name="sl_position" id="sl_position" class="form-control">
                      % for v in positions:
                        <option value="${v['id']}">${v['name']}</option>
                      % endfor
                    </select>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="control-group">
                    <label>ระดับ</label>
                    <select name="sl_position_grade" id="sl_position_grade" class="form-control">
                      % for v in grades:
                        <option value="${v['id']}">${v['name']}</option>
                      % endfor
                    </select>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-6">
                  <label>เลขที่ใบประกอบวิชาชีพ</label>
                  <input type="text" name="txt_position_id" value="" id="txt_position_id" class="form-control" placeholder="เลขที่ใบประกอบวิชาชีพ...">
                </div>
                <div class="col-sm-6">
                  <label>แผนก</label>
                  <input type="text" name="txt_department" value="" id="txt_department" class="form-control" placeholder="แผนก...">
                </div>
              </div>
              <div class="row">
                <div class="col-sm-12">
                  <div class="control-group">
                    <label>ที่อยู่</label>
                    <textarea class="form-control" rows="3" id="txt_address"></textarea>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-6">
                  <label>อีเมล์</label>
                  <input type="text" name="txt_email" value="" id="txt_email" class="form-control" placeholder="yourmail@mail.com...">
                </div>
                <div class="col-sm-6">
                  <label>เบอร์โทรศัพท์</label>
                  <input type="text" name="txt_telephone" value="" id="txt_telephone" class="form-control" placeholder="08x-xxxxxxx">
                </div>
              </div>
              <div class="row">
                <div class="col-sm-4">
                  <label>LINE</label>
                  <input type="text" name="txt_email" value="" id="txt_line" class="form-control" placeholder="...">
                </div>
                <div class="col-sm-4">
                  <label>FACEBOOK</label>
                  <input type="text" name="txt_telephone" value="" id="txt_facebook" class="form-control" placeholder="...">
                </div>
                <div class="col-sm-4">
                  <label>SKYPE</label>
                  <input type="text" name="txt_telephone" value="" id="txt_skype" class="form-control" placeholder="...">
                </div>
              </div>
              <div class="row">
                <div class="col-sm-3">
                  <div class="control-group">
                    <label>วันที่เริ่มปฏิบัติงาน</label>
                    <div class="input-group date" data-type="date-picker">
                      <input type="text" id="txt_start_date"  class="form-control" placeholder="วว/ดด/ปปปป" />
                      <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                    </div>
                  </div>
                </div>
                <div class="col-sm-3">
                  <div class="control-group">
                    <label>วันที่สิ้นสุดการปฏิบัติงาน</label>
                    <div class="input-group date" data-type="date-picker">
                      <input type="text" id="txt_end_date"  class="form-control" placeholder="วว/ดด/ปปปป" />
                      <span class="input-group-addon"><i class="fa fa-calendar"></i></span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-2">
                  <div class="control-group">
                    <label>ยังปฏิบัติงานอยู่</label>
                    <input type="checkbox" name="chk_status" id="chk_status">
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
  	  <div class="modal-footer">
        <button type="button" class="btn btn-default" id="btn_save_new">
          <i class="fa fa-save"></i> บันทึกข้อมูล
        </button>
  	    <button type="button" class="btn btn-primary" data-dismiss="modal">
          <i class="fa fa-times"></i> ปิดหน้าต่าง
        </button>    
  	 </div>
    </div>
  </div>
</div>

<!-- topic request -->
<div id="mdl_topics" class="modal fade">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header modal-header-black">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="modal-title modal-title-white"><i class="fa fa-edit"></i> ห้วข้อกิจกรรมที่ต้องการเข้าร่วม</h4>
            </div>
            <div class="modal-body">
                <ul class="nav nav-tabs">
                  <li class="active"><a href="#main-request" data-toggle="tab"><i class="fa fa-th-list"></i> ประวัติ</a></li>
                  <li><a href="#new-request" data-toggle="tab"><i class="fa fa-plus"></i> เพิ่ม/แก้ไขรายการ</a></li>
                </ul>
                <div class="tab-content">
                  <div class="tab-pane active" id="main-request">
                      <br />
                      <!-- Main list -->
                      <table class="table table-bordered" id="tbl_tlist">
                          <thead>
                              <tr>
                                  <th>#</th>
                                  <th>วันที่</th>
                                  <th>หัวข้อ</th>
                                  <th>รายละเอียด/ข้อมูลเพิ่มเติม</th>
                                  <th>ประเภท</th>
                                  <th>#</th>
                              </tr>
                          </thead>
                          <tbody>
                              <tr>
                                  <td colspan="6">..</td>
                              </tr>
                          </tbody>
                      </table>
                      <!-- /Main list -->
                  </div>
                  <div class="tab-pane" id="new-request">
                      <!-- new request -->
                      <form action="#" role="form">
                        <input type="hidden" id="txt_empid">
                        <input type="hidden" id="txt_tid">
                        <br />
                        <div class="row">
                          <div class="col-md-12">
                              <div class="form-group">
                                <label>ชื่อหัวข้อ</label>
                                <input type="text" class="form-control" id="txt_topic_name" placeholder="ชื่อหัวข้อที่ต้องการ" />
                              </div>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-md-12">
                              <div class="form-group">
                                  <label>ประเภท</label>
                                  <select class="form-control" id="sl_topic_type">
                                    <option value="1">Lectures</option>
                                    <option value="2">Documents</option>
                                    <option value="3">Teaching media</option>
                                    <option value="4">Test</option>
                                  </select>
                              </div>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-md-12">
                            <div class="form-group">
                              <label>รายละเอียดเพิ่มเติม</label>
                              <textarea class="form-control" id="txt_topic_desc" rows="3"></textarea>
                            </div>
                          </div>
                        </div>
                          
                        <button type="button" class="btn btn-default" id="btn_topic_save">
                          <i class="fa fa-save"></i> บันทึกข้อมูล
                        </button>
                      </form>
                      <!-- /new meeting -->
                  </div>
                </div>
            </div>
            <div class="modal-footer">
                
            </div>
        </div>
    </div>
</div>
<!-- /topic request -->

<script src="/static/js/apps/employers.js"></script>