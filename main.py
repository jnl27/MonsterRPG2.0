import random
import time
import sys
print("Welcome to MonsterFightRPG! A game where you randomly fight monsters to earn gold and glory. Have fun!")
print()
#playerStats
playerHP = 50
playerMP = 30
maxMP = 30
playeraccuracy = 90
sword = "Wooden Sword"
armor = "Wooden Armor"
#items & misc
potions = 3 #hp
potheal = 30
potcost = 15

superpotions = 0
superpotheal = 60
superpotcost = 35

elixirs = 1 #Mana
elixirheal = 20
elixircost = 20

bombs = 0
bombdmg = 20
bombcost = 10

sands = 1
sandaccreduction = 30
sandcost = 10

playergold = 0
woodenarmorHP = 50
ironarmorHP = 100
platarmorHP = 200
#magic
firecost = 10
firedmg = 12
fireaccuracy = 70

icecost = 15
icedmg = 10

healcost = 20

nukecost = 100
nukedmg = 9999
#keeps track of fight #
fightcount = 0

boughtironarmor = False
ironarmorcost = 100
boughtsteelsword = False
steelswordcost = 70
boughtplatarmor = False
platarmorcost = 225
boughtdiamondsword = False
diamondswordcost = 150

def fight(enemy, enemyHP, enemymaxHP, mindmg, maxdmg, enemyaccuracy):
    global playerHP
    global playerMP
    global playeraccuracy
    global potions
    global elixirs
    global superpotions
    global playerdmg
    global playergold
    global bombs
    global sands
    global sword
    while playerHP>0 and enemyHP>0:
        print()
        if armor == "God Armor":
          maxHP = 500
        elif armor == "Wooden Armor":
          maxHP = 50
        elif armor == "Iron Armor":
          maxHP = 100
        elif armor == "Plat Armor":
          maxHP = 200
        print("You have "+ str(playerHP) +"/"+ str(maxHP) + " HP left.")
        print("You have "+ str(playerMP) +"/"+ str(maxMP) + " MP left.")
        notfighttypo = True
        while notfighttypo == True:
            print()
            action = input("What do you do? [attack, magic, items, run]")
            #ATTACK
            if action.lower() == "attack":
                print("You swing your sword at the", enemy)
                time.sleep(1)
                if random.randrange(1,101)<=playeraccuracy:
                    if sword == "Wooden Sword":
                        playerdmg = random.randrange(1,11)
                    elif sword == "Steel Sword":
                        playerdmg = random.randrange(7,16)
                    elif sword == "Diamond Sword":
                        playerdmg = random.randrange(10,31)
                    elif sword == "RNGsus Sword":
                        playerdmg = random.randrange(1,667)
                    enemyHP-=playerdmg
                    print("Your swing did ", playerdmg, "damage!")
                    if enemyHP>0:
                        print()
                        print("Enemy", enemy, "has "+ str(enemyHP) + "/"+ str(enemymaxHP) + " HP left!")
                else:
                    print("Your attack missed!")
                    time.sleep(1)
                notfighttypo = False
            #MAGIC
            elif action.lower() == "magic":
                info = True
                print("Protip: type 'info' before a certain magic to see the info about that magic. Ex. to see info about ice shards type 'infoice shards'")
                while info == True:
                    print()
                    print("Choose magic; type 'n' to cancel:\n\tfireball -", firecost, "mana\n\tice shards -", icecost, "mana\n\theal -", healcost, "mana")
                    if armor == "God Armor":
                        print("\n\tNUKE -", nukecost, "mana")
                    magic = input("Type here:")
                    if magic.lower() == "infofireball":
                        print("Magic: fireball will deal one hit for", firedmg,  "damage. Relatively good accuracy.")
                        time.sleep(1)
                    elif magic.lower() == "infoice shards":
                        print("Magic: ice shards will deal 1-3 hits for", icedmg, "damage each. Decent accuracy.")
                        time.sleep(1)
                    elif magic.lower() == "infoheal":
                        print("Magic: heal will restore you to full health.")
                        time.sleep(1)
                    elif magic.lower() == "infonuke":
                        print("Magic: NUKE will deal", nukedmg, "damage to current enemy.")
                        time.sleep(1)
                    elif magic.lower() == "fireball":
                        if playerMP>=firecost:
                            print("You summon a fireball at the", enemy)
                            time.sleep(1)
                            playerMP-=firecost
                            if random.randrange(1,101)<=fireaccuracy:
                                enemyHP-=firedmg
                                print("The fireball did", firedmg, "damage!")
                                time.sleep(1)
                                if enemyHP>0:
                                    print()
                                    print("Enemy", enemy, "has "+ str(enemyHP) + "/"+ str(enemymaxHP) + " HP left!")
                            else:
                                print("Your fireball missed!")
                            time.sleep(1)
                            print("You have "+ str(playerMP) + "/" + str(maxMP) +" MP left!")
                            print()
                            info = False
                            notfighttypo = False
                        else:
                            print("You don't have enough mana for that.")
                            print()
                    elif magic.lower() == "ice shards":
                        if playerMP>=icecost:
                            print("You threw ice shards at the", enemy)
                            icehit = random.randrange(1,4)
                            for i in range(icehit):
                                print("Bam Bam Bam")
                                print("An ice shard hits the", enemy)
                                enemyHP-=icedmg
                                time.sleep(1)
                                print()
                            print("Ice shards hit", icehit, "times!")
                            print("Ice shards did a total of", icehit*icedmg, "damage!")
                            time.sleep(1)
                            if enemyHP>0:
                                print()
                                print("Enemy", enemy, "has "+ str(enemyHP) + "/"+ str(enemymaxHP) + " HP left!")
                            time.sleep(1)
                            playerMP-=icecost
                            print("You have " + str(playerMP) + "/"+ str(maxMP) + " MP left!")
                            print()
                            info = False
                            notfighttypo = False
                        else:
                            print("You don't have enough mana for that.")
                            print()
                    elif magic.lower() == "heal":
                        if playerMP>=healcost:
                            print("You used heal!")
                            time.sleep(1)
                            print("~~~")
                            time.sleep(1)
                            print("You have fully restored your HP")
                            if armor == "Wooden Armor": 
                                playerHP = woodenarmorHP
                            elif armor == "Iron Armor":
                                playerHP = ironarmorHP
                            elif armor == "Plat Armor":
                                playerHP = platarmorHP
                            playerMP-=healcost
                            print("You have "+ str(playerMP) +"/"+ str(maxMP) + " MP left.")
                            print()
                            info = False
                            notfighttypo = False
                        else:
                            print("You don't have enough mana for that.")
                            print()
                    elif magic.lower() == "nuke":
                        if playerMP>=nukecost:
                            print("You used N U K E")
                            time.sleep(1)
                            for i in range(50):
                                print("B O O M B O O M B O O M B O O M")
                            playerMP-=nukecost
                            enemyHP-=nukedmg
                            print("The N U K E did", nukedmg, "damage!")
                            time.sleep(1)
                            if enemyHP>0:
                                print()
                                print("Enemy", enemy, "has "+ str(enemyHP) + "/"+ str(enemymaxHP) + " HP left!")
                            print("You have "+ str(playerMP) + "/" + str(maxMP) +" MP left!")
                            print()
                            info = False
                            notfighttypo = False
                    elif magic.lower() == "n":
                        info = False
                    else:
                        print("Please try again.")
                    
            #ITEMS
            elif action.lower() == "items":
                yesitem = True
                while yesitem == True:
                    print()
                    print("Type item EXACTLY as shown")
                    print("Type 'n' to cancel item menu")
                    print("You have:\n\t", potions, "Potions\n\t", superpotions, "Super Potions\n\t", elixirs, "Elixirs\n\t", bombs, "Bombs\n\t", sands, "Sand Bombs")
                    use = input("Which item to use?")
                    if use.lower() == "potions" or use.lower() == "potion":
                        if potions>0:
                            print("You used a potion!")
                            potions-=1
                            time.sleep(1)
                            print("You healed yourself for ", potheal, "HP")
                            playerHP+=potheal
                            if armor == "Wooden Armor":
                                if playerHP>woodenarmorHP:
                                    playerHP = woodenarmorHP
                            elif armor == "Iron Armor":
                                if playerHP>ironarmorHP:
                                    playerHP = ironarmorHP
                            elif armor == "Plat Armor":
                                if playerHP>platarmorHP:
                                    playerHP = platarmorHP
                            print("Your HP is now "+ str(playerHP) + "/" + str(maxHP))
                            print("You have", potions, "potion(s) left.")
                            yesitem = False
                            notfighttypo = False
                        else:
                            print("You have no more potions")
                    elif use.lower() == "super potions" or use.lower() == "super potion":
                        if superpotions>0:
                            print("You used a Super Potion!")
                            superpotions-=1
                            time.sleep(1)
                            print("You healed yourself for ", superpotheal, "HP")
                            playerHP+=superpotheal
                            if armor == "Wooden Armor":
                                if playerHP>woodenarmorHP:
                                    playerHP = woodenarmorHP
                            elif armor == "Iron Armor":
                                if playerHP>ironarmorHP:
                                    playerHP = ironarmorHP
                            print("Your HP is now "+ str(playerHP) + "/" + str(maxHP))
                            print("You have", superpotions, "Super Potion(s) left.")
                            yesitem = False
                            notfighttypo = False
                        else:
                            print("You have no more Super Potions")
                    elif use.lower() == "elixirs" or use.lower() == "elixir":
                        if elixirs>0:
                            print("You used an Elixir!")
                            elixirs-=1
                            time.sleep(1)
                            print("You restored your mana by", elixirheal, "MP")
                            playerMP+=elixirheal
                            if playerMP>maxMP:
                                playerMP = maxMP
                            print("Your MP is now "+ str(playerMP) +"/"+ str(maxMP))
                            print("You have", elixirs, "Elixir(s) left.")
                            yesitem = False
                            notfighttypo = False
                        else:
                            print("You have no more Elixirs")
                    elif use.lower() == "bombs" or use.lower() == "bomb":
                        if bombs>0:
                            print("You used a bomb against the", enemy)
                            bombs-=1
                            time.sleep(1)
                            print("BOOM")
                            time.sleep(1)
                            print("The bomb did", bombdmg, "damage!")
                            enemyHP-=bombdmg
                            if enemyHP>0:
                                print("Enemy", enemy, "has "+ str(enemyHP) + "/"+ str(enemymaxHP) + " HP left!")
                            print("You have", bombs, "bomb(s) left.")
                            yesitem = False
                            notfighttypo = False
                        else:
                            print("You have no more bombs")
                    elif use.lower() == "sand bombs" or use.lower() == "sand bomb":
                        if sands>0:
                            print ("You hurled a sand bomb against the", enemy)
                            sands-=1
                            time.sleep(1)
                            print("FSHSHHSHSHHHSHSFHSFHSHDFHSHFHSFHAHFHFAHFHFHSHSFHSHHFSHFHSHFHSHFHSHFHSFHFSHFSHFHFHSFHFHHHSHFHSFHHS")
                            time.sleep(1)
                            print("The enemy had their accuracy reduced by "+ str(sandaccreduction)+ "%!")
                            enemyaccuracy-=sandaccreduction
                            yesitem = False
                            notfighttypo = False
                        else:
                            print("You have no more Sand Bombs")
                    elif use.lower() == "n":
                        yesitem = False
                    else:
                        print("Unrecognized item.")
            #RUN   
            elif action.lower() == "run":
                print("You have fled from battle.")
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                sys.exit(0) 
            else:
                print("Incorrect option.")
            
        if enemyHP<=0:
            print("You have killed the", enemy, "!")
        print()
        if enemyHP>0:
            print("Enemy", enemy, "attacks!")
            time.sleep(1)
            if random.randrange(1,101)<=enemyaccuracy:
                enemydmg = random.randrange(mindmg, maxdmg+1)
                playerHP-=enemydmg
                print("Ouch! Enemy", enemy, "did", enemydmg, "damage!")
            else:
                print("Enemy missed their attack!")
        if playerHP<=0:
            print("You have been killed by the", enemy, ".")
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            sys.exit(0)

