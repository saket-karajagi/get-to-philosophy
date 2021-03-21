### The Python program picks a random Wikipedia link and crawls the first link from the main text upto a 100 times. The possible scenarios:
- The link chain reaches 100 links and terminates
- The chain reaches the Philosphy page
- The chain sees a previous seen page which indicates a loop

Parameters:
- max number of links in the chain: 100
- number of random links for the experiment: 100

Execution:
```bash
python3 ~/get_to_philosphy.py
```

Sample results:
```
({'reached dead end': 11, 'target reached': 78, 'max steps reached': 0, 'loop': 11}, 
{'https://en.wikipedia.org/wiki/Iran': 1, 
'https://en.wikipedia.org/wiki/Visual_art': 1, 
'https://en.wikipedia.org/wiki/Amsterdam': 1, 
'https://en.wikipedia.org/wiki/Association_football': 2, 
'https://en.wikipedia.org/wiki/Art#Forms,_genres,_media,_and_styles': 1, 
'https://en.wikipedia.org/wiki/Thoroughfare': 1, 
'https://en.wikipedia.org/wiki/Stage_name': 1, 
'https://en.wikipedia.org/wiki/Intraparenchymal_bleed': 1, 
'https://en.wikipedia.org/wiki/Gissur_Einarsson': 1, 
'https://en.wikipedia.org/wiki/Terminology_science': 1}, 28)
```
- 78% of the sample set reach Philosphy.
- 28 is the longest chain link for reaching Philosophy
- No other common sinks found

Future improvements:
- condense some redundant code
- account for Wikipedia browsing limits
- clarify with comments
