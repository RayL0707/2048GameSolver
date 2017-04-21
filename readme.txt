#AI-2048 Game Solver
This is a python program for solving 2048 game.The minimax with alpha-beta pruning could help the AI to search nodes more evenly through each move. When do searching without alpha-beta pruning, the AI could typically run deeper to 10 - 15 layers to leftmost. While with alpha-beta pruning, the AI could be able to spread its search, instead of only digging one path all the way done. I also add depth limit, and help the AI to spread. For both minimax and the one with pruning, I test the total nodes it goes through for each round, and the total nodes searched are all about 70 - 100. In other words, the AI uses the same time to go more 'BFS' than 'DFS' when using pruning.

Results of 10 trials:

Trials with max tile of 2: 0.0 %
Trials with max tile of 4: 0.0 %
Trials with max tile of 8: 0.0 %
Trials with max tile of 16: 0.0 %
Trials with max tile of 32: 0.0 %
Trials with max tile of 64: 0.0 %
Trials with max tile of 128: 0.0 %
Trials with max tile of 256: 0.0 %
Trials with max tile of 512: 0.0 %
Trials with max tile of 1024: 20.0 %
Trials with max tile of 2048: 80.0 %
Trials with max tile of 4096: 0.0 %
Trials with max tile of 8192: 0.0 %
Trials with max tile of 16384: 0.0 %
Trials with max tile of 32768: 0.0 %
Trials with max tile of 65536: 0.0 %