def itemshop():
    global yesshop
    global playergold
    global playerHP
    global playerMP
    global elixirs
    global playerdmg
    global potions
    global superpotions
    global bombs
    global sands
    global sword
    global armor
    global fightcount
    global boughtironarmor
    global boughtsteelsword
    global boughtplatarmor
    global boughtdiamondsword
    while yesshop != -1:
        print("What would you like to buy? (Type the item EXACTLY as shown to buy the item)")
        print("\n\tpotions (Restores", potheal, "health) -", potcost, "gold each")
        print("\n\telixirs (Restores", elixirheal, "mana) -", elixircost, "gold each")
        print("\n\tbombs (One-time use, instantly deals", bombdmg, "dmg) -", bombcost, "gold each")
        print("\n\tsand bombs (One-time use, throw at enemy to reduce their accuracy) -", sandcost, "gold each")
        if fightcount>=5:
            print("\n\tSuper Potions (Restores", superpotheal, "health) -", superpotcost, "gold each")
        if boughtsteelsword!=True:
            print("\n\tUpgrade to Steel Sword (Increases damage to 5-15dmg) -", steelswordcost, "gold")
        if boughtironarmor!=True:
            print("\n\tUpgrade to Iron Armor (Increases HP to", ironarmorHP,") -", ironarmorcost, "gold")
        if fightcount>=8:
            if boughtdiamondsword!=True:
                print("\n\tUpgrade to Diamond Sword (Increases damage to 10-30dmg) -", diamondswordcost, "gold")
            if boughtplatarmor!=True:
                print("\n\tUpgrade to Platinum Armor (Increases HP to", platarmorHP,") -", platarmorcost, "gold")
        shopping = input("Type here: ")
        #POTIONS
        if shopping.lower() == "potions":
            potionnum = int(input("How many potions would you like to buy?(Type the number, not word)"))
            if playergold>=potcost*potionnum:            
                print("You have bought", potionnum, "potions")
                potions+=potionnum
                playergold-=potionnum*potcost
                print("You now have", potions, "potions.")
            else:
                print("You do not have enough gold for that")
        elif shopping.lower() == "elixirs":
            elixirnum = int(input("How many elixirs would you like to buy? (Type the number, not word)"))
            if playergold>=elixircost*elixirnum:
                print("You have bought", elixirnum, "elixir(s)")
                elixirs+=elixirnum
                playergold-=elixirnum*elixircost
                print("You now have", elixirs, "elixir(s).")
            else:
                print("You do not have enough gold for that")
        elif shopping.lower() == "super potions":
            if fightcount>=5:
                spotionnum = int(input("How many Super Potions would you like to buy? (Type the number, not word)"))
                if playergold>=superpotcost*spotionnum:
                    print("You have bought", spotionnum, "Super Potions.")
                    superpotions+=spotionnum
                    playergold-=spotionnum*superpotcost
                    print("You now have", superpotions, "Super Potions.")
                else:
                    print("You do not have enough gold for that")
            else:
                print("Invalid item.")
        #BOMBS
        elif shopping.lower() == "bombs":
            print("You can only have a maximum of 3 bombs in hand!")
            bombnum = int(input("How many bombs would you like to buy?(Type the number, not word)"))
            if playergold>=bombcost*bombnum:
                if bombs+bombnum>3:
                    print("Too many! You can only hold 3 bombs!")
                else:
                    print("You have bought", bombnum, "bombs")
                    bombs+=bombnum
                    playergold-=bombnum*bombcost
                    print("You now have", bombs, "bombs")
            else:
                print("You do not have enough gold for that")
        #SAND
        elif shopping.lower() == "sand bombs":
            sandnum = int(input("How many sand bombs would you like to buy? (Type the number, not word)"))
            if playergold>=sandcost*sandnum:
                print("You have bought", sandnum, "Sand bombs.")
                sands+=sandnum
                playergold-=sandnum*sandcost
                print("You now have", sands, "Sand Bombs.")
            else:
              print("You do not have enough gold for that")
        #STEEL SWORD
        elif shopping.lower() == "upgrade to steel sword":
            if sword == "RNGsus Sword":
                print("You cant upgrade  your sword in god mode!")
                print()
            elif playergold>=steelswordcost:
                print("You have upgraded your weapon to Steel Sword!")
                print("Your sword now deals 5-15 damage!")
                sword = "Steel Sword"
                boughtsteelsword = True
                playergold-=steelswordcost
            else:
                print("You do not have enough gold for that")    
        #IRON ARMOR
        elif shopping.lower() == "upgrade to iron armor":
            if sword == "RNGsus Sword":
                print("You cant upgrade Armour in God mode!")
                print()
            elif playergold>=ironarmorcost:
                print("You have upgraded to Iron Armor!")
                print("Your HP is now", ironarmorHP, "!")
                armor = "Iron Armor"
                boughtironarmor = True
                playerHP = ironarmorHP
                playergold-=ironarmorcost
            else:
                print("You do not have enough gold for that")
        #DIAMOND SWORD
        elif shopping.lower() == "upgrade to diamond sword":
            if sword == "RNGsus Sword":
                print("You cant upgrade your sword in God mode!")
                print()
            elif playergold>=diamondswordcost:
                print("You have upgraded your weapon to Diamond Sword!")
                print("Your sword now deals 10-30 damage!")
                sword = "Diamond Sword"
                boughtdiamondsword = True
                playergold-=diamondswordcost
            else:
                print("You do not have enough gold for that")
        #PLATINUM ARMOR
        elif shopping.lower() == "upgrade to platinum armor":
            if armor == "God Armor":
                print("You cant upgrade Armour in God mode!")
                print()
            elif playergold>platarmorcost:
                print("You have upgraded to Platinum Armor!")
                print("Your HP is now", platarmorHP, "!")
                armor = "Plat Armor"
                boughtplatarmor = True
                playerHP = platarmorHP
                playergold-=platarmorcost
            else:
                print("You do not have enough gold for that")
        else:
            print("Invalid item.")
        print()
        print("You have", playergold, "gold left.")
        shop = input("Would you like to buy more items?[y/n]")
        if shop.lower() == "n" or shop.lower() == "no":
            yesshop = -1


