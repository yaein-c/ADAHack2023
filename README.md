# ADAHack2023
My personal contribution to ADAhack 2023 was to work on the reputation management system for P2P based social network app. This project is ongoing and continuing as a personal project.

# An Implementation of the Eigentrust Algorithm for P2P Networks
## Reputation Systems
Within networks, users can rate eachother after each interaction with what is called a local trust value. The trust value describes whether an interaction has been satisfactory or unsatisfactory like in the case where an inauthentic file has been transferred. In centralised systems, the reputation of a certain user is the sum of all of their trust ratings over a certain period of time. A centralised system would also have to store and manage all of these trust ratings.

## What is the Eigentrust Algorithm
Eigentrust is an algorithm for P2P reputation management systems. It is named as such because the final calculated trust values correspond to the eigenvector of a matrix of normalised local trust values. Normalised in this context means that values are scaled to be between 0 and 1.

Within P2P networks, peers can also rate eachother after each interaction. However instead of summing all the ratings given to each peer, this algorithm uses a different approach. The eigentrust algorithm uses a notion called transitive trust: if you have a group of friends that are trustworthy, then you can assume that your friends' friends are also trustworthy. Similarly if a peer *i* trusts a peer *j*, peer *i* can also trust the peers that have a high trust rating given by peer *j*. 

The method that this algorithm uses of calculating the global trust value of a peer does not have the pitfall of needing to query the entire network to aggregate the rating for all peers like in other P2P algorithms. Additionally, this algorithm has been shown to be very successful in marking malicious peers within a network, even in the cases where up to 70% of the network is made up of malicious peers.
