from smashggpy.models.Event import Event
from smashggpy.util import Initializer
from smashggpy.util.QueryQueueDaemon import QueryQueueDaemon

if __name__ == '__main__':
    Initializer.initialize('68991e2848052ed278a3d88656f66ff6', 'info')
    to12_melee = Event.get('tipped-off-12-presented-by-the-lab-gaming-center', 'melee-singles')
    sets = to12_melee.get_sets()
    for ggset in sets:
        print("{0}: {1} {2} - {3} {4}".format(
            ggset.full_round_text,
            ggset.player1,
            ggset.score1,
            ggset.score2,
            ggset.player2)
        )

    QueryQueueDaemon.kill_daemon()
