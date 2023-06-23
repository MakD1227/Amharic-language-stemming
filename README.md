@ email: mekuanentde@gmail.com 
# Amharic-language-stemming
#Amharic language  text stemming for natural language processing(NLP) task
#Rrequires hornmorpho package available @https://github.com/hltdi/HornMorpho.git
#steps to use:
1. installation of hornmorpho(hm) 
1.1.  install using pip or manually download hornmorpho at@https://github.com/hltdi/HornMorpho.git
1.2.  if you manually download it, save the file in the same directory/path where your other packages are installed 
1.3.  change the name(Hornmorpho) into 'hm'
2. How to stem Amharic text/corpus   
2.1. open amharicStemmer.py or amharicStemmer.ipynb file, run it and then call 'amharicCorpusStemmer(text)' function 
     # example
   >> text=['ላለፉት ጥቂት ለማይባሉ', ' ወራት . 9 ', 'የክስ ቻርጅ የለ', ' በቃ ዘብጥያ ወደ ቤትህ ሂድ']#input text can be .xlsx, .txt or .csv file
   >>amharicCorpusStemmer(text)#returns stem of text
    # when you run u get the following output
   >> ['ለፋ ጥቂት ተባለ', 'ወር', 'ክስ ቻርጅ የለ', 'እቃ ዘብጥያ ወደ ቤት ሄደ']
2.2. write the following in you editetr.#NB the python file (amharicStemmer.py or amharicStemmer.ipynb) you download should be save in same directory
   >> from amharicStemmer import amharicCorpusStemmer
   >> text=[" put here the text to be stemmed/ስርዎ ቃሉን ልማግኘት ጽሁፍን አዚህ ያስገቡ"] #can be .xlsx, .txt or .csv file
   >> amharicCorpusStemmer(text)#returns stem for the argument text
