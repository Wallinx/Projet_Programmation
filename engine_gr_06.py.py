from blessed import Terminal
import blessed, random, time, socket, time
from random import choice, randint 

term = blessed.Terminal()

#-----------------------------------------------------------------------------------------------------------
# main function
def intro():
    """ Play a Copixhe game.
    
    Parameters
    ----------

    Notes
    -----
    The game board, the anthill and the score will be displayed thanks to 
    the Blessed extension. 

    version
    -------
    specification: Moustarih Walid (v.1 21/02/2021)
    implementation Moustarih Walid (v.1 26/03/2021)
    """

    print(term.home + term.on_white + term.clear)
    Joueur_1 = input(term.black + 'Pseudo joueur 1 : ')
    Joueur_2 = input(term.black + 'Pseudo joueur 2 : ')
    print (term.black + 'Que le meilleur gagne!')
    print (term.black + '**********************')

#-----------------------------------------------------------------------------------------------------------
# main function
def tray_game():
    """ Play a Copixhe game.
    
    Parameters
    ----------

    Notes
    -----
    The game board, the anthill and the score will be displayed thanks to 
    the Blessed extension. 

    version
    -------
    specification: Moustarih Walid (v.1 21/02/2021)
    implementation Moustarih Walid (v.1 26/03/2021)
    """

    print(term.home + term.on_green + term.clear)

    print(term.black + term.move_xy(0,0) + ("┏"), end='')
    i = 0
    while i < 20:
        i = i + 1 
        print(term.black + term.move_right(-1) + ("━"), end='')
        print(term.black + term.move_right(-1) + ("━"), end='')
        print(term.black + term.move_right(-1) + ("━"), end='')
        print(term.black + term.move_right(-1) + ("┳"), end='')
    print(term.move_xy(80,0) + ("┓"), end='')
    y = 0
    print(term.black + term.home + term.move_down(y) + ("┃"), end='')
    i = 0
    while i < 20 :
        i = i + 1 
        print(term.black + term.move_right(3) + ("┃"), end='')
    x, y, j = 0, 1, 0
    while j < 10:     
           
        y = y + 1
        print(term.black + term.home + term.move_y(y) + ("┣"), end='')
        i = 0
        while i < 20 :
            i = i + 1 
            print(term.black + term.move_right(-1) + ("━"), end='')
            print(term.black + term.move_right(-1) + ("━"), end='')
            print(term.black + term.move_right(-1) + ("━"), end='')
            print(term.black + term.move_right(-1) + ("╋"), end='')
        print(term.black + term.home + term.move_xy(80,y) + ("┫"), end='')
        y = y + 1
        print(term.black + term.home + term.move_down(y) + ("┃"), end='')
        i = 0
        while i < 20 :
            i = i + 1 
            print(term.black + term.move_right(3) + ("┃"), end='')
        j = j + 1
    
    print(term.black + term.move_xy(0,22) + ("┗"), end='')
    i = 0
    while i < 20:
        i = i + 1 
        print(term.black + term.move_right(-1) + ("━"), end='')
        print(term.black + term.move_right(-1) + ("━"), end='')
        print(term.black + term.move_right(-1) + ("━"), end='')
        print(term.black + term.move_right(-1) + ("┻"), end='')
    print(term.move_xy(80,22) + ("┛"), end='')


