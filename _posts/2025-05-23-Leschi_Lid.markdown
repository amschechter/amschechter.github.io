---
layout: post
title:  "The Leschi Lid"
date:   2025-5-23 13:17:35 -0800
categories: jekyll update
thumbnail: '/images/Leschi_Lid/Parcel_and_Tunnel_Image.png'
---

# A look at how infrastructure decisions can shape a neighborhood's finances

Hi Everyone, thanks for visiting this write-up (article? project?). To skip to the interactive maps I have made scroll near to the [Maps](#maps) section

### Context and History

I live in Leschi. It is a gorgeous neighborhood with sweeping views of and access to Lake Washington. This view includes, of course, the I-90 bridge. Leschi and the Northern portion of Mount Baker have traditionally been single family home neighborhoods with very little alternative zoning. Most days I have the privilege of walking about one mile south from 31st and Dearborn to work/play at the beloved Amy Yee Tennis Center. These walks, which sometimes go through Sam Smith park and sometimes stay on the ridge give me plenty of time to think about the history of the neighborhood and it's built environment. Particularly when it comes to the highway.

Why was it made as a tunnel? Why are some nearby highways not tunnels? Does this Tunnel/Lid benefit us? To what degree? What would daily life in the area be like if the powers that be had chosen to send the highway over rather than through the hill?

When I think of these questions, I can't help but think of the socio-economic makeup of various parts of Seattle. [This](https://dsl.richmond.edu/panorama/redlining/map/WA/Seattle/area_descriptions#loc=13/47.6113/-122.323) 1936 map, originally made with the Federal Housing Administration, digitized and annotated by the University of Richmond details the 'Grade of Security'. This depiction of Seattle splits the city into five distinct categories, 'Best', 'Still Desirable', 'Definitely Declining', 'Hazardous', and 'Business/Industrial'.

Leschi and Mount Baker as we know them were preserved partially by a decision made sometime in the 1930s. The [Mount Baker Tunnel](https://en.wikipedia.org/wiki/Mount_Baker_Tunnel) was completed in 1940. The original tunnel went below land exclusively in the 'Still Desirable' category of the 1936 FHA map. One that map the 

In the 80s and 90s the Tunnel was expanded and the 'Lid' was added. The lid is the section that goes from 23rd Ave in the West to 29th Ave on the eastern portion, allowing for Sam Smith and Jimi Hendrix Parks. For the purposes of my analysis I have treated the Tunnel and The Lid as the same. 

I am not sure if it was a tough decision nine decades ago to bore this tunnel. According to Seattle Times excerpts from the 1930's featured in [this](https://pauldorpat.com/2020/10/01/seattle-now-then-mount-baker-tunnel-1940/) recent (2020) article the tunnel's projected cost was $935,000 ($21,122,769 in 2025 dollars), which panned out to be 'about $1,400,000' ($31,627,676 in 2025 dollars) after some cost overruns. The entire project, including the bridge from Mercer Island to the tunnel in question ended up at $8,450,000 ($190,895,616 in 2025 dollars). I should also note that there was at least some sentiment against the project as a whole at the time with Seattle Times Associate Editor James Wood calling the project 'A gross and wholly unnecessary obstruction....hideous at all times'. I'm showing some restraint by not quoting more of Wood, he had some spicy things to say.

The previously mentioned Lid, spanning from 29th to 23rd cost $400 Million ($1,718,106,350 in 2025 dollars) when it was built in 1990 according to 'The Aberdeen Group'.

Today, the area has tons of growth. (Slightly) Relaxed zoning laws allow for more types of housing to be built in the area. Take for example the [Shelter Homes](https://shelterhomesseattle.com/property/adler-1301-31st-ave-s-seattle-98144/) development at 1301 31st ave S, a former gas station that is now becoming ten(!) different million plus dollar townhomes. This type enormous change is being seen all over Seattle with tons of lots being converted into denser and denser housing. This particular change is however not yet represented in the parcel and tax data that I have as they still have a couple of months until completion! This time next year the County will likely be collecting a million dollars in property taxes from the entire lot.

Apologies for the lengthy preamble. I wanted to set the stage to illustrate both the costs and the benefits of the I-90 lid + Tunnel. 

To study the lid, I am using the property values of land in the area surrounding the footprint of the tunnel/lid to estimate the overall financial impact that the project has had on the neighborhood. Luckily for me, property values are a matter of public record and are available with data on their associated parcel on the King County Website. Yippee! All data used will be linked at the bottom. 

The parcel data I am using has both appraised land value and appraised improvements value. For simplicity I chose to combine them for the purposes of this analysis, but examining the differences can be very interesting. For example the Shelter Homes development will result in that same parcel of land paying dramatically more total tax than it was before. Should we be punished for developing land and incentivizing underdevelopment? Personally I think I don't understand the full implications of these distinctions and would love to learn more. There is an economic ideology called [Georgism](https://en.wikipedia.org/wiki/Georgism) dedicated to 

For this study I am assuming that having a highway through a neighborhood affects the property values of land up to about 7/10th of a mile away. Using this assumption I took the data on all of the land in that zone and east of 23rd ave and made a rudimentary calculation of how much property tax that section paid. 

| Tax Type                                                                          | 2025 Dollar Amount | 
| --------------------------------------------------------------------------------- | ------------------ |
|  Total Appraised Land Value (Excluding Improvements)                              | $2,329,722,585     |
|  Total Appraised Improvement Value (Excluding Land Value)                         | $2,032,736,707     |
|  Combined Land and Improvement Value                                              | $4,362,459,292     |
|  Combined Land and Improvement Value Divided by the relative distance from Tunnel | $2,227,889,861     |

### Maps


![Distance from Tunnels](/images/Leschi_Lid/Parcel_and_Tunnel_Image.png){:class="img-responsive"}

Below is the Total_Parcel_Val_Map

<iframe src="/images/Leschi_Lid/Total_Parcel_Val_Map.html" height="555" width="700" allowfullscreen="" frameborder="0"> </iframe>

Below is the Tax_Per_Sq_Foot_Map

<iframe src="/images/Leschi_Lid/Tax_Per_Sq_Foot_Map.html" height="555" width="700" allowfullscreen="" frameborder="0"> </iframe>

Below is the Tax_Per_SQFT_X_Distance_Map

<iframe src="/images/Leschi_Lid/Tax_Per_SQFT_X_Distance_Map.html" height="555" width="700" allowfullscreen="" frameborder="0"> </iframe>

Thanks for reading! I had a great time working on this and am glad to know more about where I live. View the code used to come up with the numbers and make the maps [here](https://github.com/amschechter/LeschiLid/blob/master/Lid_Analysis.ipynb), the parcel data [here](https://gis-kingcounty.opendata.arcgis.com/datasets/kingcounty::parcels-for-king-county-with-address-with-property-information-parcel-address-area/explore?filters=eyJQT1NUQUxDVFlOQU1FIjpbIlNFQVRUTEUiXX0%3D&location=47.427721%2C-121.817400%2C9.59) and the tunnel data [here](https://gisdata-wsdot.opendata.arcgis.com/datasets/8a0b7336c568428faed36a67beae8075_13/explore?location=47.605211%2C-122.227590%2C11.87).
