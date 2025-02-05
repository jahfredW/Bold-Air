import sys
import getopt
from data import pollution_pyowm
from utils import meteo_utils
from business.components.pollution_ville import PollutionVille
from business.components.pollution import Pollution
from services.uvicorn_launcher import Launcher, Api_launcher, Vue_launcher
from utils.configuration import Configuration

try:
    #méthode getopt ( se référer à la doc pour plus de renseignements )
    opts, argv = getopt.getopt(sys.argv[1:], 'ahd:iwv', ['api', 'display=', 'interactive', 'help', 'web', 'vue'])

    for opt, argv in opts:
        #mode display ( Brest préconfiguré )
        if opt in ('-d', '--display'):
            p = PollutionVille(argv)
            print(p)
        #mode Help
        elif opt in ('-h', '--help'):
            print("help")
            meteo_utils.usage()

        #configuration en mode interactif
        elif opt in ('-i, --interactive'):
            ville = input('ville? : Commençant par une majuscule + accents \n')
            m = pollution_pyowm.PollutionPyown()
            liste_villes = m.get_ville(ville)
            print(liste_villes)
            if len(liste_villes) > 1:
                choix = int(input('choix?'))
                try:
                    print("Voici les données brut pour la ville de {}".format(liste_villes[choix]))
                    p = PollutionVille(liste_villes[choix])
                except KeyError as e:
                    print(f'saisie incorrecte : {e}')
                    print(f'Entrez un nombre entre 0 et {len(liste_villes) - 1}')
            else:
                choix = int(input('choix?'))
                p = PollutionVille(liste_villes[choix])

        #configuration en mode Web
        elif opt in ('-w', '--web'):
            port = 8000
            if argv != None and argv != "":
                port = argv
            Launcher(port)

        #configuration en mode Api
        elif opt in ('-a', '--api'):
            port = 8001
            if argv != None and argv != "":
                port = argv

            Configuration().get_instance().api_port = str(port)
            Api_launcher(port)

        elif opt in ('-v', '--vue'):

            Vue_launcher()




except getopt.GetoptError:
    print("Paramètres incorrects !")
    sys.exit(2)

