# IA_pig_or_dog
Machine learning algorithms for classification, estimators capable of analyzing data of an animal and claim to say it is a pig or dog.

In this my first Machine Learning and Classification algorithm, we will analyze 2 sets
different data, which we will try to classify
information in two distinct categories ie we will use
machine learning algorithms for classification, estimators capable of analyzing data
of an animal and be able to claim that it is a pig or dog.
These algorithms can also be used to classify items or predict
user behaviors when buying a product

We will do all of this using Python and the scikit-learn library, which has machine learning algorithms.

We have a table with several pictures of pigs and dogs, and we want to classify them.
For dogs, we will use the number 0, for pigs 1.


How can we make the machine learn what a pig is and differentiate it from a dog?

We will make an analogy with our own development as humans: we are usually introduced
to the animal several times and we learn by repetition.
We associate a sound with the animal, something like "oinc-oinc" for pigs, and highlight its main characteristics.
With the dog, it's no different.
We need someone to indicate this animal and teach us its classification, while this learning is supervised.
In short, we have a "teacher" who already knows what a pig or chachorro is.
A similar process will be done with the machine: we will pass on a set of data and supervise its learning
 so that animals are classified correctly. Next, we’ll display a new animal and see how
 the algorithm fits this animal into the categories available through estimators.
But how do we classify an animal between a dog or a pig? The idea is to use animal characteristics in this case, three.
 It is important to highlight that the more data we have in the training and learning phase,
 there is a tendency for the estimators' results to improve, although this is not a guarantee.
 
 
 
Let's look at the first specimen of pork:

1. there is a reasonably long hair 2. the legs are short 3.he does not emit the "au-au" sound.

Each animal will be described using these three characteristics:
if the hair is long or short;
whether the legs are long or short;
and whether the animal emits the "au-au" sound or not.

We have three features to assist us with this cataloging process and to train
the estimator so that he understands patterns. In the case of this pig, it has long hair,
then we will mark in the column "For the long?" the number 1 ("yes"). In the same way, we will mark the same
numbering in the "Short leg?" column, and 0 (no ") in the" Au Au? "column.

 
 
