#!/usr/bin/env python3
# https://www.linux-magazine.com/Issues/2018/217/A-backtracking-algorithm-tries-its-hand-at-the-bridges-of-Koenigsberg#article_l1
from bridgewalk import BridgeWalk
# original problem
g = { "1" : [["2", ["a", "b"]],
              ["3", ["d", "e"]],
              ["4", ["c"]]
             ],
       "2" : [["1", ["a", "b"]],
              ["4", ["f"]]
             ],
       "3" : [["1", ["d", "e"]],
              ["4", ["g"]],
             ],
       "4" : [["2", ["f"]],
              ["3", ["g"]],
              ["1", ["c"]]
             ]
}

# my own possible problem
g_EM = { "1" : [["2", ["a", "b"]],
              ["4", ["g", "h"]]
             ],
       "2" : [["1", ["a", "b"]],
              ["3", ["c", "d"]]
             ],
       "3" : [["2", ["c", "d"]],
              ["4", ["e", "f"]],
             ],
       "4" : [["3", ["e", "f"]],
              ["1", ["g", "h"]]
             ]
}

trail = BridgeWalk(g)
trail.explore()

print(trail.maxpath)

if len(trail.bridges) == \
    len(trail.maxpath):
    print("Solved!")
else:
    print("Impossible!")