#-----------------------------------------------------------------------------------------------------------
# main function
def creat_ants_1():
    """ Creat_ants: the function will create ants with their coordinates, life points, and strength.
    
    Parameters
    ----------

    Notesd
    -----
    The creation of ants on their anthill.

    version
    -------
    specification: Moustarih Walid (v.1 21/02/2021)
    implementation Moustarih Walid (v.1 26/03/2021)
    """

    liste_X_1 = [6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74]
    liste_Y_1 = [3]

    fourmi_1 = "\u22C1"
    fourmi_1 = u"{}".format(fourmi_1)
    fourmi_2 = "\u21CA"
    fourmi_2 = u"{}".format(fourmi_2)
    fourmi_3 = "\u22C1"
    fourmi_3 = u"{}".format(fourmi_3)
    case_1 = "\u25CC"
    case_1= u"{}".format(case_1)

    x = liste_X_1 [randint(0,17)] 
    y = liste_Y_1 [0]
    print(term.move_xy(x,y) + term.bright_red + (fourmi_1))
    print(term.move_x(x+4) + term.move_y(y)  + term.red + (case_1))
    print(term.move_x(x-4) + term.move_y(y)  + term.red + (case_1))
    print(term.move_x(x) + term.move_y(y-2)  + term.red + (case_1))
    print(term.move_x(x+4) + term.move_y(y-2)  + term.red + (case_1))
    print(term.move_x(x-4) + term.move_y(y-2)  + term.red + (case_1))
    print(term.move_x(x) + term.move_y(y+2) + term.red + (case_1))
    print(term.move_x(x+4) + term.move_y(y+2)  + term.red + (case_1))
    print(term.move_x(x-4) + term.move_y(y+2)  + term.red + (case_1))


#-----------------------------------------------------------------------------------------------------------
# main function
def placement_clods():
    """ The function will use the cpx. file to get the clods' coordinates to spawn them.
    
    Parameters
    -----------
    
    Notes
    -----
    The clods are generated from a .cpx file 
    
    version
    --------
    specification: Moustarih Walid (v.1 21/02/2021)
    implementation Moustarih Walid (v.1 26/03/2021)
    """

    clods_1 = "\u2726"
    clods_1 = u"{}".format(clods_1)
    clods_2 = "\u2737"
    clods_2 = u"{}".format(clods_2)
    clods_3 = "\u2739"
    clods_3 = u"{}".format(clods_3)
    
    liste_X_2 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78]
    liste_Y_2 = [9, 11, 13]

    i = 0
    while i < 5 :
        random.choice(liste_X_2)
        x = choice(liste_X_2)
        random.choice(liste_Y_2)
        y = choice(liste_Y_2)
        print(term.move_xy(x,y) + term.bright_black + (clods_1))
        while x in liste_X_2:
            del liste_X_2[liste_X_2.index(x)]
        i = i + 1   
    
    i = 0
    while i < 5 :
        random.choice(liste_X_2)
        x = choice(liste_X_2)
        random.choice(liste_Y_2)
        y = choice(liste_Y_2)
        print(term.move_xy(x,y) + term.bright_black + (clods_2))
        while x in liste_X_2:
            del liste_X_2[liste_X_2.index(x)]
        i = i + 1   

    i = 0
    while i < 5 :
        random.choice(liste_X_2)
        x = choice(liste_X_2)
        random.choice(liste_Y_2)
        y = choice(liste_Y_2)
        print(term.move_xy(x,y) + term.bright_black + (clods_3))
        while x in liste_X_2:
            del liste_X_2[liste_X_2.index(x)]
        i = i + 1 


#-----------------------------------------------------------------------------------------------------------
# main function
def creat_ants_2():
    """ Creat_ants: the function will create ants with their coordinates, life points, and strength.
    
    Parameters
    ----------

    Notesd
    -----
    The creation of ants on their anthill.

    version
    -------
    specification: Moustarih Walid (v.1 21/02/2021)
    implementation Moustarih Walid (v.1 26/03/2021)
    """

    liste_X_3 = [6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74]
    liste_Y_3 = [19]

    fourmi_1 = "\u22C0"
    fourmi_1 = u"{}".format(fourmi_1)
    fourmi_2 = "\u21C8"
    fourmi_2 = u"{}".format(fourmi_2)
    fourmi_3 = "\u2390"
    fourmi_3 = u"{}".format(fourmi_3)
    case_2 = "\u25CC"
    case_2= u"{}".format(case_2)

    x = liste_X_3 [randint(0,17)] 
    y = liste_Y_3 [0]
    print(term.move_xy(x,y) + term.bright_yellow + (fourmi_1))
    print(term.move_x(x+4) + term.move_y(y)   + (case_2))
    print(term.move_x(x-4) + term.move_y(y)  + (case_2))
    print(term.move_x(x) + term.move_y(y-2)  + (case_2))
    print(term.move_x(x+4) + term.move_y(y-2)   + (case_2))
    print(term.move_x(x-4) + term.move_y(y-2)  + (case_2))
    print(term.move_x(x) + term.move_y(y+2)  + (case_2))
    print(term.move_x(x+4) + term.move_y(y+2)  + (case_2))
    print(term.move_x(x-4) + term.move_y(y+2)  + (case_2))


