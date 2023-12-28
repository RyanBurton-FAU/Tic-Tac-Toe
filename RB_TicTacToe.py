import random

print("This is a simple game of Tic-Tac-Toe. Enjoy!")
Option = int(input("Do you want to play against a cpu(1) or player 2(2): "))


def options(c):
    if c == 1:
        print(grid_vs_cpu())
    if c == 2:
        print(grid_vs_player2())


def grid_vs_cpu():
    cpu = random.randint(0,8)
    #Original Playing Grid.
    position = ["0","1",'2','3','4','5','6','7','8']
    A = (" ".join(position[0:3]))
    B = (" ".join(position[3:6]))
    C = (" ".join(position[6:9]))
    print('',A,'\n',B,'\n',C)

    turns = 1
    while (turns < 6):
    
        turns = turns+1
        player_number = int(input("Enter a number "))
        cpu_number = random.randint(0,8)
    
        print("Cpu chose",cpu_number)
    
        if str(player_number) == position[player_number]:

            position[player_number] = 'X'
            A = (" ".join(position[0:3]))
            B = (" ".join(position[3:6]))
            C = (" ".join(position[6:9]))

            if (position[0] == (position[1] and position[2])) or (position[3] == (position[4] and position[5])) or (position[6] == (position[7] and position[8])):
                if ((position[0]+position[1]+position[2]) == 'XXX') or ((position[3]+position[4]+position[5]) == 'XXX') or ((position[6]+position[7]+position[8]) == 'XXX'):
                    print('',A,'\n',B,'\n',C)
                    return("The Player wins!")
                    break
            
            if (position[0] == (position[3] and position[6])) or (position[1] == (position[4] and position[7])) or (position[2] == (position[5] and position[8])) or (position[2] == (position[4] and position[6])) or (position[0] == (position[4] and position[8])):
                 if ((position[0]+position[3]+position[6]) == 'XXX') or ((position[1]+position[4]+position[7]) == 'XXX') or ((position[2]+position[5]+position[8]) == 'XXX') or ((position[2]+position[4]+position[6]) == 'XXX') or ((position[0]+position[4]+position[8]) == 'XXX'):
                    print('',A,'\n',B,'\n',C)
                    return("The Player wins!")
                    break
                  
        if str(cpu_number) == position[cpu_number]:
        
            position[cpu_number] = 'O'
            A = (" ".join(position[0:3]))
            B = (" ".join(position[3:6]))
            C = (" ".join(position[6:9]))
            print('',A,'\n',B,'\n',C)
            
            if (position[0] == (position[1] and position[2])) or (position[3] == (position[4] and position[5])) or (position[6] == (position[7] and position[8])):
                if ((position[0]+position[1]+position[2]) == 'XXX') or ((position[3]+position[4]+position[5]) == 'XXX') or ((position[6]+position[7]+position[8]) == 'XXX'):
                    return("The Player wins!")
                    break
                if ((position[0]+position[1]+position[2]) == 'OOO') or ((position[3]+position[4]+position[5]) == 'OOO') or ((position[6]+position[7]+position[8]) == 'OOO'):
                    return("The Cpu wins!")
                    break
            
            if (position[0] == (position[3] and position[6])) or (position[1] == (position[4] and position[7])) or (position[2] == (position[5] and position[8])) or (position[2] == (position[4] and position[6])) or (position[0] == (position[4] and position[8])):
                 if ((position[0]+position[3]+position[6]) == 'XXX') or ((position[1]+position[4]+position[7]) == 'XXX') or ((position[2]+position[5]+position[8]) == 'XXX') or ((position[2]+position[4]+position[6]) == 'XXX') or ((position[0]+position[4]+position[8]) == 'XXX'):
                   
                    return("The Player wins!")
                    break
                 if ((position[0]+position[3]+position[6]) == 'OOO') or ((position[1]+position[4]+position[7]) == 'OOO') or ((position[2]+position[5]+position[8]) == 'OOO') or ((position[2]+position[4]+position[6]) == 'OOO') or ((position[0]+position[4]+position[8]) == 'OOO'):
                    
                    return("The Cpu wins!")
                    break

            continue
        
        if (str(cpu_number) != position[cpu_number]):
            while (str(cpu_number) != position[cpu_number]) == True:

                cpu_number = random.randint(0,8)

                if (str(cpu_number) != position[cpu_number]):
                    continue
                if (str(cpu_number) == position[cpu_number]):
                
                    position[cpu_number] = 'O'
                    A = (" ".join(position[0:3]))
                    B = (" ".join(position[3:6]))
                    C = (" ".join(position[6:9]))
                    print('',A,'\n',B,'\n',C)

                    
                    if ((position[0]+position[1]+position[2]) == 'OOO') or ((position[3]+position[4]+position[5]) == 'OOO') or ((position[6]+position[7]+position[8]) == 'OOO'):
                        print('',A,'\n',B,'\n',C)
                        return("The Cpu wins!")
                        break
            
                    if ((position[0]+position[3]+position[6]) == 'OOO') or ((position[1]+position[4]+position[7]) == 'OOO') or ((position[2]+position[5]+position[8]) == 'OOO') or ((position[2]+position[4]+position[6]) == 'OOO') or ((position[0]+position[4]+position[8]) == 'OOO'):
                        print('',A,'\n',B,'\n',C)
                        return("The Cpu wins!")
                        break

                    break

