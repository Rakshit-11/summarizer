import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest


def summarize(text, num_sentences):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]
    
    # Create a frequency distribution of the words
    freq_dist = nltk.FreqDist(words)
    
    # Calculate the score for each sentence
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in freq_dist:
                if len(sentence.split(' ')) < 30:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = freq_dist[word]
                    else:
                        sentence_scores[sentence] += freq_dist[word]
    
    # Get the top N sentences with the highest score
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    
    # Combine the summary sentences into a summary
    summary = ''.join(summary_sentences)
    
    return summary
