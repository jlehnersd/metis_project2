# Webscraped Data

---

* `champion`:
  * Type: string (`str`)
  * Descripton: name of champion
  * Source: scraped from [League of Legends Wiki](https://leagueoflegends.fandom.com/wiki/List_of_champions)

* `release_date`:
  * Type: string (`str`)
  * Description: date that champion was released (format 'yyyy-mm-dd')
  * Source: scraped from [League of Legends Wiki](https://leagueoflegends.fandom.com/wiki/List_of_champions)
* `last_patch`:
  * Type: string (`str`)
  * Description: the patch number in which the champion was most recently changed
  * Source: scraped from [Leaguepedia](https://lol.gamepedia.com/) champion pages
* `num_skins`:
  * Type: integer (`int`)
  * Description: number of nonbase skins the champion has as of the date the data was collected
  * Source: scraped from [League of Legends Wiki](https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki) champion skin pages
* `win_rate`:
  * Type: string (`str`)
  * Description: percentage of ranked games that champion wins when picked across all tiers
  * Source: scraped from [op.gg]('https://na.op.gg/statistics/champion/')
* `ban_rate`:
  * Type: string (`str`)
  * Description: percentage of ranked games in which that champion is banned across all tiers
  * Source: scraped from [op.gg]('https://na.op.gg/statistics/champion/')
* `pick_rate`:
  * Type: string (`str`)
  * Description: percentage of ranked games in which that champion is played across all tiers
  * Source: scraped from [op.gg]('https://na.op.gg/statistics/champion/')
* `date_data`:
  * Type: string (`str`)
  * Description: date on which the data of this row was collected
  * Source: determined via the datetime module at the time of scraping