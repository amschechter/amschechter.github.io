---
layout: post
title:  "A look at Seattle's Land Use and Tax Income"
date:   2023-11-30 13:17:35 -0800
categories: jekyll update
---

Today we are looking at Seattle's Land Use and how it relates to its Tax income.

Thanks to King County we have access to geographic data about each individual parcel in the entire county, which I was able to combine with a different data set containing information about each parcel's tax payments.

The original data set categorizes each one of the 750,540 parcels in Seattle into one of 115 different sections with categories as mundane as 'Office Building' or 'Bank' to slightly more surprising land uses such as 'Fraternity/Sorority House' or 'Tavern/Lounge'.

For the sake of chart legibility I split those 115 categories into 14 different groups and charted the land use of them all.

!['Seattle Land Use by Category'](/images/SeattleTax/Land_Use_By_Cat.png){:class="img-responsive"}

Now lets take a look at the Amount of Tax each individual parcel generates. Note that the scale on this chart and the following charts are logarithmic, meaning that the values increase more quickly than on a standard linear chart. Note the concentration of dark colors in various business centers around the city, including downtown. Also note that many of the largest parcels such as the Zoo near Greenlake, Magnusen park and many of the industrial parcels in SODO are high tax parcels.

In case you are wondering, the city's highest paying parcel is the Columbia Tower in downtown Seattle, bringing in a whopping $622,098,534 in just one years worth of taxes.

!['Seattle Tax Value by Parcel'](/images/SeattleTax/Tax_By_Parcel.png){:class="img-responsive"}

The next chart shows only single family homes, and wow there are a lot of them! 529,117 to be exact, representing a little over 70% of all land parcels in the city. Note that in the central business areas of the city there are almost no parcels designated as single family and also see that the deeper red color, signifying higher tax payments tend to be centered closer to the waterfront.

!['Seattle Single Family Home Tax Values'](/images/SeattleTax/Single_Family_Tax.png){:class="img-responsive"}

The final chart here is the tax value per square foot. It makes sense that a larger lot should generate more tax revenue, so now I am trying to control for that. We can still see darker colors centered towards business districts but a lot of the larger lots that in the prior chart looked like big earners are revealed to actually not bring in so much money per square foot!

!['Seattle Single Family Home Tax Values'](/images/SeattleTax/Tax_Per_Sq_Foot.png){:class="img-responsive"}

Thanks for reading! All data was provided by king county, find the tax data [here](https://data.kingcounty.gov/Property-Assessments/Real-Property-Tax-Receivables/dkna-i698), and the parcel data [here](https://gis-kingcounty.opendata.arcgis.com/datasets/kingcounty::parcels-for-king-county-with-address-with-property-information-parcel-address-area/explore). All the tax data is from 2023.