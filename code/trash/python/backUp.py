########################################################################################
#wait for the name of the soul to be invoked and search it using the GOOGLE SEARCH API
countSoulName = 0
print "////////////////////////////////////////////////////"
soulName = raw_input ( 'Type the name of the soul: ' )
print "////////////////////////////////////////////////////"
soulName = urllib.urlencode ( { 'q' : soulName } )
response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + soulName ).read()
jsonSoulName = m_json.loads ( response )
results = jsonSoulName [ 'responseData' ] [ 'results' ]
for result in results:
    url = result['url']   # for every url object count +1
    countSoulName = countSoulName + 1

#Check is nothing was found...
if countSoulName == 0:
	print "THE SOUL IS NOT AVAILABLE"
else:
	print "HELLO IM HERE"

########################################################################################
#Wait for a question, word, etc from the user...
countQuestion = 0
print "////////////////////////////////////////////////////"
question = raw_input ('say something: ')
print "////////////////////////////////////////////////////"
question = urllib.urlencode ({ 'q' : question })
response = urllib.urlopen ('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + soulName + ' ' + question).read()
jsonQuestion = m_json.loads (response)
results = jsonQuestion ['responseData'] ['results']
for result in results:
    title = result['title'] #get the title of the search result
    content = result['content'] #get the content of the link
    url = result['url']   # URL
    #print (title + '; ' + content + '; ' + url ) #multiple prints
    print (content)
    countQuestion = countQuestion + 1

#Check is nothing was found...
if countQuestion == 0:
	print "NO ANSWER"
else: #if there is a response.... the board's pointer must move char by char
	print "THIS IS MY ANSWER"

########################################################################################
