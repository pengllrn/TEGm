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
    number = models.CharField(db_column='Number',max_length=20,blank=True,null=True) #设备编号(可能不唯一)
    typeid = models.IntegerField(db_column="TypeId",blank=True,null=True)  #设备类型id
    univalence = models.FloatField(db_column='Univalence',blank=True,null=True)  #设备单价
    #indentifier = models.CharField(db_column='Identifier',max_length=50,blank=True,null=True)  #传感器的编号
    sensorid = models.IntegerField(db_column='SensorId',blank=True, null=True)  # 传感器的编号
    schoolid = models.IntegerField(db_column='SchoolId',blank=True,null=True)  #学校id
    checkerid = models.IntegerField(db_column="CheckerId",blank=True,null=True) #检查人，负责人编号
    checkername = models.CharField(db_column='CheckerName',max_length=20,blank=True,null=True) #负责人的名字
    status = models.IntegerField(db_column="Status",blank=True,null=True) #设备的状态

    class Meta:
        db_table = 'Device'

class DeviceGis(models.Model):
    longitude = models.FloatField(db_column='Longitude',blank=True,null=True)  #经度
    latitude = models.FloatField(db_column='Latitude',blank=True,null=True)  #维度
    deviceid = models.IntegerField(db_column="DeviceId",blank=True,null=True)  #设备ID
    devicenum = models.CharField(db_column='DeviceNum', max_length=20, blank=True, null=True)  # 设备编号
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # 学校id

    class Meta:
        db_table = 'DeviceGis'

class DeviceAlarm(models.Model):
    deviceid = models.IntegerField(db_column="DeviceId", blank=True, null=True)  # 设备ID
    devicenum = models.CharField(db_column='DeviceNum', max_length=20, blank=True, null=True)  # 设备编号
    schoolid = models.IntegerField(db_column='SchoolId',blank=True, null=True)  # 学校id
    roomid = models.IntegerField(db_column='RoomId',blank=True, null=True) #房间ID
    ordernum = models.IntegerField(db_column='OrderNum',blank=True, null=True)  #设备在房间里的序号
    alarmstart = models.BooleanField(db_column='AlarmStart',blank=True)  #设备是否处于报警状态

    class Meta:
        db_table = 'DeviceAlarm'

class DeviceUseRecord(models.Model):
    deviceid = models.IntegerField(db_column="DeviceId", blank=True, null=True)  # 设备ID
    schoolid = models.IntegerField(db_column='SchoolId',blank=True, null=True)  # 学校id
    existimage = models.BooleanField(db_column='ExistImage',blank=True)  #是否有图像
    imageaddress = models.CharField(db_column='ImageAddress', max_length=40,blank=True, null=True)  # 图片地址
    begintime = models.DateField(db_column='BeginTime',blank=True, null=True)  #设备开始使用的时间
    endtime = models.DateField(db_column='EndTime',blank=True, null=True)  #设备结束使用的时间

    class Meta:
        db_table = 'DeviceUseRecord'

class DeviceToSensor(models.Model):
    sensornum = models.CharField(db_column='SensorNum', max_length=50, blank=True, null=True)  # 传感器的编号
    #indentifier = models.CharField(db_column='Identifier', max_length=50, blank=True, null=True)  # 传感器的编号
    #sensorid = models.IntegerField(db_column='SensorId',blank=True, null=True) #传感的硬件编号

    class Meta:
        db_table = 'DeviceToSensor'

class DeviceType(models.Model):
    #typeid = models.IntegerField(db_column="TypeId", blank=True, null=True)  # 设备类型id
    typename = models.CharField(db_column="TypeName",max_length=30,blank=True,null=True)  #设备名称

    class Meta:
        db_table = "DeviceType"

class SchoolInfo(models.Model):
    #schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # 学校id
    schoolname = models.CharField(db_column='SchoolName',max_length=40,blank=True,null=True)  #学校名字
    schoolregister = models.CharField(db_column="SchoolRegister",max_length=50,blank=True,null=True)  #学校的注册号
    schoolstatus = models.IntegerField(db_column='SchoolStatus',blank=True,null=True)  #学校的状态
    schoolresper = models.IntegerField(db_column="SchoolResper",blank=True,null=True)  #学校负责人id
    schooltel = models.CharField(db_column="SchoolTel",max_length=20,blank=True,null=True)  #学校联系电话

    class Meta:
        db_table = "SchoolInfo"

