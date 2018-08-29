#!/usr/bin/python
# -*- coding: utf-8 -*-

import spacy



if __name__ == "__main__":
	nlp = spacy.load("./model")
	text = u"The room had a sea view. The food was very good, but it took over half an hour to be seated,... \
			and the service was terrible. The room was very noisy and cold wind blew \
			in from a curtain next to our table. Deserts were very good, but because of \
			[the] poor service, I’m not sure we’ll ever go back!"

	doc = nlp(text)
	print 'Entities', [(ent.text, ent.label_) for ent in doc.ents]
	print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])