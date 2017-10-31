# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import time
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import models
import json

url="http://192.168.1.20:9999"

icon_path = url+"static/img/"
damage_device_path = ""

# Create your views here.
def ard_login(request,user_id,user_pwd):
    user = models.Login.objects.filter(pk=user_id)
    if user[0] != None:
        if user[0].user_id == user_id and user[0].user_pwd == user_pwd:
            request.session['IS_LOGIN'] = True
            return HttpResponse("true")
    return HttpResponse("false")

def formatDicts(objs):
    obj_arr=[]
    for o in objs:
        obj_arr.append(o.format())
    return obj_arr

@csrf_exempt
def getDeviceInfo(request):
    is_login = request.session.get("IS_LOGIN",True)
    if is_login:
        obj_json={}
        devices = models.DeviceInfo.objects.all().order_by("id")
        obj_json["device"]=format_dev_info(devices)
        roominfo = models.RoomInfo.objects.all()
        obj_json["schoolbyid"]=format_room_info(roominfo)
        type =models.DeviceType.objects.all()
        obj_json["type"]=formatDicts(type)
        return HttpResponse(json.dumps(obj_json))

@csrf_exempt
def get_school_building_room(request):
    roominfo = models.RoomInfo.objects.all()
    obj_arr = []
    building = []
    for rm in roominfo:
        if not rm.building in building:
            building.append(rm.building)
    for bd in building:
        d = {}
        d["building"] = bd
        room=models.RoomInfo.objects.filter(building=bd)
        f = []
        for rm in room:
            e = {}
            e["roomname"]=rm.roomname
            f.append(e)
        d["room"]=f
        obj_arr.append(d)
    return HttpResponse(json.dumps(obj_arr))

@csrf_exempt
def get_detail_device(request):
    deviceid=request.POST.get("deviceid")
    if deviceid != None:
        device=models.Device.objects.get(pk=deviceid)
        dict1=device.format2()
        deviceinfo=models.DeviceInfo.objects.get(deviceid=deviceid)
        dict2=deviceinfo.format2()
        object_json=dict(dict1,**dict2)
        #获取type
        type = models.DeviceType.objects.get(pk=device.typeid)
        object_json["type"]=type.typename
        #获取sensor
        sensor = models.DeviceToSensor.objects.get(pk=device.sensorid)
        object_json["sensor"]=sensor.sensornum
        ##获取gis
        gis = models.DeviceGis.objects.get(deviceid=deviceid)
        object_json["gis"]="("+str(gis.latitude)+","+str(gis.longitude)+")"
        ##获取学校名字
        school=models.SchoolInfo.objects.get(pk=device.schoolid)
        object_json["schoolname"]=school.schoolname
        ##获取联系人电话
        person=models.UserModel.objects.get(pk=device.checkerid)
        object_json["checktel"]=person.telephonenum
        ##获取10天的使用率
        userate=models.DeviceUseRate.objects.filter(deviceid=deviceid).order_by("date")
        if len(userate)>10:
            userate_10=userate[len(userate)-10:len(userate)]
        else:
            userate_10=userate[0:10]
        object_json["userate_10"]=formatDicts(userate_10)
        ##初始化平均使用率
        object_json['avgrate']="0"
        ##获取房间信息
        room = models.RoomInfo.objects.get(pk=deviceinfo.roomid)
        object_json['roominfo']=room.format()
        # 获取使用状态
        if object_json["useflag"] == True:
            object_json["useflag"] = "正在使用"
        else:
            object_json["useflag"] = "未使用"
        return HttpResponse(json.dumps(object_json))
    return None


def format_dev_info(obj):
    device = obj[0:99]
    obj_arr = []
    for dv in device:
        d = dv.format()
        # 获取设备类型名
        Type = models.DeviceType.objects.get(pk=dv.typeid)
        typename = Type.typename
        d["TypeId"] = typename
        # 获取房间名
        Room = models.RoomInfo.objects.get(pk=dv.roomid)
        d["BuildName"]=Room.building
        d["RoomName"] = Room.roomname
        # 获取使用状态
        if d["UseFlag"] == 1:
            d["UseFlag"] = "正在使用"
        else:
            d["UseFlag"] = "未使用"
        # 添加设备类型图片的静态地址
        d["imgUrl"] = url+"/static/img/" + str(dv.typeid) + ".jpg"
        obj_arr.append(d)
    return obj_arr

def format_room_info(obj_roominfo):
    obj_arr = []
    building = []
    for rm in obj_roominfo:
        if not rm.building in building:
            building.append(rm.building)
    for bd in building:
        d = {}
        d["building"] = bd
        room = models.RoomInfo.objects.filter(building=bd)
        f = []
        for rm in room:
            e = {}
            e["roomname"] = rm.roomname
            f.append(e)
        d["room"] = f
        obj_arr.append(d)
    return obj_arr


@csrf_exempt
def device_damage_apply(request):
    if request.method == "POST":
        deviceid = request.POST.get("deviceid")
        record = models.PropertyDamage.objects.filter(deviceid=deviceid)
        if(record[0] !=None):
            return HttpResponse(json.dumps({"message":"This device had been recorded,needn't apply again!","code":0}))
        applierid = request.POST.get("applierid")
        appliername = request.POST.get("appliername")
        damagedepict = request.POST.get("damagedepict")
        vocie = request.POST.get("voice")
        datetime = request.POST.get("datetime")
        num=[0,1,2,3,4,5]
        photo=[None,None,None,None,None,None]
        for n in num:
            image = request.FILES.get('image'+str(n))
            if image==None:
                break
            else:
                f = open(".//TEGApp//static//damageapply_img//" + image.name, 'wb')
                for chunk in image.chunks(chunk_size=1024):
                    f.write(chunk)
                    photo[n]=url+"/static/damageapply_img/"+image.name
        if deviceid != None and applierid != None and damagedepict != None and photo[0] != None and datetime != None:
            damagedevice = models.PropertyDamage.objects.create(deviceid=deviceid, applierid=applierid, applier=appliername,
                datetime=datetime, damagedepict=damagedepict, photo1=photo[0],photo2=photo[1], photo3=photo[2],
                photo4=photo[3],photo5=photo[4],photo6=photo[5],voice=vocie)
            damagedevice.save()
        return HttpResponse(json.dumps({"message":"This device had been recorded successfully!","code":1}))
    return HttpResponse(json.dumps({"message":"System Error!","code":-1}))


class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    headImg = forms.FileField()

@csrf_exempt
def search_device_bynum(request):
    devicenum = request.POST.get("devicenum")
    device = models.DeviceInfo.objects.filter(devicenum=devicenum)
    d = {}
    if device[0]!=None:
        d["deviceid"]=device[0].deviceid
        type=models.DeviceType.objects.get(pk=device[0].typeid)
        d["devicetype"]=type.typename
        room=models.RoomInfo.objects.get(pk=device[0].roomid)
        d["deviceplace"]=room.building+"  "+room.roomname
    return HttpResponse(json.dumps(d))


