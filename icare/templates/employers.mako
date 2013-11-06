<%inherit file="layout/default.mako" />

<%! import datetime %>
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ข้อมูลบุคลากร</li>
</ul>

<ul class="nav nav-tabs">
  <li class="active"><a href="#home" data-toggle="tab"><i class="icon-windows"></i> ทะเบียนบุคลากร <span class="badge" id="spn_total">0</span></a></li>
  <!--<li><a href="#new" data-toggle="tab"><i class="icon-plus-sign"></i> เพิ่มข้อมูล</a></li> -->
</ul>
<div class="tab-content">
  <div class="tab-pane active" id="home">
      <br>
      <div class="navbar navbar-default">
          <form action="#" class="form-inline navbar-form">
              <label for="">ค้นหา</label>
              <input type="text" value="" id="txt_query" class="form-control" style="width: 220px;"
			  placeholder="ชื่อ-สกุล หรือ เลขบัตรประชาชน">
			  <div class="btn-group">
	              <button type="button" class="btn btn-primary" id="btn_search">
	                  <i class="icon-search"></i> ค้นหา
	              </button>
	              <button type="button" class="btn btn-default" id="btn_refresh">
	                  <i class="icon-refresh"></i> รีเฟรช
	              </button>
			  </div>
			  
			  <button class="btn btn-success pull-right" type="button" id="btn_new">
				  <i class="icon-plus-sign"></i> เพิ่มรายการ
			  </button>
          </form>
      </div>

      <table class="table table-striped" id="tbl_list">
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
  <!--
  <div class="tab-pane" id="new">
	  <br />
	  <div class="alert alert-success">
		  <span class="text text-muted">กรุณาตรวจสอบข้อมูลก่อนบันทึก</span>
		  <button class="btn btn-success">
			  <i class="icon-save"></i> บันทึกข้อมูล
		  </button>
		  <button class="btn btn-danger">
			  <i class="icon-refresh"></i> ยกเลิก
		  </button>
	  </div>
	  <ul class="nav nav-tabs">
		  <li class="active">
			  <a href="#info" data-toggle="tab">
				  <i class="icon-edit"></i> ข้อมูลทั่วไป
			  </a>
		  </li>
		  <li>
			  <a href="#edu" data-toggle="tab">
				  <i class="icon-briefcase"></i> การศึกษา/ฝึกอบรม
			  </a>
		  </li>
	  </ul>
	  <div class="tab-content">
		  <div class="tab-pane active" id="info">
			  <br />
			  <form role="form">
			    <div class="form-group">
			      <label for="txt_cid">เลขบัตรประชาชน</label>
			      <input type="text" class="form-control" id="txt_cid" style="width: 300px;" placeholder="xxxxxxxxxxxxx">
			    </div>
			    <div class="form-group">
			      <label for="txt_fullname">ชื่อ - สกุล</label>
			      <input type="text" class="form-control" style="width: 300px;" id="txt_fullname" placeholder="ระบุชื่อ - สกุล">
			    </div>

			    <div class="form-group">
			      <label for="txt_birth">วันเกิด</label>
			      <input type="text" class="form-control" style="width: 110px;" id="txt_birth" data-type="date" placeholder="dd/mm/yyyy">
			    </div>

			    <div class="form-group">
			      <label for="txt_position">ตำแหน่ง</label>
			      <input type="text" class="form-control" style="width: 300px;" id="txt_position" placeholder="ระบุตำแหน่ง">
			    </div>

			    <div class="form-group">
			      <label for="txt_telephone">โทรศัพท์</label>
			      <input type="text" class="form-control" style="width: 300px;" id="txt_telephone" placeholder="xxxxxxxxxx">
			    </div>
			  </form>
		  </div>
		  <div class="tab-pane" id="edu">
			  <div class="page-header">
			    <h3>ข้อมูลการศึกษา <small>ประวัติการศึกษา</small></h3>
			  </div>
			  <table class="table table-striped">
				  <thead>
	  			  	<tr>
	  					<th>ปี</th>
	  					<th>ระดับ</th>
	  					<th>หลักสูตร</th>
	  					<th>สถานศึกษา</th>
						<th></th>
	  				</tr>
				  </thead>
				  <tbody>
					  <tr>
						  <td colspan="5">...</td>
					  </tr>
				  </tbody>
			  </table>
			  <button class="btn btn-primary pull-right">
				  <i class="icon-plus-sign"></i>
			  </button>
			  
			  
			  <br />
			  <br />
		  </div>
	  </div>
  </div>
  -->
</div>

