from bitstream import *
from Packet import *
from DBHandlers import *


class Writable:
	def _isWritable(self):
		return True

###################### Component 1 Stuff ######################
class Component1_Data1():
	def __init__(self, d1, d2, d3):
		self.d1 = c_ulong(d1)
		self.d2 = c_bit(d2)
		self.d3 = c_bit(d3)

class Component1_Data2():
	def __init__(self, d1, d2, d3, d4, d5, d6, d7):
		self.d1 = c_ulong(d1)
		self.d2 = c_ulong(d2)
		self.d3 = c_ulong(d3)
		self.d4 = c_ulong(d4)
		self.d5 = c_ulong(d5)
		self.d6 = c_ulong(d6)
		self.d7 = c_ulong(d7)

class Component1_Data3():
	def __init__(self, d1, d2):
		self.d1 = c_float(d1)
		self.d2 = c_float(d2)

class Component1_Data4():
	def __init__(self, d1, d2):
		self.d1 = c_ulong(d1)
		self.d2 = c_bit(d2)

class Component1_Data5():
	def __init__(self, d1, d2):
		self.d1 = c_ulong(d1)
		self.d2 = c_bit(d2)

class Component1_Position():
	def __init__(self, x, y, z):
		self.x = c_float(x)
		self.y = c_float(y)
		self.z = c_float(z)


class Component1_Rotation():
	def __init__(self, x, y, z, w):
		self.x = c_float(x)
		self.y = c_float(y)
		self.z = c_float(z)
		self.w = c_float(w)


class Component1_Data6():
	def __init__(self, position, rotation, onGround, d4):
		self.position = position
		self.rotation = rotation
		self.onGround = c_bit(onGround)
		self.d4 = c_bit(d4)

class Component1_Velocity():
	def __init__(self, x, y, z):
		self.x = c_float(x)
		self.y = c_float(y)
		self.z = c_float(z)



class Component1_Velocity_Angular():
	def __init__(self, x, y, z):
		self.x = c_float(x)
		self.y = c_float(y)
		self.z = c_float(z)


class Component1_Data6_3():
	def __init__(self, objid, d2, d3, d4):
		self.objid = c_longlong(objid)
		self.d2 = c_float(d2)
		self.d3 = c_float(d3)
		self.d4 = c_float(d4)


class Component1_Data3_1():
	def __init__(self, d1, d2, d3):
		self.d1 = c_float(d1)
		self.d2 = c_float(d2)
		self.d3 = c_float(d3)
###################### End of 1 Stuff ######################


##################### Comonent 4 Stuff #####################
class Component4_Data3:
	def __init__(self, d1, d2):
		self.d1 = c_bit(d1)
		self.d2 = c_bit(d2)


class Component4_Data9:
	def __init__(self, d1=False, d2=False, d3=0, d4=False, d5=0):
		self.a = c_bit(d1)
		self.b = c_bit(d2)
		self.c = c_ubyte(d3)
		self.d = c_bit(d4)
		self.e = c_ubyte(d5)

class Component4_Data11:
	def __init__(self, d1=1, d2=0, d3=True, d4=0xFFFFFFFF):
		self.a = c_ulonglong(d1)
		self.b = c_ubyte(d2)
		self.c = c_bit(d3)
		self.d = c_ulong(d4)
###################### End of 4 Stuff ######################


class PlayerStyle():
	def __init__(self):
		self.a = c_ulong(0)#hairColor
		self.b = c_ulong(0)#hairStyle
		self.c = c_ulong(0)#HD_HDC
		self.d = c_ulong(0)#shirtColor
		self.e = c_ulong(0)#pantsColor
		self.f = c_ulong(0)#CD
		self.g = c_ulong(0)#HDC_HD
		self.h = c_ulong(0)#eyebrowsStyle
		self.i = c_ulong(0)#eyesStyle
		self.j = c_ulong(0)#mouthStyle
	def setStyle(self, playerID):
		data = getCharacterDataByID(str(playerID))
		self.a = c_ulong(data[7])
		self.b = c_ulong(data[8])
		self.c = c_ulong(0)
		self.d = c_ulong(data[4])
		self.e = c_ulong(data[6])
		self.f = c_ulong(0)
		self.g = c_ulong(0)
		self.h = c_ulong(data[11])
		self.i = c_ulong(data[12])
		self.j = c_ulong(data[13])

class PlayerInfo():
	def __init__(self):
		self.a = None
		self.b = c_ulonglong(0)
		self.c = c_ulonglong(0)
		self.d = None
		self.e = c_bit(False)
	def setInfo(self, playerID):
		data = getCharacterDataByID(str(playerID))
		self.a = c_ulonglong(int(data[1]))
		self.d = c_ulonglong(int(data[23]))

