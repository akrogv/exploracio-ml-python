The goal of this competition is to predict e-commerce clicks, cart additions, and orders. You'll build a multi-objective recommender system based on previous events in a user session.
Your work will help improve the shopping experience for everyone involved. Customers will receive more tailored recommendations while online retailers may increase their sales.

## Dataset information
Realistic ecommerce dataset
https://github.com/otto-de/recsys-dataset
https://www.kaggle.com/competitions/otto-recommender-system/discussion/363973

    train.jsonl - the training data, which contains full session data
        session - the unique session id
        events - the time ordered sequence of events in the session
            aid - the article id (product code) of the associated event
            ts - the Unix timestamp of the event
            type - the event type, i.e., whether a product was clicked, added to the user's cart, or ordered during the session
    test.jsonl - the test data, which contains truncated session data
        your task is to predict the next aid clicked after the session truncation, as well as the the remaining aids that are added to carts and orders; you may predict up to 20 values for each session type
    sample_submission.csv - a sample submission file in the correct format

## Difficulties & Timing
Good timing: 3 months to go. Active competition.

Kaggle Points :P

## Score
### **8.5/10**