def healer():
    global playergold
    global playerHP
    global armor
    print("You have", playergold, "gold")
    error = True
    while error!=False:
        heal = input("Would you like to fully restore your health for 30 gold?[y/n]")
        if heal.lower() == "y" or heal.lower() == "yes":
            print("You have paid 30 gold to restore your health by "+ str(maxHP-playerHP))
            time.sleep(1)
            playergold-=30
            if armor == "Wooden Armor":
                playerHP = woodenarmorHP
            elif armor == "Iron Armor":
                playerHP = ironarmorHP
            elif armor == "Plat Armor":
                playerHP = platarmorHP
            print("Your HP is now", playerHP)
            print("You have", playergold, "gold left.")
            error = False
        elif heal.lower() == "n" or heal.lower() == "no":
            print("You have decided not to restore your health.")
            error = False
        else:
            print("Invalid Option.")
        
def afterbattle():
    global gold
    global playergold
    time.sleep(1)
    print("You have earned", gold, "gold!")
    playergold+=gold
    time.sleep(1)
    print("You have", playergold, "gold")
    if armor == "God Armor":
      maxHP = 1000
    elif armor == "Wooden Armor":
      maxHP = 50
    elif armor == "Iron Armor":
      maxHP = 100
    elif armor == "Plat Armor":
      maxHP = 200
    print("You have "+ str(playerHP) +"/"+ str(maxHP) +" HP left.")
    print("You have "+  str(playerMP) +"/"+ str(maxMP) +" MP left.")
    print()

