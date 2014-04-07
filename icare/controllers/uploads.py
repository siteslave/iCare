# -*- coding: utf8
import uuid
import os
from pyramid.httpexceptions import HTTPFound

from pyramid.view import view_config


@view_config(route_name='uploads', renderer='uploads.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    return {'title': u'อัปโหลดไฟล์'}


@view_config(route_name='uploads', request_method='POST', renderer="do_uploads.mako")
def do_upload(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    if request.POST['file'].file:

        uploaded_directory = '/tmp/hdc/data'
        # True file name
        file_name = request.POST['file'].filename
        # Actual file data
        input_file = request.POST['file'].file

        file_extension = file_name.split(".")[-1]

        if file_extension.upper() == 'ZIP':
            # New file name
            #file_path = os.path.join(uploaded_directory, '%s.zip' % uuid.uuid4())
            file_path = os.path.join(uploaded_directory, '%s' % file_name)
            # Temp file while uploading success
            temp_file = file_path + '~'
            output_file = open(temp_file, 'wb')
            # Write file to a temporary file
            input_file.seek(0)

            while True:
                data = input_file.read(2 << 16)
                if not data:
                    break

                output_file.write(data)
            # Now close file
            output_file.close()
            # Rename temporary file to new file
            os.rename(temp_file, file_path)

            request.session.flash(u'อัปโหลดไฟล์เสร็จเรียบร้อย')
        else:
            request.session.flash(u'ไม่สามารถอัปโหลดไฟล์ได้')

    else:
        request.session.flash(u'ไม่พบไฟล์')

    return {'title': u'อัปโหลดไฟล์'}