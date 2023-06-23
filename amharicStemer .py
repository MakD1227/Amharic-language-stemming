#!/usr/bin/env python
# coding: utf-8

# In[153]:


#import neccessary packages 

#importing hornmorpho packas as hm
#if unable to install  the hornmorpho(hm) package using 'pip', download zip file@https://github.com/hltdi/HornMorpho.git
# unzip it and save inside current path(the path/directory where other packages are installed,then 
# change its name(folder name) to 'hm' in the distination directory, where it is installed
from hm import anal#import anal function from package hornmorpho(hm)
import re
import pandas as pd

#part I
"""
define/declartion methods for text preprocessing such as:
#removePunct(), #removeAsciiandNumbers(),#removeEmoj()
these function takes only 1 D text i.e sentence or word only, doesn't support list of sentences  
"""

#removing punctuations and special characters
def removePunct(text_input):    
        am_punc='[፨፧፦!፥፤፣፣።፡,():;.]+'
        clean_txt = re.sub(am_punc, ' ',text_input)
        clean_txt=re.sub('[\(\)[\]\{\}|]',' ',clean_txt)
        #replacing any existance of special character or punctuation to null  
        special_char="[@#$%^&ǝ=?×!,;:_.`'\'/+*<>\"¤—„\-®¯™ṣčṣṣᵂᵂṭᵂč̣ǝwannǝt¡¡\x10»€«·‘0e1b§”¬¦…""f÷\~¨©±¥£¶–°•˜’“|]"
        clean_txt= re.sub(special_char,' ',clean_txt) 
        return clean_txt
def removeAsciiandNumbers(text_input):
        #remove all ascii characters and Arabic and ge'ez numbers
        #your input should be text, cats its data type if it is not text
        rm_num_and_ascii=re.sub('[A-Za-z0-9]','',text_input)
        rm_geez_num=re.sub('[\'\u1369-\u137C\']+','',rm_num_and_ascii)
        return rm_geez_num
    
#remove emoj
def removeEmoj(text_input):
        #your input should be text, cats its data type if it is not text
        #remove imojs
        RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
        clean_text = RE_EMOJI.sub(r'',text_input)
        emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"# emoticons
                                   u"\U0001F300-\U0001F5FF" # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF" # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF" # flags
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'',clean_text)
    
#pack all the function presented in the above 
def cleanDocument(text_input): # takes ssentence or paragraph and return cleaned text
        #if the input data is list it must be converted into string to preprocess        
        cleaned_text=removePunct(text_input)
        cleaned_text=removeAsciiandNumbers(cleaned_text)
        cleaned_text=removeEmoj(cleaned_text)        
        return cleaned_text

