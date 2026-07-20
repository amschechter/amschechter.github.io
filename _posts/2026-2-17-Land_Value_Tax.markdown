---
layout: post
title:  "Value Capture tax and ST3"
date:   2026-7-17 13:17:35 -0800
categories: jekyll update
thumbnail: '/images/Value_Capture/Ballard_Gradient_Image.png'
---

# Exploring a Value Capture Tax

As you may have heard, SoundTransit is facing a significant budget issue. ST3, approved by voters in 2016, is meant to deliver the West Seattle Link Extension, the Ballard Link Extension, the 4 line from Issaquah to South Kirkland and more. A few months ago SoundTransit announced a 34 billion dollar budget gap and despite their best efforts have had to make a lot of significant cuts/concessions, including terminating the Ballard line at Seattle Center.

Sound Transit should consider a Value-Capture tax to pay for this irreplaceable service.

A Value Capture tax functions by making a very powerful inference. *When rapid transit is built, land around the stations becomes more valuable*. Often dramatically more so. In a normal transit-building scenario, the additional tax collected from the land value increase goes to the same services that they typically would have. More money for the City and County Budget, more money for the Schools, etc. All made possible by the train. Increased property value and tax revenue from transit is clearly a good thing, and is yet another reason that building rapid transit is an amazing decision.

