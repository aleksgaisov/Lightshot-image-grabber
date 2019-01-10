from urllib.request import urlopen
from urllib.request import Request
import requests
from random import randint

################INITIALIZING LOGO################

R  = '\033[31m' # red
G  = '\033[32m' # green
W  = '\033[0m'  # white (normal)

print(' ')     #figlet terminal command

print(G+'======================================================================'+W)
print(W+' _'+G+'     _       _     _       _           _           ')
print(W+'| |'+G+'   (_) __ _| |__ | |_ ___| |__   ___ | |_         ')
print(W+"| |"+G+"   | |/ _` | '_ \| __/ __| '_ \ / _ \| __|  _____ ")
print(W+'| |___'+G+'| | (_| | | | | |_\__ \ | | | (_) | |_  |_____|')
print(W+'|_____|'+G+'_|\__, |_| |_|\__|___/_| |_|\___/ \__|        ')
print('         |___/                                       ')
print(W+' _'+G+'                              '+W+' ____'+G+'           _     _               ')
print(W+'(_)'+G+'_ __ ___   __ _  __ _  ___   '+W+'/ ___|'+G+'_ __ __ _| |__ | |__   ___ _ __ ')
print(W+"| |"+G+" '_ ` _ \ / _` |/ _` |/ _ \ "+W+"| |  _|"+G+" '__/ _` | '_ \| '_ \ / _ \ '__|")
print(W+'| |'+G+' | | | | | (_| | (_| |  __/ '+W+'| |_| |'+G+' | | (_| | |_) | |_) |  __/ |   ')
print(W+'|_|'+G+'_| |_| |_|\__,_|\__, |\___|  '+W+'\____|'+G+'_|  \__,_|_.__/|_.__/ \___|_|   ')
print('                   |___/                                              ')
print(' ')
print(G+'======================================================================'+W)

print(' ')
##################################################

###############INITIALIZING PROCESS###############
print('-----------------------------------')
print('CHOOSE THE GRABBING ATTACK:')
print(' ')
print(G+'Dictionary(1)'+W)
print(G+'Random-key(2)'+W)
print(G+'Only-Numbers(3)'+W)
print(G+'Only-Alphabet(4)'+W)
print('-----------------------------------')
print(' ')

while True:
    grabbing_type = input(G+'-->'+W+' ')    #The type of grabing algorithm
    if grabbing_type.isdigit() == True:
        if int(grabbing_type) <= 4:
            if int(grabbing_type) > 0:
                break
            else:
                print(R+'Please, enter the amount larger than 0:'+W)
                continue
        else:
            print(R+'Please, enter the correct digit:'+W)
            continue
    else:
        print(R+'Please, enter a digit:'+W)
        continue

print(' ')

print('-----------------------------------')
print('SPECIFY THE NUMBER OF IMAGES:')
print(G+'(Choose the number less than 10000)'+W)
print('-----------------------------------')
print(' ')

while True:
    img_amount = input(G+'-->'+W+' ')     #The quantity of images to grab
    if img_amount.isdigit() == True:
        if int(img_amount) <= 10000:
            if int(img_amount) > 0:
                break
            else:
                print(R+'Please, enter the amount larger than 0:'+W)
                continue
        else:
            print(R+'Please, enter the amout less than 10000:'+W)
            continue
    else:
        print(R+'Please, enter a digit:'+W)
        continue

print(' ')

print('-----------------------------------')
print('SPECIFY THE SAVING PATH:')
print('-----------------------------------')
print(' ')

while True:
    save_path = input(G+'-->'+W+' ')    #The path to save the grabed images
    if save_path[0] == '/':
        break
    else:
        print(R+'Please, enter the correct path:'+W)
        continue
    
print(' ')

#Some required arrays for the attack number 2, 3 and 4
alp_list_init = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alp_list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz']
num_list = [i for i in range(100, 1000)]

img_quantity = int(0)     #Counting the amount of images downloaded
##################################################