#-----------------------------------------------------------------------------------------------------------
# main function
def exemple():
    """ this function shows the different models of ant and clods.

    parameters
    ----------

    version
    -------
    specification: Moustarih Walid (v.1 21/02/2021)
    implementation Moustarih Walid (v.1 26/03/2021)
    """

    case_1 = "\u25CC"
    case_1 = u"{}".format(case_1)
    fourmi_1_1 = "\u22C0"
    fourmi_1_1 = u"{}".format(fourmi_1_1)
    fourmi_2_1 = "\u21CA"
    fourmi_2_1 = u"{}".format(fourmi_2_1)
    fourmi_3_1 = "\u25BC"
    fourmi_3_1 = u"{}".format(fourmi_3_1)
    fourmi_1_2 = "\u22C0"
    fourmi_1_2 = u"{}".format(fourmi_1_2)
    fourmi_2_2 = "\u21C8"
    fourmi_2_2 = u"{}".format(fourmi_2_2)
    fourmi_3_2 = "\u25B2"
    fourmi_3_2 = u"{}".format(fourmi_3_2)
    clods_1 = "\u2726"
    clods_1 = u"{}".format(clods_1)
    clods_2 = "\u2737"
    clods_2 = u"{}".format(clods_2)
    clods_3 = "\u2739"
    clods_3 = u"{}".format(clods_3)
    
    print(term.move_xy(82,3) + term.white + 'DEPOT : ' + (case_1))
    print(term.move_xy(82,5) + term.white + 'Clods de niveau 1 : ' + (clods_1))
    print(term.move_xy(82,6) + term.white + 'Clods de niveau 2 : ' + (clods_2))
    print(term.move_xy(82,7) + term.white + 'Clods de niveau 3 : ' + (clods_3))
    print(term.move_xy(82,8) + term.white + 'Fourmis de niveau 1 : ' + (fourmi_1_1) + ' ' + (fourmi_1_2))
    print(term.move_xy(82,9) + term.white + 'Fourmis de niveau 2 : ' + (fourmi_2_1) + ' ' + (fourmi_2_2))
    print(term.move_xy(82,10) + term.white + 'Fourmis de niveau 3 : ' + (fourmi_3_1) + ' ' + (fourmi_3_2))
    print(term.move_xy(82,12) + term.white + 'Joueur 1 vous jouez en rouge.')
    print(term.move_xy(82,13) + term.white + 'Joueur 2 vous jouez en jaune.')


#-----------------------------------------------------------------------------------------------------------
# main function
def score():
    """ this function displays the score of both players.

    parameters
    ----------

    version
    -------
    specification: Moustarih Walid (v.1 21/02/2021)
    implementation Moustarih Walid (v.1 26/03/2021)
    """

    point_1 = 0
    point_2 = 0
    print(term.move_xy(82,15) + term.white + 'Score joueur 1 : ', end='')
    print(point_1)
    print(term.move_xy(82,16) + term.white + 'Score joueur 2 : ', end='' )
    print(point_2)


