# Lightshot-image Grabber

## Warnings
I would like to warn you that via creating this project I did not mean to intervene in anybody’s  privacy or personal life.

The goal of this project is to show that even the beginner programmer, knowing the ‘conditional programming’ and how to use the @Stack Overflow can exploit some simple security holes within the wide-spread service. Therefore to show the importance of choosing the right services a both, user’s and the service’s, main concern for keeping private things as private. 

**I am not advising you to use this project as it's name is suggesting, but conversely, as an example code (debatable) and as an example of real life situation.**


## About the programm

In this project I would like to talk about the [LightShot](https://prnt.sc/) screen capture tool and their attitude towards the people's privacy in terms of the ‘Print-Screen’ images that were uploaded on their service.

The main idea is that by modification of the last 3 elements within the image link (after the letter ‘q’):

> https://prnt.sc/m0q111 (in stead of ‘111’ there could be any combination of the digits and Latin letters e.g ‘a56’ or ‘j9d’ etc.)

Allows you to see not only yours, but also every other screen shots of other users that had uploaded them.

There are several GitHub repositories that have the tools for exploiting this feature of the ‘LightShot’ service for watching and downloading the pictures of the other users. However, the goal of creating my own repository with the similar program seemed feasible to me (even with my ‘best in the world’ programming skills).

This program is been written in Python programming language (3.6.7 version) and what it does is gives you is the ability to download (or Grab) the images from the ‘LightShot’ using the link modification (specifically the last three elements) via different brute force methods(see attack methods below).


## How to use

1.**How to run**

  - The Python 3.6 was used to code this program, therefore you can use any ide (or original python idle) as well as the simple command line (terminal) typing `python3 Lightshot_image_Graber.py` to run it.
  - You may also want to install some packages for the python, such as ‘urllib’ to make this program work. You can do it by typing in the terminal`pip install urllib`.
  - Also make sure that you store the 'grab_keys.txt' (Dictionary file) file in the same forlder as the 'Lightshot_image_Graber.py' (Program file).


2.**General algorithm**

I came up with the algorithm for the image grabber in a ridiculously strange way. It even made me laugh when I first thought of it, but when implementing, it came out working perfectly fine. Therefore, so far, so good. Below I will list the most important steps of the Lightshot-image Grabber algorithm.
  1. Initializing all the fancy logos, important variables and importing necessary libraries.
  2. Asking user all important information. (The grabbing method, amount of images to download and where to save them; "/home/user/Desktop/" as an examle)
  3. Downloading the source code of the chosen page, that is being formed with the initial link: ‘https://prnt.sc/m0q’ + additional 3 symbols being added depending on the chosen attack algorithm.
  4. Searching for the  `<img class="no-click screenshot-image" src=` string element within the page source code. 
  5. After finding it, algorithm copies all further 58 elements (depending on the image type - .png: 58; .jpeg: 59), and therefore forming the initial link of the image.(This very nice process of getting the image link is being used because I was not able to came up with something more advanced than this)
  6. Then the program downloads the image and stores it in the specified path.
  7. The procedure repeats depending on how many images did the user specified. (Step 2)
  

3.**Attack methods**

This project includes 4 different attack (grabbing) methods.The only differences between them is how the link to the image page is being formed (Mentioned in Step 3). Those attacks are:
- **Dictionary (72 images per 1 min in average)**
   - The first grabbing method is using the simple dictionary attack that includes forming the page links using the pre–generated 3 element strings and adding them to the initial link. Overall, the dictionary (grab_keys.txt) file includes around 50000 combinations of a,b,c… letters and digits from 0 till 100.
- **Random-key (66 images per 1 min in average)**
   - This algorithm generates those 3 element strings by combining one a,b,c… letter with the number from 10 till 99. That results the pseudo-random string every time, that is being then added to the initial link forming the complete one.
- **Only-Numbers (102 images per 1 min in average)**
   - The third attack uses only the numbers from 100 till 99 to form the 3 element strings:111, 123, etc.; and then again being added to the initial link.
- **Only-Alphabet (84 images per 1 min in average)**
   - Very similar to the previous grabbing method, but in stead of three digits, this one uses the three letters strings: aaa, bbb, sfd etc.


## Implications of the project

This project resulted several things to me personally, which are:
- More practicing in programming
- More brain storming
- Creation of the GitHub repository :)

What it may imply to you:
- Make you to be more careful with the privacy of you data
- Choosing more responsible services
- Real life example of the private data being insecure (in our case, in quite large amounts, because only the Dictionary includes 50000 combinations for links formation and even if the half of them are not valid, it is still being the large number)
