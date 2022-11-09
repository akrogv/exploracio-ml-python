Intro to Recommender Systems


- Content Based: recommendations based on user preferences for product features, identified by user’s previous actions. (High level).

- Collaborative filtering-based: user-item interactions across a population of users in order to make recommendations for one particular user, based on the preferences of other similar users.  These systems tend to utilize historical user-item interaction.

Both systems rely on historical interactions.
But a user’s choice of items not only depends on long-term historical preference, but also on short-term and recent preferences.
This consideration has prompted the exploration of new algorithms known as session-based recommendation algorithms.
Specially advantageous because a user can appear anonymously.

![imatge](https://user-images.githubusercontent.com/62561223/200885398-4c670503-04fc-49db-b45d-4d70fa842f97.png)

Rhonda’s browsing history in one session. 

Multiple user interactions that happen in a period of time.
What product within the session will Rhonda click on? This is called Next Event Prediction (NEP)

Modeling Session-based Recommenders:

Simplest and most common: recommend the item that most frequently co-occurs with the last item in the session. —> “Association Rules”.

Approach fet servir: word2vec (neural network with a single layer). 
2 versions —> Skip-gram & CBOW

![imatge](https://user-images.githubusercontent.com/62561223/200885315-fce5f5df-53fe-409b-8002-2bd66734eaf5.png)

Més info sobre skip-gram de word2vec:
https://gruizdevilla.medium.com/introducci%C3%B3n-a-word2vec-skip-gram-model-4800f72c871f

Continuar...