class PlayerStats():
	def __init__(self):
		self.a = c_ulonglong(0)
		self.b = c_ulonglong(0)
		self.c = c_ulonglong(0)
		self.d = c_ulonglong(0)
		self.e = c_ulonglong(0)
		self.f = c_ulonglong(0)
		self.g = c_ulonglong(0)
		self.h = c_ulonglong(0)
		self.i = c_ulonglong(0)
		self.j = c_ulonglong(0)
		self.k = c_ulonglong(0)
		self.l = c_ulonglong(0)
		self.m = c_ulonglong(0)
		self.n = c_ulonglong(0)
		self.o = c_ulonglong(0)
		self.p = c_ulonglong(0)
		self.q = c_ulonglong(0)
		self.r = c_ulonglong(0)
		self.s = c_ulonglong(0)
		self.t = c_ulonglong(0)
		self.u = c_ulonglong(0)
		self.v = c_ulonglong(0)
		self.w = c_ulonglong(0)
		self.x = c_ulonglong(0)
		self.y = c_ulonglong(0)
		self.z = c_ulonglong(0)
		self.z1 = c_ulonglong(0)

class ControllablePhysicsComponent:
	def __init__(self):
		self.flag1 = False #Boolean
		self.data1 = None #Component1Data1
		self.flag2 = False #Boolean
		self.data2 = None #Component1Data2
		self.flag3 = False #Boolean
		self.data3 = None #Component1Data3
		self.flag4 = False #Boolean
		self.data4 = None #Component1Data4
		self.flag5 = False #Boolean
		self.flag5_1 = False #Boolean
		self.data5 = None #Component1Data5
		self.flag6 = False #Boolean
		self.data6 = None #Component1Data6
		self.flag6_1 = False #Boolean
		self.data6_1 = None #Component1_Velocity
		self.flag6_2 = False #Boolean
		self.data6_2 = None #Component1_Velocity_Angular
		self.flag6_3 = False #Boolean
		self.data6_3 = None #Component1Data6_3
		self.flag6_3_1 = False #Boolean
		self.data6_3_1 = None #Component1_Data3_1

	def get_packet(self, PACKET_TYPE):
		packet = BitStream()
		if(PACKET_TYPE == ReplicaTypes.REPLICA_CONSTRUCTION_PACKET):#Creation only data
			packet.write(c_bit(self.flag1))
			if(self.flag1 == True):
				packet.write(self.data1.d1)
				packet.write(self.data1.d2)
				packet.write(self.data1.d3)
			packet.write(c_bit(self.flag2))
			if(self.flag2 == True):
				packet.write(self.data2.d1)
				packet.write(self.data2.d2)
				packet.write(self.data2.d3)
				packet.write(self.data2.d4)
				packet.write(self.data2.d5)
				packet.write(self.data2.d6)
				packet.write(self.data2.d7)
		#End of creation only
		packet.write(c_bit(self.flag3))
		if(self.data3 == True):
			packet.write(self.data3.d1)
			packet.write(self.data3.d2)
		packet.write(c_bit(self.flag4))
		if(self.data4 == True):
			packet.write(self.data4.d1)
			packet.write(self.data4.d2)
		packet.write(c_bit(self.flag5))
		if(self.flag5 == True):
			packet.write(c_bit(self.flag5_1))
			if(self.flag5_1 == True):
				packet.write(self.data5.d1)
				packet.write(self.data5.d2)
		packet.write(c_bit(self.flag6))
		if(self.flag6 == True):
			packet.write(self.data6.position.x)#Position
			packet.write(self.data6.position.y)
			packet.write(self.data6.position.z)
			packet.write(self.data6.rotation.x)#Rotation
			packet.write(self.data6.rotation.y)
			packet.write(self.data6.rotation.z)
			packet.write(self.data6.rotation.w)
			packet.write(self.data6.onGround)
			packet.write(self.data6.d4)
			packet.write(c_bit(self.flag6_1))
			if(self.flag6_1 == True):#Velocity
				packet.write(self.data6_1.x)
				packet.write(self.data6_1.y)
				packet.write(self.data6_1.z)
			packet.write(c_bit(self.flag6_2))
			if(self.flag6_2 == True):#Angular Velocity
				packet.write(self.data6_2.x)
				packet.write(self.data6_2.y)
				packet.write(self.data6_2.z)
			packet.write(c_bit(self.flag6_3))
			if(self.flag6_3 == True):
				packet.write(self.data6_3.objid)
				packet.write(self.data6_3.d2)
				packet.write(self.data6_3.d3)
				packet.write(self.data6_3.d4)
				packet.write(c_bit(self.flag6_3_1))
				if(self.flag6_3_1 == True):
					packet.write(self.data6_3_1.d1)
					packet.write(self.data6_3_1.d2)
					packet.write(self.data6_3_1.d3)
		if(PACKET_TYPE == ReplicaTypes.REPLICA_SERIALIZATION_PACKET):#Serialization only
			packet.write(c_bit(True))
		return packet


