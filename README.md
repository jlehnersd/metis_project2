# Effect of Skin Releases on Champion Play Rates in League of Legends
## Jeremy Lehner

---

### Motivation:

League of Legends (LoL), developed by Riot Games, is one of the most popular online multiplayer video games in the world. Each game of LoL consists of two teams of five players where each of those ten players chooses to play as a different champion (LoL characters) among a roster of nearly 150 champions. 

Since the release of LoL in 2009, Riot Games has grown to be a billion-dollar company. The game is free to play, but players may spend real money on in-game points that can be used to purchase cosmetic items. The greatest revenue source come from skins, which are like costumes that change how a champion looks and sounds during a game.

I am curious if champion play rates are affected by the release of new skins. If skin releases do affect champion play rates, does that effect depend on the particular champion or skin line/tier? These are the questions I hope to answer in this project.

### Methodolgy:
1. Scrape champion and skin data from League of Legends Wiki
2. Determine champion play rates from Riot API data
3. Build linear regression model
4. Perform analysis to gain insights

### Data Sources:
* [League of Legends Wiki](https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki)
* [Riot API](https://developer.riotgames.com/)

### Target:
* MVP: determine the effect of a new skin release on champion play rate
* Goal: predict the dependence of change in play rate on the champion, skin line, and skin tier

### Features:
* __Skin name__
  * Data type: str
  * Example: 'Arcade Sona'
* __Champion name__
  * Data type: str
  * Example: 'Sona'
* __Skin line__
  * Data type: str
  * Example: 'Arcade: Heroes'
* __Skin price__
  * Data type: int
  * Example: 1350
* __Release date__
  * Data type: str
  * Example: '30-Aug-2012'
* __Play rate 1 day prior__
  * Data type: float
  * Example: 0.064
* __Play rate 2 days prior__
* __Play rate 3 days prior__
* __Play rate 4 days prior__
* __Play rate 5 days prior__
* __Play rate 6 days prior__
* __Play rate 7 days prior__
* __Play rate 1 day after__
* __Play rate 2 days after__
* __Play rate 3 days after__
* __Play rate 4 days after__
* __Play rate 5 days after__
* __Play rate 6 days after__
* __Play rate 7 days after__

### Considerations
* Champion play rates are not directly available from the Riot API, but can be estimated indirectly. My plan to estimate play rates is to make API calls for certain dates on a list player IDs that are known to be valid and then choose random IDs from other players in each of those games and so on until I have data from a few thousand games with which I will calculate the play rates of each champion on those dates.


* Play rates are not static. I will estimate average play rates on each day for a week before and a week after each skin release, then use the daily averages to estimate overall average champion play rates before and after skin release.

---

## Project Organization 
------------

(generated with [datasciencemvp](https://github.com/cliffclive/datasciencemvp/))

(modified from [cookiecutter-datascience](https://drivendata.github.io/cookiecutter-data-science/))

```
    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
```
