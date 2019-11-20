import collections

NumberedPhrase = collections.namedtuple("NumberedPhrase",["string","number"])
Phrase = collections.namedtuple("NumberedPhrase",["string"])

metaphor = {
NumberedPhrase(string = 'how you use metaphor', number = 'singular'),
NumberedPhrase(string = 'your use of metaphor', number = 'singular'),
NumberedPhrase(string = 'how you employ metaphor', number = 'singular'),
NumberedPhrase(string = 'how you use metaphorical language', number = 'singular'),
NumberedPhrase(string = 'your metaphorical language', number = 'singular'),
NumberedPhrase(string = 'your metaphorical imagery', number = 'singular'),
NumberedPhrase(string = 'the metaphorical imagery in your piece', number = 'singular'),
NumberedPhrase(string = 'the metaphorical imagery in your writing', number = 'singular'),
NumberedPhrase(string = 'your metaphors', number = 'plural'),
NumberedPhrase(string = 'how you use metaphor', number = 'singular'),
NumberedPhrase(string = 'the metaphorical associations you use', number = 'plural')
}

structure = {
NumberedPhrase(string = 'the structure of your piece', number = 'singular'),
NumberedPhrase(string = 'how you employ structure', number = 'singular'),
NumberedPhrase(string = 'how you use structure', number = 'singular'),
NumberedPhrase(string = 'your use of structure', number = 'singular'),
NumberedPhrase(string = 'the structure of your writing', number = 'singular'),
NumberedPhrase(string = 'your structural framework', number = 'singular'),
NumberedPhrase(string = 'your structural plan', number = 'singular')
}

punctuation = {
NumberedPhrase(string = 'the accuracy of your punctuation', number = 'singular'),
NumberedPhrase(string = 'the pattern of your punctuation', number = 'singular'),
NumberedPhrase(string = 'how you use punctuation', number = 'singular'),
NumberedPhrase(string = 'how you employ punctuation', number = 'singular'),
NumberedPhrase(string = 'the appropriateness of your punctuation', number = 'singular'),
NumberedPhrase(string = 'the punctuation in your piece', number = 'singular'),
NumberedPhrase(string = 'your punctuation style', number = 'singular')
}

topicGood = {
Phrase(string = '$ is superb'),
Phrase(string = 'I was impressed by $'),
Phrase(string = '$ is impressive'),
Phrase(string = '$ is excellent'),
Phrase(string = '$ is strong'),
Phrase(string = '$ is fully fit for purpose'),
Phrase(string = 'I really liked $'),
Phrase(string = 'I was impressed by $')
}

topicOK = {
Phrase(string = '$ is of an acceptable standard'),
Phrase(string = '$ is satisfactory'),
Phrase(string = '$ is fairly good'),
Phrase(string = '$ is moderately good'),
Phrase(string = '$ is OK'),
Phrase(string = '$ is average'),
Phrase(string = '$ shows room for improvement'),
Phrase(string = '$ is reasonable'),
Phrase(string = '$ is good (though could be better)'),
Phrase(string = 'I feel that $ is fair')
}

topicPoor = {
Phrase(string = '$ does not yet reach a satisfactory standard'),
Phrase(string = 'you may need some help with $'),
Phrase(string = '$ requires a lot more work'),
Phrase(string = 'I would suggest you give much more attention to $'),
Phrase(string = '$ sadly fell short'),
Phrase(string = '$ is weak')
}

finalGood = {
Phrase(string = 'fantastic effort'),
Phrase(string = 'this made me proud'),
Phrase(string = 'this was a great effort'),
Phrase(string = 'this piece is outstanding'),
Phrase(string = 'top quality'),
Phrase(string = 'this piece shows your talent')
}

finalOK = {
Phrase(string = 'a good try'),
Phrase(string = 'a reasonable showing'),
Phrase(string = 'overall your work is satisfactory'),
Phrase(string = 'a moderately good attempt'),
Phrase(string = 'a good effort'),
Phrase(string = 'a fairly good attempt'),
Phrase(string = 'a reasonable attempt'),
Phrase(string = 'your writing is of a reasonable standard'),
Phrase(string = 'this piece is fairly good'),
Phrase(string = 'your work shows some promise')
}

finalPoor = { 
Phrase(string = 'you are struggling here'),
Phrase(string = 'a weak performance overall'),
Phrase(string = 'unfortunately this missed the mark'),
Phrase(string = 'overall sadly disappointing'),
Phrase(string = 'this doesn\t show your true potential'),
Phrase(string = 'your real capability is not in evidence here')
}

signoffGood = {
Phrase(string = 'don’t rest on your laurels, though!'),
Phrase(string = 'gimme more!'),
Phrase(string = 'no problem in doing well in the exam…if you don’t slack off!'),
Phrase(string = 'keep up the good work!'),
Phrase(string = 'lovin\' it!'),
Phrase(string = 'Wonderful!')
}

signoffOK = {
Phrase(string = 'crack on with your efforts!'),
Phrase(string = 'more work will yield beneficial results.'),
Phrase(string = 'keep working on the weaker areas.'),
Phrase(string = 'keep at it!'),
Phrase(string = 'keep up the focus!'),
Phrase(string = 'keep up the energy and you will improve.'),
Phrase(string = 'work to make the most of your potential.'),
Phrase(string = 'polish up the weaker areas and you will do well.'),
Phrase(string = 'good expectations for your exam if you work hard.'),
Phrase(string = 'I am hopeful for a good result in your exam but you will need to put in some effort.')
}

signoffPoor = {
Phrase(string = 'more work is required; please see me if you need help.'),
Phrase(string = 'please allow me to assist if you would like.'),
Phrase(string = 'please review the topics we have covered.'),
Phrase(string = 'Please have a chat with me so that we can remove some of the mental blocks, OK?'),
Phrase(string = 'passing your exam is in jeopardy: please see me.'),
Phrase(string = 'Let\s work together and see if we can remedy the situation.')
}

verbDict = {'is': {'singular':'is', 'plural':'are'},
            'does': {'singular':'does', 'plural':'do'},
            'shows': {'singular':'shows', 'plural':'show'},
            'requires': {'singular':'requires', 'plural':'require'}
}

secondAndThirdSentenceConj = {Phrase(string = ' though'),Phrase(string = ', however'), Phrase(string = 'However, ')}
    






