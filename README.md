<section align="center">

[![Maintenance](https://img.shields.io/badge/make%20with-love%20%E2%99%A5-red?style=for-the-badge)]() [![issues](https://img.shields.io/github/issues/dev-willcode/feelingtweets?style=for-the-badge)](https://github.com/dev-willcode/feelingtweets/issues) [![forks](https://img.shields.io/github/forks/dev-willcode/feelingtweets?style=for-the-badge)](https://github.com/dev-willcode/feelingtweets/network) [![stars](https://img.shields.io/github/stars/dev-willcode/feelingtweets?style=for-the-badge)](https://github.com/dev-willcode/feelingtweets/stargazers)

</section>
<h1 align="center">
  Feelingtweets - Sentiments Analysis on Twitter 📊📳
</h1>

A library to collect tweets, clean it (pre-processing), translate it, and create analytics with Textblob and VADER methods.

## 🚧 Requirements

- Python 3.6+

## 🔧 Install

```bash
pip install feelingtweets
```

## 👷‍♀️ Usage

Pass an image (_array buffer_) to the input of node, and receive:

- The prediction model, that includes: bbox array, prediction array, and label array (_0 = mask object_)
- Original image processed.
- Boolean value (_detected_) any mask on the picture.
- Quantity of mask detected
- threshold configurated to evaluate that picture.

You can configure the threshold value to detect with more or less precision.

```py
    import feelingtweets as ft

    config = Config(input_collect_language="es")
    collector = ft.TweetCollector(config)
    cleaner = ft.Cleaner(config)
    traductor = ft.Traductor(config)
    analizer = ft.Analizer()

    # Twitter API search
    search = "(ECUADOR OR TRI OR FEF) AND (FUTBOL OR FÚTBOL OR partido OR selección OR seleccion OR copa OR mundial)"
    query = ft.Query(search, date_start="2021-09-06", limit_tweets=100)
    # collecting phase
    collected_data = collector.collect(query, True)
    # pre-processing phase
    cleaned_data = cleaner.clean(collected_data, True)
    # translateting phase
    translate_data = traductor.traduce(cleaned_data, True)

    if translate_data is not None:
        # analize with both methods
        analized_data = analizer.analize(translate_data["traduced"])
        # standard pandas DataFrame with text, texblob_score, vader_score
        print(analized_data)
```

## Analize only with one:

### Textblob:

```py

        # analize with textblob method
        analized_data = analizer.analize_with_textblob(translate_data["traduced"])
        # standard pandas DataFrame with text, score
        print(analized_data)
```

### VADER:

```py

        # analize with VADER method
        analized_data = analizer.analize_with_vader(translate_data["traduced"])
        # standard pandas DataFrame with text, score
        print(analized_data)
```

## 🎯 Purpose

This project has made for educational purposes, to practice about data mining techniques and get some useful experience on Python, and libs related to data science.
