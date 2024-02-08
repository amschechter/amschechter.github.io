---
layout: post
title:  "Austin Airbnbs"
date:   2024-1-10 13:17:35 -0800
categories: jekyll update
thumbnail: '/images/AustinAirbnb/Austin_Airbnb_Prices_by_Zip.png'
---

#### A look at Austin's Airbnb market

The Austin Airbnb market is large! 

In Austin Texas, the single most expensive listing is $38143 per night! Check it out [here](https://www.airbnb.com/rooms/567281208428241281) if you're interested. The data set contained 15419 individual listings, making Austin a large Airbnb destination. Only 12291 of those listings had price information, so the maps I made related to price only include those listings.

First lets take a look at the location of all listings in the city of Austin. The lines on the below map represent the zip codes of the city. You will notice that there are Airbnb concentrations in some areas. That is because the city limits of Austin are quite large so the areas of the map with more listings reflect the population density of those exact locations.

!['All Austin Airbnb listings'](/images/AustinAirbnb/AllAustinAirbnbLocations.png){:class="img-responsive"}

Now lets take a look at the average price by zip code. There are 44 different zip codes in Austin and each one has a different profile of listings. Not that the color indicates the averge price.

!['Seattle Land Use by Category'](/images/AustinAirbnb/Austin_Airbnb_Prices_by_Zip.png){:class="img-responsive"}

For my last map of the day, you can see nearly the same thing but in interactive form! Zoom in or out to better see the map of Austin and hover over zip codes to see the average price in that zip.

<br>

<div class="video-container">
    <iframe src="/images/AustinAirbnb/Austin_Airbnb_Prices_by_Zip.html" height="415" width="700" allowfullscreen="" frameborder="0">
    </iframe>
</div>

<br>

Thanks for reading! Many thanks to [insideairbnb.com](http://insideairbnb.com/get-the-data/) for providing historical data of Airbnb listings in many cities and making research of a private company possible.If you want to see this same data displayed in much more advanced fashion, you can visit the [Austin page of insideairbnb](http://insideairbnb.com/austin). Just goes to show that there are a lot of ways to display the same data! Some may be a bit better than others :). Also you can see the code I used to make this project [here.](https://github.com/amschechter/amschechter.github.io/blob/main/DataScience/censusData/Austin_Airbnb.ipynb)