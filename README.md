# CMU Energy Storage Class: HW5

In this homework, we will analyze how to design battery packs for EVTOLs by understanding the intricate link between the application and choice of the battery chemistry and its performance. You are a battery engineer who has been offered a gig to design the battery pack for one of the five EVTOL manufacturers. You may choose one of the five EVTOL aircraft to design the battery pack and build a battery model.

This repository contains the following files and folders:

- `parameters` folder:
    - Spec sheet for the LGM50 cell
    - Parameter set for the LGM50 cell, adapted from the paper ``Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W. Dhammika Widanage, and Emma Kendrick. ["Development of Experimental Techniques for Parameterization of Multi-scale Lithium-ion Battery Models."](https://iopscience.iop.org/article/10.1149/1945-7111/ab9050) Journal of the Electrochemical Society 167 (2020): 080534''
    - OCP data for each electrode of the LGM50 cell

- `powerprofiles` folder:
    - A csv file for a typical EVTOL mission with one of five designs 
    - `motm.txt`: the maximum takeoff mass for each of the five designs
    - `mission_assignments.txt`: which mission you should use (assigned by last name)

- `HW5.pdf`: the problem set
- `HW5_template.ipynb`: a template to help you get started

Materials to help with learning PyBaMM are available at [pybamm.org](https://www.pybamm.org/training)