def afterbattle2():
    afterbattle()
    healer()
    
def afterbattleshop():
    global yesshop
    afterbattle()
    healer()
    print()
    print("The travelling merchant Reggi has appeared!")
    shop = input("Would you like to buy some items?[y/n]")
    if shop.lower() == "y" or shop.lower() == "yes":
        yesshop = 0
    elif shop.lower() == "n" or shop.lower() == "no":
        yesshop = -1
    itemshop()

def roundbegin():
    global fightcount
    fightcount+=1
    print()
    print("~~~~~~~~~~~ FIGHT", fightcount, "~~~~~~~~~~~")
    print()
    

typo = True
while typo == True:
    begin = input("Are you ready to begin the fight? [y/n]" )
    if begin.lower() == "y" or begin.lower() == "yes":
        start = True
        typo = False
        while start!=False:
            global name
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~GAME START~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("You are an adventurer seeking to destroy all enemies you encounter. You have 50HP, 30MP, and deal 1-10 damage. Good luck!")
            time.sleep(2)
            name = input("What shall your name be? ")
            print("Welcome adventurer", name)
            if name=="godmode":
              print("Now entering God Mode. Your HP will be increased to 500, your MP will be increased to 100, and your sword has become the RNGsus Sword, dealing 1-666 damage with each swing.")
              playerHP = 500
              armor = "God Armor"
              playerMP = 100
              maxMP = 100
              sword = "RNGsus Sword"
            time.sleep(1)
            print("Protip: The game is over once you defeat all monsters or die.")
            print("Protip: Running away will quit your adventure.")
            print("Protip: Item: potion will heal you for 30HP.")
            print("Protip: Item: elixir will restore 20MP.")
            #fight1
            roundbegin()
            print("A wild mini goblin has appeared! It has 10HP, deals 3-6 damage, and has relatively good accuracy. It will drop 20-50 gold when defeated.")
            gold = random.randrange(20,51)
            fight("Goblin", 10, 10, 3, 6, 80)
            afterbattle()
            print()
            print("Protip: Starting from after fight 2, if you're low on HP, you can pay the healer for 30 gold to fully restore your HP.")
            #fight2
            roundbegin()
            print("A wicked troll has appeared! It has 15HP, deals 5-8 damage, and has good accuracy. It will drop 40-60 gold when defeated.")
            gold = random.randrange(40,61)
            fight("Troll", 15, 15, 5, 8, 75)
            afterbattle2()
            #fight3
            roundbegin()
            print("A gang of goblins has appeared! They have 25HP, deal 2-10 damage, and have superb accuracy. They will drop 20-50 gold when defeated.")
            gold = random.randrange(20,51)
            fight("Goblin Gang", 25, 25, 2, 10, 90)
            afterbattleshop()
            #fight4
            roundbegin()
            print("A Masked Ghoul has appeared! It has 30HP, deals 5-12 damage, and has decent accuracy. It will drop 50 gold when defeated.")
            gold = 50
            fight("Masked Ghoul", 30, 30, 5, 12, 60)
            afterbattle2()
            print()
            print("Protip: You may not always get a chance to heal or shop after every battle, so spend that gold!")
            time.sleep(1)
            print("Protip: After fight 5, the Super Potion will be available for purchase in the item shop!\n\tThe Super Potion will heal you for", superpotheal, "HP!")
            time.sleep(1)
            #fight5
            roundbegin()
            print("A Shadow Knight has appeared! It has 45HP, deals 10-20 damage, and has neva-miss accuracy! It will drop 70-100 gold when defeated.")
            time.sleep(1)
            print()
            print("Shadow Knight: 'You have come far enough. This is where you end!'")
            time.sleep(1)
            print()
            print("Protip: WARNING - Shadow Knight is a mini-boss. He is significantly stronger than all the enemies you have faced so far. Be careful!")
            time.sleep(1)
            gold = random.randrange(70,101)
            fight("Shadow Knight", 45, 45, 12, 20, 100)
            afterbattleshop()
            #fight6
            roundbegin()
            print("A Large Goblin has appeared! It has 35HP, deals 7-12 damage, and has decent accuracy. It will drop 30-70 gold when defeated.")
            gold = random.randrange(30,71)
            fight("Large Goblin", 35, 35, 7, 12, 70)
            afterbattle()
            print()
            #fight7
            roundbegin()
            print("A Haunting Banshee has appeared! It has 30HP, deals 10-20 damage, and has superb accuracy! It will drop 50-80 gold when defeated.")
            print("Banshee: 'EEEEEEEEEEEEEEEEEEEEEEE'")
            gold = random.randrange(50,81)
            fight("Haunting Banshee", 30, 30, 10, 20, 90)
            afterbattleshop()
            print()
            print("Protip: After fight 8, you can upgrade your equipment even further!")
            #fight8
            roundbegin()
            print("A Sturdy Golem has appeared! It has 80HP, deals 8-15 damage, but has poor accuracy. It will drop 100-150 gold when defeated.")
            print("Golem: '...'")
            gold = random.randrange(100,151)
            fight("Sturdy Golem", 70, 70, 3, 15, 40)
            afterbattleshop()
            #fight9
            roundbegin()
            print("A Two-Headed Hydra has appeared! It has 60HP, deals 12-20 damage, and has good accuracy! It will drop 80-130 gold when defeated.")
            gold = random.randrange(80,131)
            fight("Two-Headed Hydra", 60, 60, 12, 20, 75)
            print()
            print("Protip: This is your LAST chance to shop/heal, make sure you're ready for the next fight!")
            afterbattleshop()
            #fight10
            print("Protip: This is the final battle. Get ready!")
            print()
            roundbegin()
            print("The Mighty Dragon has appeared! It has a whopping 100HP and deals 20-40 damage! It's accuracy shall not be questioned. It will drop 500 gold when defeated.")
            print()
            time.sleep(2)
            print("Dragon: 'NYYYYYYYYEEEEEEeEEEEEeeEEeEEEEEEAAAAAHHHHHHHH!!!'")
            print()
            time.sleep(2)
            print("Dragon: 'So you have made it this far, yea? You came here to steal my gold, yea? You and your stupid adventurers, I hate all of you! PREPARE TO MEET YOUR DOOM!")
            print()
            time.sleep(2)
            print("Protip: EXTREME WARNING - The Dragon is the FINAL-BOSS. It is the strongest monster you have yet to conquer. It is incredibly strong. Exercise EXTREME Caution!")
            time.sleep(2)
            gold = 500
            fight("Lord Dragon", 100, 100, 20, 40, 100)
            print()
            time.sleep(2)
            print("Dragon: '. . .'")
            print()
            time.sleep(2)
            print("Dragon: 'You have beaten me this time, foolish human.'")
            print()
            time.sleep(2)
            print("Dragon: 'Nggh, I guess I must forfeit my treasure thus far.'")
            print()
            time.sleep(2)
            print("Dragon: 'Do NOT think you've have defeated me. This was just but a battle. I WILL win next time, you hear?'")
            print()
            time.sleep(2)
            print("Dragon: 'Until then. Farewell.'")
            print()
            time.sleep(2)
            print("Dragon: 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'")
            print()
            time.sleep(2)
            print("The mysterious dragon teleported away.")
            afterbattle()
            time.sleep(2)
            print("AND so, the brave adventurer known as", name, "has finally defeated the Mighty Dragon, securing themselves the title of Greatest Adventurer in the Land.")
            time.sleep(2)
            print()
            print("~~~~~~~~~~~~~~~CONGRATULATIONS! YOU HAVE BEAT THE GAME!~~~~~~~~~~~~~~~")
            print("                        Thanks for playing!")
            print()
            print()
            start = False


    elif begin.lower() == "n" or begin.lower() == "no":
        print("You have decided that you are not ready to fight. Come back later!")
        typo = False
    else:
        print("Invalid selection, try again")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
       
