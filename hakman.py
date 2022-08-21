from time import sleep
print("                     _                                                                                                   ")
print("|          |        / \        |    /       / \         /\             /\             /\            /")
print("|          |       /   \       |   /       /   \       /  \           /  \           /  \          / ")
print("|          |      /     \      |  /       /     \     /    \         /    \         /    \        /")
print("|----------|     /_______\     | /       /       \   /      \       /------\       /      \      /")
print("|          |    /         \    | \      /         \ /        \     /        \     /        \    /")
print("|          |   /           \   |  \    /                      \   /          \   /          \  /")
print("|          |  /             \  |   \  /                        \ /            \ /            \/")
print("                                                           report problems at hakman@gmail.com")
print("█░█ ▄▀█ █▄▀ █▀▄▀█ ▄▀█ █▄░█")
print("█▀█ █▀█ █░█ █░▀░█ █▀█ █░▀█")

#importing libraries
from bs4 import BeautifulSoup
import requests

#instagram URL
URL = "https://www.instagram.com/{}/"


#parse function
def parse_data(s):
    #creating a dictionary
    data = {}

    #splitting the content
    #then taking the first part
    s = s.split("-")[0]

    #again splitting the content
    s = s.split(" ")

    # assigning the values
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]

    #returning the dictionary
    return data


#scrape function
def scrape_data(b1):
    #getting the request from url
    r = requests.get(URL.format(b1))

    #converting the text
    s = BeautifulSoup(r.text, "html.parser")

    #finding meta info
    meta = s.find("meta", property="og:description")

    #calling parse method
    return parse_data(meta.attrs['content'])


#main function
if __name__ == "__main__":
    #username
    a2=a1=input("ENTER USERNAME:")
    print("FINDING ACCOUNT....")
    sleep(3)

    #calling scrape function
    data = scrape_data(a2)

    #printing the info
    print(data)
a2=input("(っ◔◡◔)っ ♥ ENTER ♥ⱣȺSSWØɌĐ:")

sleep(5)
print(a2+ ":ⱣȺSSWØɌĐ MATCHING ")
import time
import sys
def write(write):
    # Repeats for each letter.
    for i in write:
        # sys.stdout.write doesn't create a new line for each print
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.05)
    # Do you want to continue to the next text?

    print(".")
write("FETCHING DATA FROM ACCOUNT...")

from time import sleep
def loadbar(iteration, total, prefix='', suffix='', decimals=1, lenght=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledlenght = int(lenght * iteration // total)
    bar = fill * filledlenght + '-' * (lenght - filledlenght)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

items = list(range(0, 50))
l = len(items)

loadbar(0, l,prefix='progress:', suffix='complete', lenght=l)
for i, item in enumerate(items):
    sleep(0.1)
    loadbar(i + 1, l, prefix='progress:', suffix='complete', lenght=l)
print("instagram followers tool")
input("y,n(default-y)=")
print("--------------------------")
print("--------------------------")
import itertools
import threading
import time
import sys

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLOGGING IN ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10)
done = True
sleep(5)
print(">")


print("₣ØⱠⱠØ₩ł₦₲ ₳₦Đ Ʉ₦₣ØⱠⱠØ₩ł₦₲ ₱ⱤØ₣łⱠɆ₴:")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(5)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")
print("VERIFYING|")
sleep(5)
print("USERNAME=" + a1)
print("ⱣȺSSWØɌĐ=" + a2)
print("LOGGING OUT")
sleep(4)
import sys
from time import sleep

def animate(text):
  for letter in text:
    print(letter, end="")
    sys.stdout.flush()
    sleep(0.05) # I use 0.05 but you can change it


animate("█░█ ▄▀█ █▄▀ █▀▄▀█ ▄▀█ █▄░█")
print("")
animate("█▀█ █▀█ █░█ █░▀░█ █▀█ █░▀█")
print("")
input("$")
