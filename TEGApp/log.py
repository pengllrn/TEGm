#coding=utf-8
import time

class Log(object):
    def write_msg(self,msg):
        fo = open("log.txt","ab")
        fo.write(time.strftime("%Y-%m-%d %H:%M", time.localtime())+"    ")
        fo.write(msg + '\n')