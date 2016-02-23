## Machine


分享照片，电子书，视频的网站，后续添加各种功能

## Deploy:
####1.Install packages:
`pip install -r requirements.txt`

####2.Create database
Edit database configuration in settings.py, then use your local mysql.
`python manage.py makemigrations`
`python manage.py migrate`

####3.Run
`python manage.py runserver 0.0.0.0:8000`


##To-Do:
####1. admin对照片批量管理
####2. 对照片评论
####3. 电子书上传分享，下载
####4. 视频
