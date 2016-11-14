#! /usr/bin/env python 
def text_analyzer():

    file = open('textfile.txt', 'r')
    source = file.read()
    unique_count, words = 0, ''
    sentences, frequency = [],[]
    length_in_words = []
    word_list = source.split()
    word_count = len(word_list)
    for e in word_list:
      word_freq = source.count(e)
      frequency.append(word_freq)
      if word_freq == 1:
        unique_count += 1
    for f in source:
       if f =='.':
         if words:
           sentences.append(words)
           words = ''
       else:
         words += f
    for s in sentences:
       length_in_words.append(len(s.split()))
    average_words = sum(length_in_words)/float(len(length_in_words))
    
    print 'Total word count: ' + str(word_count)
    print 'Count of unique words: ' + str(unique_count)
    print 'Number of sentences: ' + str(len(sentences))
    print 'Average words per sentence: ' + str(average_words)
    
    
text_analyzer()
    
       
    
        
      
        
      
    