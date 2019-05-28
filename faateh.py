# _   __                 ______          _       _        ___  _ _           
#| | / /                 |  ___|        | |     | |      / _ \| (_)          
#| |/ /  ___  ___ _ __   | |_ __ _  __ _| |_ ___| |__   / /_\ \ |___   _____ 
#|    \ / _ \/ _ \ '_ \  |  _/ _` |/ _` | __/ _ \ '_ \  |  _  | | \ \ / / _ \
#| |\  \  __/  __/ |_) | | || (_| | (_| | ||  __/ | | | | | | | | |\ V /  __/
#\_| \_/\___|\___| .__/  \_| \__,_|\__,_|\__\___|_| |_| \_| |_/_|_| \_/ \___|
#                | |                                                         
#                |_|                                                         

import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a", "1"]
answer_B = ["B", "b", "2"]
answer_C = ["C", "c", "3"]
yes = ["Y", "y", "yes", "Yes", "YES"]
no = ["N", "n", "no", "No", "NO"]

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m' #using this for end text
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def retry():
    time.sleep(2)
    print("\n")
    retry = input(color.BLUE + "Play again? (y/n)" + color.END)
    print("\n")
    if retry in yes:
        print("Let\'s try this again...\n\n\n")
        game()
    if retry in no:
        print("K, cya\n")
        exit()

def disappoint():
        print("\"I got a 60\"\n")
        time.sleep(2)
        print("\"Son, I'm extremely disappointed in you. You have talent, and you have the ability to succeed if you put your mind to it. Try harder next time.\"\n")
        print(color.GREEN + "Faateh survives." + color.END)
        print("Score: 1/10")
        retry()

def dies():
    time.sleep(2)
    print(color.RED + "Faateh dies.\n" + color.END)
    print("Score: 0/10")
    retry()

def slipper():
    print("Faateh's mom is waiting at the doorway with a slipper in her hand\n")
    b6 = input("A. Juke her\nB. Accept defeat\nC. Run up the stairs\n")
    if b6 in answer_A:
        b7 = input("A. Juke to the left\nB. Juke to the right\nC. Slide under her legs\n")
        if b7 in answer_A:
            print("Faateh attempts to juke his mom, but he is not athletic, so he slips and tears his ACL\n")
            dies()
        if b7 in answer_B:
            print("By God\'s grace, Faateh miraculously slips past his mom and makes it out the door.\n")
            time.sleep(2)
            print("However, Evan is waiting outside with a basketball.\n")
            time.sleep(2)
            print("\"Yo, nice jukes Fay. 1v1 me scrub.\"\n")
            b8 = input("A. Accept his challenge\nB. Decline and keep running\n")
            if b8 in answer_A:
                print("\"Yeah man, let\'s go\"\n")
                time.sleep(2)
                print("During the check, Faateh slips and falls over\n")
                time.sleep(2)
                print("\"My ACL!\"\n")
                time.sleep(2)
                print(color.RED + "Faateh bleeds out and dies.\n" + color.END)
                print("Score: 0/10")
            if b8 in answer_B:
                print("Faateh runs into the street and is run over by Bus 17\n")
                dies()
        if b7 in answer_C:
            print("Faateh attempts to slide under his mom\'s legs, but he is not athletic\n")
            print(color.RED + "Faateh slips and dies.\n" + color.END)
            print("Score: 0/10")
    if b6 in answer_B:
        print("Faateh's dad comes up behind him with a whip and knocks him unconcious\n")
        dies()
    if b6 in answer_C:
        print("Faateh sprints up the stairs into his room. He can hear his parents running up the stairs while screaming slurs in his native language. Faateh locks the door.\n")
        b9 = input("A. Jump out the window\nB. Hide in the closet\n")
        if b9 in answer_A:
            print("Faateh miraculoudly survives the jump. However, Faateh's dad does as well and starts sprinting towards Faateh with whip in hand\n")
            b10 = input("A. Run to Auntie\'s house\nB. Run to Bus 17\n")
            if b10 in answer_A:
                print("BANG BANG BANG\n")
                time.sleep(2)
                print("\"Auntie, let me in!\"\n")
                time.sleep(2)
                print("BANG BANG BANG\n")
                time.sleep(2)
                print("\"Quick, open the door!\"\n")
                time.sleep(2)
                print("Faateh\'s dad walks up behind him and kicks Faateh to the ground\n")
                time.sleep(2)
                print("\"Ah, my ACL!\"\n")
                time.sleep(2)
                print("Faateh gets whipped on the spot\n")
                dies()
            if b10 in answer_B:
                print("Faateh spots Bus 17 barreling down the road. Debby the bus driver scoops him up, but Faateh notices his parents have gotten into the '01 Accord and are in hot pursuit after him.\n")
                b11 = input("A. Stay in the bus\nB. Run inside HHS\n")
                if b11 in answer_A:
                    print("Faateh stays inside the bus as his parents walk up to the door\n")
                    time.sleep(2)
                    print("Debby refuses to open the door, and after 2 hours of waiting his parents decide to go home\n")
                    time.sleep(2)
                    print(color.GREEN + "Faateh barely survives.\n" + color.END)
                    print("Score: 8/10")
                    retry()
                if b11 in answer_B:
                    print("Faateh runs by Mrs. Fairbanks\n")
                    time.sleep(2)
                    print("\"Oh hey, Faateh! I wanted to discuss your recent test score with you.\"\n")
                    time.sleep(2)
                    print("I\'ve called your parents and they said they are on their way right now\"\n")
                    dies()
        if b9 in answer_B:
            print("Faateh cowers inside his closet. Dad opens the closet door and pulls out his whip\n")
            time.sleep(2)
            print("\"Dad, no!\"\n")
            dies()

