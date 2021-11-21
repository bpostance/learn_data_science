import spacy
import neuralcoref #
nlp = spacy.load('en_core_web_lg')


neuralcoref.add_to_pipe(nlp)

# You're done. You can now use NeuralCoref as you usually manipulate a SpaCy document annotations.
doc = nlp(u'My sister has a dog. She loves him.')

print(doc._.has_coref)
print(doc._.coref_clusters)