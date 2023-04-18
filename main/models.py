from django.db import models

class OS(models.Model):
    id_os = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    date_start = models.DateField()
    date_end = models.DateField(null=True)
    description = models.CharField(max_length=1000, null=True)
    accepted = models.BooleanField()

class Devices(models.Model):
    id_device = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    premier = models.DateField()
    device_type = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    picture = models.BinaryField(null=True)
    accepted = models.BooleanField()

class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    login = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    theme = models.BooleanField()
    admin_acc = models.BooleanField()

class Followed_devices(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    devices_id = models.ForeignKey(Devices, on_delete=models.CASCADE)

class Specification(models.Model):
    id_spec = models.IntegerField(primary_key=True)
    processor = models.CharField(max_length=50, null=True)
    ram = models.IntegerField(null=True)
    memory = models.IntegerField(null=True)
    battery = models.IntegerField(null=True)
    size = models.CharField(max_length=10, null=True)
    price = models.FloatField(null=True)
    screen_type = models.CharField(max_length=20, null=True)
    devices_id = models.ForeignKey(Devices, on_delete=models.CASCADE)

class OS_devices(models.Model):
    os_id = models.ForeignKey(OS, on_delete=models.CASCADE)
    devices_id = models.ForeignKey(Devices, on_delete=models.CASCADE)

class Error_report(models.Model):
    id_error = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=500)
    date_start = models.DateField()
    date_end = models.DateField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    devices_id = models.ForeignKey(Devices, on_delete=models.CASCADE, null=True)
    os_id = models.ForeignKey(OS, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=250)
    main_comment_id = models.IntegerField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    devices_id = models.ForeignKey(Devices, on_delete=models.CASCADE, null=True)
    os_id = models.ForeignKey(OS, on_delete=models.CASCADE, null=True)

class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    os_id = models.ForeignKey(OS, on_delete=models.CASCADE, null=True)
    devices_id = models.ForeignKey(Devices, on_delete=models.CASCADE, null=True)
    like = models.BooleanField()
    dislike = models.BooleanField()