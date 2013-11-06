<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li><a href="/">หน้าหลัก</a></li>
  <li class="active">ทะเบียนเยี่ยมแม่หลังคลอด</li>
</ul>

<form action="#" class="well well-sm form-inline">
    <label for="txt_start_date">ครบกำหนดฝากครรภ์ ตั้งแต่</label>
    <input type="text" id="txt_start_date" style="width: 110px;" class="form-control" placeholder="dd/mm/yyyy" data-type="date" />
    <label for="txt_end_date">ถึง</label>
    <input type="text" id="txt_end_date" style="width: 110px;" class="form-control" placeholder="dd/mm/yyyy" data-type="date" />
    <div class="btn-group">
        <button type="button" id="btn_filter" class="btn btn-primary" rel="tooltip" title="แสดงตามเงื่อนไข">
            <i class="icon-search"></i> แสดง
        </button>
        <button type="button" id="btn_refresh" class="btn btn-success" rel="tooltip" title="แสดงทั้งหมด">
            <i class="icon-refresh"></i> รีเฟรช
        </button>
    </div>
    |
    <input type="text" id="txt_query" class="form-control" style="width: 180px;"
            placeholder="เลขบัตรประชาชน" />
    <button type="button" id="btn_search" class="btn btn-primary" rel="tooltip" title="ค้นหา">
        <i class="icon-search"></i> ค้นหา
    </button>

    <button type="button" class="btn btn-danger pull-right" id="btn_process">
        <i class="icon-refresh"></i> ประมวลผล
    </button>
</form>

<table class="table table-striped" id="tbl_list">
    <thead>
    <tr>
        <th>เลขบัตรประชาชน</th>
        <th>ชื่อ-สกุล</th>
        <th>อายุ (ปี)</th>
        <th>ครั้งที่ 1</th>
        <th>ครั้งที่ 2</th>
        <th>ครั้งที่ 3</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td colspan="6">...</td>
    </tr>
    </tbody>
</table>

<ul class="pagination" id="paging"></ul>

<script src="/static/js/apps/reports_mch.js"></script>