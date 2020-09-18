from inputHandler import inputReader
from node import node
from node import state
from algorithms import bfs
import configs

IR = inputReader.InputReader(configs.TEST_FILE_ADDRESS)

initState = state.State(IR.snakePrimaryPosition, IR.bounuses)
initNode = node.Node(initState)
bfsObj = bfs.BFS(initNode, IR.mapSize[0], IR.mapSize[1])
bfsObj.run()
bfsObj.printSolution()

# a = tuple([(1, 3)])
# b = a
# print(b)

# bfsObj.printSolution()

# idsObj = ids.IDS(initNode)
# idsObj.run()
# idsObj.printSolution()

# aStarObj = aStar.AStar(initNode, "Manhattan")
# aStarObj.run()
# aStarObj.printSolution()

# aStarObj = aStar.AStar(initNode, "Euclidean")
# aStarObj.run()
# aStarObj.printSolution()

# print("\n\n")