from config import *
from requests_html import HTMLSession
import os
from slugify import slugify
import wget
from urllib.parse import urljoin
import shutil


# If output directory does not exist, create it
outputDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "output")
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

# Start session
session = HTMLSession()
currentURL = START_URL

downloaded = 0

visitedSlideshows = set()
nextSlideshows = set()

nextSlideshows.add(START_URL)

while downloaded <= MAX_PER_SESSION and len(nextSlideshows) > 0:
    currentURL = nextSlideshows.pop()
    # Get contents of page
    try:
        content = session.get(currentURL)
    except:
        print("Presentation does not exist, nothing downloaded, continuing.")
        continue
    # Get title
    title_element = content.html.find('span.j-title-breadcrumb', first=True)
    if title_element is None or title_element.text is None:
        print("Title not found, nothing downloaded, continuing.")
        continue
    else:
        title = title_element.text
    print(f'Downloading \"{title}\"...')
    # Get image index and download link
    slides = [(int(s.attrs['data-index']), s.find('img.slide_image', first=True).attrs['data-full']) for s in content.html.find('section.slide')]
    # Calculate padding length for best filename
    nSlides = len(slides)
    nPad = len(str(nSlides))
    # Create output directory
    if nSlides > 0:
        currentDir = os.path.join(outputDir, slugify(title))
        if os.path.exists(currentDir):
            print("Directory exists (probably already downloaded or with the same name than one that is), skipping.")
            pass # This will be a continue when the scraper is fully done
        else:
            os.makedirs(currentDir)
            # Save slides
            for slide in slides:
                filename = f'{slide[0]:0{nPad}d}' + '.jpg'
                slidePath = os.path.join(currentDir, filename)
                try:
                    wget.download(slide[1], bar=None, out=slidePath)
                except:
                    print("Failed download, deleting presentation folder.")
                    shutil.rmtree(currentDir)
                    continue
            print("Completed.")
            visitedSlideshows.add(currentURL)
            downloaded += 1
    else:
        print("No slides were found for this presentation")
    # Add current presentation to visited slideshows
    visitedSlideshows.add(currentURL)
    # Find related content
    relatedItems = content.html.find('.j-related-item > a')
    relatedSlideshows = [urljoin(currentURL, s.attrs['href']) for s in relatedItems]
    for s in relatedSlideshows:
        if s not in visitedSlideshows:
            nextSlideshows.add(s)

            
    