#part II    
""" 
define functions such as: #characterNormalize(),#spellForwardCorrect(), #spellReverseCorrect()
#these function takes only 1 D text i.e sentence or word only, doesn't support list of sentences
"""
#normalizting characters 
def characterNormalize(text_input):
        #your input should be text, cats its data type if it is not text
        #normalize ceach characters
        #simlar sound but different morphes
        rep1=re.sub('[ሃኅኃሐሓኻ]','ሀ',text_input)
        rep2=re.sub('[ሑኁዅ]','ሁ',rep1)
        rep3=re.sub('[ኂሒኺ]','ሂ',rep2)
        rep4=re.sub('[ኌሔዄ]','ሄ',rep3)
        rep5=re.sub('[ሕኅ]','ህ',rep4)
        rep6=re.sub('[ኆሖኾ]','ሆ',rep5)
        rep7=re.sub('[ሠ]','ሰ',rep6)
        rep8=re.sub('[ሡ]','ሱ',rep7)
        rep9=re.sub('[ሢ]','ሲ',rep8)
        rep10=re.sub('[ሣ]','ሳ',rep9)
        rep11=re.sub('[ሤ]','ሴ',rep10)
        rep12=re.sub('[ሥ]','ስ',rep11)
        rep13=re.sub('[ሦ]','ሶ',rep12)
        rep14=re.sub('[ዓኣዐ]','አ',rep13)
        rep15=re.sub('[ዑ]','ኡ',rep14)
        rep16=re.sub('[ዒ]','ኢ',rep15)
        rep17=re.sub('[ዔ]','ኤ',rep16)
        rep18=re.sub('[ዕ]','እ',rep17)
        rep19=re.sub('[ዖ]','ኦ',rep18)
        rep20=re.sub('[ጸ]','ፀ',rep19)
        rep21=re.sub('[ጹ]','ፁ',rep20)
        rep22=re.sub('[ጺ]','ፂ',rep21)
        rep23=re.sub('[ጻ]','ፃ',rep22)
        rep24=re.sub('[ጼ]','ፄ',rep23)
        rep25=re.sub('[ጽ]','ፅ',rep24)
        rep26=re.sub('[ጾ]','ፆ',rep25)
        #Normalizing words with Labialized Amharic characters such as በልቱዋል or  በልቱአል to  በልቷል  
        rep27=re.sub('(ሉ[ዋአ])','ሏ',rep26)
        rep28=re.sub('(ሙ[ዋአ])','ሟ',rep27)
        rep29=re.sub('(ቱ[ዋአ])','ቷ',rep28)
        rep30=re.sub('(ሩ[ዋአ])','ሯ',rep29)
        rep31=re.sub('(ሱ[ዋአ])','ሷ',rep30)
        rep32=re.sub('(ሹ[ዋአ])','ሿ',rep31)
        rep33=re.sub('(ቁ[ዋአ])','ቋ',rep32)
        rep34=re.sub('(ቡ[ዋአ])','ቧ',rep33)
        rep35=re.sub('(ቹ[ዋአ])','ቿ',rep34)
        rep36=re.sub('(ሁ[ዋአ])','ኋ',rep35)
        rep37=re.sub('(ኑ[ዋአ])','ኗ',rep36)
        rep38=re.sub('(ኙ[ዋአ])','ኟ',rep37)
        rep39=re.sub('(ኩ[ዋአ])','ኳ',rep38)
        rep40=re.sub('(ዙ[ዋአ])','ዟ',rep39)
        rep41=re.sub('(ጉ[ዋአ])','ጓ',rep40)
        rep42=re.sub('(ደ[ዋአ])','ዷ',rep41)
        rep43=re.sub('(ጡ[ዋአ])','ጧ',rep42)
        rep44=re.sub('(ጩ[ዋአ])','ጯ',rep43)
        rep45=re.sub('(ጹ[ዋአ])','ጿ',rep44)
        rep46=re.sub('(ፉ[ዋአ])','ፏ',rep45)
        rep47=re.sub('[ቊ]','ቁ',rep46) #ቁ can be written as ቊ
        rep48=re.sub('[ኵ]','ኩ',rep47) #ኩ can be also written as ኵ  
        return rep48

#correcting misspelled words   
def spellForwardCorrect(token_input):#helps to correct miss spelled character 
        rep1=re.sub(('ወች'),'ዎች',token_input)
        rep2=re.sub('[ዉ]','ው',rep1)
        rep3=re.sub('[ጂ]','ጅ',rep2)
        rep4=re.sub('[ቸ]','ቼ',rep3)
        rep5=re.sub('[የ]','ዬ',rep4)
        rep6=re.sub('[ጀ]','ጄ',rep5)
        rep7=re.sub('[ኜ]','ኘ',rep6)
        rep8=re.sub('[ሽ]','ሺ',rep7)
        rep9=re.sub('[ጨ]','ጬ',rep8)
        rep10=re.sub('[ጪ]','ጭ',rep9)
        rep11=re.sub('[ዥ]','ዢ',rep10)
        rep12=re.sub('[ዪ]','ይ',rep11)
        return rep12
    