class CharacterComponent:
	def __init__(self):
		self.flag1 = False
		self.flag1_1 = False
		self.data1_1 = c_ulonglong(0)#ULongLong
		self.data1_2 = c_bit(0)#Ubyte
		self.hasLevel = False
		self.level = 0#ULong
		self.flag3 = False
		self.data3 = None#Component4Data3
		self.flag4 = False
		self.data4 = c_ulonglong(0)#ULongLong
		self.flag5 = False
		self.data5 = c_ulonglong(0)#ULongLong
		self.flag6 = False
		self.data6 = c_ulonglong(0)#ULongLong
		self.flag7 = False
		self.data7 = c_ulonglong(0)#ULongLong
		self.style = None#PlayerStyle
		self.info = None#PlayerInfo
		self.stats = None#PlayerStats
		self.flag8a = False
		self.flag8b = False
		self.data8 = ""#WString
		self.flag9 = False
		self.data9 = None#Component4_Data9
		self.flag10 = False
		self.headGlow = c_ulong(1)#ULong
		self.flag11 = False
		self.data11 = None#Component4_Data11

	def get_packet(self, PACKET_TYPE):
		packet = BitStream()
		packet.write(c_bit(self.flag1))
		if(self.flag1 == True):
			packet.write(c_bit(self.flag1_1))
			if(self.flag1_1 == True):
				packet.write(self.data1_1)
			packet.write(self.data1_2)
		packet.write(c_bit(self.hasLevel))
		if(self.hasLevel == True):
			packet.write(self.level)
		packet.write(c_bit(self.flag3))
		if(self.flag3 == True):
			packet.write(self.data3.d1)
			packet.write(self.data3.d2)
		if(PACKET_TYPE == ReplicaTypes.REPLICA_CONSTRUCTION_PACKET):#Construction only
			packet.write(c_bit(self.flag4))
			if(self.flag4 == True):
				packet.write(self.data4)
			packet.write(c_bit(self.flag5))
			if(self.flag5 == True):
				packet.write(self.data5)
			packet.write(c_bit(self.flag6))
			if(self.flag6 == True):
				packet.write(self.data6)
			packet.write(c_bit(self.flag7))
			if(self.flag7 == True):
				packet.write(self.data7)
			#PlayerStyle
			packet.writeTemplate(self.style)
			############
			#PlayerInfo
			packet.writeTemplate(self.info)
			###########
			#PlayerStats
			for _ in range (27):
				packet.write(c_ulonglong(0))
			############
			packet.write(c_bit(self.flag8a))
			packet.write(c_bit(self.flag8b))
			if(self.flag8b == True and self.flag8a == False):
				encodedData = self.data8.encode("utf-16-le")
				packet.write(c_ushort(len(encodedData)))  # wString length
				packet.write_bits(encodedData, number_of_bits=len(encodedData))  # String
		packet.write(c_bit(False))
		packet.write(c_bit(True))
		packet.write(self.headGlow)
		packet.write(c_bit(False))
		return packet

