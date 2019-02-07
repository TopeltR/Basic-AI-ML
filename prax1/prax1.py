from queue import Queue

lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]
start_row=14
start_col=16

lava_map2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]





def minu_otsing(kaart):
    # start (algolek) on näiteks tuple kujul (x, y)
    start = (start_col,start_row)
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    path = []
    while not frontier.empty():
        current = frontier.get()
        if current == 'B' :
            path.append(current)
            break

       # for next in graph.neighbors(current):  # see osa tuleb suht palju ümber teha.
                                               # tuleb leida sobivad naaberruudud kaardilt
                                               # nagu ta meile ette on antud (ülal, all,
                                               # paremal ja vasakul olev ruut)
            # if next not in came_from:
            #     frontier.put(next)
            #     came_from[next] = current


    # Kui teemant on leitud, tuleb ka teekond rekonstrueerida
    # mis andmestruktuurina teekonda esitada, pole oluline,
    # aga loomulik viis oleks list
    return path