##################################################
def get_img_link(inner_req):     #Function for getting the image link from the page source code
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers = { 'User-Agent' : user_agent }
    req = Request(inner_req, None, headers)
    response = urlopen(req)
    page = response.read()
    response.close() 
    
    
    page_string = str(page)
    init_str = '<img class="no-click screenshot-image" src='
    
    init_index = page_string.find(init_str, 0, len(page_string))     #The initial index of the '<' element (init_str)
    
    start_index = init_index + 44     #Element of start index should be 'h' (page_string[start_index])
    counter_index = start_index
    
    image_link = ''     #The future link of the image
    
    
    if page_string[counter_index + 55] == 'j' and page_string[start_index] != '/':     #If .jpeg
        image_link = page_string[start_index:start_index + 59]     #The link of the image if: image.jpeg
    elif page_string[counter_index + 55] == 'p' and page_string[start_index] != '/':     #If .png
        image_link = page_string[start_index:start_index + 58]     #The link of the image if: image.png
    elif page_string[start_index] == '/':
        image_link = '///'     #The link of the image if: image.no such image
   
    return image_link
##################################################

##################################################
if int(grabbing_type) == 1:     #If the 'Dictionary' grab in chosen
    
    grab_keys = open('grab_keys.txt', 'r')
    grab_keys_list = [line.strip() for line in grab_keys]
    
    for i in range(int(img_amount)):
        url_grab = 'https://prnt.sc/m0q' + str(grab_keys_list[i])     #Adding the 3 elements to the initial link
        
        if get_img_link(url_grab)[0] != '/':
            r = requests.get(get_img_link(url_grab))
            path = save_path    
            
            print(G+'Image found on:'+W, url_grab)
            
            with open(path + str(i), 'wb') as f:     #Downloading the image
                f.write(r.content) 
            
            img_quantity = img_quantity + 1
            
        else:
            print(R+'No image on this link'+W)
            continue
    grab_keys.close()
    
    
elif int(grabbing_type) == 2:     #If the 'Random-key' grab in chosen
    
    for i in range(int(img_amount)):
        
        rand_chooser = randint(0, 1)
        if rand_chooser == 0:
            search_key = str(randint(10, 100)) + str(alp_list_init[randint(0, 25)])
        elif rand_chooser == 1:
            search_key = str(alp_list_init[randint(0, 25)]) + str(randint(10, 100))
        
        url_grab = 'https://prnt.sc/m0q' + str(search_key)     #Adding the 3 elements to the initial link
        if get_img_link(url_grab)[0] != '/':
            r = requests.get(get_img_link(url_grab))
            path = save_path  
            
            print(G+'Image found on:'+W, url_grab)
            
            with open(path + str(i), 'wb') as f:     #Downloading the image
                f.write(r.content)
                
            img_quantity = img_quantity + 1
                
        else:
            print(R+'No image on this link'+W)
            continue

            
elif int(grabbing_type) == 3:     #If the 'Only-Numbers' grab in chosen
    
    for i in range(int(img_amount)):
        search_key = num_list[i]
        
        url_grab = 'https://prnt.sc/m0q' + str(search_key)     #Adding the 3 elements to the initial link
        
        if get_img_link(url_grab)[0] != '/':
            r = requests.get(get_img_link(url_grab))
            path = save_path     
            
            print(G+'Image found on:'+W, url_grab)
            
            with open(path + str(i), 'wb') as f:     #Downloading the image
                f.write(r.content)
                
            img_quantity = img_quantity + 1
                
        else:
            print(R+'No image on this link'+W)
            continue
            
    
elif int(grabbing_type) == 4:     #If the 'Only-Alphabet' grab in chosen
    
    for i in range(0, 26):
        search_key = alp_list[i]
        
        url_grab = 'https://prnt.sc/m0q' + str(search_key)     #Adding the 3 elements to the initial link
        
        if get_img_link(url_grab)[0] != '/':
            r = requests.get(get_img_link(url_grab))
            path = save_path  
            
            print(G+'Image found on:'+W, url_grab)
            
            with open(path + str(i), 'wb') as f:     #Downloading the image
                f.write(r.content)
                
            img_quantity = img_quantity + 1
                
        else:
            print(R+'No image on this link'+W)
            continue
            
print(' ')
print('==============================')     #Displaying the results of the grabbing process
print('GRABBING PROCESS COMPLETED')
print(' ')

print(G+'Images grabbed:'+W, img_quantity)

if int(grabbing_type) == 1:
    print(G+'Grabbing attack:'+R+' Dictionary')
elif int(grabbing_type) == 2:
    print(G+'Grabbing attack:'+R+' Random-key')
elif int(grabbing_type) == 3:
    print(G+'Grabbing attack'+R+': Only-Numbers')
elif int(grabbing_type) == 4:
    print(G+'Grabbing attack:'+R+' Only-Alphabet')
    
print(G+'Saved:'+W,save_path)
print('==============================')
##################################################    
