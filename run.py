from inputHandler import inputReader
from node import node
from node import state
from algorithms import bfs, ids, heuristic
import configs

IR = inputReader.InputReader(configs.TEST_FILE_ADDRESS)


initState = state.State(IR.snakePrimaryPosition, IR.bounuses, IR.mapSize[0], IR.mapSize[1])
initNode = node.Node(initState)


bfsObj = bfs.BFS(initNode)
bfsObj.run()
bfsObj.printSolution()

idsObj = ids.IDS(initNode)
idsObj.run()
idsObj.printSolution()

aStarObj = heuristic.AStar(initNode, 1)
aStarObj.run()
aStarObj.printSolution()

aStarObj = heuristic.AStar(initNode, 2)
aStarObj.run()
aStarObj.printSolution()

aStarObj = heuristic.AStar(initNode, 1, 2)
aStarObj.run()
aStarObj.printSolution()

aStarObj = heuristic.AStar(initNode, 2, 2)
aStarObj.run()
aStarObj.printSolution()

aStarObj = heuristic.AStar(initNode, 1, 5)
aStarObj.run()
aStarObj.printSolution()

aStarObj = heuristic.AStar(initNode, 2, 5)
aStarObj.run()
aStarObj.printSolution()


