# loot_box_sim


## TODO
	Build a game loop
		~~purchace loot boxes~~
		~~sell items~~

	~~Implement Selling~~
	Update weapon values(balance)

	fix name save/file to be all lowercase.



## Idea:

Loot Box simulator
	display ~3 boxes and user chooses one, show user their loot(put in an inventory?), show user what they missed out on
    inventory system saved to player name, trading, weapons, money



## Summary:
	Players open one loot box of three. They can collect, sell, or trade the items for gold or other items. Players use gold to purchace
more loot boxes. The loot table will be pre-determined, with randomness to stats and rarity.

## SAVE SYSTEM
	save, load player data

## INVENTORY SYSTEM:
	display
	order
	delete
	trade

## PLAYER:
	Name, GoldTotal, Inventory, TradeStatus, level (increese chance to not get trash?)

## WEAPON:
	weapon name : [type, rarity, max_value]
	

## LOOT BOXES:
	player will purchace the right to choose a box. Three boxes will be presented, loot pre-determined. Player chooses box and recieves loot. Player is 	shown what loot is missed out on. Loot goes to inventory, player save.

## TRADING SYSTEM:
	Player1 will initiate the trade with and offer of loot or gold.
	When player2 plays the trade notification will pop up, they can deny or offer something in return
	when player1 returns they may accecpt or deny the offer
	This will all be done through tags on the playsers save file(player1 will have to write to player2 and so on)

## SELING ITEMS:
	Ingame vendor who will buy equipment based on rarity, stats, and a little razzle dazzle.


### EXTENDED GOAL:
	trade
	Chat
    Delete old player profiles