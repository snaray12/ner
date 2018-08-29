# training data
TRAIN_DATA = [
    (u'The food is very good', {
        'entities':[(4,8, 'FD')]
    }),
    (u'The service is very good', {
        'entities':[(4,11, 'SER')]
    }),
    (u'the service was terrible', {
        'entities':[(4,11, 'SER')]
    }),
    (u'because of the poor service, I am', {
        'entities':[(20,27, 'SER')]
    }),
    (u'The room had a sea facing view', {
        'entities': [(15,30, 'RV'), (4,8,'RA')]
    }),
    (u'The room was facing towards garden',{
        'entities':[(13,34, 'RV'),(4,8,'RA')]
    }),
    (u'The room had a city view',{
        'entities':[(15,24,'RV'),(4,8,'RA')]
    }),
    (u'Deserts were very good',{
        'entities':[(0,7,'FD')]
    })
]
