---
layout: page
title: La Compo Website
description: A website project
img: assets/img/projects/lacompo/lacompo.gif
importance: 2
category: work
---

<p>
    <img align="center" src="https://github.com/ElSacho/Sport-website" alt="GitHub Repository" />
</p>

### Authors

Axel Navarro and Sacha Braun

### Date

24/02/2022

### Introduction

The objective of this report is to present the different features of the LA COMPO website and to describe the used database. This website aims to assist the X rugby team's coaches in forming their team for upcoming matches and providing feedback to players on their performance in past games. Please find in another attached file (`readme.txt`), some settings and useful tips for using the site.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/lacompo/Accueil02.png" title="Home page of the website" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


### Users

There are two types of users on this site, the coaches and the players, each with access to different features.

**Player:**

The player is the basic user representing a rugby team player on the site. The player's attributes are:

- Usual position
- Year of promotion
- Email
- Date of birth
- Photo (modifiable by the player)
- Login information (login, password)

The player can view the upcoming matches he will play, his player file with all the matches he participated in and his average rating. He also has access to all of his team's player files and can modify his account information.

**Coach:**

The coach is an admin of the site as they are the only one who can modify the database beyond login information. The coach can:

- Schedule a new match and assemble a team for this match
- Modify the team composition for a match that has not yet been completed (we will see later what it means to complete a match)
- Fill in the score of a played match and rate each player who played this match
- Delete a match
- Modify a player's usual position
- View all the player files of the team

In practice, to create a coach profile, validation by another administrator designated as the Sports Bureau Director, for example, would be required.

### Databases

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/lacompo/base_de_donnees.png" title="Database" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


The database consists of 4 tables:

- The `joueurs` table groups all the users attached to the Player class. Each player in the table is recognized by the primary key "login". This table contains 9 different fields. The profile pictures of the players are stored in the "images" directory of the folder and are in the form "login.jpg". To facilitate the setup of the database, we chose the login "prenom.nom" for each user of the site (except alice and bob).

- The `entraîneurs` table groups all users attached to the Coach class. The primary key is also "login".

- The `matchs` table is made up of the different rugby matches inserted by the registered coaches on the site. The primary key of this table is `idMatch` (auto-incremented). The other fields are the date, the location of the match, the home and visiting team, the score, the coach who inserted the match, and the boolean `marked`. This field serves as a witness on the site to know if the match has been completed by a coach or not.

- Finally, the `ficheMatchJoueur` table which links the previous tables, it is used to know the team composition for a match. The elements of this table represent the presence of a player for a given match, which is why the primary key is double. It is the `idMatch` and `login` fields that ensure the uniqueness of the element. Once the corresponding match has been completed by a coach, the `note` field goes from `NULL` to an integer between 1 and10 to assess the player's performance in the match.

In the following pages, we will see the different features of the LA COMPO site.

### Forming a match

To create a match, you must be logged in with a coach's profile. The creation of a match was done in JavaScript. When the coach (currently only rugby) arrives on the interface, they have on their left a menu with all their players sorted by drawers according to their positions and on their right a rugby field with places to come and drop their players. All you have to do is click on a position, for example "1st line" to see all the players from the corresponding position appear. Then, thanks to a drag and drop system, the coach can drag the names of his players to the indicated places.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/lacompo/nouveauMatch.png" title="Drag and drop to create a match" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


Once the entire composition is complete, along with information such as date, opposing team, etc., the coach can validate, which will create a new match with their composition and automatically send an email to each of the selected players.

### Managing a team and its matches

Once the match is created, it is visible to all users: they can click on the match card and go see the composition. When a composition is displayed, any logged-in user can click on a player in the match to access their file. Thus a coach quickly has all the information on their team composition and can decide before the start of the match to modify this composition. For this, they must click on "Edit" and access an interface of the same type as that of match formation.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/lacompo/modifier02.png" title="Match page before it's played" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


The coach also has the option to delete a match in the `My matches` menu by clicking on the cross next to the match to be deleted.
