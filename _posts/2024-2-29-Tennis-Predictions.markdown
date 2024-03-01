---
layout: post
title:  "Predicting Tennis Match Outcomes"
date:   2024-2-29 13:17:35 -0800
categories: jekyll update
thumbnail: '/images/Misc/Tennis-Stock-Image.png'
---

Hello! If you have been following my recent work, you may have noticed that it mostly follows one theme. Geodata! I have been thoroughly enjoying working with geographical data and visualizing data using geography to add dimension.

For this project I thought that I would change it up.

I am a big tennis fan, and have been following the professional circuit rather closely for the past couple years. There are constantly tournaments being held nearly year round on different continents, played on different surfaces with wildly different atmospheres, stakes and fan bases. All of these things come together to make rather unpredicatble results about who can win any given match between two competitors.

However, we have at our disposal a ton of data about completed matches, and we can attempt to use the past to predict the future. Thanks to the prominent (in the tennis nerd world) website, TennisAbstract, I was able to download data on every single match from 2021, 2022, and 2023. There is data available going back to the 1970s, but I decided to stick with the three most recent years for now.

The original data sets included 49 columns containing information about the Tournament, each player competeing in the match and specifics about the outcome of the match, things like the amount of Aces hit, or the amount of times the losing playyer broke serve. 

Over the course of four different jupyter notebooks, I slowly evolved a way of extracting shaping the data in a way that I could best feed it to a machine learning model. I tried different methods of predicting the outcomes of winners, such as isolating each player and only running the algorithm on them, which produced sporadic results, likely due to its smaller sample size. 

In the end I managed to use Sklearn.ensemble's 'RandomForestClassifier' to predict with 63.2% Accuracy the outcomes of 2023 tennis matches. Let me add some context to this statement. When I used literally only the player's ATP ranking to predict the outcomes, I got a 60.9% success rate, meaning that before a match occurs, the higher ranked player will win about 60% of the time. That figure is alarmingly and upsettingly close to the 63.2 percent that I achieved after adding in all of the things that us tennis fans would tell you are extremely important in matchups, such as surface, recent form of a player based on wins and losses as well as things like percent of serve games held in recent matches, percent of return games broken in recent matches, first serve percentage in recent matches and more. While the 2.3 percent increase I got after adding all those different parameters seems small it is reproducable and over the course of the seasons represents about 98 correct predictions that would have otherwise been wrong.

I have a long way to go in this arena and there are many different wayys that I could attempt to improve my work on this project. It has been a very interesting study in machine learning, and tinkering with different variables has sometimes raised more questions that it has answered.

Thanks for reading and stay tuned for the next project!

Thanks to to Jeff Sackman anad tennis abstract for the data, which you can find [here](https://github.com/JeffSackmann/tennis_atp). See the code that I wrote to make this project [here](https://github.com/amschechter/amschechter.github.io/blob/main/DataScience/Shape%20Projects/Providence_Property_Tax.ipynb).