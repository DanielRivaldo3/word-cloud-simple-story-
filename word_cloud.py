#first of all install matplotlib and wordcloud first
#import wordcloud and matplotlib
from wordcloud import WordCloud, STOPWORDS, wordcloud
import matplotlib.pyplot as plt


#open and load data from santa_story.txt
text = open('santa_story.txt', 'r', encoding= 'utf-8').read()
stopwords = set(STOPWORDS)

#make wordcloud as an object
wc =  WordCloud(
    background_color= 'black',
    max_words= 100,
    stopwords=stopwords
)
#generate

wc.generate(text)
#show wordcloud
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()


#use mask for santa story to santa picture
from PIL import Image
import numpy as np
santa_mask = np.array(Image.open('santa.jpg'))

#show santa picture
fig = plt.figure()
fig.set_figwidth(14) 
fig.set_figheight(18) 
plt.imshow(santa_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off') 
plt.show()


#make new wordcloud as an object with mask
santa_wc = WordCloud(
    background_color='white', 
    mask= santa_mask , 
    stopwords=stopwords)

#generate
santa_wc.generate(text)
fig = plt.figure()
fig.set_figwidth(20)
fig.set_figheight(35)
plt.imshow(santa_wc, interpolation='bilinear')
plt.axis('off')
plt.show()

#save to file
#rename if there is already picture with same name 
santa_wc.to_file("word_cloud_santa_mask.png")