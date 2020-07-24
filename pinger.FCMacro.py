## Pinger macro
## By: TheMarkster
## 2020.07.22
## Aids in pinging users on the forum
## Select the user from the list and paste clipboard contents into the forum


from PySide import QtGui,QtCore
limitToTopNUsers = 10000 #change to 100 for example to use only top 100 users (by number of posts)
dict1 = {'chrisb': '5646', 'NormandC': '202', 'wmayer': '69', 'yorik': '68', 'bernd': '2069', 'jmaustpc': '611', 'triplus': '782', 'DeepSOIC': '3888', 'Kunda1': '12229', 'freecad-heini-1': '2598', 'bejant': '1940', 'sgrogan': '4252', 'microelly2': '2364', 'vocx': '21943', 'openBrain': '22265', 'wandererfan': '1375', 'quick61': '2030', 'abdullah': '3232', 'jriegel': '67', 'looo': '2349', 'mario52': '1058', 'PrzemoF': '3666', 'ickby': '686', 'meme2704': '14145', 'easyw-fc': '6387',
'shoogen': '765', 'renatorivo': '918', 'paullee': '8738', 'GlouGlou': '5772', 'kisolre': '22435', 'r-frank': '1529', 'kkremitzki': '7997', 'Jee-Bee': '6234', 'papyblaise': '25808', 'ulrich1a': '1928', 'herbk': '4353', 'sliptonic': '708', 'Joel_graff': '14673', 'thschrader': '15166', 'rockn': '681', 'TheMarkster': '19292', 'realthunder': '12167', 'uwestoehr': '23505', 'tanderson69': '208', 'saso': '3305', 'mlampert': '10163', 'freedman': '19098', 'Roy_043': '22936', 'carlopav': '23005', 'Willem': '9760',
'Chris_G': '2561', 'keithsloan52': '930', 'GeneFC': '8180', 'roerich_64': '6075', 'HarryGeier': '15774', 'UR_': '12184', 'hammax': '12483', 'HoWil': '6222', 'freman': '22524', 'HarryvL': '18062', 'bitacovir': '3136', 'drmacro': '2867', 'peterl94': '1819', 'Forthman': '19652', 'cox': '4523', 'kbwbe': '19380', 'Zolko': '22794', 'reox': '9769', 'pablogil': '4517', 'HakanSeven12': '23711', 'ArminF': '11953', 'RatonLaveur': '24547', 'jeno': '3508', 'thomas-neemann': '29293', 'flachyjoe': '984',
'regis': '6401', 'Syres': '21041', 'ian.rees': '3449', 'pperisin': '356', 'ppemawm': '1807', 'mrlukeparry': '607', 'logari81': '270', 'fc_tofu': '29038', 'ezzieyguywuf': '6058', 'emills2': '5929', 'vejmarie': '7506', 'Dirk.B': '23630', 'eivindkvedalen': '1546', 'damian': '6134', 'jrheinlaender': '997', 'Jimidi': '15956', '-alex-': '23825', 'dubstar-04': '1642', 'Gift': '6611', 'Joyas': '3582', 'drei': '3278', 'cappy0815': '4130', 'Bance': '5418', 'Russ4262': '20523', 'r.tec': '4264',
'agryson': '11337', 'dcapeletti': '3651', 'manuelkrause': '20592', 'Mar': '14191', 'JoshM': '16808', 'teobo': '2833', 'schupin': '18259', 'jpg87': '13810', 'danielfalck': '689', 'makkemal': '5932', 'Fran': '16427', 'onekk': '5245', 'bill': '5185', 'oliveroxtoby': '11950', 'leoheck': '19003', 'blacey': '7328', 'fandaL': '3658', 'shaise': '6188', 'johnwang': '23504', 'fosselius': '8591', 'fran6t': '3600', 'herrdeh': '3918', 'nemesis': '2986', 'holdi': '11560', 'piffpoof': '4556',
'adrianinsaval': '19302', 'furti': '17491', 'f3nix': '6125', 'jreinhardt': '2072', 'chakkree': '6331', 'galou_breizh': '334', 'bavariaSHAPE': '3425', 'FaDa3D': '16107', 'jaisejames': '10269', 'apeltauer': '16146', 'plgarcia': '6249', 'fcaduser': '2823', 'jp-willm': '7776', 'Pauvres_honteux': '2803', 'clintonsam75': '3470', 'Claud': '29138', 'amrit3701': '9146', 'OldDraftsman': '16332', 'ebrahi': '21433', 'usbhub': '24632', 'Sudhanshu': '21878', 'efyx': '4074', 'jbe': '2330', 'JMG': '2538', 'lemonbug': '4228',
'kwahoo': '2441', 'Repman': '3536', 'koluna': '21576', 'polymer': '3974', 'Moult': '23100', 'joha2': '10551', 'david69': '2566', 'Roland': '6638', 'Konstantin': '3649', 'Renat': '3315', 'hobbes1069': '725', 'blonblon': '10279', 'oldmachine': '15343', 'user1234': '9411', 'wega': '2347', 'salp': '2409', 'Drederwisch': '11726', 'arturromarr': '15598', 'bgoodr': '3447', 'jruiz': '4299', 'arcol': '2320', 'garya': '22407', 'blue0cean': '23920', 'CharlieMAC': '3179', 'Marco_T': '7564',
'lainegates': '1295', 'davecoventry': '2481', 'kaktus': '26846', 'FC-Architecter': '19079', 'Sura': '21412', 'chrisf': '2578', 'ceremcem': '18069', 'ediloren': '1783', 'dxp.dev': '22713', 'qingfeng.xia': '6825', 'jean.thil': '6498', 'pl7i92LCNC': '24265', 'OficineRobotica': '23938', 'j-dowsett': '652', 'kwahooo': '254', 'memfis': '11177', 'nahshon': '1973', 'cram': '11546', 'yoshimitsuspeed': '1337', 'HartmutG': '10744', 'gdo35': '858', 'ProBowlUk': '4171', 'freecadjam': '20736', 'HBC0': '6833', 'paul18': '3622',
'rentlau_64': '4246', 'AR795': '20058', 'catman': '23210', 'heilo': '12525', 'Turro75': '9800', 'joel': '12631', 'hardeeprai': '255', 'Fat-Zer': '4325', 'Sam': '8192', 'Giuli': '9935', 'kanagan': '5980', 'jnxd': '5734', 'S.N.A.L': '3080', 'Renato': '5905', 'Markymark': '28078', 'papy': '21427', 'm42kus': '3911', 'freecc': '18704', 'M4x': '13711', 'Brutha': '5971', 'TopDown': '20410', 'Leatherman': '12789', 'gsandy': '23521', 'un1corn': '7434', 'cblt2l': '251',
'psicofil': '789', 'dimitar': '25801', 'TomB19': '25136', 'a3bksll47': '19044', 'crobar': '3893', 'project4': '1944', 'rynn': '20919', 'wsteffe': '3846', 'industromatic': '2997', 'MaurinoWeb': '15573', 'nyholku': '12058', 'wvmarle': '4214', 'derschutzhund': '3592', 'sanguinariojoe': '574', 'MSOlsen65': '29727', 'Anderl': '17746', 'crashfridh': '1483', '1D_Inc': '23696', 'ektus': '1283', 'Eric': '25272', 'ikua': '14240', 'hhassey': '6158', 'japie': '3493', 'zbigg': '17804', 'clytle374': '2207',
'C_h_o_p_i_n': '25037', 'FemUser': '16291', 'Mongrel_Shark': '10595', 'Spindoctor': '6848', 'foxint': '7589', 'dan-miel': '21478', 'oddtopus': '10205', 'IzzY': '14602', 'xibinke': '5703', 'aapo': '22095', 'jakob': '3595', 'lot': '25410', 'ajoeiam': '24132', 'jonasthomas': '873', 'schnebeck': '15579', 'JiPe38': '28975', 'scrungy_doolittle': '20416', 'eason': '5803', 'KAP': '28935', 'kcleung': '512', 'Luixx': '18322', 'prrvchr': '4119', 'roivai': '12794', 'brjhaverkamp': '6838', 'mnesarco': '30314',
'bbear123': '2465', 'cnirbhay': '9824', 'iplayfast': '27301', 'kreso-t': '20975', 'more11': '4079', 'alex::freecad': '3892', 'Galahad': '20671', 'Wsk8': '22665', 'Hannu': '6761', 'heideachim': '18226', 'aguseguedre': '535', 'frecd': '5116', 'Do': '11781', 'hds': '13102', 'Jos': '31258', 'rjpeek': '7415', 'babaroga': '9780', 'etrombly': '28581', 'Norus': '6964', 'rebeltaz': '24648', 'EkaitzEsteban': '21473', 'Koemi': '17917', 'NateM': '2390', 'jmplonka': '11876', 'django013': '5218',
'jmplonka': '11876', 'django013': '5218', 'lhagan': '108', 'Daniel84': '13510', 'tom': '5727', 'Andr': '7655', 'm.cavallerin': '20120', 'bzb.dev001': '25224', 'neondata': '1573', 'DrBwts': '4281', 'Gauthier': '3532', 'balazs': '4211', 'Cyril': '16289', 'OakLD': '18151', 'waebbl': '21119', 'atzensepp': '5514', 'spikey': '7624', 'oldestfox': '1910', 'albertdela': '16540', 'Xav-83': '3750', 'Lauri': '13429', 'jmh': '4317', 'Linden': '6627', 'andre': '2370', 'j9lemmon': '2018',
'Crossleyuk': '20393', 'iogui': '24401', 'mack5': '15924', 'falviani': '25270', 'godblessfq': '6436', 'mandeep7': '8229', 'Tilli': '18331', 'ckl6767': '24834', 'capucin': '16725', 'onesz': '729', 'Maavhamt': '6189', 'Opus': '17261', 'vanuan': '22024', 'ccccrnr': '698', 'Serchu': '5411', 'foadsf': '5587', 'NC3D': '10606', 'luggw1': '13046', 'dave_w': '30076', 'jobermayr': '769', 'tanj': '16319', 'murdic': '2856', 'MrRossi': '11492',
#add new users and userids here
#some examples:
'Enyalios': '13094',
'agima2': '12024'

}
def getClipText():
    clip = QtGui.QClipboard()
    return clip.text(QtGui.QClipboard.Clipboard)

