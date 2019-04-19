from data import Articles, StoreItems


Articulos = Articles()
Store_items = StoreItems()

def dailyItems():
  items = []

  for item in Store_items:
    if item['storeCategory'] == 'BRDailyStorefront':
      items.append(item)
  return items


def weeklyItems():
  items = []

  for item in Store_items:
    if item['storeCategory'] == 'BRWeeklyStorefront':
      items.append(item)
  return items


if __name__ == '__main__':
  #print(Store_items)
  daily_items = dailyItems()
  print('+++++++++++++++++++++')
  print('Daily Store')
  print('+++++++++++++++++++++')
  print(daily_items)

  weekly_items = weeklyItems()
  print('+++++++++++++++++++++')
  print('Weekly Store')
  print('+++++++++++++++++++++')
  print(weekly_items)


'''
  {
  "accountId": "b4c4e32f-2c2c-4486-9faf-f9e6dfd7b1d8",
  "platformId": 2,
  "platformName": "psn",
  "platformNameLong": "PlayStation 4",
  "epicUserHandle": "MBA_53",
  "stats": {
    "p2": {
      "trnRating": {
        "label": "TRN Rating",
        "field": "TRNRating",
        "category": "Rating",
        "valueInt": 1148,
        "value": "1148",
        "rank": 1699220,
        "percentile": 57.0,
        "displayValue": "1,148"
      },
      "score": {
        "label": "Score",
        "field": "Score",
        "category": "General",
        "valueInt": 78311,
        "value": "78311",
        "rank": 38361884,
        "percentile": 6.0,
        "displayValue": "78,311"
      },
      "top1": {
        "label": "Wins",
        "field": "Top1",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 24060639,
        "displayValue": "0"
      },
      "top3": {
        "label": "Top 3",
        "field": "Top3",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top5": {
        "label": "Top 5",
        "field": "Top5",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top6": {
        "label": "Top 6",
        "field": "Top6",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top10": {
        "label": "Top 10",
        "field": "Top10",
        "category": "Tops",
        "valueInt": 49,
        "value": "49",
        "rank": 35812509,
        "percentile": 12.0,
        "displayValue": "49"
      },
      "top12": {
        "label": "Top 12",
        "field": "Top12",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top25": {
        "label": "Top 25",
        "field": "Top25",
        "category": "Tops",
        "valueInt": 157,
        "value": "157",
        "rank": 38784532,
        "percentile": 5.0,
        "displayValue": "157"
      },
      "kd": {
        "label": "K/d",
        "field": "KD",
        "category": "General",
        "valueDec": 0.26,
        "value": "0.26",
        "rank": 47715775,
        "percentile": 93.0,
        "displayValue": "0.26"
      },
      "winRatio": {
        "label": "Win %",
        "field": "WinRatio",
        "category": "General",
        "valueDec": 0.0,
        "value": "0",
        "rank": 23998785,
        "displayValue": "0.00"
      },
      "matches": {
        "label": "Matches",
        "field": "Matches",
        "category": "General",
        "valueInt": 806,
        "value": "806",
        "rank": 39415368,
        "percentile": 1.7,
        "displayValue": "806"
      },
      "kills": {
        "label": "Kills",
        "field": "Kills",
        "category": "General",
        "valueInt": 206,
        "value": "206",
        "rank": 42711504,
        "percentile": 31.0,
        "displayValue": "206"
      },
      "kpg": {
        "label": "Kills Per Match",
        "field": "KPG",
        "category": "General",
        "valueDec": 0.26,
        "value": "0.26",
        "rank": 47704798,
        "percentile": 93.0,
        "displayValue": "0.26"
      },
      "scorePerMatch": {
        "label": "Score per Match",
        "field": "ScorePerMatch",
        "category": "General",
        "valueDec": 97.16,
        "value": "97.16",
        "rank": 20128915,
        "percentile": 85.0,
        "displayValue": "97.16"
      }
    },
    "p10": {
      "trnRating": {
        "label": "TRN Rating",
        "field": "TRNRating",
        "category": "Rating",
        "valueInt": 1148,
        "value": "1148",
        "rank": 1585090,
        "percentile": 55.0,
        "displayValue": "1,148"
      },
      "score": {
        "label": "Score",
        "field": "Score",
        "category": "General",
        "valueInt": 80722,
        "value": "80722",
        "rank": 51114471,
        "percentile": 8.0,
        "displayValue": "80,722"
      },
      "top1": {
        "label": "Wins",
        "field": "Top1",
        "category": "Tops",
        "valueInt": 2,
        "value": "2",
        "rank": 28600476,
        "percentile": 48.0,
        "displayValue": "2"
      },
      "top3": {
        "label": "Top 3",
        "field": "Top3",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top5": {
        "label": "Top 5",
        "field": "Top5",
        "category": "Tops",
        "valueInt": 39,
        "value": "39",
        "rank": 41380947,
        "percentile": 17.0,
        "displayValue": "39"
      },
      "top6": {
        "label": "Top 6",
        "field": "Top6",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top10": {
        "label": "Top 10",
        "field": "Top10",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top12": {
        "label": "Top 12",
        "field": "Top12",
        "category": "Tops",
        "valueInt": 136,
        "value": "136",
        "rank": 46629790,
        "percentile": 6.0,
        "displayValue": "136"
      },
      "top25": {
        "label": "Top 25",
        "field": "Top25",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "kd": {
        "label": "K/d",
        "field": "KD",
        "category": "General",
        "valueDec": 0.18,
        "value": "0.18",
        "rank": 13486824,
        "percentile": 95.0,
        "displayValue": "0.18"
      },
      "winRatio": {
        "label": "Win %",
        "field": "WinRatio",
        "category": "General",
        "valueDec": 0.3,
        "value": "0.3",
        "rank": 28598957,
        "percentile": 61.0,
        "displayValue": "0.30"
      },
      "matches": {
        "label": "Matches",
        "field": "Matches",
        "category": "General",
        "valueInt": 706,
        "value": "706",
        "rank": 49735649,
        "percentile": 1.6,
        "displayValue": "706"
      },
      "kills": {
        "label": "Kills",
        "field": "Kills",
        "category": "General",
        "valueInt": 129,
        "value": "129",
        "rank": 47099191,
        "percentile": 43.0,
        "displayValue": "129"
      },
      "kpg": {
        "label": "Kills Per Match",
        "field": "KPG",
        "category": "General",
        "valueDec": 0.18,
        "value": "0.18",
        "rank": 13023893,
        "percentile": 95.0,
        "displayValue": "0.18"
      },
      "scorePerMatch": {
        "label": "Score per Match",
        "field": "ScorePerMatch",
        "category": "General",
        "valueDec": 114.34,
        "value": "114.34",
        "rank": 50827236,
        "percentile": 85.0,
        "displayValue": "114.34"
      }
    },
    "p9": {
      "trnRating": {
        "label": "TRN Rating",
        "field": "TRNRating",
        "category": "Rating",
        "valueInt": 1067,
        "value": "1067",
        "rank": 1755059,
        "percentile": 57.0,
        "displayValue": "1,067"
      },
      "score": {
        "label": "Score",
        "field": "Score",
        "category": "General",
        "valueInt": 147307,
        "value": "147307",
        "rank": 45065745,
        "percentile": 7.0,
        "displayValue": "147,307"
      },
      "top1": {
        "label": "Wins",
        "field": "Top1",
        "category": "Tops",
        "valueInt": 13,
        "value": "13",
        "rank": 35098248,
        "percentile": 29.0,
        "displayValue": "13"
      },
      "top3": {
        "label": "Top 3",
        "field": "Top3",
        "category": "Tops",
        "valueInt": 67,
        "value": "67",
        "rank": 37877137,
        "percentile": 12.0,
        "displayValue": "67"
      },
      "top5": {
        "label": "Top 5",
        "field": "Top5",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top6": {
        "label": "Top 6",
        "field": "Top6",
        "category": "Tops",
        "valueInt": 177,
        "value": "177",
        "rank": 39772185,
        "percentile": 4.6,
        "displayValue": "177"
      },
      "top10": {
        "label": "Top 10",
        "field": "Top10",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top12": {
        "label": "Top 12",
        "field": "Top12",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top25": {
        "label": "Top 25",
        "field": "Top25",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "kd": {
        "label": "K/d",
        "field": "KD",
        "category": "General",
        "valueDec": 0.21,
        "value": "0.21",
        "rank": 48309634,
        "percentile": 94.0,
        "displayValue": "0.21"
      },
      "winRatio": {
        "label": "Win %",
        "field": "WinRatio",
        "category": "General",
        "valueDec": 1.2,
        "value": "1.2",
        "rank": 35098205,
        "percentile": 67.0,
        "displayValue": "1.20"
      },
      "matches": {
        "label": "Matches",
        "field": "Matches",
        "category": "General",
        "valueInt": 1097,
        "value": "1097",
        "rank": 46927997,
        "percentile": 1.1,
        "displayValue": "1,097"
      },
      "kills": {
        "label": "Kills",
        "field": "Kills",
        "category": "General",
        "valueInt": 233,
        "value": "233",
        "rank": 49707992,
        "percentile": 37.0,
        "displayValue": "233"
      },
      "kpg": {
        "label": "Kills Per Match",
        "field": "KPG",
        "category": "General",
        "valueDec": 0.21,
        "value": "0.21",
        "rank": 48232716,
        "percentile": 94.0,
        "displayValue": "0.21"
      },
      "scorePerMatch": {
        "label": "Score per Match",
        "field": "ScorePerMatch",
        "category": "General",
        "valueDec": 134.28,
        "value": "134.28",
        "rank": 11337954,
        "percentile": 84.0,
        "displayValue": "134.28"
      }
    },
    "curr_p2": {
      "trnRating": {
        "label": "TRN Rating",
        "field": "TRNRating",
        "category": "Rating",
        "valueInt": 1148,
        "value": "1148",
        "rank": 1699220,
        "percentile": 80.0,
        "displayValue": "1,148"
      },
      "score": {
        "label": "Score",
        "field": "Score",
        "category": "General",
        "valueInt": 3865,
        "value": "3865",
        "rank": 7209481,
        "percentile": 58.0,
        "displayValue": "3,865"
      },
      "top1": {
        "label": "Wins",
        "field": "Top1",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 4604293,
        "displayValue": "0"
      },
      "top3": {
        "label": "Top 3",
        "field": "Top3",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top5": {
        "label": "Top 5",
        "field": "Top5",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top6": {
        "label": "Top 6",
        "field": "Top6",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top10": {
        "label": "Top 10",
        "field": "Top10",
        "category": "Tops",
        "valueInt": 1,
        "value": "1",
        "rank": 8234969,
        "percentile": 81.0,
        "displayValue": "1"
      },
      "top12": {
        "label": "Top 12",
        "field": "Top12",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top25": {
        "label": "Top 25",
        "field": "Top25",
        "category": "Tops",
        "valueInt": 6,
        "value": "6",
        "rank": 7365918,
        "percentile": 64.0,
        "displayValue": "6"
      },
      "kd": {
        "label": "K/d",
        "field": "KD",
        "category": "General",
        "valueDec": 0.17,
        "value": "0.17",
        "rank": 10740724,
        "percentile": 91.0,
        "displayValue": "0.17"
      },
      "winRatio": {
        "label": "Win %",
        "field": "WinRatio",
        "category": "General",
        "valueDec": 0.0,
        "value": "0",
        "rank": 4604278,
        "displayValue": "0.00"
      },
      "matches": {
        "label": "Matches",
        "field": "Matches",
        "category": "General",
        "valueInt": 52,
        "value": "52",
        "rank": 5468171,
        "percentile": 43.0,
        "displayValue": "52"
      },
      "kills": {
        "label": "Kills",
        "field": "Kills",
        "category": "General",
        "valueInt": 9,
        "value": "9",
        "rank": 8651005,
        "percentile": 73.0,
        "displayValue": "9"
      },
      "kpg": {
        "label": "Kills Per Match",
        "field": "KPG",
        "category": "General",
        "valueDec": 0.17,
        "value": "0.17",
        "rank": 10740105,
        "percentile": 91.0,
        "displayValue": "0.17"
      },
      "scorePerMatch": {
        "label": "Score per Match",
        "field": "ScorePerMatch",
        "category": "General",
        "valueDec": 74.33,
        "value": "74.33",
        "rank": 11071979,
        "percentile": 93.0,
        "displayValue": "74.33"
      }
    },
    "curr_p10": {
      "trnRating": {
        "label": "TRN Rating",
        "field": "TRNRating",
        "category": "Rating",
        "valueInt": 1148,
        "value": "1148",
        "rank": 1585090,
        "percentile": 81.0,
        "displayValue": "1,148"
      },
      "score": {
        "label": "Score",
        "field": "Score",
        "category": "General",
        "valueInt": 9367,
        "value": "9367",
        "rank": 6455688,
        "percentile": 45.0,
        "displayValue": "9,367"
      },
      "top1": {
        "label": "Wins",
        "field": "Top1",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 6684248,
        "displayValue": "0"
      },
      "top3": {
        "label": "Top 3",
        "field": "Top3",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top5": {
        "label": "Top 5",
        "field": "Top5",
        "category": "Tops",
        "valueInt": 7,
        "value": "7",
        "rank": 5183350,
        "percentile": 44.0,
        "displayValue": "7"
      },
      "top6": {
        "label": "Top 6",
        "field": "Top6",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top10": {
        "label": "Top 10",
        "field": "Top10",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top12": {
        "label": "Top 12",
        "field": "Top12",
        "category": "Tops",
        "valueInt": 22,
        "value": "22",
        "rank": 5207147,
        "percentile": 36.0,
        "displayValue": "22"
      },
      "top25": {
        "label": "Top 25",
        "field": "Top25",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "kd": {
        "label": "K/d",
        "field": "KD",
        "category": "General",
        "valueDec": 0.21,
        "value": "0.21",
        "rank": 10527597,
        "percentile": 89.0,
        "displayValue": "0.21"
      },
      "winRatio": {
        "label": "Win %",
        "field": "WinRatio",
        "category": "General",
        "valueDec": 0.0,
        "value": "0",
        "rank": 6684248,
        "displayValue": "0.00"
      },
      "matches": {
        "label": "Matches",
        "field": "Matches",
        "category": "General",
        "valueInt": 62,
        "value": "62",
        "rank": 6861725,
        "percentile": 47.0,
        "displayValue": "62"
      },
      "kills": {
        "label": "Kills",
        "field": "Kills",
        "category": "General",
        "valueInt": 13,
        "value": "13",
        "rank": 9006303,
        "percentile": 72.0,
        "displayValue": "13"
      },
      "kpg": {
        "label": "Kills Per Match",
        "field": "KPG",
        "category": "General",
        "valueDec": 0.21,
        "value": "0.21",
        "rank": 10521289,
        "percentile": 89.0,
        "displayValue": "0.21"
      },
      "scorePerMatch": {
        "label": "Score per Match",
        "field": "ScorePerMatch",
        "category": "General",
        "valueDec": 151.08,
        "value": "151.08",
        "rank": 3865383,
        "percentile": 45.0,
        "displayValue": "151.08"
      }
    },
    "curr_p9": {
      "trnRating": {
        "label": "TRN Rating",
        "field": "TRNRating",
        "category": "Rating",
        "valueInt": 1067,
        "value": "1067",
        "rank": 1755059,
        "percentile": 100.0,
        "displayValue": "1,067"
      },
      "score": {
        "label": "Score",
        "field": "Score",
        "category": "General",
        "valueInt": 16116,
        "value": "16116",
        "rank": 4228038,
        "percentile": 30.0,
        "displayValue": "16,116"
      },
      "top1": {
        "label": "Wins",
        "field": "Top1",
        "category": "Tops",
        "valueInt": 5,
        "value": "5",
        "rank": 3941439,
        "percentile": 35.0,
        "displayValue": "5"
      },
      "top3": {
        "label": "Top 3",
        "field": "Top3",
        "category": "Tops",
        "valueInt": 11,
        "value": "11",
        "rank": 4116772,
        "percentile": 33.0,
        "displayValue": "11"
      },
      "top5": {
        "label": "Top 5",
        "field": "Top5",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top6": {
        "label": "Top 6",
        "field": "Top6",
        "category": "Tops",
        "valueInt": 24,
        "value": "24",
        "rank": 3551748,
        "percentile": 27.0,
        "displayValue": "24"
      },
      "top10": {
        "label": "Top 10",
        "field": "Top10",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top12": {
        "label": "Top 12",
        "field": "Top12",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "top25": {
        "label": "Top 25",
        "field": "Top25",
        "category": "Tops",
        "valueInt": 0,
        "value": "0",
        "rank": 1,
        "displayValue": "0"
      },
      "kd": {
        "label": "K/d",
        "field": "KD",
        "category": "General",
        "valueDec": 0.35,
        "value": "0.35",
        "rank": 9897576,
        "percentile": 84.0,
        "displayValue": "0.35"
      },
      "winRatio": {
        "label": "Win %",
        "field": "WinRatio",
        "category": "General",
        "valueDec": 4.5,
        "value": "4.5",
        "rank": 5112887,
        "percentile": 45.0,
        "displayValue": "4.50"
      },
      "matches": {
        "label": "Matches",
        "field": "Matches",
        "category": "General",
        "valueInt": 112,
        "value": "112",
        "rank": 3928757,
        "percentile": 28.0,
        "displayValue": "112"
      },
      "kills": {
        "label": "Kills",
        "field": "Kills",
        "category": "General",
        "valueInt": 37,
        "value": "37",
        "rank": 6813671,
        "percentile": 55.0,
        "displayValue": "37"
      },
      "kpg": {
        "label": "Kills Per Match",
        "field": "KPG",
        "category": "General",
        "valueDec": 0.33,
        "value": "0.33",
        "rank": 9931373,
        "percentile": 85.0,
        "displayValue": "0.33"
      },
      "scorePerMatch": {
        "label": "Score per Match",
        "field": "ScorePerMatch",
        "category": "General",
        "valueDec": 143.89,
        "value": "143.89",
        "rank": 6669585,
        "percentile": 57.0,
        "displayValue": "143.89"
      }
    }
  },
  "lifeTimeStats": [
    {
      "key": "Top 5s",
      "value": "39"
    },
    {
      "key": "Top 3s",
      "value": "67"
    },
    {
      "key": "Top 6s",
      "value": "177"
    },
    {
      "key": "Top 10",
      "value": "49"
    },
    {
      "key": "Top 12s",
      "value": "136"
    },
    {
      "key": "Top 25s",
      "value": "157"
    },
    {
      "key": "Score",
      "value": "306,340"
    },
    {
      "key": "Matches Played",
      "value": "2609"
    },
    {
      "key": "Wins",
      "value": "15"
    },
    {
      "key": "Win%",
      "value": "1%"
    },
    {
      "key": "Kills",
      "value": "568"
    },
    {
      "key": "K/d",
      "value": "0.22"
    }
  ],
  "recentMatches": [
    {
      "id": 1620026096,
      "accountId": "b4c4e32f-2c2c-4486-9faf-f9e6dfd7b1d8",
      "playlist": "p10",
      "kills": 3,
      "minutesPlayed": 0,
      "top1": 0,
      "top5": 0,
      "top6": 0,
      "top10": 0,
      "top12": 4,
      "top25": 0,
      "matches": 16,
      "top3": 0,
      "dateCollected": "2019-04-19T09:27:06.66",
      "score": 1724,
      "platform": 2,
      "trnRating": 1148.4,
      "trnRatingChange": -0.14140691994184404
    },
    {
      "id": 1620026097,
      "accountId": "b4c4e32f-2c2c-4486-9faf-f9e6dfd7b1d8",
      "playlist": "p2",
      "kills": 0,
      "minutesPlayed": 0,
      "top1": 0,
      "top5": 0,
      "top6": 0,
      "top10": 0,
      "top12": 0,
      "top25": 0,
      "matches": 2,
      "top3": 0,
      "dateCollected": "2019-04-19T09:27:06.66",
      "score": 129,
      "platform": 2,
      "trnRating": 1148.5,
      "trnRatingChange": -1.3789050000000014
    },
    {
      "id": 1620026098,
      "accountId": "b4c4e32f-2c2c-4486-9faf-f9e6dfd7b1d8",
      "playlist": "p9",
      "kills": 0,
      "minutesPlayed": 0,
      "top1": 0,
      "top5": 0,
      "top6": 0,
      "top10": 0,
      "top12": 0,
      "top25": 0,
      "matches": 1,
      "top3": 0,
      "dateCollected": "2019-04-19T09:27:06.66",
      "score": 120,
      "platform": 2,
      "trnRating": 1067.9,
      "trnRatingChange": -3.5364999999999975
    },
    {
      "id": 1617025157,
      "accountId": "b4c4e32f-2c2c-4486-9faf-f9e6dfd7b1d8",
      "playlist": "p2",
      "kills": 0,
      "minutesPlayed": 0,
      "top1": 0,
      "top5": 0,
      "top6": 0,
      "top10": 0,
      "top12": 0,
      "top25": 0,
      "matches": 4,
      "top3": 0,
      "dateCollected": "2019-04-18T06:58:46.04",
      "score": 161,
      "platform": 2,
      "trnRating": 1151.2,
      "trnRatingChange": -1.3066290092109381
    },
    {
      "id": 1617025158,
      "accountId": "b4c4e32f-2c2c-4486-9faf-f9e6dfd7b1d8",
      "playlist": "p9",
      "kills": 0,
      "minutesPlayed": 0,
      "top1": 0,
      "top5": 0,
      "top6": 2,
      "top10": 0,
      "top12": 0,
      "top25": 0,
      "matches": 9,
      "top3": 0,
      "dateCollected": "2019-04-18T06:58:46.04",
      "score": 1064,
      "platform": 2,
      "trnRating": 1071.4,
      "trnRatingChange": -3.4413357096733521
    },
    {
      "id": 1617025155,
      "accountId": "b4c4e32f-2c2c-4486-9faf-f9e6dfd7b1d8",
      "playlist": "p10",
      "kills": 3,
      "minutesPlayed": 0,
      "top1": 0,
      "top5": 2,
      "top6": 0,
      "top10": 0,
      "top12": 7,
      "top25": 0,
      "matches": 10,
      "top3": 0,
      "dateCollected": "2019-04-18T06:58:46.037",
      "score": 1970,
      "platform": 2,
      "trnRating": 1142.4,
      "trnRatingChange": -1.5409809756321977
    },
    {
      "id": 1612201808,
      "accountId": "b4c4e32f-2c2c-4486-9faf-f9e6dfd7b1d8",
      "playlist": "p9",
      "kills": 2,
      "minutesPlayed": 0,
      "top1": 0,
      "top5": 0,
      "top6": 1,
      "top10": 0,
      "top12": 0,
      "top25": 0,
      "matches": 1,
      "top3": 1,
      "dateCollected": "2019-04-16T10:04:32.413",
      "score": 380,
      "platform": 2,
      "trnRating": 1054.3,
      "trnRatingChange": 49.945
    },
    {
      "id": 1612201806,
      "accountId": "b4c4e32f-2c2c-4486-9faf-f9e6dfd7b1d8",
      "playlist": "p2",
      "kills": 2,
      "minutesPlayed": 0,
      "top1": 0,
      "top5": 0,
      "top6": 0,
      "top10": 0,
      "top12": 0,
      "top25": 0,
      "matches": 4,
      "top3": 0,
      "dateCollected": "2019-04-16T10:04:32.413",
      "score": 457,
      "platform": 2,
      "trnRating": 1156.2,
      "trnRatingChange": -1.1723863027851604
    },
    {
      "id": 1612201804,
      "accountId": "b4c4e32f-2c2c-4486-9faf-f9e6dfd7b1d8",
      "playlist": "p10",
      "kills": 0,
      "minutesPlayed": 0,
      "top1": 0,
      "top5": 0,
      "top6": 0,
      "top10": 0,
      "top12": 1,
      "top25": 0,
      "matches": 2,
      "top3": 0,
      "dateCollected": "2019-04-16T10:04:32.397",
      "score": 210,
      "platform": 2,
      "trnRating": 1159.5,
      "trnRatingChange": -1.0836787500000014
    },
    {
      "id": 1609969704,
      "accountId": "b4c4e32f-2c2c-4486-9faf-f9e6dfd7b1d8",
      "playlist": "p9",
      "kills": 1,
      "minutesPlayed": 0,
      "top1": 0,
      "top5": 0,
      "top6": 0,
      "top10": 0,
      "top12": 0,
      "top25": 0,
      "matches": 3,
      "top3": 0,
      "dateCollected": "2019-04-15T14:23:45.08",
      "score": 459,
      "platform": 2,
      "trnRating": 1004.4,
      "trnRatingChange": -5.2347034265624988
    }
  ]
}

'''