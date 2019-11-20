
#Bring in the source phrases to be the components of the teacher feedback.

from source_phrases import *
import re
import collections

NumberedPhrase = collections.namedtuple("NumberedPhrase",["string","number"])
Phrase = collections.namedtuple("NumberedPhrase",["string"])
VerbDeclension = collections.namedtuple("VerbDeclension",["singular","plural"])

#Initialise the temporary phrase sets. Temporary sets are used so that the originals are left untouched when elements are 'popped'.

metaphorTemp = metaphor.copy()
structureTemp = structure.copy()
punctuationTemp = punctuation.copy()
topicGoodTemp = topicGood.copy()
topicOKTemp = topicOK.copy()
topicPoorTemp = topicPoor.copy()
finalGoodTemp = finalGood.copy()
finalOKTemp = finalOK.copy()
finalPoorTemp = finalPoor.copy()
signoffGoodTemp = signoffGood.copy()
signoffOKTemp = signoffOK.copy()
signoffPoorTemp = signoffPoor.copy()
secondAndThirdSentenceConjTemp = secondAndThirdSentenceConj.copy()

#define needed classes and functions

NumberedPhrase = collections.namedtuple("NumberedPhrase",["string","number"])
Phrase = collections.namedtuple("NumberedPhrase",["string"])

def decline(string, number, dict):
    newString = string
    for key in dict:
        newString = newString.replace(key,dict[key][number])
    return newString
        
#Set up the phrase dictionaries.

topicDict = {'metaphor': metaphorTemp,'structure':structureTemp, 'punctuation':punctuationTemp}
topicLevelsDict = {0:topicPoorTemp, 1:topicOKTemp, 2:topicGoodTemp}
finalLevelsDict = {0:finalPoorTemp, 1:finalOKTemp, 2:finalGoodTemp}
signoffLevelsDict = {0:signoffPoorTemp, 1:signoffOKTemp, 2:signoffGoodTemp}

print('\nENGLISH SUBMISSION FEEDBACK GENERATOR\n\nFirst submission:\n')

q = True

while q:

#Get the teacher to input the topic marks. Calculate the aggregate mark.

    metaphorScore = int(input("Please score use of metaphor on a scale of 1 to 3: "))-1
    structureScore = int(input("Please score use of structure on a scale of 1 to 3: "))-1
    punctuationScore = int(input("Please score use of punctuation on a scale of 1 to 3: "))-1
    aggregateScore = metaphorScore + structureScore + punctuationScore

#Order the three topics in the output paragraph so that the lowest-rated topic is in the middle and the highest-rated is at the end.

    topicOrder = [('metaphor',metaphorScore),('structure',structureScore),('punctuation',punctuationScore)]

    topicOrder.sort(key = lambda tup: tup[1])

    topicOrder[0],topicOrder[1] = topicOrder[1],topicOrder[0]

#First topic sentence creation

#Replenish 1

    if topicDict[topicOrder[0][0]] == set():
        topic = topicOrder[0][0]
        if topic == 'metaphor':
            metaphorTemp = metaphor.copy()
        elif topic == 'structure':
            structureTemp = structure.copy()
        else:
            punctuationTemp = punctuation.copy()

        topicDict = {'metaphor': metaphorTemp,'structure':structureTemp, 'punctuation':punctuationTemp}

    firstTopicPhraseObj = topicDict[topicOrder[0][0]].pop()

    firstTopicPhrase = firstTopicPhraseObj.string

#Replenish 2

    if topicLevelsDict[(topicOrder[0][1])] == set():
        topicLevel = topicOrder[0][1]
        if topicLevel == 0:
            topicPoorTemp = topicPoor.copy()
        elif topicLevel == 1:
            topicOKTemp = topicOK.copy()
        else:
            topicGoodTemp = topicGood.copy()

        topicLevelsDict = {0:topicPoorTemp, 1:topicOKTemp, 2:topicGoodTemp}

    firstScorePhrase = topicLevelsDict[topicOrder[0][1]].pop().string

    firstTopicSentenceProto = firstScorePhrase.replace('$',firstTopicPhrase)
    firstTopicSentenceProto2 = decline(firstTopicSentenceProto,firstTopicPhraseObj.number,verbDict)


#Second topic sentence creation

#Replenish 3

    if topicDict[topicOrder[1][0]] == set():
        topic = topicOrder[1][0]
        if topic == 'metaphor':
            metaphorTemp = metaphor.copy()
        elif topic == 'structure':
            structureTemp = structure.copy()
        else:
            punctuationTemp = punctuation.copy()

        topicDict = {'metaphor': metaphorTemp,'structure':structureTemp, 'punctuation':punctuationTemp}

    secondTopicPhraseObj = topicDict[topicOrder[1][0]].pop()

    secondTopicPhrase = secondTopicPhraseObj.string

#Replenish 4

    if topicLevelsDict[(topicOrder[1][1])] == set():
        topicLevel = topicOrder[1][1]
        if topicLevel == 0:
            topicPoorTemp = topicPoor.copy()
        elif topicLevel == 1:
            topicOKTemp = topicOK.copy()
        else:
            topicGoodTemp = topicGood.copy()

        topicLevelsDict = {0:topicPoorTemp, 1:topicOKTemp, 2:topicGoodTemp}

    secondScorePhrase = topicLevelsDict[(topicOrder[1][1])].pop().string

    secondTopicSentenceProto = secondScorePhrase.replace('$',secondTopicPhrase)
    secondTopicSentenceProto2 = decline(secondTopicSentenceProto,secondTopicPhraseObj.number,verbDict)


