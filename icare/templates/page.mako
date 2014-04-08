<%inherit file="layout/default.mako" />
<ul class="breadcrumb">
  <li class="active">หน้าหลัก</li>
</ul>
<p class="lead"><i class="icon-th-list"></i> Dashboard : หน้าหลัก</p>
##<div class="row">
##    <div class="col-sm-6">
##        <ul class="ds-btn">
##             <li>
##                  <a class="btn btn-success btn-lg" href="http://dotstrap.com/">
##                  <i class="fa fa-file fa-lg pull-left"></i><span>User Profile<br><small>Lorem ipsum dolor</small></span></a>
##
##                </li>
##                <li>
##                     <a class="btn btn-lg btn-primary" href="http://dotstrap.com/">
##                  <i class="glyphicon glyphicon-user pull-left"></i><span>User Profile<br><small>Lorem ipsum dolor</small></span></a>
##
##                </li>
##                <li>
##                     <a class="btn btn-lg btn-primary" href="http://dotstrap.com/">
##                  <i class="glyphicon glyphicon-user pull-left"></i><span>User Profile<br><small>Lorem ipsum dolor</small></span></a>
##
##                </li>
##                <li>
##                     <a class="btn btn-lg btn-primary" href="http://dotstrap.com/">
##                  <i class="glyphicon glyphicon-user pull-left"></i><span>User Profile<br><small>Lorem ipsum dolor</small></span></a>
##
##                </li>
##        </ul>
##    </div>
##    <div class="col-sm-6">
##        <div class="blockquote-box clearfix">
##                <div class="square pull-left">
##                    <img src="http://placehold.it/60/8e44ad/FFF&text=15" alt="" class="" />
##                </div>
##                <h4>
##                    Bootsnipp</h4>
##                <p>
##                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a
##                    ante.
##                </p>
##            </div>
##            <div class="blockquote-box blockquote-primary clearfix">
##                <div class="square pull-left">
##                    <span class="glyphicon glyphicon-music glyphicon-lg"></span>
##                </div>
##                <h4>
##                    Let's music play</h4>
##                <p>
##                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a
##                    ante. <a href="http://www.jquery2dotnet.com/search/label/jquery">jquery2dotnet</a>
##                </p>
##            </div>
##    </div>
####    <div class="col-sm-6">
####        <div class="alert alert-success">
####            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">
####                ×</button>
####           <span class="fa fa-check"></span> <strong>Success Message</strong>
####            <hr class="message-inner-separator">
####            <p>
####                You successfully read this important alert message.</p>
####        </div>
####    </div>
##</div>
##<div class="row">
##    <div class="col-sm-6">
##        <div class="blockquote-box blockquote-primary clearfix">
##            <div class="square pull-left">
##                <h3 style="color: white;"><span class="fa fa-cogs fa-lg"></span></h3>
##            </div>
##            <h4>
##                ประมวลผลข้อมูล</h4>
##            <p>
##                ประมวลข้อมูลเพื่อใช้สำหรับการตรวจสอบความครอบคลุมและความสมบูรณ์ของข้อมูล ซึ่งจำเป็นที่ทุกครั้งหลังจากอัปโหลดไฟล 43 แฟ้มแล้ว
##                เราต้องทำการประมวลผลข้อมูล
##            </p>
##        </div>
##    </div>
##
##    <div class="col-sm-6">
##        <div class="alert alert-primary">
##            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">
##                ×</button>
##           <span class="fa fa-refresh"></span> <strong>ประมวลผลข้อมูล</strong>
##            <hr class="message-inner-separator">
##            <p>
##                คลิกที่ปุ่มนี้เพื่อทำการประมวลผลข้อมูล สำหรับการคำนวณผลงานและความสมบูรณ์ของข้อมูล ทุกครั้งหลังจากอัปโหลด 43 แฟ้ม ควรคลิกที่ปุ่มประมวลผลข้อมูล
##                <button type="button" class="btn btn-primary">
##                    <i class="fa fa-refresh fa-lg"></i> ประมวลผลข้อมูล
##                </button>
##            </p>
##        </div>
##    </div>
##
##</div>
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
                        <td>ฝากครรภ์ครบ 5 ครั้ง</td><td><span id="spn_coverages"></span></td>
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
                <table class="table table-bordered" id="tbl_anc_list">
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
                    ดูรายชื่อทั้งหมด [ <span class="label label-primary" id="spn_anc_all"></span> ] <i class="icon-arrow-right"></i>
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
                    ดูรายชื่อทั้งหมด [ <span class="label label-primary" id="spn_mch_all"></span> ] <i class="icon-arrow-right"></i>
                </a>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript" src="https://www.google.com/jsapi"></script>
<script src="/static/js/apps/page.js"></script>
