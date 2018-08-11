import time , os , requests , pygame , urllib
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class color:   
   MAGENTA = '\033[35m'                                                                                                                                                                                                 
   YELLOW = '\033[33m'                                                                                            
   BLUE = '\033[94m'
   DARKCYAN = '\033[96m'                                                                                                                                                                                         
   GREEN = '\033[92m'                                                                                                                                                                                       
   RED = '\033[91m'                                                                                               
   BOLD = '\033[1m' 
   WHITE = '\033[37m'                                                                                              
   END = '\033[0m'
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
dic = {}
def sys():
  print(color.BOLD + color.RED + ' /------------------------------\\' + color.END)
  print(color.BOLD + color.RED + ' |    ' + color.GREEN + 'mahsol' + color.RED + '    |    ' + color.GREEN + 'gheymat' + color.RED + '    |' + color.END)
  print(color.BOLD + color.RED + ' |------------------------------|' + color.END)
  for SYS113 in dic.items():
      print(color.BOLD +color.RED + ' |    ' + color.BLUE + SYS113[0] + color.RED + ' \t|    ' + color.BLUE + SYS113[1] + color.RED + '\t|' + color.END)
  print(color.BOLD + color.RED + ' \\------------------------------/' + color.END)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
cls()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def loading():
  cls()
  print(color.BOLD + color.YELLOW + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t     " + "loading " + color.RED + "." + color.END)
  time.sleep(1)
  cls()
  print(color.BOLD + color.YELLOW + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t     " + "loading " + color.RED + "." + color.GREEN + "." + color.END)
  time.sleep(1)
  cls()
  print(color.BOLD + color.YELLOW + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t     " + "loading " + color.RED + "." + color.GREEN + "." + color.BLUE + "." + color.END)
  time.sleep(1)
  cls()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
os.system('mkdir -p ~/.SYS113')
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
home = os.path.expanduser('~')
homeee = home + '/.SYS113/'
dirme = home + '/Desktop/'
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
url = 'https://github.com/sys113/shopping-list/raw/master/SYS113.mp3'
fileName = '%sSYS113.mp3'%(homeee)
req = requests.get(url)
file = open(fileName, 'wb')
for chunk in req.iter_content(100000):
  file.write(chunk)
file.close()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if 'SYS113.mp3' not in os.listdir(homeee):
  while True:
    loading()
    if 'SYS113.mp3' in os.listdir(homeee):
            break
loading()
loading()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pygame.mixer.init(44100, -16,2,2048)
pygame.mixer.music.load(homeee + 'SYS113.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def all(): 
  print(color.BOLD + color.GREEN + " -+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+- " + color.RED + "CODED"+ color.YELLOW + " BY " + color.BLUE +"SYS113"+ color.GREEN + " -+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+- " + color.END)
  print(color.BOLD + color.BLUE + "\n\t\t\t\t\t\t      [" + color.RED + "+" + color.BLUE + "]" + color.GREEN + "  0 = exit             " + color.BLUE + "[" + color.RED + "+" + color.BLUE + "]" + color.END)
  print(color.BOLD + color.BLUE + "\n\t\t\t\t\t\t      [" + color.RED + "+" + color.BLUE + "]" + color.BLUE + "  1 = add item         " + color.BLUE + "[" + color.RED + "+" + color.BLUE + "]" + color.END)
  print(color.BOLD + color.BLUE + "\n\t\t\t\t\t\t      [" + color.RED + "+" + color.BLUE + "]" + color.RED + "  2 = show items       " + color.BLUE + "[" + color.RED + "+" + color.BLUE + "]" + color.END)
  print(color.BOLD + color.BLUE + "\n\t\t\t\t\t\t      [" + color.RED + "+" + color.BLUE + "]" + color.MAGENTA + "  3 = remove item      " + color.BLUE + "[" + color.RED + "+" + color.BLUE + "]" + color.END)
  print(color.BOLD + color.BLUE + "\n\t\t\t\t\t\t      [" + color.RED + "+" + color.BLUE + "]" + color.YELLOW + "  4 = remove all items " + color.BLUE + "[" + color.RED + "+" + color.BLUE + "]" + color.END)
  print(color.BOLD + color.BLUE + "\n\t\t\t\t\t\t      [" + color.RED + "+" + color.BLUE + "]" + color.WHITE + "  5 = clear screen     " + color.BLUE + "[" + color.RED + "+" + color.BLUE + "]" + color.END)
  print(color.BOLD + color.BLUE + "\n\t\t\t\t\t\t      [" + color.RED + "+" + color.BLUE + "]" + color.DARKCYAN + "  6 = save             " + color.BLUE + "[" + color.RED + "+" + color.BLUE + "]" + color.END)
  print(color.BOLD + color.BLUE + "\n\t\t\t\t\t\t      [" + color.RED + "+" + color.BLUE + "]" + color.RED + "  7 = cal              " + color.BLUE + "[" + color.RED + "+" + color.BLUE + "]" + color.END)
  print(color.BOLD + color.BLUE + "\n\t\t\t\t\t\t      [" + color.RED + "+" + color.BLUE + "]" + color.BLUE + "  8 = contact me       " + color.BLUE + "[" + color.RED + "+" + color.BLUE + "]" + color.END)
  print(color.BOLD + color.GREEN + "\n -+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+- "+ color.RED + "CODED"+ color.YELLOW + " BY " + color.BLUE +"SYS113"+ color.GREEN + " -+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+- \n"+color.END)
all()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    send = input(color.BOLD+color.BLUE+" >"+color.RED+">"+color.GREEN+"> " + color.YELLOW)
    print(color.END)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if send == "0":
      close = input(color.BOLD + color.DARKCYAN + "motmaeni k mikhay kharj beshi ? [y / n] : " +  color.YELLOW)
      print(color.END)
      if close in "y":
        print(color.BOLD + color.BLUE + " b" + color.GREEN + "y" + color.RED + "!" + color.YELLOW + ":D\n" + color.END)
        time.sleep(1)
        break
      elif close in "n":
        print(color.BOLD + color.DARKCYAN + "besiar khob pas nmikhay kharj beshi :D\n" + color.END)
      else:
        print(color.BOLD + color.DARKCYAN + "faghat mitoni y , n vared koni!!!\n" + color.END)
# =====================================================================================================================================================================
    elif send == "1":
      jens= input(color.BOLD + color.DARKCYAN + " esm jenso bego : " + color.YELLOW)
      gheymat = input(color.BOLD + color.DARKCYAN + "\n gheymatesho bego : " + color.YELLOW)
      print(color.BOLD + color.DARKCYAN + "\n hale ezafash kardam be list jensa! :|\n")
      dic[jens] = gheymat
# =====================================================================================================================================================================
    elif send == "2":
      if len(dic) == 0:
        print(color.BOLD + color.DARKCYAN + " hanoz k hich jensi ezafe nakardi!\n")
      elif len(dic) != 0:
        print(color.BOLD + color.DARKCYAN + " ta alan {} jens ezafe kardi!\n".format((len(dic))))
        sys()
        print(color.END)
# =====================================================================================================================================================================
    elif send == "3":
      remove = input(color.BOLD + color.DARKCYAN + " esm jenso bego : " + color.YELLOW)
      if remove in dic:
        del dic[remove]
        print(color.BOLD + color.DARKCYAN + "\n %s ro az list jensa pakidam! :|\n"%(remove))

      elif remove not in dic:
        print(color.BOLD + color.DARKCYAN + "\n %s to list jensa nis k baradare man! :|\n"%(remove))
# =====================================================================================================================================================================
    elif send == "4":
      if len(dic) == 0:
        print(color.BOLD + color.DARKCYAN + " chio pak konm vaghti hanoz hichi ezafe nakardi ? :| \n" + color.END)
      else:
        rm = input(color.BOLD + color.DARKCYAN + " kol item haro bepakam ? [y / n] : " +  color.YELLOW)
        if rm == "y":
          dic.clear()
          print(color.BOLD + color.DARKCYAN + "\n kol item haye list hazf shod :|\n" + color.END)
        elif rm == "n":
          print(color.BOLD + color.DARKCYAN + "\n ok pas item haye list ro hazf nmikonam :))\n" + color.END)
        else:
          print(color.BOLD + color.DARKCYAN + "\n faghat mitoni y , n vared koni!!!\n" + color.END)
# =====================================================================================================================================================================
    elif send == "5":
      print(color.BOLD + color.DARKCYAN + " bezar safhe ro clear konam alan miam! :|\n" + color.END)
      time.sleep(3)
      cls()
      all()
# =====================================================================================================================================================================
    elif send == "6":
      shop_txt =dirme + "shopping-list-by-SYS113.txt"
      SYS113_shop = open(shop_txt, "w")
      SYS113_shop.write(' /------------------------------\\\n')
      SYS113_shop.write(' |    mahsol    |     gheymat   |')
      SYS113_shop.write('\n |------------------------------|\n')
      for k, v in dic.items():
        SYS113_shop.write(' |    {} \t|    {}\t|\n'.format(str(k) , str(v)))
      SYS113_shop.write(' \\------------------------------/\n') 
      SYS113_shop.close()


      print(color.BOLD + color.DARKCYAN + 'save shod list mahsolat dar %sshopping-list-by-SYS113.txt !\n'%(dirme) + color.END)
# =====================================================================================================================================================================
    elif send == "7":
      calc1 = int(input(color.BOLD + color.BLUE + "\n add aval : " + color.YELLOW))
      operator = input(color.BOLD + color.GREEN + "\n - , + , * : " + color.YELLOW)
      calc2 = int(input(color.BOLD + color.RED + "\n add dovom : " + color.YELLOW))

      if operator == "-":
        opera = calc1-calc2
        print(color.BOLD + color.MAGENTA + "\n hasele %d - %d mishavad : %d ! :D\n"%(calc1,calc2,opera) + color.END)

      elif operator == "+":
        opera = calc1+calc2
        print(color.BOLD + color.MAGENTA + "\n hasele %d + %d mishavad : %d ! :D\n"%(calc1,calc2,opera) + color.END)

      elif operator == "*":
        opera = calc1*calc2
        print(color.BOLD + color.MAGENTA + "\n hasele %d * %d mishavad : %d ! :D\n"%(calc1,calc2,opera) + color.END)

      else:
        print(color.BOLD + color.RED + "\nfaghat mitavanid - , + , * vared konid!\n")
# =====================================================================================================================================================================
    elif send == "8":
      print(color.BOLD + color.GREEN + '\t\t\t\t\t\t      ' + '-='*16 + '-' + color.END)
      print(color.BOLD + color.GREEN + '\t\t\t\t\t\t      ' + '|\t\t\t\t      |')
      print(color.BOLD + color.GREEN + '\t\t\t\t\t\t      ' + '| ' + color.RED + '     telegram' + color.YELLOW + ' : ' + color.BLUE + '@SYS113' + color.GREEN + '\t      |'  + color.END)
      print(color.BOLD + color.GREEN + '\t\t\t\t\t\t      ' + '|\t\t\t\t      |')
      print(color.BOLD + color.GREEN + '\t\t\t\t\t\t      ' + '|  ' + color.RED + 'github' + color.YELLOW + ' : ' + color.BLUE + 'github.com/SYS113/' + color.GREEN + '  |'  + color.END)
      print(color.BOLD + color.GREEN + '\t\t\t\t\t\t      ' + '|\t\t\t\t      |')
      print(color.BOLD + color.GREEN + '\t\t\t\t\t\t      ' + '| ' + color.RED + 'mail' + color.YELLOW + ' : ' + color.BLUE + '051.SYS113@gmail.com' + color.GREEN + '  |'  + color.END)
      print(color.BOLD + color.GREEN + '\t\t\t\t\t\t      ' + '|\t\t\t\t      |')
      print(color.BOLD + color.GREEN + '\t\t\t\t\t\t      ' + '-='*16 + '-\n' + color.END)
# =====================================================================================================================================================================
    else:
      print(color.END + color.BOLD + color.DARKCYAN + " faghat mitoni 1...7 ro vared koni! :D\n")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
