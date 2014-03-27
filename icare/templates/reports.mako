<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ทะเบียนเด็ก 0-2 ปี</li>
</ul>

<ul class="nav nav-tabs">
  <li class="active"><a href="#home" data-toggle="tab"><i class="icon-windows"></i> ทะเบียนเด็ก 0-2 ปี <span class="badge" id="spn_total">0</span></a></li>
  <li><a href="#profile" data-toggle="tab"><i class="icon-briefcase"></i> ประวัติการรับวัคซีน</a></li>
</ul>
<div class="tab-content">
    <div class="tab-pane active" id="home">
        <br>
        <div class="navbar navbar-default">
            <form action="#" class="form-inline navbar-form">
                <label for="">เกิดตั้งแต่</label>
                <input type="text" data-type="date" class="form-control" style="width: 100px;"
                        id="txt_start_date" placeholder="วว/ดด/ปปปป" title="ระบุวันเกิด วว/ดด/ปปปป" rel="tooltip" />
                <label for="">ถึง</label>
                <input type="text" data-type="date" class="form-control" style="width: 100px;"
                        id="txt_end_date" placeholder="วว/ดด/ปปปป" title="ระบุวันเกิด วว/ดด/ปปปป" rel="tooltip" />
                <select id="sl_villages" class="form-control" style="width: 250px;">
                    <option value="">ทุกหมู่บ้านในเขตรับผิดชอบ</option>
                    % for v in villages:
                            <option value="${v['vid']}">หมู่ ${v['vid'][6:8]} ${v['name']}</option>
                    % endfor
                </select>
                <button type="button" class="btn btn-primary" id="btn_filter">
                    <i class="icon-search"></i> แสดง
                </button>
            </form>
        </div>
        <table class="table table-bordered" id="tbl_list">
            <thead>
            <tr>
                <th>เลขบัตรประชาชน</th>
                <th>ชื่อ-สกุล</th>
                <th class="hidden-md hidden-sm">วันเกิด</th>
                <th>อายุ (ป-ด-ว)</th>
                <th>เพศ</th>
                <th class="hidden-md hidden-sm">ที่อยู่</th>
                <th>พัฒนาการ</th>
                <th>% วัคซีน</th>
                <th></th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td colspan="9">กรุณากำหนดเงื่อนไข</td>
            </tr>
            </tbody>
        </table>
    </div>
</div>