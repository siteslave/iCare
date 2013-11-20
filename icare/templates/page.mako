<%inherit file="layout/default.mako" />
<p class="lead"><i class="icon-th-list"></i> Dashboard : หน้าหลัก</p>
<div class="row">
    <div class="col-sm-6">
        <div class="panel panel-info">
            <div class="panel-heading">
                <h3 class="panel-title">ผลงานการฝากครรภ์</h3>
            </div>
            <div class="panel-body">
                <table class="table">
                    <thead>
                    <tr>
                        <th>รายการ</th>
                        <th>จำนวน (คน)</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>ทั้งหมด</td><td><span id="spn_anc_total"></span></td>
                    </tr>
                    <tr>
                        <td>พบความเสี่ยง</td><td><span id="spn_anc_risk"></span></td>
                    </tr>
                    <tr>
                        <td>คลอดแล้ว</td><td><span id="spn_labor"></span></td>
                    </tr>
                    <tr>
                        <td>ฝากครรภ์ <= 12 สัปดาห์</td><td><span id="spn_weeks"></span></td>
                    </tr>
                    <tr>
                        <td>เยี่ยมครบ 5 ครั้ง</td><td><span id="spn_coverages"></span></td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <div class="col-sm-6">
        <div class="panel panel-info">
            <div class="panel-heading">
                <h3 class="panel-title">กราฟแสดงผลงานการฝากครรภ์</h3>
            </div>
            <div class="panel-body">
                <div class="row">
                    <div class="col-sm-6">
                        <div id="anc_chart"></div>
                    </div>
                    <div class="col-sm-6">
                        <div id="anc_chart2"></div>
                    </div>
                </div>
                <br/>
                <em><i class="icon-fire"></i> เป็นข้อมูลในช่วงปีงบประมาณปัจจุบัน (2557)</em>
            </div>
        </div>
    </div>
</div>

<div class="row">
    <div class="col-sm-6">
        <div class="panel panel-warning">
            <div class="panel-heading">
                <h3 class="panel-title">รายชื่อหญิงครบกำหนดฝากครรภ์ (ในเดือนนี้)</h3>
            </div>
            <div class="panel-body">
                <table class="table table-striped" id="tbl_anc_list">
                    <thead>
                    <tr>
                        <th>เลขบัตรประชาชน</th>
                        <th>ชื่อ-สกุล</th>
                        <th>อายุ (ปี)</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td colspan="3">...</td>
                    </tr>
                    </tbody>
                </table>
            </div>

            <div class="panel-footer">
                <a href="/reports/anc" class="btn btn-success">
                    ดูรายชื่อทั้งหมด [ <span class="label label-danger" id="spn_anc_all"></span> ] <i class="icon-arrow-right"></i>
                </a>
            </div>
        </div>
    </div>
    <div class="col-sm-6">
        <div class="panel panel-warning">
            <div class="panel-heading">
                <h3 class="panel-title">รายชื่อหญิงครบกำหนดเยี่ยมหลังคลอด (ในเดือนนี้)</h3>
            </div>
            <div class="panel-body">
                <table class="table" id="tbl_mch_list">
                    <thead>
                    <tr>
                        <th>เลขบัตรประชาชน</th>
                        <th>ชื่อ-สกุล</th>
                        <th>อายุ (ปี)</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td colspan="3">...</td>
                    </tr>
                    </tbody>
                </table>
            </div>
            <div class="panel-footer">
                <a href="/reports/mch" class="btn btn-success">
                    ดูรายชื่อทั้งหมด [ <span class="label label-danger" id="spn_mch_all"></span> ] <i class="icon-arrow-right"></i>
                </a>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript" src="https://www.google.com/jsapi"></script>
<script src="/static/js/apps/page.js"></script>