#-----------------------------------------------------------------------------------------------------------
# main function
def order():
    """This function takes the orders that the player gives and converts them to make them executable by the other functions. 
    
    Parameters:
    -----------

    Notes:
    ------
    instructions: instruction chain to give orders (str(input))
    
    Returns:
    --------
    the function order() to ask again for the instructions

    versions:
    ---------
    specification: Moustarih Walid (v.1 21/02/2021) Bonjean Selim (v.2 12/03/2021) (v.3 19/03/2021)
    implémentation: Bonjean Selim (v.1 01/03/2021) (v.2 19/03/2021) (v.3 26/03/2021)

    """
    #The syntax is 'r1-c1:*r2-c2 r1-c1:@r2-c2 r-c:lift r-c:drop'
    
    instructions = input(term.move_xy(82,18) + 'Give your orders:')
    the_orders = instructions.split()
    
    for element in the_orders:
        if ':@' in element:
            for char in '@,-,:':
                element = element.replace(char,' ')
            move_order = element.split()
            move_ant(*move_order)

        elif ':*' in element:
            for char in '*,-,:':
                element = element.replace(char,' ')
            shoot_order = element.split()
            shoot(*shoot_order)    
        
        elif ':lift' in element:
            for char in 'l,i,f,t,-:':
                element = element.replace(char,' ')
            lift_order = element.split()
            moving_clods(*lift_order)

        elif ':drop' in element:
            for char in 'd,r,o,p,-:':
                element = element.replace(char,' ')
            drop_order = element.split()
            moving_clods(*drop_order)
        
        else:
            print(term.move_xy(82,20) + '**************')
            print(term.move_xy(82,21) + ' syntax error ')
            print(term.move_xy(82,22) + '**************')
            return(order())


#-----------------------------------------------------------------------------------------------------------
# main function
def shoot (ant_1,ant_2,r1,c1,r2,c2) :
    """
    Parmeters:
    ----------
    r: location according to lines numbers (int).
    c: location according to column numbers (int).
    ant : ant information (dictionary) (int,str...).
    
    Notes:
    -----
    Shoot: Check the aiming conditions, then shoot and at the end reduce the life points of the ants.
    specification: Achraf El aich (v.1 21/02/2021).

    """

# Utuliser les parametres de la fonction d'ordre .
    if -2 <= r1 - r2 <= 2 and -2 <= c1 - c2 <= 2 :
# Niveau 1 :
# Pour preciser l ataquant et le recevoir il faut utuliser la fonction d ordre .
        if (ant_1["strength"] == 1) and (ant_2["strength"] == 1)  :

            if ant_1 == 'attack ant_2':
                ant_2["point_life"] -= 1

            elif ant_2 == 'attack ant_1':
                ant_1["point_life"] -= 1 

        if (ant_1["strength"] == 1) and (ant_2["strength"] == 2):

            if ant_1 == 'attack ant_2':
                ant_2["point_life"] -= 1

            elif ant_2 == 'attack ant_1':
                ant_1["point_life"] -= 2 

        if (ant_1["strength"] == 1) and (ant_2["strength"] == 3):

            if ant_1 == 'attack ant_2':
                ant_2["point_life"] -= 1

            elif ant_2 == 'attack ant_1':
                ant_1["point_life"] == 0  
                print('ant suppression')
        

# Niveau 2 :
        if (ant_1["strength"] == 2) and (ant_2["strength"] == 1)  :

            if ant_1 == 'attack ant_2':
                ant_2["point_life"] -= 2

            elif ant_2 == 'attack ant_1':
                ant_1["point_life"] -= 1 

        if (ant_1["strength"] == 2) and (ant_2["strength"] == 2):

            if ant_1 == 'attack ant_2':
                ant_2["point_life"] -= 1

            elif ant_2 == 'attack ant_1':
                ant_1["point_life"] -= 1 

        if (ant_1["strength"] == 2) and (ant_2["strength"] == 3):

            if ant_1 == 'attack ant_2':
                ant_2["point_life"] -= 2
                
            elif ant_2 == 'attack ant_1':
                ant_1["point_life"] -= 3  
                
        
# Niveau 3 :
        if (ant_1["strength"] == 3) and (ant_2["strength"] == 1)  :

            if ant_1 == 'attack ant_2':
                ant_2["point_life"] == 0
                print('ant suppression')
