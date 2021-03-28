from police import Police
from timo import Timo


police = Police()
timo = Timo()
police.fight(timo.name,timo.hp,timo.power)
police.speak_lines()
timo.speak_lines()