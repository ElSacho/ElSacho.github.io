---
layout: page
title: On the stability of Deep Q-Learning
description: Studying the ability of DQN to transfer knowledge from an environment to another one similar, without transfer learning.
img: assets/img/projects/chaseTag/GIF_chaseTag.gif
importance: 2
category: work
---

# HideOrJump

<div class="repo p-2 text-center">
  <a href="https://github.com/ElSacho/World_Chase_Tag_project">
    <img class="repo-img-dark w-100" alt="World Chase Tag Project" src="https://github-readme-stats.vercel.app/api/pin/?username=ElSacho&repo=World_Chase_Tag_project&theme={{ site.repo_theme_dark }}&show_owner={{ show_owner }}">
  </a>
</div>

## Find our report

You can read the report we made of this project [here](/assets/pdf/INF581___Chase_tag.pdf)

## Abstract 

The goal of this project is to code a pygame environment where several agents will confront each other: on a discrete mesh of space, an agent of type "Cat" pursues an agent of type "Mouse". As soon as the cat catches the mouse, the game stops. The objective of this project is to successfully train adversary agents on complex boards, with walls and speed bumps for example, and then to study the stability of Deep Q-Learning algorithms by testing our agents on boards where we have rearranged the location of these special boxes.


## Introduction

This project involves the study of the adaptation of Deep Q-Learning networks in an interchangeable environment. What happens if we teach a mouse to escape from a cat on a board, and how does the cat adapt to the modification of the board, by moving walls or boxes that slow down the agents for example? 

This aspect is interesting insofar as Deep Q-Learning, compared to classical Q-Learning, is supposed to react better to situations that it has never seen. Thus, we will study the reaction of two types of agents who discover new situations while they have been trained on similar but not identical situations. 

The challenges of this project are first to create a modular environment from scratch with PyGame \cite{TutoYoutube}, on which the players will be able to play with the board as they wish, and then to succeed in creating two agents who will compete on this board, and who will be able to progress with the appropriate methods. 

This project is similar to the game "Frozen-Lake" in that an agent (the cat) must move to eat the mouse. The uncertainty of the movements of the agent of "Frozen-Lake" is replaced by the uncertainty of the movement of the objective (the mouse) and it is not possible for the cat to die if it goes on a bad square. Moreover, we want to train our agents with Deep-Q Learning compared to the Q-Learning methods usually used on "Frozen-Lake" to be able to test our agents on new boards. 

So we recreated from scratch a game environment on which we trained our agents. Since this game is a winning game for the mouse given the implementation features, we can expect the mouse agent to constantly beat the cat. This is indeed what we observe on simple boards, and it remains true despite a slightly lower win rate on more complex boards. We also managed to create a cat agent that optimize all its moves on simple boards as it catches the mouse in a minimum number of moves when the mouse is immobile. Concerning the stability of the Deep Q-Learning methods, we draw two conclusions: on the one hand, training on a complex terrain still leads to a victory of the cat when we test our agents on simple terrains. On the other hand, on complex terrain most of the actions performed by the agents are good, but some observations still lead to sub-optimal decisions. 

If we had more time, we would have tried to model several agents. For example, start with a single cat and several mice, and as soon as a mouse is touched it becomes a cat with it. This would have allowed us to observe possible group behavior, where several cats would have helped each other to block a mouse for example. Finally, we could have pushed the study of stability by performing transfer learning on new game boards.
