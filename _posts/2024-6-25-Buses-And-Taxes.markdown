---
layout: post
title:  "Seattle Metro and Property tax"
date:   2024-6-25 13:17:35 -0800
categories: jekyll update
thumbnail: '/images/TriMet/TriMet_Hexes_Cover.png'
---

Hello Readers,

Thanks for stopping by!


For this project I wanted to analyze how bus frequency relates to property tax! We could entertain many different theories as to how these two go together but I just wanted to do some basic visualizing.

A few months ago, I did a [study](https://amschechter.github.io) on property tax per square foot in Seattle. I will be using that same data for the individual parcels their associated property tax for this project, and in addition to that I will be using GTFS data from king county metro to track the stop locations and frequencies for all stops in Seattle. 

Lets first take a look at the parcel and tax data for the city of Seattle. 

![Parcel Display](/images/Seattle_GTFS/Parcel_Display.png){:class="img-responsive"}

As you can see here, this map displays every property parcel in the city, colored by how much property tax that property pays. You can also probably see that the map is a bit difficult to look at. The colors are so smushed together and it is hard to tell what is going on. I will try to remedy that.

Lets now look at the bus data! To try to best approximate which parts of Seattle are best served by our public transit, I used stop location and route data to calculate exaclty how many times each stop was stopped at in a multi - month period. 

See the location of every stop here. 

<div class="video-container">
    <iframe src="/images/Seattle_GTFS/Seattle_Stop_location_and_frequency_map.html" height="555" width="700" allowfullscreen="" frameborder="0">
    </iframe>
</div>

Lets take these two very different images of Seattle and try to chop up the data to find some similarities and differences between our property taxes and our transit system. 

To help aggregate this data in an effort to make it more digestable, I opted for hexagons! As usual I used the H3 python library, developed by uber to divide everything into hexes. 

Here is the property taxes broken down into hexagons.

<div class="video-container">
    <iframe src="/images/Seattle_GTFS/seattle_tax_hex_map.html" height="555" width="700" allowfullscreen="" frameborder="0">
    </iframe>
</div>

Note how you can really see the neighborhood centers bringing in the most tax income. Outside of downtown, we see Ballard, Fremont and the U District as the most profitable areas.

Now lets look at the bus frequencies with that same hexagon break down. Note that the hexagons are a bit bigger this time around, this is to accomadate for the fact that bus stops are a more spread out through the city than the property parcels. 

<div class="video-container">
    <iframe src="/images/Seattle_GTFS/metro_hexagon_map.html" height="555" width="700" allowfullscreen="" frameborder="0">
    </iframe>
</div>

We can see in this map that the concentration in the downtown district is even more pronounced than the property taxes, and the neighborhood hotspots are even more pronounced.

After making these maps I started to think that the hexagons were not the ideal way of representing the different parts of the city. So I took those same data, transferred the parcels to points and arranged by neighborhood!

Here are both of those maps, first the property tax.

<div class="video-container">
    <iframe src="/images/Seattle_GTFS/tax_by_neighborhood_map.html" height="555" width="700" allowfullscreen="" frameborder="0">
    </iframe>
</div>

And now the bus frequency map. 

<div class="video-container">
    <iframe src="/images/Seattle_GTFS/seattle_bus_stops_by_nhood_map.html" height="555" width="700" allowfullscreen="" frameborder="0">
    </iframe>
</div>

These maps are both adjusted to account for the land area of the neighborhoods so it is really property tax paid per square foot and amoount of bus arrivals paid by square foot. This helps illustrate how our tax incomes and transit services differ neighborhood by neighborhood.

And finally, just for fun, here is a map of Amazon's internal bus service - from March of 2018. 

<div class="video-container">
    <iframe src="/images/Seattle_GTFS/amazon_bus_freq_map.html" height="555" width="700" allowfullscreen="" frameborder="0">
    </iframe>
</div>