class UserModel(models.Model):
    userid = models.CharField(db_column='UserId',max_length=40,blank=True,null=True)  #用户账号
    userpassword = models.CharField(db_column='UserPassword',max_length=40,blank=True,null=True)  #用户密码
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  #用户姓名
    authority = models.BooleanField(db_column='Authority',blank=True)  #操作权限:查看，维护
    systemcontrol = models.BooleanField(db_column='SystemControl',blank=True)  #系统权限：审核
    level = models.IntegerField(db_column='Level',blank=True,null=True)  #用户等级
    email = models.EmailField(db_column='Email', blank=True, null=True)  #Email
    telephonenum = models.TextField(db_column='TelephoneNum', blank=True, null=True) #Tel
    weixin = models.TextField(db_column='Weixin', blank=True, null=True) #微信

    class Meta:
        db_table = 'UserModel'

class UserAuthority(models.Model):
    userid = models.CharField(db_column='UserId', max_length=40, blank=True, null=True)  # 用户账号
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # 学校id

    class Meta:
        db_table = 'UserAuthority'

class PropertyDamage(models.Model):
    deviceid = models.IntegerField(db_column="DeviceId", blank=True, null=True)  # 设备ID
    applier = models.CharField(db_column='Applier',max_length=40,blank=True,null=True)  #申请人姓名
    applierid = models.IntegerField(db_column='ApplierId',blank=True,null=True) #申请人ID
    appliertel = models.TextField(db_column="ApplierTel",blank=True,null=True)  #申请人电话
    datetime = models.DateField(db_column='DateTime',blank=True,null=True)  #申述时间

    class Meta:
        db_table = "PropertyDamage"

class PropertyCheck(models.Model):
    deviceid = models.IntegerField(db_column="DeviceId", blank=True, null=True)  # 设备ID
    checkerid = models.CharField(db_column='CheckerId',max_length=40,blank=True,null=True)  #审核人ID
    checkername = models.CharField(db_column='CheckerName',max_length=40,blank=True,null=True) #审核人姓名
    checketime = models.DateField(db_column='CheckeTime',blank=True,null=True)  #审核时间
    checkerflag = models.BooleanField(db_column='CheckFlag',blank=True)  #审核结果

    class Meta:
        db_table = 'PropertyCheck'

class DeviceInfo(models.Model):
    deviceid = models.IntegerField(db_column="DeviceId", blank=True, null=True)  # 设备ID
    devicenum = models.CharField(db_column='DeviceNum', max_length=20, blank=True, null=True)  # 设备唯一的编号
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # 学校id
    typeid = models.IntegerField(db_column="TypeId", blank=True, null=True)  # 设备类型id
    roomid = models.CharField(db_column='RoomId', max_length=20, blank=True, null=True)  #房间ID
    ordernum = models.IntegerField(db_column='OrderNum', blank=True, null=True)  # 设备在房间里的序号
    devicekind = models.CharField(db_column='DeviceKind',max_length=50,blank=True,null=True)  #设备型号
    description = models.TextField(db_column='Description',blank=True,null=True)  #设备描述
    configureinfo = models.CharField(db_column='ConfigureInfo',max_length=30,blank=True,null=True)  #配置信息
    useflag = models.BooleanField(db_column="UseFlag",blank=True)  #使用状态

    def __str__(self):
        return self.id
    def format(self):
        return {u'DeviceId':self.deviceid,u'TypeId':self.typeid,u'DeviceNum':self.devicenum,u'RoomId':self.roomid,
                u'OrderNum':self.ordernum,u'UseFlag':self.useflag}

    class Meta:
        db_table = 'DeviceInfo'

class RoomInfo(models.Model):
    schoolid = models.IntegerField(db_column='SchoolId', blank=True, null=True)  # 学校id
    building = models.CharField(db_column='Building',max_length=50,blank=True,null=True)  #楼层名
    roomname = models.CharField(db_column='RoomName',max_length=50,blank=True,null=True)  #房间名

    class Meta:
        db_table = 'RoomInfo'