class BaseData:
	def __init__(self):
		self.objectID = c_longlong(0) #LongLong
		self.LOT = c_long(0)#Long
		self.NameLength = c_byte(0) #UChar
		self.Name = "" #WString
		self.Time_Since_Created = c_ulong(0)
		self.flag1 = False
		self.SizeOfStruct = c_ulong(0)#ULong
		self.LDF_1 = None
		self.trigger = False
		self.flag2 = False
		self.SpawnerObjID = c_longlong(0)#LongLong
		self.flag3 = False
		self.SpawnerNode = c_ulong(0)#ULong
		self.ScaleFlag = True
		self.Scale = c_float(1)
		self.flag4 = False
		self.objectWorldState = c_byte(0)#UChar
		self.flag5 = False
		self.gmLevel = c_byte(0)#UChar
		self.flag6 = False
		self.flag6_1 = False
		self.ParentID = c_longlong(0)#LongLong
		self.data6_1_1 = c_bit(0)#Bit
		self.flag6_2 = False
		self.Count = c_ushort(0)#UShort
		self.ChildObjIds = c_longlong(0)#LongLong
	def get_packet(self, PacketType):
		packet = BitStream()
		if(PacketType == ReplicaTypes.REPLICA_CONSTRUCTION_PACKET):
			packet.write(self.objectID)
			packet.write(self.LOT)
			packet.write(c_byte(self.NameLength))
			if(self.NameLength != c_byte(0)):
				strBuffer = BitStream()
				strBuffer.write(self.Name, allocated_length=(self.NameLength*2)+2)
				packet.write(strBuffer[:-2])
			packet.write(self.Time_Since_Created)
			packet.write(c_bit(self.flag1))
			if(self.flag1 == True):
				packet.write(self.SizeOfStruct)
				packet.write(self.LDF_1)
			packet.write(c_bit(self.trigger))
			packet.write(c_bit(self.flag2))
			if(self.flag2 == True):
				packet.write(self.SpawnerObjID)
			packet.write(c_bit(self.flag3))
			if(self.flag3 == True):
				packet.write(self.SpawnerNode)
			packet.write(c_bit(self.ScaleFlag))
			if(self.ScaleFlag == True):
				packet.write(self.Scale)
			packet.write(c_bit(self.flag4))
			if(self.flag4 == True):
				packet.write(self.objectWorldState)
			packet.write(c_bit(self.flag5))
			if(self.flag5 == True):
				packet.write(self.gmLevel)
		packet.write(c_bit(self.flag6))
		if(self.flag6 == True):
			packet.write(c_bit(self.flag6_1))
			if(self.flag6_1 == True):
				packet.write(self.ParentID)
				packet.write(self.data6_1_1)
			packet.write(c_bit(self.flag6_2))
			if(self.flag6_2 == True):
				packet.write(self.Count)
				packet.write(self.ChildObjIds)
		return packet

class DestructibleIndex():
	def __init__(self):
		self.flag1 = False
		self.data1_1 = c_ulong(0)#ULong
		self.data1_2 = c_ulong(0)#ULong
		self.flag1_1 = False
		self.data1_1_1 = c_ulong(0)#ULong
		self.unknown1 = False
		self.unknown2 = False
		self.unknown3 = False
		self.unknown4 = False
		self.unknown5 = False
		self.unknown6 = False
		self.unknown7 = False
		self.unknown8 = False
		self.trigger = False
		self.unknown9 = False
		self.trigger_1 = c_longlong(0)#LongLong
		self.data1_3 = c_ulong(0)#ULong
	def get_packet(self, PacketType):
		packet = BitStream()
		if(PacketType == ReplicaTypes.REPLICA_CONSTRUCTION_PACKET):
			packet.write(c_bit(self.flag1))
			if(self.flag1 == True):
				packet.write(self.data1_1)
				packet.write(self.data1_2)
				packet.write(c_bit(self.flag1_1))
				packet.write(self.data1_1_1)
				packet.write(self.unknown1)
				packet.write(self.unknown2)
				packet.write(self.unknown3)
				packet.write(self.unknown4)
				packet.write(self.unknown5)
				packet.write(self.unknown6)
				packet.write(self.unknown7)
				packet.write(self.unknown8)
				packet.write(c_bit(self.trigger))
				packet.write(self.unknown9)
				if(self.trigger == True):
					packet.write(self.trigger_1)
				packet.write(self.data1_3)
			packet.write(c_bit(False))
		return packet

