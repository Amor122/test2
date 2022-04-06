import os
import zipfile

from django.http import JsonResponse, HttpResponse, StreamingHttpResponse, FileResponse
from django.shortcuts import render
import pymysql


# 与数据库交互的公共函数
def get_data(sql):
    client = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='sa123456',
        database='test_db',
        charset='utf8'
    )
    cursor = client.cursor()
    rows = cursor.execute(sql)
    client.commit()
    cursor.close()
    client.close()
    return rows


# 添加员工
def add_emp(request):
    data = {
        'status': '添加数据失败'
    }
    if request.method == 'POST':
        id = request.POST.get('id')
        emp_name = request.POST.get('emp_name')
        emp_gender = request.POST.get('emp_gender')
        emp_phone = request.POST.get('emp_phone')
        print((id, emp_phone, emp_name, emp_gender))
        if all((id, emp_phone, emp_name, emp_gender)):
            sql = f"""INSERT INTO employees
            (`id`,`emp_name`, `emp_gender`, `emp_phone`)
            VALUES
            ({id},"{emp_name}", "{emp_gender}", "{emp_phone}");"""
            rows = get_data(sql)
            if rows:
                data = {
                    'status': '添加数据成功'
                }

    return JsonResponse(data=data, safe=True, json_dumps_params={"ensure_ascii": False})


# 展示添加员工页面
def show_add_emp(request):
    return render(request, 'add_emp.html', locals())


# 添加记录
def add_record(request):
    data = {
        'status': '添加数据失败'
    }
    if request.method == 'POST':
        meal_date = request.POST.get('meal_date')
        meal_emp_id = request.POST.get('meal_emp_id')
        meal_name = request.POST.get('meal_name')
        print((meal_emp_id, meal_date, meal_name,))
        if all((meal_emp_id, meal_date, meal_name,)):
            sql = f"""INSERT INTO meal_records
            (`meal_date`,`meal_emp_id`, `meal_name`)
            VALUES
            ("{meal_date}","{meal_emp_id}", "{meal_name}");"""
            try:
                rows = get_data(sql)
                if rows:
                    data = {
                        'status': '添加数据成功'
                    }
            except:
                data = {
                    'status': '添加数据失败,员工账号或用餐类型错误'
                }

    return JsonResponse(data=data, safe=True, json_dumps_params={"ensure_ascii": False})


# 展示添加就餐记录页面
def show_add_record(request):
    return render(request, 'add_record.html', locals())


def file_upload(request):
    return render(request, 'file_upload.html', locals())


# 这里是接收文件的地方
def test_file(request):
    import hashlib
    files = request.FILES.get('my_file')
    m = hashlib.md5()
    for i in files:
        m.update(i)
    hash_value = m.hexdigest()
    print(hash_value)
    zip_name = 'files/' + hash_value + '.zip'
    zip_folder = 'files/' + hash_value
    file_name = hash_value + '.zip'

    if not os.path.exists(zip_folder):
        os.mkdir(zip_folder)
    content_list = os.listdir('files')
    print(content_list)
    if file_name not in content_list:
        print('not')
        with open(zip_name, 'wb') as f:
            for i in files:
                f.write(i)

        zip_file = zipfile.ZipFile(zip_name)  # 文件的路径与文件名
        zip_list = zip_file.namelist()  # 得到压缩包里所有文件
        print(zip_list)

        for f in zip_list:
            zip_file.extract(f, zip_folder, pwd="mima".encode("utf8"))  # 循环解压文件到指定目录

        zip_file.close()  # 关闭文件，必须有，释放内存

        def make_zip(source_dir, output_filename):
            zipf = zipfile.ZipFile(output_filename, 'w')
            pre_len = len(os.path.dirname(source_dir))
            for parent, dirnames, filenames in os.walk(source_dir):
                for filename in filenames:
                    pathfile = os.path.join(parent, filename)
                    arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                    zipf.write(pathfile, arcname)
            zipf.close()

        make_zip(zip_folder, zip_name)

    file = open(zip_name, 'rb')

    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment;filename="{file_name}"'
    response['hash_value'] = hash_value
    return response
    # response = HttpResponse(file)
    # response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
    # response['Content-Disposition'] = 'attachment;filename="name.txt"'
    # return response
