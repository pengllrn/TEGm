# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import models
from . import log
import json

# Create your views here.
def ard_login(request,user_id,user_pwd):
    user = models.Login.objects.filter(pk=user_id)
    msg = log.Log()
    msg.write_msg( request.META.get("REMOTE_ADDR")+" try to login")
    if user[0] != None:
        if user[0].user_id == user_id and user[0].user_pwd == user_pwd:
            msg.write_msg(request.META.get("REMOTE_ADDR") + " login success!"+'\n')
            return HttpResponse("true")
    msg.write_msg(request.META.get("REMOTE_ADDR") + " login debeat!"+'\n')
    return HttpResponse("false")

@csrf_exempt
def getFruits(request):
    fruits = models.Fruits.objects.all().order_by("id")
    fruit = fruits[0:99]
    print request.POST.get("username")

    #     d[fruit.id] = fruit.fruitname
    c = {"fruits":formatDicts(fruit),}
    return HttpResponse(json.dumps(c["fruits"]))

def formatDicts(objs):
    obj_arr=[]
    for o in objs:
        obj_arr.append(o.format())
    return obj_arr

@csrf_exempt
def getDeviceInfo(request):
    devices = models.DeviceInfo.objects.all().order_by("id")
    device = devices[0:99]
    obj_arr=[]
    for dv in device:
        d = dv.format()
        # School=models.SchoolInfo.objects.get(pk =dv.schoolid)
        # name =School.schoolname
        # d["SchoolName"] = name
        Type = models.DeviceType.objects.get(pk = dv.typeid)
        typename = Type.typename
        d["TypeId"] = typename

        Room = models.RoomInfo.objects.get(pk = dv.roomid)
        roomname = Room.building+" "+Room.roomname
        d["RoomId"] = roomname

        if d["UseFlag"]== 1:
            d["UseFlag"]="（正在使用）"
        else:
            d["UseFlag"] = "（未使用）"
        obj_arr.append(d)
    return HttpResponse(json.dumps(obj_arr))

