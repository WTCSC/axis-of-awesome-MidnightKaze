[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18859027)
# Axis of Awesome
Are you a complete Pokemon ~~addict~~ fan like me? Well maybe you're curious in seeing how all of the types have a rather unfair distribution of each "type" of Pokemon. I'm talking about the fact that psychic type pokemon have __ten__ mega evolutions compared to the __two__ in eletric type. That's just a little unfair. 

And listen, only a nerd would care about that, but it's kind of cool. And instead of a boring old data table, you can look at some awesome visualizations!

## How to Visualize
To get visualizing it's really as simple as just cloning these two files:

1) `data.csv` which is the file that actually contains the data table
2) `visuals.py` which is the file that contains the Python that will make the visuals

With both of them in the same directory you can just run `python3 visuals.py` and in just a few seconds both visualizations will appear.

## Visual Descriptions
There are two main visuals that I made using my Pokemon data set: __A Scatterplot__ and a __Double Donut Chart__ (aka a double pie chart). Both of these visualize the same thing. The Scatterpolt... well it plots all of data above their respective types. There's also a very nice ledgend because I'm so nice.

The Double Donut Chart take's it a bit further. The outside circle has all of the types (color codes respectively) along with their percent out of the total set. The inside circle further breaks that down into each "type" that I listed above. That is also broken down by their percent out of the total.

__*Do note that for my sanity I only did this for Gen 5 and 6 combined. That totals a total of 451 Pokemon in this data sample. Yes it does include multiple forms of a Pokemon if it has one. Yes it is also probably off by a few.*__