def setClipText(txt):
    clip = QtGui.QClipboard()
    clip.setText(txt)

def parseHtml(txt):
    """parse html copied from list of users view source
returns dictionary of usernames and user ids"""
    lines = txt.split()
    dictionary = {}
    userNext = True
    idNext = False
    currentUser = ""
    currentId = ""
    for line in lines:
        if "class=\"username" in line:
            currentUser = line[line.find('>')+1:line.find('<')]
        elif "author_id=" in line:
            currentId = line[line.find("id=")+3:line.find("&amp")]
            dictionary[currentUser] = currentId
    return dictionary
        


#following code used to generate original dictionary
#open the member list on the freecad website
#sort by number of posts
#right click, view source
#copy all html to the clipboard, run macro
#in report view will be 25 username / userid keys
#uncomment the next 3 lines and run
#url = getClipText()
#userDict = parseHtml(url)
#Msg(str(userDict))
Msg("pinger macro -- "+str(len(dict1.keys()))+" users in database.  Edit source code to add more.\n")

items = []
for k in dict1.keys():
    #Msg(str(k))
    items.append(k)
    pass
items = ["select user to ping"] + sorted(items[:limitToTopNUsers], key=str.casefold)
username,ok = QtGui.QInputDialog.getItem(QtGui.QMainWindow(),"Select user", "Select user:\n\n\
WARNING: (Will replace current clipboard contents.)\n\n\
Tip: Enter first letter in name to skip through the list.\n\
",items,0,0)

if ok and username != items[0]:
    ping = "[quote="+username+" user_id="+dict1[username]+"]\npinged by pinger macro\n[/quote]"
    setClipText(ping)
    FreeCAD.Console.PrintMessage("Success!\n\nNow copied to clipboard: \n\n"+ping)
else:
    Msg("pinger macro: User canceled\n")