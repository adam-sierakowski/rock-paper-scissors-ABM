This is a first sketch of my custom approach to agent based modeling. It still requires a lot of work. For the moment, there is a script called deathmatch.py in which creatures belonging to three different species (rock, paper, scissors) fight with each other until only one species is left.

I've chosen the rock paper scissors game as an inspiration because it has a natural mathematical balance. For now, each species is essentialy the same, but the goal is to be able to tweak their stats and introduce different mechanics for each one of them, looking for another possible balanced ecosystem.

TODOs/ideas:
- implement sexual reproduction (basic one, with two individual needed for an offspring)
   - variables: different number of offsprings
   - different random chance to get an offspring
   - etc.
- implement sexual reproduction (with variations on the number of sexes, how many individuals are needed for reproduction, and other factors)
- implement asexual reproduction
- implement species stats
   - durability (e.g. rock can be defeated two times before it dies)
   - longevity (how many turns without fighting until a creature dies)
   - etc.
- implement a blueprint architecture in which the rules are specified in a separate file from the engine
- add a functionality to create a simulation graph showing how the population changes over time
- add a functionality to run many simulations one after another and print the graphs and overal outcomes so that the user can compare and draw conclusions

