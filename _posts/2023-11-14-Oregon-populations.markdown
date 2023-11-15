---
layout: post
title:  "A look at Oregon"
date:   2023-11-14 13:17:35 -0800
categories: jekyll update
---

## Examining population and spread in Oregon

Hello! I will be taking a look at the population of Oregon in 2020 and some of its different qualities.

All data for this study came from the 2020 census.

Let's get some basic data out of the way first. This data set shows 4,237,256 people in the state, about 1,876,940 of whom live in the greater Portland area.

To demonstrate how populated Portland is, I made some (slightly silly) graphs showing the population by latitude and longitude.

!['Population by Longitude'](/images/OregonTracts/LongitudeXPopulation.png){:class="img-responsive"}
!['Population by Latitude'](/images/OregonTracts/LatitudeXPopulation.png){:class="img-responsive"}

These two graphs display just how centered the population is at the northwestern corner of the state.

Now to stop keeping secrets from you, I will show the location of all population tracts in the state.

!['All Tract Locations'](/images/OregonTracts/PopTractsByLocation.png){:class="img-responsive"}

This map, made just of dots shows quite well the shape of Oregon, as well as the population centers. You may notice that the South Eastern Region of the state is extremely sparse in its dots which is because nobody lives there! Nearly.

Let's also take a look at the housing occupancy of the state. I took the metric for vacant units and divided it by the number total housing units. This revealed that there were certain regions with huge vacancies, but overall a very full state. See below.

!['Percent Vacant Housing Units'](/images/OregonTracts/PercentVacantHousingUnits.png){:class="img-responsive"}

Also observe the same statistic for only the Portland Metro Region. You can see that the red dots, which represent up to 25% vacant are all in the downtown Portland Area. Why could this be?
!['Percent Vacant Housing Units Portland Region'](/images/OregonTracts/PercentVacantHousingUnitsPDX.png){:class="img-responsive"}

Finally, take a look at the tract population graphed with the total housing units. In no surprise whatsoever, the two data points are strongly correlated. But also observe the color of the dots, which still represents percent vacancies! The number is significantly darker at the lower end of the trend line, meaning that a lot of empty houses does indeed mean more vacancies. 

!['Percent Vacant Housing Units Portland Region'](/images/OregonTracts/TractPopXHousingUnits.png){:class="img-responsive"}






See the source for my data [here](https://catalog.data.gov/dataset/census-tracts), and the code I wrote for this [project here.](https://github.com/amschechter/amschechter.github.io/blob/main/DataScience/censusData/OregonTracts.ipynb)