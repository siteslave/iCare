$(function(){

    $('#file').val('');

   $('#btn_select_file').on('click', function(){
       $('#file').trigger('click');
   });

    $('#file').on('change', function(){
        $('#txt_file_name').val($(this).val());
    });

    $('#btn_upload').on('click', function(){
        var file = $('#txt_file_name').val();
        if(!file)
        {
            alert('กรุณาเลือกไฟล์เพื่ออัปโหลด');
            return false;
        }
    });
});