def spellReverseCorrect(token_input): #helps to correct miss spelled character
        #reversese vesion of  spellForwardCorrect() funcspellForwardCorrection      
        rep1=re.sub(('ኚ'),'ኝ',token_input)
        rep2=re.sub('[ው]','ዉ',rep1)
        rep3=re.sub('[ጅ]','ጂ',rep2)
        rep4=re.sub('[ቼ]','ቸ',rep3)
        rep5=re.sub('[ዬ]','የ',rep4)
        rep6=re.sub('[ጄ]','ጀ',rep5)
        rep7=re.sub('[ኜ]','ኘ',rep6)
        rep8=re.sub('[ሽ]','ሺ',rep7)
        rep9=re.sub('[ጬ]','ጨ',rep8)
        rep10=re.sub('[ጭ]','ጪ',rep9)
        rep11=re.sub('[ዢ]','ዥ',rep10)
        rep12=re.sub('[ይ]','ዪ',rep11)
        return rep12

#part III
#stemmer prepartion
"""
#define stemer which custumize output of hornmorpho stemmer
# hornmorph stemmer is developed by Michael Gesser, and 
#the stemer is also called Gesser stemmer
#anal() method of gesser stemmer returns part of speech.
#hence special_char and ummeccssary words should remove
# amharicStemmer() return only stem of the word by utilizing cleanDocument() function defined above
"""
#amharicStemer() takes word and return its stem
#in amharicWordStemer() part of speech tag(pos) list is removed 
#while corpusStemmer takes corpus as argument and return stem of a corpus
def amharicWordStemmer(token_input):       
        pos_list=anal('am',token_input,raw=True)
        stem=cleanDocument(str(pos_list))
        stem=stem.split()
        if stem !=[]:
            return stem[0]
        else:
            return ''

 #takes corpus, list of sentence(s),phrases or word(s) and returns stem 
def amharicCorpusStemmer(corpus):   
    cleaned_text=[]# create empty list to store pcleaned text later
    stemed_text=[]
    for i in range(len(corpus)):
        #clean the text from noises such as punctuation marks
        cleaned_text.append(cleanDocument(corpus[i]))

    for i in range(len(cleaned_text)):
        strg=''
        for token_in in cleaned_text[i].split():
                    stem=amharicWordStemmer(token_in)
                    if(stem==''):
                        stem=amharicWordStemmer(characterNormalize(token_in))
                        if(stem==''):
                            stem=amharicWordStemmer(spellForwardCorrect(token_in))                    
                            if(stem==''):
                                stem=amharicWordStemmer(spellReverseCorrect(token_in))
                    if(stem!=''):
                       strg=strg+stem+' '
                    else:
                      #take the word as it is if the word is not stemmed
                      strg=strg+token_in+' '
        stemed_text.append(strg[:-1])
    return stemed_text


#Part IV how to use:
#conculusion:
""" 
 we can use amharicCorpusStemmer() to stem a corpus by passing 'corpus' argument to it
 amharicCorpusStemmer(corpus), corpus parameter could be: word, list of words(pandaSereies), list of of senences, or dataFrame
 """
#using amharicCorpusStemmer() 
corpus=['ላለፉት ጥቂት ለማይባሉ', ' ወራት . 9 ', 'የክስ ቻርጅ የለ', ' በቃ ዘብጥያ ወደ ቤትህ ሂድ']
stem=amharicCorpusStemmer(corpus)
print('The stem word of the text ',corpus,' is ',stem) 
print() 
#part V: Evaluation 
#Evaluation of Gesser stemmer and customized stemmers: amharicStemmer() and corpus stemmer
token_in='ቤትህ'
corpus=['ላለፉት ጥቂት ለማይባሉ', ' ወራት . 9 ', 'የክስ ቻርጅ የለ', ' በቃ ዘብጥያ ወደ ቤትህ ሂድ']
print() 
print('Evaluation of Gesser stemmer and customized stemmers: amharicStemmer() and corpus stemmer')
print() 
print('Out put of Gesser stemmer: ', anal('am',token_in,raw=True))
print() 
print() 
print('Out put of amharicWordStemmer:', amharicWordStemmer(token_in))
print()
print() 
print('Out put of amharicCorpusStemmer:', amharicCorpusStemmer(corpus))


# In[15]:


amharicStemer('እለት')


# In[ ]:




