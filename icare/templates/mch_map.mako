<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ระบบแผนที่งานแม่และเด็ก</li>
</ul>

<div class="row">
    <div class="col-sm-5">
        <div class="navbar navbar-default">
            <form action="#" class="navbar-form form-inline">
                <select id="sl_villages" class="form-control" style="width: 220px;">
                    <option value="">เลือกหมู่บ้าน</option>
                    % for v in villages:
                    <option value="${v['vid']}">หมู่ ${v['vid'][6:8]} ${v['name']}</option>
                    % endfor
                </select>
                <select id="sl_by" class="form-control" style="width: 150px;">
                    <option value="0">ยังไม่คลอด</option>
                    <option value="1">คลอดแล้ว</option>
                </select>
                <a href="#" class="btn btn-primary" id="btn_get_anc_list">
                    <i class="icon-search"></i>
                </a>
            </form>
        </div>
        <table class="table table-striped" id="tbl_anc">
            <thead>
            <tr>
                <th>CID</th>
                <th>ชื่อ-สกุล</th>
                <th>อายุ (ปี)</th>
                <th>#</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td colspan="4">กรุณาระบุเงื่อนไข</td>
            </tr>
            </tbody>
        </table>
        <ul class="pagination" id="paging"></ul>
    </div>
    <div class="col-sm-7">
        <div class="row" id="div_mark_map" style="display: none;">
            <div class="col-md-12">
                <div class="navbar navbar-default">
                <form action="#" class="navbar-form">
                    ชื่อ-สกุล <input type="text" class="form-control" id="txt_ptname" style="width: 220px;" disabled />
                    CID <input type="text" class="form-control" id="txt_cid" style="width: 180px;" disabled />
                    <input type="hidden" id="txt_hid" value="" />
                    <input type="hidden" id="txt_hospcode" value="" />

                    <div class="btn-group">
                    <button type="button" class="btn btn-success" id="btn_save_marker" title="บันทึกพิกัด" rel="tooltip" disabled>
                        <i class="icon-save"></i>
                    </button>
                    <button type="button" class="btn btn-danger" id="btn_clear_marker" title="เคลียร์พิกัด" rel="tooltip">
                        <i class="icon-refresh"></i>
                    </button>
                    <button type="button" class="btn btn-default" id="btn_cancel_marker" title="ยกเลิก/ปิด" rel="tooltip">
                        <i class="icon-remove"></i>
                    </button>
                </div>
                </form>
            </div>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-12">
                <div id="map" style="width: 650px; height: 480px;"></div>
            </div>
        </div>

    </div>
</div>

<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&language=th"></script>
<script charset="utf-8" src="/static/js/apps/mch_map.js"></script>