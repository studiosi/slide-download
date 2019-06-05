# slide-download

Scraper to download datasets from slideshare.

# How it works

You establish an initial URL and the beast feeds itself from the related links, until there are no more or the maximum number per session is reached. It saves the slides as images in an output folder inside the directory where you are executing your script. Each presentation is saved to a folder which is the title of the presentation, slugified. If the folder already exists, it skips the presentation, but still adds the related items.

# Installation

Install the anaconda python environment and activate it. Copy the config-sample.py to a file called config.py in the same folder. Change the values to what you desire.

The initial URL is the URl that will be used to start the scrape. You can change this between sessions in order to increase the chances of success. The scraper feeds itself from the related slides.

The maximum number per session is the amount of presentations that the scraper will download in one session. A sensitive value might be 100.

# Execution

Just do it

```
python slide-download.py
```

# Be gentle

You don't want to accidentally DOS Slideshare. Thake that in mind. Respect above all things.