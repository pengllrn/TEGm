# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import models
import json

# Create your views here.
def ard_login(request,user_id,user_pwd):
    user = models.Login.objects.filter(pk=user_id)
    if user[0] != None:
        if user[0].user_id == user_id and user[0].user_pwd == user_pwd:
            request.session['IS_LOGIN'] = True
            return HttpResponse("true")
    return HttpResponse("false")

@csrf_exempt
def getFruits(request):
    fruits = models.Fruits.objects.all().order_by("id")
    fruit = fruits[0:99]
    print request.POST.get("username")
    c = {"fruits":formatDicts(fruit),"apple":formatDicts(fruit)}
    return HttpResponse(json.dumps(c["apple"]))

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

def get_detail_device(request):
    deviceid=request.POST.get("deviceid")
    if deviceid != None:
        device=models.Device.objects.filter(pk=deviceid)
        d = {}
        d["deviceNum"]=device.number
        type=models.DeviceType.objects.get(pk=device.typeid)
        d["deviceName"]=type.typename
        d["sensorNum"]=device.sensorid



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
        roomname = Room.building + " " + Room.roomname
        d["RoomId"] = roomname
        # 获取使用状态
        if d["UseFlag"] == 1:
            d["UseFlag"] = "正在使用"
        else:
            d["UseFlag"] = "未使用"
        # 添加设备类型图片的静态地址
        d["imgUrl"] = "http://192.168.1.20:9999/static/img/" + str(dv.typeid) + ".jpg"
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