Please note that for this article, I am speaking exclusively about land value, not the improved value upon the land. Read about the difference [here](https://www.theurbanist.org/op-ed-the-case-for-shifting-to-a-land-value-tax/)

Here is where the Value Capture tax comes in. This tax operates by ‘freezing’ the property values at a certain number and point in time, and then allocating any additional property value to the project that created (or will create) the value. As we all know, the Ballard Link Extension is in serious jeopardy. If the extension all the way to 15th and Market doesn’t happen, or is delayed until 2060 (🤮), there will be billions of dollars in property tax income (among many other significant benefits) left vanishing into thin air. This would be a truly historic fumble. Instead, SoundTransit can fund itself by capturing the future property value increase! 

That increased value will literally *not exist* if the project doesn’t happen. The increased value *will exist* if the project does happen.

## Now for some light data analysis

The area around 15th and Market in Ballard is currently valuable land, but will become much more so if and when the light rail is completed. If you go there today, there is a huge amount of car activity, as well as plenty of space dedicated to the personal automobile. That space looks like large parking lots at Walgreens and Safeway, a gas station, the gigantic right of way of the streets themselves and more.

### Comparing 2018 with 2027

For this data analysis and visualization I took data from the King County Assessor, who publishes an extensive [datadownload page](https://info.kingcounty.gov/assessor/datadownload/) with property tax information going back over 15 years. For this analysis I used the most up to date data, 2027, to compare with data from 2018. Check out this chart showing the mean increase in land value in the 2000 feet around various light rail stations and non light rail stations. I chose to exclude downtown and SODO light rail stations from this analysis because of their differences with proposed Ballard Station.

Below is a bar graph showing the amount that land around various points has increased in value over the past nine years. Note the clear increase around the lightrail stations. Correlation or causation?

!['Land Value Increase in 12 Seattle locations'](/images/Value_Capture/Increase_in_land_value_2000_feet_around_points.svg){:class="img-responsive"}

Now lets visualize some of those numbers. First, take a look at this map of the entire city, aggregated into hexagons, showing the median increase from 2018 to now in that hexagon. You can almost see the path of the light rail. The northern stations (U-District, Roosevelt, and Northgate) have only been open since 2021, but the stations in South Seattle all have had time to reap the benefits of the train access and are significantly more valuable than they were in 2018.

###### *Land Value 2018 vs 2027, Aggregated into Hexagons*

<iframe src="/images/Value_Capture/land_val_change_2018_to_2027.html" height="555" width="700" allowfullscreen="" frameborder="0"> </iframe>

Now take a look at three different map images, showing individual parcels in the 2000 foot radius around their respective center points. 

#### Southern Seattle Light Rail Station Areas (2000 foot raidus)
<iframe src="/images/Value_Capture/southern_LR_station_map.html" height="555" width="700" allowfullscreen="" frameborder="0"> </iframe>
________________________________________________________

#### Northern Seattle Light Rail Station Areas (2000 foot raidus)
<iframe src="/images/Value_Capture/northern_LR_station_map.html" height="555" width="700" allowfullscreen="" frameborder="0"> </iframe>
________________________________________________________

#### Northern Seattle Non Light Rail Station Areas (2000 foot raidus)
<iframe src="/images/Value_Capture/northern_non_LR_station_map.html" height="555" width="700" allowfullscreen="" frameborder="0"> </iframe>


Note that in the 9 years between the 2018 and 2027 assessments, some parcels have been divided and new ones created in their place. Consequently a direct 1 to 1 comparison is not possible in those instances. Due to this reason, as well as certain public property not being evaluated in the same way (Public Universities, Parks) not all parcels will show in these maps. This applies, albeit less frequently, to the aggregated hexagon maps.

### Directly Applied to Ballard, with some math

The land in a 2000 foot radius around Ballard Station (15th and Market) is currently worth $1,926,924,400, close to 2 Billion Dollars. Seattle's property tax rate is just shy of 1% (Often denoted as $10 per $1000 in value), meaning that the land around Ballard Station brings in about $19,269,000, or 19 million. If a TIF district were to be made for those properties, and it grows about 2.5 times in 9 years, as can be reasonably expected based on value growth surrounding light rail stations since 2017 (see initial bar graph), we can translate that to 10% per year (Actually 10.7%, but we're lowballing). If that 10% per year is 'Captured' and all the growth from $19.27 million goes to funding ST3, the growth would capture $114 million in its first decade, $718 million in its first 20 years and a generous $2.59 billion in a 30 year period. 2.59 Billion is a significant portion of the nearly $12 billion that the Ballard Link Extension *and* downtown tunnel cost(see [this document](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.soundtransit.org/st_sharepoint/download/sites/PRDA/FinalRecords/2025/Memo%20-%20Updated%20ST3%20Capital%20Project%20Cost%20Estimates%2009-11-2025_updated.pdf) for ST price estimates).

This 2.59 Billion over 30 years at 10% value growth per year may not be realistic. In fact it probably is not. There are a huge amount of variables at play here, such as the radius of the financing zone, the percentage of the value increase allocated to SoundTransit, the increase in land value and more. Also keep in mind that this was calculated for just one station, but could be applied to many more stations, such as Interbay, Smith Cove, the extremely high land value Denny station, and even stations on the West Seattle and 4 lines. 

The point is that a Value Capture Tax should be considered here. It finds a lot of money for transit that otherwise would not exist. Ballard station will provide staggering positive externalities to the community, and if we can capture just some of them, maybe the project will actually see the light at the end of the tunnel.

Thanks for reading. You can check out my code for the project [here](https://github.com/amschechter/Value_Capture_Tax/blob/master/Polycentric_Study.ipynb), and please don't hesitate to reach out with your thoughts at aaron.m.schechter@gmail.com.

Below are some sources I used to learn about Value Capture tax and Tax Increment Financing.


[FTA info page](https://www.transit.dot.gov/valuecapture)

['Legal Clarity'](https://legalclarity.org/what-is-local-capture-in-tax-increment-financing/)

https://www.psrc.org/asset/growing-transit-communities-value-capture-financing-washington-2336 (Ben Bakkenta)

https://www.fhwa.dot.gov/ipd/value_capture/strategies_in_practice/wa_tax_increment_financing.aspx

King County Assessor → https://info.kingcounty.gov/assessor/datadownload/ErrorDefault.aspx?aspxerrorpath=/assessor/DataDownload/default.aspx