# Dispartion de la fourmis et creation d une autre fourmi.

            elif ant_2 == 'attack ant_1':
                ant_1["point_life"] -= 1 

        if (ant_1["strength"] == 3) and (ant_2["strength"] == 2):

            if ant_1 == 'attack ant_2':
                ant_2["point_life"] -= 3

            elif ant_2 == 'attack ant_1':
                ant_1["point_life"] -= 2 

        if (ant_1["strength"] == 3) and (ant_2["strength"] == 3):

            if ant_1 == 'attack ant_2':
                ant_2["point_life"] -= 1
                
            elif ant_2 == 'attack ant_1':
                ant_1["point_life"] -= 3  
                
        
    else :
     print("You can't shoot")

    if ant_1["point_life"]==0 or ant_2["point_life"]==0 :
        print ('ant suppression')


#-----------------------------------------------------------------------------------------------------------
# main function
{
"map":[30, 40],
"anthtills":[[12, 5], [17, 36]],
"clods":[
[30, 40, 1],
[15, 19, 1],
[15, 20, 1],
[14, 21, 1],
[14, 22, 2],
[1, 22, 1],
[2, 23, 1],
[3, 5, 1],
[4, 28, 1],
[5, 34, 1],
[5, 12, 1],
[6, 1, 1],
[7, 4, 2],
[7, 40, 1],
[9, 21, 1],
[10, 1, 1],
[11, 28, 1],
[12, 34, 1],
[13, 12, 1],
[14, 39, 1],
[15, 1, 1],
[16, 7, 2],
[17, 30, 1],
[18, 30, 1],
[19, 12, 1],
[20, 20, 1],
[21, 32, 1],
[22, 34, 1],
[23, 1, 1],
[25, 17, 3],
[25, 32, 1],
[26, 39, 1],
[27, 12, 1],
[28, 1, 1],
[28, 18, 1],
[29, 32, 1],
[29, 6, 1],
[30, 16, 3]
]
}

LIST = []
Map       = ("map")
Anthtills = ("anthtills")
Clods     = ("clods")

def moving_clods(x, y, strenght, key):
    Permitting = None
    """
    Parmeters:
    ----------

    x: location according to lines numbers (int).
    y: location according to column numbers (int).
    strenght : level of ant (int).
    Notes:
    ------
    moving_clods : The function allows you to move the clods of earth according to the coordinates of the parameters. 

    version
    --------
    specification: Achraf el aich (v.1 21/02/2021)
    """

    global LIST

    LIST = [x, y, strenght]

    if (LIST in Clods) and (key == 'LEFT'):
        Permitting = True
    if key == 'DOWN' and (Permitting):
        Permitting = False

    return Permitting


#-----------------------------------------------------------------------------------------------------------
# main function
def create_server_socket(local_port, verbose):
    """Creates a server socket.
    
    Parameters
    ----------
    local_port: port to listen to (int)
    verbose: True if verbose (bool)
    
    Returns
    -------
    socket_in: server socket (socket.socket)
    
    """
    
    socket_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_in.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # deal with a socket in TIME_WAIT state

    if verbose:
        print(' binding on local port %d to accept a remote connection' % local_port)
    
    try:
        socket_in.bind(('', local_port))
    except:
        raise IOError('local port %d already in use by your group or the referee' % local_port)
    socket_in.listen(1)
    
    if verbose:
        print('   done -> can now accept a remote connection on local port %d\n' % local_port)
        
    return socket_in


#-----------------------------------------------------------------------------------------------------------
# main function
def create_client_socket(remote_IP, remote_port, verbose):
    """Creates a client socket.
    
    Parameters
    ----------
    remote_IP: IP address to send to (int)
    remote_port: port to send to (int)
    verbose: True if verbose (bool)
    
    Returns
    -------
    socket_out: client socket (socket.socket)
    
    """

    socket_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_out.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # deal with a socket in TIME_WAIT state
    
    connected = False
    msg_shown = False
    
    while not connected:
        try:
            if verbose and not msg_shown:
                print(' connecting on %s:%d to send orders' % (remote_IP, remote_port))
                
            socket_out.connect((remote_IP, remote_port))
            connected = True
            
            if verbose:
                print('   done -> can now send orders to %s:%d\n' % (remote_IP, remote_port))
        except:
            if verbose and not msg_shown:
                print('   connection failed -> will try again every 100 msec...')
                
            time.sleep(.1)
            msg_shown = True
            
    return socket_out
    