print(color.PURPLE + "+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+" + color.END)
print(color.PURPLE + "|K|e|e|p| |F|a|a|t|e|h| |A|l|i|v|e|" + color.END)
print(color.PURPLE + "+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+\n\n" + color.END) #epic ascii time
time.sleep(2)
def game():
    print("Faateh is going home and is going to get whipped because of his math grade.")
    time.sleep(2)
    print("What should he do?\n\n")
    ab = input("A. Tell his dad the truth\nB. Lie to him\n")
    print("\"Hi Dad\"\n")
    time.sleep(2)
    print("\"Hi Son, how was your day at school?\"\n")
    time.sleep(2)
    if ab in answer_A:
        print("\"It wasn't good...I got back my math test\"\n")
        time.sleep(2)
        print("\"What did you get?\"\n")
        time.sleep(2)
        disappoint()
    if ab in answer_B:
        print('\"It was good\"\n')
        time.sleep(2)
        print('\"Did you get back your math test?\"\n')
        time.sleep(2)
        print('\"I did not have math today, so I didn\'t get it back\"\n')
        time.sleep(2)
        b0 = input('\"Are you sure?\" (y/n)\n')
        if b0 in yes:
            print('\"Yes, I didn\'t recieve my math test\"\n')
            time.sleep(2)
            print('\"Well that is not what your PowerSchool shows.\nDo you really think you can lie to your father and get away with it? Bend Over\"\n')
            time.sleep(2)
            b1 = input('A. Bend Over\nB. Don\'t bend over\n')
            if b1 in answer_A:
                print('Faateh bends over\n')
                time.sleep(2)
                print('Dad whips him\n')
                print(color.RED + 'Faateh is now dead.' + color.END)
                print('Score: 0/10')
            if b1 in answer_B:
                print('\"No Dad, you can no longer use force on me. I\'ll call child services on you\"\n')
                time.sleep(2)
                print('\"Oh Really? But the child services will take 5 minutes to get here. Until then, somebody is going to get really hurt\"\n')
                time.sleep(2)
                print('\"Dad if you do that, I\'ll run away\"\n')
                b2 = input('A. Run away\nB. Keep talking\n')
                if b2 in answer_A:
                    print('\"Thats it dad, I\'m running away\"\n')
                    time.sleep(2)
                    print('\"Son, go to your room right now\"\n')
                    b3 = input("A. Go to room\nB. Really run away\n")
                    if b3 in answer_A:
                        print("Faateh runs up the stairs and hides in his room\n")
                        print(color.GREEN + "Faateh barely survives." + color.END)
                        print("Score: 4/10")
                        retry()
                    if b3 in answer_B:
                        print("\"No Dad, I\'m done with listening to you\"\n")
                        time.sleep(2)
                        print("\"Faateh do your RSM right now!\"\n")
                        time.sleep(2)
                        print("\"No, I don\'t wanna!\"\n")
                        time.sleep(2)
                        print("Faateh starts to run to the front door\n")
                        time.sleep(2)
                        print("\"Faateh! Get back here!\"\n")
                        b5 = input("A. Go back and do RSM\nB. Keep running\n")
                        if b5 in answer_A:
                            print("*sigh* \"OK, I\'m sorry Dad. I\'ll do RSM. Please forgive me.\"\n")
                            time.sleep(2)
                            print("\"After the way you behaved with me? I don\'t think so.\"\n")
                            dies()
                        if b5 in answer_B:
                            slipper() #branch at top runs
                if b2 in answer_B:
                    print("\"You won't m8\"\n")
                    time.sleep(2)
                    print("\"Oh really?\"\n")
                    time.sleep(2)
                    print("\"It\'ll take you 10 minutes to pack your bag\"\n")
                    b4 = input("A. I already packed my bag\nB. I don\'t think so\n")
                    if b4 in answer_A:
                        print("\"Well where is it then?\"\n")
                        time.sleep(2)
                        print("Dad pulls out whip\n")
                        b12 = input("A. Show him\nB. Lie to him\n")
                        if b12 in answer_A:
                            print("\"Son is this a vape?\"\n")
                            time.sleep(2)
                            print("\"Dad, no it\'s not I swear\"\n")
                            time.sleep(2)
                            print("\"C\'mere Son\"\n")
                            time.sleep(2)
                            print("\"DAD that\'s my pencil lea-\"\n")
                            time.sleep(2)
                            print("Faateh gets whipped\n")
                            dies()
                        if b12 in answer_B:
                            print("\"It\'s in my bedroom closet\"\n")
                            time.sleep(2)
                            print("\"It had better be or no curry for you tonight! Stay right there\"\n")
                            time.sleep(2)
                            print("Dad walks upstairs to the closet\n")
                            b13 = input("A. Stay where you are\nB. Run away\n")
                            if b13 in answer_A:
                                print("While Dad gets the bag, Mom walks into the room with a slipper\n")
                                time.sleep(2)
                                print(".")
                                time.sleep(0.5)
                                print(".")
                                time.sleep(0.5)
                                print(".\n")
                                dies()
                            if b13 in answer_B:
                                slipper() #branch at top runs
                    if b4 in answer_B:
                        print("\"Are you sassing me, Son?\"\n")
                        time.sleep(2)
                        print("Faateh gets whipped\n")
                        dies()
        if b0 in no:
            disappoint()
game()
