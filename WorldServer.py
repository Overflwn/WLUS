from typing import Callable
import WorldPackets
from PacketHeaders import PacketHeader
from Enum import *
from GameManager import *
from GameDB import GameDB
import threading
from ServerUtilities import *
import pyraknet
from structures import Vector3, Vector4
from pyraknet.replicamanager import *
from core import GameServer, GameReplicaManager
from time import sleep
import threading
import LVLFiles

class WorldServer(GameServer):
	def __init__(self, address: Address, max_connections: int, incoming_password: bytes, GameManager : GameManager, CDClient : GameDB, ServerDB : GameDB):
		super().__init__(address, max_connections, incoming_password, GameManager, CDClient, ServerDB)
		self.add_handler(pyraknet.server.Event.UserPacket, self.handlePacket)
		self.add_handler(pyraknet.server.Event.Disconnect, self.handleWorldDisconnect)
		self.WorldHandlers = {}
		self.ReplicaManagers = {}

		self.registerWorldHandler(PacketHeader.ClientUserSessionInfo.value, WorldPackets.HandleSessionKey)
		self.registerWorldHandler(PacketHeader.ClientMinifigureListRequest.value, WorldPackets.HandleMinifigListRequest)
		self.registerWorldHandler(PacketHeader.ClientMinifigureCreateRequest.value, WorldPackets.HandleMinifigureCreation)
		self.registerWorldHandler(PacketHeader.ClientDeleteMinifigureRequest.value, WorldPackets.HandleMinifigureDeletion)
		self.registerWorldHandler(PacketHeader.ClientEnterWorld.value, WorldPackets.HandleJoinWorld)
		self.registerWorldHandler(PacketHeader.RoutedPacket.value, WorldPackets.HandleRoutedPacket)
		self.registerWorldHandler(PacketHeader.ClientGameMessage.value, WorldPackets.HandleGameMessage)
		self.registerWorldHandler(PacketHeader.ClientPositionUpdate.value, WorldPackets.UpdateCharacterPositon)
		self.registerWorldHandler(PacketHeader.ClientLoadComplete.value, WorldPackets.HandleDetailedLoad)
		self.registerWorldHandler(PacketHeader.Handshake.value, WorldPackets.HandleHandshake)
		print("World Server Started")

		for Zone in ZoneNames:
			self.registerZone(Zone, SpawnLocation=DefaultZoneSpawns[Zone], lvlFiles=ZoneLvls[Zone])
		print("Finished Registering Zones!")

		updateThread = threading.Thread(target=self.updateLoop)
		updateThread.start()
	def handlePacket(self, data : bytes, address : Address):
		if(data[0:8] in self.WorldHandlers):
			t = threading.Thread(target=self.WorldHandlers[data[0:8]], args=[self, data[8:], address])
			t.start()
		else:
			print("Header {} Has No Handler!".format(data[0:8]))
	def registerReplicaManager(self, WorldID : int):
		self.ReplicaManagers[WorldID] = GameReplicaManager(self)
	def registerWorldHandler(self, header : PacketHeader, function : Callable):
		self.WorldHandlers[header] = function
	def registerZone(self, WorldID : int, lvlFiles : list, SpawnLocation : Vector3 = Vector3(0,0,0)):
		World = Zone(self.Game)
		World.ZoneID = WorldID
		World.SpawnLocation = SpawnLocation
		self.registerReplicaManager(WorldID)
		result = self.Game.registerZone(World, lvlFiles, self)
		if(result is not Exception): print("Registered '{}'".format(ZoneNames[WorldID]))

	def handleWorldDisconnect(self, address : Address):
		print("Got Disconnect From {}".format(address))
		game : GameManager = self.Game
		session : Session = game.getSessionByAddress(address)
		character : Character = game.getObjectByID(session.ObjectID)
		if(character is not None):
			zoneID = character.Zone
			if(session.State != SessionState.CharacterScreen and session.State != SessionState.LoggingIn):
				self.ReplicaManagers[zoneID].remove_participant(address)
				self.ReplicaManagers[zoneID].destruct(character)
				del game.getZoneByID(zoneID).Objects[game.getZoneByID(zoneID).Objects.index(character)]
		del self.Game.Sessions[game.Sessions.index(session)]

	def updateLoop(self):
		while True:
			for Zone in self.Game.Zones:
				RM: GameReplicaManager = self.ReplicaManagers[Zone.ZoneID]
				for Object in Zone.Objects:
					if(isinstance(Object, ReplicaObject)):
						try:
							RM.serialize(Object)
						except:
							pass
					if(isinstance(Object, Character)):
						if((Object.ObjectConfig["Health"] <= 0 or self.inKillElevation(Object)) and "Unkillable" not in Object.Tag.split(" ") and Object.ObjectConfig["LoadingIn"] == False):
							if(Object.ObjectConfig["Alive"] == True):
								Object.ObjectConfig["Alive"] = False
								Object.ObjectConfig["Health"] = 0
								Object.Kill(self)
			sleep(.1)

	def inKillElevation(self, Player : Character):
		zone = Player.Zone
		yPos = Player.ObjectConfig["Position"].Y
		#TODO: Find death elevation for Ninjago
		if((zone == ZoneID.VentureExplorer or zone == ZoneID.ReturnToVentureExplorer) and yPos < 575):
			return True
		elif(zone == ZoneID.AvantGardens and yPos < 255):
			return True
		elif((zone == ZoneID.BlockYard or zone == ZoneID.AvantGrove or zone == ZoneID.NimbusRock or zone == ZoneID.ChanteyShantey or zone == ZoneID.RavenBluff) and yPos < 375):
			return True
		elif(zone == ZoneID.NimbusIsle and yPos < 445):
			return True
		elif(zone == ZoneID.GnarledForest and yPos < 165):
			return True
		elif(zone == ZoneID.CanyonCove and yPos < 210):
			return True
		elif(zone == ZoneID.ForbiddenValley and yPos < 60):
			return True
		elif(zone == ZoneID.Starbase3001 and yPos < 900):
			return True
		elif(zone == ZoneID.LEGOClub and yPos < 800):
			return True
		elif(zone == ZoneID.CruxPrime and yPos < -20):
			return True
		return False

	# def addItemToInventory(self, LOT : int, Player : Character, Quantity : int = 1, Linked : bool = False):
	# 	inventory : Inventory = Player.ObjectConfig["Inventory"]
	# 	objectID = random.randint(100000000000000000, 999999999999999999)
	# 	inventory.addItem(LOT, objectID, Quantity=Quantity, Linked=Linked, Equipped=False)
	# 	syncPacket = WriteStream()
	# 	self.InitializeGameMessage(syncPacket, Player.ObjectConfig["ObjectID"], 227)
	# 	syncPacket.write(c_bit(Linked))#Linked
	# 	syncPacket.write(c_bit(False))
	# 	syncPacket.write(c_bit(False))
	# 	syncPacket.write(c_bit(False))
	# 	syncPacket.write(c_ulong(0))
	# 	syncPacket.write(c_long(LOT))
	# 	syncPacket.write(c_bit(False))
	# 	syncPacket.write(c_bit(False))
	# 	syncPacket.write(c_bit(False))
	# 	syncPacket.write(c_bit(False))
	# 	syncPacket.write(c_longlong(objectID))
	# 	syncPacket.write(c_float(0))#X flying loot
	# 	syncPacket.write(c_float(0))#Y flying loot
	# 	syncPacket.write(c_float(0))#Z flying loot
	# 	syncPacket.write(c_bit(True))
	# 	syncPacket.write(c_int(inventory.getItemByID(objectID)["Slot"]))
	# 	session = self.Game.getSessionByCharacterID(Player.ObjectConfig["ObjectID"])
	# 	self.send(syncPacket, session.address)

	def spawnObject(self, LOT : int, zoneID : ZoneID, CustomConfig : dict, Position : Vector3 = Vector3(0,0,0), Rotation : Vector4 = Vector4(0,0,0,0), debug : bool = True):
		objectType = str(self.CDClient.Tables["Objects"].select(["type"], "id = {}".format(LOT))[0]["type"])
		zone: Zone = self.Game.getZoneByID(zoneID)
		if(objectType == "Smashables"):
			smashable = Smashable(zone)
			smashable.ObjectConfig["LOT"] = LOT
			smashable.ObjectConfig["Position"] = Position
			smashable.ObjectConfig["Rotation"] = Rotation
			smashable.ObjectConfig["ObjectType"] = "Smashables"
			for key in CustomConfig:
				smashable.ObjectConfig[key] = CustomConfig[key]
			smashable.setDestructible(self.CDClient)
			zone.createObject(smashable)
			smashable.Components = smashable.findComponentsFromCDClient(self.CDClient)
			self.ReplicaManagers[zoneID].construct(smashable)
		elif(objectType == "Enemies"):
			enemy = Enemy(zone)
			enemy.ObjectConfig["LOT"] = LOT
			enemy.ObjectConfig["Position"] = Position
			enemy.ObjectConfig["Rotation"] = Rotation
			enemy.ObjectConfig["ObjectType"] = "Enemies"
			enemy.setDestructible(self.CDClient)
			zone.createObject(enemy)
			enemy.Components = enemy.findComponentsFromCDClient(self.CDClient)
			self.ReplicaManagers[zoneID].construct(enemy)
		else:
				gameObject = ReplicaObject(zone)
				gameObject.ObjectConfig["LOT"] = LOT
				gameObject.ObjectConfig["Position"] = Position
				gameObject.ObjectConfig["Rotation"] = Rotation
				gameObject.ObjectConfig["ObjectType"] = objectType
				zone.createObject(gameObject)
				gameObject.Components = gameObject.findComponentsFromCDClient(self.CDClient)
				self.ReplicaManagers[zoneID].construct(gameObject)
		if(debug == True):
			print("Spawned Object with Type '{}' and LOT '{}'".format(objectType, LOT))

	def LoadWorld(self, Player: Character, zoneID: ZoneID, address: Address, SpawnAtDefault: bool = False):
		packet = WriteStream()
		print("Sending Player {} to {}".format(Player.ObjectConfig["ObjectID"], ZoneNames[zoneID]))
		writeHeader(packet, PacketHeader.WorldInfo)
		zone: Zone = self.Game.getZoneByID(zoneID)
		packet.write(c_uint16(zoneID))
		packet.write(c_uint16(0))  # MapInstance
		packet.write(c_ulong(0))  # MapClone
		packet.write(c_ulong(ZoneChecksums[zoneID]))
		if (SpawnAtDefault):
			packet.write(c_float(zone.SpawnLocation.X))
			packet.write(c_float(zone.SpawnLocation.Y))
			packet.write(c_float(zone.SpawnLocation.Z))
			Player.ObjectConfig["Position"] = zone.SpawnLocation
		else:
			packet.write(c_float(Player.ObjectConfig["Position"].X))
			packet.write(c_float(Player.ObjectConfig["Position"].Y))
			packet.write(c_float(Player.ObjectConfig["Position"].Z))
		if (zone.ActivityWorld):
			packet.write(c_ulong(4))
		else:
			packet.write(c_ulong(0))
		session: Session = self.Game.getSessionByAddress(address)
		session.ZoneID = zoneID
		session.ObjectID = Player.ObjectConfig["ObjectID"]
		Player.ObjectConfig["LoadingIn"] = True
		Player.Zone = zoneID
		for zone in self.ReplicaManagers:
			manager = self.ReplicaManagers[zone]
			if (manager.is_participant(address)):
				manager.remove_participant(address)
		RM: GameReplicaManager = self.ReplicaManagers[zoneID]
		RM.add_participant(address)
		self.send(packet, address)