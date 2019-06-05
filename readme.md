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

You don't want to accidentally DOS Slideshare. Take that in mind. Respect above all things.

# License

Copyright 2019 David Gil de Gómez (Studiosi)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.