#-----------------------------------------------------------------------------------------------------------
# main function   
def wait_for_connection(socket_in, verbose):
    """Waits for a connection on a server socket.
    
    Parameters
    ----------
    socket_in: server socket (socket.socket)
    verbose: True if verbose (bool)
    
    Returns
    -------
    socket_in: accepted connection (socket.socket)
    
    """
    
    if verbose:
        print(' waiting for a remote connection to receive orders')
        
    socket_in, remote_address = socket_in.accept()
    
    if verbose:
        print('   done -> can now receive remote orders from %s:%d\n' % remote_address)
        
    return socket_in            


#-----------------------------------------------------------------------------------------------------------
# main function
def create_connection(your_group, other_group=0, other_IP='127.0.0.1', verbose=False):
    """Creates a connection with a referee or another group.
    
    Parameters
    ----------
    your_group: id of your group (int)
    other_group: id of the other group, if there is no referee (int, optional)
    other_IP: IP address where the referee or the other group is (str, optional)
    verbose: True only if connection progress must be displayed (bool, optional)
    
    Returns
    -------
    connection: socket(s) to receive/send orders (dict of socket.socket)
    
    Raises
    ------
    IOError: if your group fails to create a connection
    
    Notes
    -----
    Creating a connection can take a few seconds (it must be initialised on both sides).
    
    If there is a referee, leave other_group=0, otherwise other_IP is the id of the other group.
    
    If the referee or the other group is on the same computer than you, leave other_IP='127.0.0.1',
    otherwise other_IP is the IP address of the computer where the referee or the other group is.
    
    The returned connection can be used directly with other functions in this module.
            
    """
    
    # init verbose display
    if verbose:
        print('\n[--- starts connection -----------------------------------------------------\n')
        
    # check whether there is a referee
    if other_group == 0:
        if verbose:
            print('** group %d connecting to referee on %s **\n' % (your_group, other_IP))
        
        # create one socket (client only)
        socket_out = create_client_socket(other_IP, 42000+your_group, verbose)
        
        connection = {'in':socket_out, 'out':socket_out}
        
        if verbose:
            print('** group %d successfully connected to referee on %s **\n' % (your_group, other_IP))
    else:
        if verbose:
            print('** group %d connecting to group %d on %s **\n' % (your_group, other_group, other_IP))

        # create two sockets (server and client)
        socket_in = create_server_socket(42000+your_group, verbose)
        socket_out = create_client_socket(other_IP, 42000+other_group, verbose)
        
        socket_in = wait_for_connection(socket_in, verbose)
        
        connection = {'in':socket_in, 'out':socket_out}

        if verbose:
            print('** group %d successfully connected to group %d on %s **\n' % (your_group, other_group, other_IP))
        
    # end verbose display
    if verbose:
        print('----------------------------------------------------- connection started ---]\n')

    return connection
        