<!-- Meeting -->
<div id="mdl_meeting" class="modal fade">
    <div class="modal-dialog" style="width: 870px;">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="modal-title"><i class="icon-edit"></i> ประวัติการผึกอบรม</h4>
            </div>
            <div class="modal-body">
                <ul class="nav nav-tabs">
                  <li class="active"><a href="#main-meeting" data-toggle="tab"><i class="icon-th-list"></i> ประวัติ</a></li>
                  <li><a href="#new-meeting" data-toggle="tab"><i class="icon-plus-sign"></i> เพิ่มรายการ</a></li>
                </ul>
                <div class="tab-content">
                  <div class="tab-pane active" id="main-meeting">
                      <br />
                      <!-- Main list -->
                      <table class="table table-striped" id="tbl_mlist">
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
                          <div class="col-md-2">
                              <div class="form-group">
                                  <label for="txt_mstart_date">วันที่เริ่ม</label>
                                  <input type="text" data-type="date" name="txt_mstart_date" value="" id="txt_mstart_date" style="width: 110px;" class="form-control" placeholder="dd/mm/yyyy">
                                </div>
                          </div>
                          <div class="col-md-2">
                              <div class="form-group">
                                  <label for="txt_mstart_date">วันที่สิ้นสุด</label>
                                  <input type="text" class="form-control" data-type="date" name="txt_mend_date" value="" id="txt_mend_date" style="width: 110px;" placeholder="dd/mm/yyyy">
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
                          <button type="button" class="btn btn-success" id="btn_msave"><i class="icon-save"></i> บันทึกข้อมูล</button>
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
  <div class="modal-dialog" style="width: 780px;">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title"><i class="icon-edit"></i> ข้อมูลทั่วไปเจ้าหน้าที่ผู้ปฏิบัติงาน</h4>
      </div>
      <div class="modal-body">
        <div class="panel panel-default">
            <div class="panel-heading">
                ข้อมูลทั่วไป
            </div>
			<input type="hidden" name="txt_id" value="" id="txt_id">
            <table class="table">
                <thead>
                <tr>
                    <th>ชื่อ - สกุล</th>
                    <th><input type="text" name="txt_fullname" value="" id="txt_fullname" class="form-control"
						placeholder="ชื่อ - สกุล"></th>
                </tr>
                </thead>
                <tbody>
	                <tr>
	                    <td>เลขบัตรประชาชน</td>
	                    <td><input type="text" name="txt_cid" value="" id="txt_cid" class="form-control"
							placeholder="xxxxxxxxxxxxx"></td>
	                </tr>
                <tr>
                    <td>วันเกิด</td>
                    <td><input type="text" name="txt_birth" value="" id="txt_birth" class="form-control" style="width: 110px;" data-type="date" placeholder="dd/mm/yyyy"></td>
                </tr>
				<tr>
					<td>เพศ</td>
					<td>
						<select class="form-control" id="sl_sex" style="width: 110px;">
							<option value="2">หญิง</option>
							<option value="1">ชาย</option>
						</select>
					</td>
				</tr>
                <tr>
                    <td>ตำแหน่ง</td>
                    <td>
                    	<select name="sl_position" id="sl_position" class="form-control">
		                    % for v in positions:
		                            <option value="${v['id']}">${v['name']}</option>
		                    % endfor
                    	</select>
                    </td>
                </tr>

                <tr>
                    <td>ระดับ</td>
                    <td>
                    	<select name="sl_position_grade" id="sl_position_grade" class="form-control">
		                    % for v in grades:
		                            <option value="${v['id']}">${v['name']}</option>
		                    % endfor
                    	</select>
                    </td>
                </tr>
                <tr>
                    <td>เลขที่ใบประกอบวิชาชีพ</td>
                    <td><input type="text" name="txt_position_id" value="" id="txt_position_id" class="form-control" placeholder="เลขที่ใบประกอบวิชาชีพ..."></td>
                </tr>
				<tr>
                    <td>แผนก</td>
                    <td><input type="text" name="txt_department" value="" id="txt_department" class="form-control" placeholder="แผนก..."></td>
                </tr>
                <tr>
                    <td>อีเมล์</td>
                    <td><input type="text" name="txt_email" value="" id="txt_email" class="form-control" placeholder="yourmail@mail.com..."></td>
                </tr>
                <tr>
                    <td>เบอร์โทรศัพท์</td>
                    <td><input type="text" name="txt_telephone" value="" id="txt_telephone" class="form-control" placeholder="xxxxxxxxxx..."></td>
                </tr>
                <tr>
                    <td>วันที่เริ่มปฏิบัติงาน</td>
                    <td><input type="text" name="txt_start_date" value="" id="txt_start_date" class="form-control" data-type="date" style="width: 110px;" placeholder="dd/mm/yyyy"></td>
                </tr>
                <tr>
                    <td>วันที่สิ้นสุดการปฏิบัติงาน</td>
                    <td><input type="text" name="txt_end_date" value="" id="txt_end_date" class="form-control" data-type="date" style="width: 110px;" placeholder="dd/mm/yyyy"></td>
                </tr>
				<tr>
					<td>Active</td>
					<td><input type="checkbox" name="chk_status" value="" id="chk_status"></td>
				</tr>
                </tbody>
            </table>
        </div>
      </div>
	  <div class="modal-footer">
	          <button type="button" class="btn btn-danger" data-dismiss="modal"><i class="icon-remove"></i> ปิดหน้าต่าง</button>
	          <button type="button" class="btn btn-success" id="btn_save_new"><i class="icon-save"></i> บันทึกข้อมูล</button>
	        </div>
    </div>
  </div>
</div>

<script src="/static/js/apps/employers.js"></script>