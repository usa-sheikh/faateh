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
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

required = ("\nYou can only choose option A, B, or C\n") #Cutting down on duplication
required2 = ("\nYou can only choose option A or B\n")

print("+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+")
print("|K|e|e|p| |F|a|a|t|e|h| |A|l|i|v|e|")
print("+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+\n\n")


print("Faateh is going home and is going to get whipped because of his math grade.\nWhat should he do?\n\n")
ab = input("A. Tell his dad the truth\nB. Lie to him\n")
if ab in answer_A:
    print("\"Hi Dad\"\n")
    time.sleep(1)
    print("\"Hi Son, how was your day at school?\"\n")
    time.sleep(2)
    print("\"It wasn't good...I got back my math test\"\n")
    time.sleep(2)
    print("\"What did you get?\"\n")
    time.sleep(2)
    print("\"I got a 60\"\n")
    time.sleep(2)
    print("\"Son, I'm extremely disappointed in you. You have talent, and you have the ability to succeed. Try harder next time.\"\n")
    print(color.BOLD + "Faateh survives." + color.END)
    print("Score: 1/10")

if ab in answer_B:
    print('\"Hi Dad\"\n')
    time.sleep(1)
    print('\"Hi Son, how was your day at school?\"\n')
    time.sleep(2)
    print('\"It was good\"\n')
    time.sleep(2)
    print('\"Did you get back your math test?\"\n')
    time.sleep(2)
    print('\"I did not have math today, so I didn\'t get it back\"\n')
    time.sleep(2)
    b0 = input('\"Are you sure?\"\n')
    #b0

    if b0 in yes:
        print('\"Yes, I didn\'t recieve my math test\"\n')
        time.sleep(2)
        print('\"Well that is not what your PowerSchool shows.\nDo you really think you can lie to your father and get away with it? Bend Over\"\n')
        time.sleep(4)
        #b1

    if b0 in no:
        print("\"I got a 60\"\n")
        time.sleep(2)
        print("\"Son, I'm extremely disappointed in you. You have talent, and you have the ability to succeed if you put your mind to it. Try harder next time.\"\n")
        time.sleep(4)
        print(color.BOLD + "Faateh survives." + color.END)
        print("Score: 1/10")

    b1 = input('A. Bend Over\nB. Don\'t bend over\n')

    if b1 in answer_A or yes:
        print('Faateh bends over\n')
        time.sleep(1)
        print('Dad whips him\n')
        time.sleep(1)
        print(color.BOLD + 'Faateh is now dead.' + color.END)
        print('Score: 0/10')

    if b1 in answer_B or b1 in no:
        print('\"No Dad, you can no longer use force on me. I\'ll call child services on you\"\n')
        time.sleep(3)
        print('\"Oh Really? But the child services will take 5 minutes to get here. Until then, somebody is going to get really hurt\"\n')
        time.sleep(4)
        print('\"Dad if you do that, I\'ll run away\"\n')
        time.sleep(2)
        b2 = input('A. Run away\nB. Keep talking\n')

    if b2 in answer_A:
        print('\"Thats it dad, I\'m running away\"\n')
        time.sleep(2)
        print('\"Son, go to your room right now\"\n')
        time.sleep(2)
        b3 = input("A. Go to room\nB. Really run away\n")

    if b2 in answer_B:
        print("\"You won't m8\"\n")
        time.sleep(2)
        print("\"Oh really?\"\n")
        time.sleep(2)
        print("\"It\'ll take you 10 minutes to pack your bag\"\n")
        time.sleep(2)
        b4 = input("A. I already packed my bag\nB. I don\'t think so\n")

    if b3 in answer_A:
        print("Faateh runs up the stairs and hides in his room\n")
        time.sleep(2)
        print(color.BOLD + "Faateh barely survives." + color.END)
        print("Score: 4/10")

    if b3 in answer_B:
        print("\"Thats it dad, I\'m done with you\"\n")
        time.sleep(2)
        print("\"Faateh do your RSM right now!\"\n")
        time.sleep(2)
        print("\"I don't think so\"\n")
        time.sleep(2)
        print("Faateh starts to run to the front door\n")
        time.sleep(2)
        print("\"Faateh! Get back here!\"\n")
        time.sleep(2)
        b5 = input("A. Go back and do RSM\nB. Keep running\n")
        time.sleep(2)

    if b4 in answer_A:
        print("\"Well where is it then?\"\n")
        print("Dad pulls out whip\n")
    if b4 in answer_B:
        print("\"Are you sassing me, sonny?\"\n")
        print("Faateh gets whipped\n")
        print(color.BOLD + "Faateh dies." + color.END)
        print("Score: 0/10")

    if b5 in answer_A:
        print("Faateh accepts defeat and walks back to do RSM\n")
        print(color.BOLD + "Faateh barely survives." + color.END)
        print("Score: 5/10")

    if b5 in answer_B:
        print("Faateh's mom is waiting at the doorway with a slipper in her hand\n")
        time.sleep(2)
        b6 = input("A. Juke her\nB. Accept defeat\nC. Run up the stairs\n")

    if b6 in answer_A:
        b7 = input("A. Juke to the left\nB. Juke to the right\nC. Slide under her legs\n")

    if b6 in answer_B:
        print("Faateh's dad comes up behind him with a whip and knocks him unconcious\n")
        print(color.BOLD + "Faateh dies.\n" + color.END)
        print("Score: 0/10")

    if b6 in answer_C:
        print("Faateh sprints up the stairs into his room. He can hear his parents running up the stairs while screaming slurs in his native language. Faateh locks the door.\n")
        b9 = input("A. Jump out the window\nB. Hide in the closet\n")

    if b9 in answer_A:
        print("Faateh miraculoudly survives the jump. However, Faateh's dad does as well and starts sprinting towards Faateh with whip in hand\n")
        b10 = input("A. Run to Auntie\'s house\nB. Run to Bus 17\n")

    if b10 in answer_A:
        print("BANG, BANG, BANG\n")
        print("\"Auntie, let me in!\"\n")
        print("BANG, BANG, BANG\n")
        print("\"Quick, open the door!\"\n")
        print("Faateh\'s dad walks up behind him and kicks Faateh to the ground\n")
        print("\"Ah, my ACL!\"\n")
        print("Faateh gets whipped on the spot\n")
        print(color.BOLD + "Faateh dies.\n" + color.END)
        print("Score: 0/10")

    if b10 in answer_B:
        print("Faateh spots Bus 17 barreling down the road. Debby the bus driver scoops him up, but Faateh notices his parents have gotten into the '01 Accord and are in hot pursuit after him.\n")
        b11 = input("A. Stay in the bus\nB. Run inside HHS\n")

    if b11 in answer_A:
        print("Faateh stays inside the bus as his parents walk up to the door\n")
        print("Debby refuses to open the door, and after 2 hours of waiting his parents decide to go home\n")
        print(color.BOLD + "Faateh barely survives.\n" + color.END)
        print("Score: 8/10")

    if b11 in answer_B:
        print("Faateh runs by Mrs. Fairbanks\n")
        print("\"Oh hey, Faateh! I wanted to discuss your recent test score with you. I\'ve called your parents and they said they are on their way right now\"\n")
        print(color.BOLD + "Faateh dies.\n" + color.END)
        print("Score: 0/10")

    if b9 in answer_B:
        print("Faateh cowers inside his closet. Dad opens the closet door and pulls out his whip\n")
        print("\"Dad, no!\"\n")
        print("Faateh\'s vision goes dark\n")
        print(color.BOLD + "Faateh dies.\n" + color.END)
        print("Score: 0/10")

    if b7 in answer_A:
        print("Faateh attempts to juke his mom, but he is not athletic, so he slips and tears his ACL\n")
        print(color.BOLD + "Faateh dies.\n" + color.END)
        print("Score: 0/10")

    if b7 in answer_B:
        print("By God\'s grace, Faateh miraculously slips past his mom and makes it out the door.\n")
        print("However, Evan Theodorough is waiting outside with a basketball.\n")
        print("\"Yo, nice jukes Fay. 1v1 me.\"\n")
        b8 = input("A. Accept his challenge\nB. Decline and keep running\n")

    if b7 in answer_C:
        print("Faateh attempts to slide under his mom\'s legs, but he is not athletic\n")
        print(color.BOLD + "Faateh slips and dies.\n" + color.END)
        print("Score: 0/10")

    if b8 in answer_A:
        print("\"Yeah man, let\'s go\"\n")
        print("Faateh walks and falls over, scraping his knee\n")
        print("\"My ACL!\"\n")
        print(color.BOLD + "Faateh bleeds out and dies.\n" + color.END)
        print("Score: 0/10")

    if b8 in answer_B:
        print("Faateh runs into the street and is run over by Bus 17\n")
        print(color.BOLD + "Faateh dies.\n" + color.END)
        print("Score: 0/10")
