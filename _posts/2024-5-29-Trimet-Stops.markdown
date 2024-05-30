---
layout: post
title:  "Portland Trimet stop frequency"
date:   2024-5-29 13:17:35 -0800
categories: jekyll update
thumbnail: '/images/TriMet/TriMet_Hexes_Cover.png'
---

Hello Readers! 

In today's post I am diving in to General Transit Feed Specification (GTFS) data for the first time! I'm excited to start working with GTFS data becasue it is critically important to much of today's transit data infrastrucutre. Giants such as Google Maps use GTFS as its data standard for bus and transit routes across most of the worlds major cities. The open nature of GTFS, which was developed by TriMet of Portland, Oregon in conjunction with Google, is why they also provide data structure and specification for some older and beloved transit info applications such as the Seattle area's [OneBusAway](https://onebusaway.org/). 

To pay respect to TriMet I chose to use their data for my mapping today! I'm keeping it simple by using only data pertaining to the bus stops for this project, but the GTFS provides data on both scheduled and real-time trips. All three categories are critical in delivering complete information and I'll be using all of them for analysis in the future! 

The map below displays every bus stop operated by TriMet, mapped using their latitude and longitude. The color scale signifies how many times per day buses are scheduled to arrive at that particular stop. Dark Blue means close to zero, yellow is a few thousand and grey is in the middle! Note the Log scale used to help visualize the scale.

![Stop Frequency Static](/images/TriMet/TriMet_Stop_Frequency.png){:class="img-responsive"}

Below is a display of nearly the same map, but interactive! Hover to see the stop name and amount of scheduled bus trips per day at that stop. 

<div class="video-container">
    <iframe src="/images/TriMet/Trimet_Stop_Frequency_Interactive.html" height="555" width="700" allowfullscreen="" frameborder="0">
    </iframe>
</div>

As with any large data set, displaying a large amount of data in one chart or image is a big challenge. That is why we aggregate! For this aggregation I chose to use the PyDeck, a Python visualization library to help turn my data into interactive hexagons! In this chart the height and color are on the same scale, the amount of stops today. This map helps to show the different transit hubs across the Portland area and the significant concentration in the center of the city. To change the viewing angle of the graph, click and drag with your mouse while holding Ctrl or Command!

<div class="video-container">
    <iframe src="/images/TriMet/Trimet_Stop_Frequency_PyDeck.html" height="555" width="700" allowfullscreen="" frameborder="0">
    </iframe>
</div>

I hope these visualizations helped to communicate some of what is going on with the TriMet service.

Thanks for reading! Check out the code I used to make this post [here](), the official site of [GTFS](https://gtfs.org/) and the [data source](https://transitfeeds.com/p/trimet/43/20231016).