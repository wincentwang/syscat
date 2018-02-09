# -*- coding: utf-8 -*-
import psutil
import time


# CPU Info
def getCPUCount():
	return {'cc':psutil.cpu_count(),'ccl':psutil.cpu_count(logical=False)}

# Physic Memory
def getPhyMem():
	total="%.1f G"%(psutil.virtual_memory().total/1024/1024/1024)
	available='%.1f G'%(psutil.virtual_memory().total/1024/1024/1024)
	percent='%.1f %%'%psutil.virtual_memory().percent
	used='%.1f G'%(psutil.virtual_memory().used/1024/1024/1024)
	free='%.1f G'%(psutil.virtual_memory().free/1024/1024/1024)
	return {'total':total,'available':available,'used':used,'free':free}

# Disk Info
def getDisk():
	total='%.1f'%(psutil.disk_usage('/').total/1024/1024/1024)
	used='%.1f G'%(psutil.disk_usage('/').used/1024/1024/1024)
	free='%.1f G'%(psutil.disk_usage('/').free/1024/1024/1024)
	percent='%.1f %%'%psutil.disk_usage('/').percent
	return {'total':total,'used':used,'free':'free','percent':percent}