def grid_vs_player2():
    cpu = random.randint(0,8)
    #Original Playing Grid.
    position = ["0","1",'2','3','4','5','6','7','8']
    A = (" ".join(position[0:3]))
    B = (" ".join(position[3:6]))
    C = (" ".join(position[6:9]))
    print('',A,'\n',B,'\n',C)

    turns = 1
    while (turns < 6):
    
        turns = turns+1
        player_number = int(input("Enter a number P1:"))
        cpu_number = int(input("Enter a number P2:"))
        print("Player 1 chose",player_number)
        print("Player 2 chose",cpu_number)
    
        if str(player_number) == position[player_number]:

            position[player_number] = 'X'
            A = (" ".join(position[0:3]))
            B = (" ".join(position[3:6]))
            C = (" ".join(position[6:9]))

            if (position[0] == (position[1] and position[2])) or (position[3] == (position[4] and position[5])) or (position[6] == (position[7] and position[8])):
                if ((position[0]+position[1]+position[2]) == 'XXX') or ((position[3]+position[4]+position[5]) == 'XXX') or ((position[6]+position[7]+position[8]) == 'XXX'):
                    print('',A,'\n',B,'\n',C)
                    return("Player 1 wins!")
                    break
            
            if (position[0] == (position[3] and position[6])) or (position[1] == (position[4] and position[7])) or (position[2] == (position[5] and position[8])) or (position[2] == (position[4] and position[6])) or (position[0] == (position[4] and position[8])):
                 if ((position[0]+position[3]+position[6]) == 'XXX') or ((position[1]+position[4]+position[7]) == 'XXX') or ((position[2]+position[5]+position[8]) == 'XXX') or ((position[2]+position[4]+position[6]) == 'XXX') or ((position[0]+position[4]+position[8]) == 'XXX'):
                    print('',A,'\n',B,'\n',C)
                    return("Player 1 wins!")
                    break
                  
        if str(cpu_number) == position[cpu_number]:
        
            position[cpu_number] = 'O'
            A = (" ".join(position[0:3]))
            B = (" ".join(position[3:6]))
            C = (" ".join(position[6:9]))
            print('',A,'\n',B,'\n',C)
            
            if (position[0] == (position[1] and position[2])) or (position[3] == (position[4] and position[5])) or (position[6] == (position[7] and position[8])):
                if ((position[0]+position[1]+position[2]) == 'XXX') or ((position[3]+position[4]+position[5]) == 'XXX') or ((position[6]+position[7]+position[8]) == 'XXX'):
                    return("Player 1 wins!")
                    break
                if ((position[0]+position[1]+position[2]) == 'OOO') or ((position[3]+position[4]+position[5]) == 'OOO') or ((position[6]+position[7]+position[8]) == 'OOO'):
                    return("Player 2 wins!")
                    break
            
            if (position[0] == (position[3] and position[6])) or (position[1] == (position[4] and position[7])) or (position[2] == (position[5] and position[8])) or (position[2] == (position[4] and position[6])) or (position[0] == (position[4] and position[8])):
                 if ((position[0]+position[3]+position[6]) == 'XXX') or ((position[1]+position[4]+position[7]) == 'XXX') or ((position[2]+position[5]+position[8]) == 'XXX') or ((position[2]+position[4]+position[6]) == 'XXX') or ((position[0]+position[4]+position[8]) == 'XXX'):
                   
                    return("Player 1 wins!")
                    break
                 if ((position[0]+position[3]+position[6]) == 'OOO') or ((position[1]+position[4]+position[7]) == 'OOO') or ((position[2]+position[5]+position[8]) == 'OOO') or ((position[2]+position[4]+position[6]) == 'OOO') or ((position[0]+position[4]+position[8]) == 'OOO'):
                    
                    return("Player 2 wins!")
                    break

            continue
        
        if (str(cpu_number) != position[cpu_number]):
            while (str(cpu_number) != position[cpu_number]) == True:

                cpu_number = random.randint(0,8)

                if (str(cpu_number) != position[cpu_number]):
                    continue
                if (str(cpu_number) == position[cpu_number]):
                
                    position[cpu_number] = 'O'
                    A = (" ".join(position[0:3]))
                    B = (" ".join(position[3:6]))
                    C = (" ".join(position[6:9]))
                    print('',A,'\n',B,'\n',C)

                    
                    if ((position[0]+position[1]+position[2]) == 'OOO') or ((position[3]+position[4]+position[5]) == 'OOO') or ((position[6]+position[7]+position[8]) == 'OOO'):
                        print('',A,'\n',B,'\n',C)
                        return("Player 2 wins!")
                        break
            
                    if ((position[0]+position[3]+position[6]) == 'OOO') or ((position[1]+position[4]+position[7]) == 'OOO') or ((position[2]+position[5]+position[8]) == 'OOO') or ((position[2]+position[4]+position[6]) == 'OOO') or ((position[0]+position[4]+position[8]) == 'OOO'):
                        print('',A,'\n',B,'\n',C)
                        return("Player 2 wins!")
                        break

                    break

options(Option)