#-----------------------------------------------------------------------------------------------------------
# main function   
def bind_referee(group_1, group_2, verbose=False):
    """Put a referee between two groups.
    
    Parameters
    ----------
    group_1: id of the first group (int)
    group_2: id of the second group (int)
    verbose: True only if connection progress must be displayed (bool, optional)
    
    Returns
    -------
    connections: sockets to receive/send orders from both players (dict)
    
    Raises
    ------
    IOError: if the referee fails to create a connection
    
    Notes
    -----
    Putting the referee in place can take a few seconds (it must be connect to both groups).
        
    connections contains two connections (dict of socket.socket) which can be used directly
    with other functions in this module.  connection of first (second) player has key 1 (2).
            
    """
    
    # init verbose display
    if verbose:
        print('\n[--- starts connection -----------------------------------------------------\n')

    # create a server socket (first group)
    if verbose:
        print('** referee connecting to first group %d **\n' % group_1)        

    socket_in_1 = create_server_socket(42000+group_1, verbose)
    socket_in_1 = wait_for_connection(socket_in_1, verbose)

    if verbose:
        print('** referee succcessfully connected to first group %d **\n' % group_1)        
        
    # create a server socket (second group)
    if verbose:
        print('** referee connecting to second group %d **\n' % group_2)        

    socket_in_2 = create_server_socket(42000+group_2, verbose)
    socket_in_2 = wait_for_connection(socket_in_2, verbose)

    if verbose:
        print('** referee succcessfully connected to second group %d **\n' % group_2)        
    
    # end verbose display
    if verbose:
        print('----------------------------------------------------- connection started ---]\n')

    return {1:{'in':socket_in_1, 'out':socket_in_1},
            2:{'in':socket_in_2, 'out':socket_in_2}}


#-----------------------------------------------------------------------------------------------------------
# main function
def close_connection(connection):
    """Closes a connection with a referee or another group.
    
    Parameters
    ----------
    connection: socket(s) to receive/send orders (dict of socket.socket)
    
    """
    
    # get sockets
    socket_in = connection['in']
    socket_out = connection['out']
    
    # shutdown sockets
    socket_in.shutdown(socket.SHUT_RDWR)    
    socket_out.shutdown(socket.SHUT_RDWR)
    
    # close sockets
    socket_in.close()
    socket_out.close()
    
    
#-----------------------------------------------------------------------------------------------------------
# main function
def notify_remote_orders(connection, orders):
    """Notifies orders to a remote player.
    
    Parameters
    ----------
    connection: sockets to receive/send orders (dict of socket.socket)
    orders: orders to notify (str)
        
    Raises
    ------
    IOError: if remote player cannot be reached
    
    """

    # deal with null orders (empty string)
    if orders == '':
        orders = 'null'
    
    # send orders
    try:
        connection['out'].sendall(orders.encode())
    except:
        raise IOError('remote player cannot be reached')


#-----------------------------------------------------------------------------------------------------------
# main function
def get_remote_orders(connection):
    """Returns orders from a remote player.

    Parameters
    ----------
    connection: sockets to receive/send orders (dict of socket.socket)
        
    Returns
    ----------
    player_orders: orders given by remote player (str)

    Raises
    ------
    IOError: if remote player cannot be reached
            
    """
   
    # receive orders    
    try:
        orders = connection['in'].recv(65536).decode()
    except:
        raise IOError('remote player cannot be reached')
        
    # deal with null orders
    if orders == 'null':
        orders = ''
        
    return orders


#-----------------------------------------------------------------------------------------------------------
# main function
def timer():
    """ This fonction is a timer set to indicate the length of the game. It will appear at the end of the game alongside the score.
    Its purpose is also to skip a player's turn if the player doesn't do anything during a set period of time (in seconds).

    parameters
    ----------

    version
    -------
    specification: Moustarih Walid (v.1 21/02/2021)
    implementation Moustarih Walid (v.1 26/03/2021)
    """

    T = 0
    while True:
        print (term.white + term.move_xy(82,1) + 'TIMER : ', end='')
        print(T, end='\r')
        time.sleep(1)
        T = T + 1 


#-----------------------------------------------------------------------------------------------------------
# main function
def general_function():
    """ This function performs all the steps for one turn

    Parameters
    ----------

    Version:
    --------
    specification: Moustarih Walid (v.1 21/02/2021)
    implementation Moustarih Walid (v.1 26/03/2021)
    """
    
    intro()
    tray_game()
    creat_ants_1()
    placement_clods()
    creat_ants_2()
    exemple()
    score()
    order()
    shoot ()
    moving_clods()
    create_server_socket()
    create_client_socket()
    wait_for_connection()
    create_connection()
    bind_referee()
    close_connection()
    notify_remote_orders()
    get_remote_orders()
    timer()
    
    

 
#-----------------------------------------------------------------------------------------------------------
general_function()