class StatsIndex():
	def __init__(self):
		self.flag1 = False
		self.data1_1 = c_ulong(0)  # ULong
		self.isBoss = c_ulong(0)  # ULong
		self.data1_3 = c_ulong(0)  # ULong
		self.data1_4 = c_ulong(0)  # ULong
		self.data1_5 = c_ulong(0)  # ULong
		self.data1_6 = c_ulong(0)  # ULong
		self.data1_7 = c_ulong(0)  # ULong
		self.data1_8 = c_ulong(0)  # ULong
		self.data1_9 = c_ulong(0)  # ULong

		self.flag2 = False
		self.currentHealth = c_ulong(20)#Ulong
		self.weirdFloat1 = c_float(1)
		self.currentArmor = c_ulong(20)#Ulong
		self.weirdFloat2 = c_float(1)
		self.currentImagination = c_ulong(20)#Ulong
		self.weirdFloat3 = c_float(1)
		self.data2_1 = c_ulong(0)
		self.data2_2 = c_bit(False)
		self.data2_3 = c_bit(False)
		self.data2_4 = c_bit(False)
		self.maxHealth = c_float(20)  # Float
		self.maxArmor = c_float(20)  # Float
		self.maxImagination = c_float(20)  # Float
		self.count = c_ulong(1)#ULong
		self.factionID = c_long(1)#Long
		self.isSmashable = False

		self.bit1 = c_bit(False)
		self.bit2 = c_bit(False)
		self.smashable1 = c_bit(False)
		self.smashable2 = c_bit(False)
		self.smashable2_1 = None#Ulong

		self.flag3 = False
		self.data3_1 = c_bit(False)
	def get_packet(self, PacketType):
		packet = BitStream()
		if(PacketType == ReplicaTypes.REPLICA_CONSTRUCTION_PACKET):
			packet.write(c_bit(self.flag1))
			if(self.flag1 == True):
				packet.write(self.data1_1)
				packet.write(self.isBoss)
				packet.write(self.data1_3)
				packet.write(self.data1_4)
				packet.write(self.data1_5)
				packet.write(self.data1_6)
				packet.write(self.data1_7)
				packet.write(self.data1_8)
				packet.write(self.data1_9)
		packet.write(c_bit(self.flag2))
		if(self.flag2 == True):
			packet.write(self.currentHealth)
			packet.write(self.weirdFloat1)
			packet.write(self.currentArmor)
			packet.write(self.weirdFloat2)
			packet.write(self.currentImagination)
			packet.write(self.weirdFloat3)
			packet.write(self.data2_1)
			packet.write(self.data2_2)
			packet.write(self.data2_3)
			packet.write(self.data2_4)
			packet.write(self.maxHealth)
			packet.write(self.maxArmor)
			packet.write(self.maxImagination)
			packet.write(self.count)
			packet.write(self.factionID)
			packet.write(c_bit(self.isSmashable))
			if(PacketType == ReplicaTypes.REPLICA_CONSTRUCTION_PACKET):
				packet.write(self.bit1)
				packet.write(self.bit2)
				if(self.isSmashable == True):
					packet.write(self.smashable1)
					packet.write(self.smashable2)
					if(self.smashable2 == True):
						packet.write(self.smashable2_1)
		packet.write(c_bit(self.flag3))
		if(self.flag3 == True):
			packet.write(self.data3_1)
		return packet

#TODO: Actually Implement
class SkillComponent():
	def __init__(self):
		self.flag1 = False
	def get_packet(self, PacketType):
		packet = BitStream()
		if(PacketType == ReplicaTypes.REPLICA_CONSTRUCTION_PACKET):
			packet.write(c_bit(self.flag1))
		return packet


class InventoryComponent():
	def __init__(self):
		self.flag1 = False
		self.flag2 = False
		self.characterObjID = None
	def get_packet(self, PacketType):
		packet = BitStream()
		packet.write(c_bit(self.flag1))
		if(self.flag1 == True):
			items = getEquippedItems(str(self.characterObjID))
			packet.write(c_ulong(len(items)))
			for item in items:
				LOT = getLOTFromObject(str(item[0]))
				info = getItemInfo(str(item[0]))
				packet.write(c_longlong(item[0]))#ObjectID
				packet.write(c_long(int(LOT[0])))
				packet.write(c_bit(False))
				packet.write(c_bit(True))#Flag For Count
				packet.write(c_ulong(int(info[0])))#ItemCount
				packet.write(c_bit(True))#Flag for item slot
				packet.write(c_ushort(int(info[1])))#ItemSlot
				packet.write(c_bit(False))
				packet.write(c_bit(False))
				packet.write(c_bit(True))
		packet.write(c_bit(self.flag2))
		return packet

#TODO Actually Implement
class RenderComponent():
	def __init__(self):
		self.FXCount = c_long(0)
	def get_packet(self, PacketType):
		packet = BitStream()
		packet.write(self.FXCount)
		return packet

class Component107():
	def __init__(self):
		self.flag1 = False
		self.data1_1 = c_longlong(0)
	def get_packet(self, PacketType):
		packet = BitStream()
		packet.write(c_bit(self.flag1))
		if(self.flag1 == True):
			packet.write(self.data1_1)
		return packet

class ReplicaObject():
	def __init__(self, components):
		self.components = components
		self._serialize = False
	def send_construction(self):
		packet = BitStream()
		for component in self.components:
			packet.write(component.get_packet(ReplicaTypes.REPLICA_CONSTRUCTION_PACKET))
		return packet
	def serialize(self):
		packet = BitStream()
		for component in self.components:
			packet.write(component.get_packet(ReplicaTypes.REPLICA_SERIALIZATION_PACKET))
		return packet


