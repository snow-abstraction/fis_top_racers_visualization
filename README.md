# fis_top_racers_visualization
Some Python code for scraping FIS cross-country skiing results and displaying the results as heat map/graph.

Assuming that you've got python3 set up with the packages needed and you are comfortable with your Linux terminal. You generate a heat map like this:
1.) save the html from the top 12 racers views available from fis to a file called saved.html. For example. https://data.fis-ski.com/global-links/statistics/overview-top-ranked-in-all-competitions.html?place=&season=2016&sector=CC&nation_place=&gender=L&category=WC&nbr=13&nation_comp=&discipline=SP&Submit=Search
2.) run parse_best_to_heat_graph saved.html "Title_for_graph" optional_python_regex

So to only show sprints, this could be something like:
./parse_best_to_heat_graph ../women2016.txt  "Pre-Tour Women's Sprints" 'SP'

(There's no date filtering implemented so I generated pre-Tour results by running against html saved before the Tour started.)

If you're running Debian, these might be useful too:

apt-get install python-requests
apt-get install python3-bs4
apt-get install python3-matplotlib