#Third topic sentence creation

#Replenish 5

    if topicDict[topicOrder[2][0]] == set():
        topic = topicOrder[2][0]
        if topic == 'metaphor':
            metaphorTemp = metaphor.copy()
        elif topic == 'structure':
            structureTemp = structure.copy()
        else:
            punctuationTemp = punctuation.copy()

        topicDict = {'metaphor': metaphorTemp,'structure':structureTemp, 'punctuation':punctuationTemp}

    thirdTopicPhraseObj = topicDict[topicOrder[2][0]].pop()

    thirdTopicPhrase = thirdTopicPhraseObj.string

#Replenish 6

    if topicLevelsDict[(topicOrder[2][1])] == set():
        topicLevel = topicOrder[2][1]
        if topicLevel == 0:
            topicPoorTemp = topicPoor.copy()
        elif topicLevel == 1:
            topicOKTemp = topicOK.copy()
        else:
            topicGoodTemp = topicGood.copy()
            
        topicLevelsDict = {0:topicPoorTemp, 1:topicOKTemp, 2:topicGoodTemp}


    thirdScorePhrase = topicLevelsDict[(topicOrder[2][1])].pop().string

    thirdTopicSentenceProto = thirdScorePhrase.replace('$',thirdTopicPhrase)
    thirdTopicSentenceProto2 = decline(thirdTopicSentenceProto,thirdTopicPhraseObj.number,verbDict)


#Combining the topic sentences

    if ((topicOrder[0][1] > topicOrder[1][1]) and (topicOrder[1][1] == 0)) :
        paragraphProto = firstTopicSentenceProto2.capitalize() + ', but ' + secondTopicSentenceProto2 + '. '

    else:
        paragraphProto = firstTopicSentenceProto2.capitalize() + '. ' + secondTopicSentenceProto2.capitalize() + '. '

    if ((topicOrder[1][1] < topicOrder[2][1]) and (topicOrder[1][1] == 0)) :

#Replenish 7

        if secondAndThirdSentenceConjTemp == set():
            secondAndThirdSentenceConjTemp = secondAndThirdSentenceConj.copy()

        conj2and3 = secondAndThirdSentenceConjTemp.pop().string
        
        if conj2and3 == ' though':
            paragraphProto = paragraphProto + thirdTopicSentenceProto2.capitalize() + ' though' + '. '

        elif conj2and3 == ', however':
            paragraphProto = paragraphProto + thirdTopicSentenceProto2.capitalize() + ', however' + '. '

        else:
            paragraphProto = paragraphProto + 'However, ' + thirdTopicSentenceProto2 + '. '

    else:
        
        paragraphProto = paragraphProto + thirdTopicSentenceProto2.capitalize() + '. '

#Final sentence creation

    if ((aggregateScore == 0) or (aggregateScore == 1)):

#Replenish 8

        if finalLevelsDict[0] == set():
            finalPoorTemp = finalPoor.copy()

            finalLevelsDict = {0:finalPoorTemp, 1:finalOKTemp, 2:finalGoodTemp}
        
        finalSentenceProto = finalLevelsDict[0].pop().string

    elif ((aggregateScore == 2) or (aggregateScore == 3) or (aggregateScore == 4)):

#Replenish 9

        if finalLevelsDict[1] == set():
            finalOKTemp = finalOK.copy()

            finalLevelsDict = {0:finalPoorTemp, 1:finalOKTemp, 2:finalGoodTemp}

        finalSentenceProto = finalLevelsDict[1].pop().string
        
    else:

#Replenish 10

        if finalLevelsDict[2] == set():
            finalGoodTemp = finalGood.copy()

            finalLevelsDict = {0:finalPoorTemp, 1:finalOKTemp, 2:finalGoodTemp}
            
        finalSentenceProto = finalLevelsDict[2].pop().string

    finalSentence = finalSentenceProto.capitalize()+'. '

#Signoff creation

    if ((aggregateScore == 0) or (aggregateScore == 1)):

#Replenish 11

        if signoffLevelsDict[0] == set():
            signoffPoorTemp = signoffPoor.copy()

            signoffLevelsDict = {0:signoffPoorTemp, 1:signoffOKTemp, 2:signoffGoodTemp}

        signoffProto = signoffLevelsDict[0].pop().string


    elif ((aggregateScore == 2) or (aggregateScore == 3) or (aggregateScore == 4)):

#Replenish 12

        if signoffLevelsDict[1] == set():
            signoffOKTemp = signoffOK.copy()

            signoffLevelsDict = {0:signoffPoorTemp, 1:signoffOKTemp, 2:signoffGoodTemp}

        signoffProto = signoffLevelsDict[1].pop().string

        
    else:

#Replenish 13

        if signoffLevelsDict[2] == set():
            signoffGoodTemp = signoffGood.copy()

            signoffLevelsDict = {0:signoffPoorTemp, 1:signoffOKTemp, 2:signoffGoodTemp}

        signoffProto = signoffLevelsDict[2].pop().string

    signoff = signoffProto.capitalize()

#Result and rerun

    paragraph = paragraphProto + finalSentence + signoff
    print('\n' + paragraph)
    print('\n')
    cont = input('Another submission? (y/n): ')
    q = (cont == 'y')






