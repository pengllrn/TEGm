# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Login(models.Model):
    user_id = models.CharField(max_length=40,primary_key=True)
    user_pwd = models.CharField(max_length=40)

    class Meta:
        db_table = 'Login'

class Fruits(models.Model):
    fruitname = models.CharField(max_length=40)
    def __str__(self):
        return self.id
    def format(self):
        return {u'id':self.id,u'fruitname':self.fruitname}

    class Meta:
        db_table = 'Fruits'

class Test(models.Model):
    nametest = models.CharField(max_length=10,blank=True,null=True)

    class Meta:
        db_table='test'

class Device(models.Model):
    number = models.CharField(db_column='Number',max_length=20,blank=True,null=True) #设备唯一的编号
    typeid = models.IntegerField(db_column="TypeId",blank=True,null=True)  #设备类型id
    univalence = models.FloatField(db_column='Univalence',blank=True,null=True)  #设备单价
    indentifier = models.CharField(db_column='Identifier',max_length=50,blank=True,null=True)  #传感器的编号
    schoolid = models.IntegerField(db_column='SchoolId',blank=True,null=True)  #学校id
    checkerid = models.IntegerField(db_column="CheckerId",blank=True,null=True) #检查人，负责人编号
    checkername = models.CharField(db_column='CheckerName',blank=True,null=True) #负责人的名字
    status = models.IntegerField(db_column="Status",blank=True,null=True) #设备的状态

    class Meta:
        db_table = 'Device'

class DeviceGis(models.Model):
    longitude = models.FloatField(db_column='Longitude',blank=True,null=True)  #经度
    latitude = models.FloatField(db_column='Latitude',blank=True,null=True)  #维度
    deviceid = models.IntegerField(db_column="DeviceId",blank=True,null=True)  #设备ID
    deviceno = models.CharField(db_column='DeviceNo', max_length=20, blank=True, null=True)  # 设备唯一的编号
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # 学校id

    class Meta:
        db_table = 'GisDevice'

class DeviceAlarm:
    deviceid = models.IntegerField(db_column="DeviceId", blank=True, null=True)  # 设备ID
    deviceno = models.CharField(db_column='DeviceNo', max_length=20, blank=True, null=True)  # 设备唯一的编号
    schoolid = models.IntegerField(db_column='SchoolId',blank=True, null=True)  # 学校id
    roomid = models.CharField(db_column='RoomId',max_length=20,blank=True, null=True) #房间ID
    orderno = models.IntegerField(db_column='OrderNo',blank=True, null=True)  #设备在房间里的序号
    alarmstart = models.BooleanField(db_column='AlarmStart',blank=True, null=True)  #设备是否处于报警状态

    class Meta:
        db_table = 'DeviceAlarm'

class DeviceUseRecord:
    deviceid = models.IntegerField(db_column="DeviceId", blank=True, null=True)  # 设备ID
    schoolid = models.IntegerField(db_column='SchoolId',blank=True, null=True)  # 学校id
    existimage = models.BooleanField(db_column='ExistImage',blank=True, null=True)  #是否有图像
    imageaddress = models.CharField(db_column='ImageAddress', blank=True, null=True)  # 图片地址
    begintime = models.DateField(db_column='BeginTime',blank=True, null=True)  #设备开始使用的时间
    endtime = models.DateField(db_column='EndTime',blank=True, null=True)  #设备结束使用的时间

    class Meta:
        db_table = 'DeviceUseRecord'

class DeviceToSensor:
    indentifier = models.CharField(db_column='Identifier', max_length=50, blank=True, null=True)  # 传感器的编号
    sensorid = models.IntegerField(db_column='SensorId',blank=True, null=True) #传感的硬件编号

    class Meta:
        db_table = 'DeviceToSensor'

class DeviceType:
    typeid = models.IntegerField(db_column="TypeId", blank=True, null=True)  # 设备类型id
    typename = models.CharField(db_column="TypeName",blank=True,null=True)  #设备名称

    class Meta:
        db_table = "DeviceType"

class SchoolInfo:
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # 学校id
    schoolname = models.CharField(db_column='SchoolName',max_length=40,blank=True,null=True)  #学校名字
    schoolregister = models.CharField(db_column="SchoolRegister",max_length=50,blank=True,null=True)  #学校的注册号
    schoolstatus = models.IntegerField(db_column='SchoolStatus',blank=True,null=True)  #学校的状态
    schoolresper = models.IntegerField(db_column="SchoolResper",blank=True,null=True)  #学校负责人id
    schooltel = models.CharField(db_column="SchoolTel",max_length=20,blank=True,null=True)  #学校联系电话

    class Meta:
        db_table = "SchoolInfo"









