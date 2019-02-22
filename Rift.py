import sys
import math

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
z_link=[[] for i in range(link_count)]
for i in range(zone_count):
	# zone_id: this zone's ID (between 0 and zoneCount-1)
	# platinum_source: Because of the fog, will always be 0
	zone_id, platinum_source = [int(j) for j in input().split()]

for i in range(link_count):
	zone_1, zone_2 = [int(j) for j in input().split()]
	z_link[zone_1].append(zone_2)
	z_link[zone_2].append(zone_1)

# game loop
while True:
	z_pods=[]
	will_move = []
	z_link_cnt=[]

	my_platinum = int(input())  # your available Platinum
	for i in range(zone_count):
		# z_id: this zone's ID
		# owner_id: the player who owns this zone (-1 otherwise)
		# pods_p0: player 0's PODs on this zone
		# pods_p1: player 1's PODs on this zone
		# visible: 1 if one of your units can see this tile, else 0
		# platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
		z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]

		if my_id == 0 :
			if pods_p0 > 0:
				will_move.append(z_id)
				z_pods.append(pods_p0)
		else:
			if pods_p1 > 0:
				will_move.append(z_id)
				z_pods.append(pods_p1)

	for i in will_move:
		z_link_cnt.append(len(z_link[i]))

	# Write an action using print
	# To debug: print("Debug messages...", file=sys.stderr)


	# first line for movement commands, second line no longer used (see the protocol in the statement for details)
	for i in range(len(will_move)):
		for j in range(z_link_cnt[i]):
			if z_pods[i] > 1:
				print(z_pods[i]//z_link_cnt[i], end=" ")
				print(will_move[i], end=" ")
				print(z_link[will_move[i]][j], end=" ")
			else:
				print(1, will_move[i], end=" ")
				print(z_link[will_move[i]][j], end=" ")

	print()
	print("WAIT")
