# verification du moteur avec l'exemple du cours (diapo 67)
# sur 10 tours TIT-FOR-TAT fait 18 et ALL-D fait 23
# si on obtient (18, 23) le moteur calcule bien les points

from moteur import partie
from strategies import all_d, tit_for_tat

print(partie(tit_for_tat, all_d, 10))   # on doit voir (18, 23)