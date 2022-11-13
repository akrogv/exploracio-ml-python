# Initial Preprocessing

## Introduction & Context
During our research of cool use-cases that were aprochable from our end, we stumbled upon a kaggle competition featuring session-based recommendations from an e-comerce data source. We decided to take on this problem though it may be difficult to obtain remarkable results because given its difficulty it can be of great help in order to improve our understanding about the python ecosystem and the tools and techniques used to process data in these scenarios.

## Objectives
For our initial exploration, we aim to gather information about the dataset that can help us to process and model it better, we hope to keep improving iteratively in that regard.
1. Obtain a concrete vision on the aproach the problem requires
2. Create a methodology that allows us to work with the data somewhat quickly given its size by sampling the data.
3. Identify features or other meaningful insight about the data that may help with the first objective.

## Dataset 
Until now, the data consisted of a *jsonl* file in which there were 256M events grouped in sessions (12M). The format of the data made it so that it was a bit cumbersome to read and work with because it was nested and it occupied a lot of system memory. That is why the first task we worked on was to extract the data into a more usable format, in this case we chose parquet.

Right now, the data is presented as directory that contains over 40 parquet files that we read with *Apache Arrow* in order to obtain a pandas dataset.

### Data Schema
| ColumnName | ColumnType | Comment |
|------------|------------|---------|
| SessionId  | integer    | Session identifier |
| aid        | integer    | Product identifier |
| type       | string     | Category of the event |
| ts         | datetime   | Timestamp representing the moment the event occurs|

## Business Understanding
### Session Based Recommendation Systems - E-Comerce
- **Problem Target:** Generate up to 20 product recommendations for each event type given a session.

### Initial Insights
Taking into account that the data comes from an online store, we have to acknowledge that some products may be more popular than others, and that may be affected by time of the year, day,...

Also, the population being monitored can vary greatly in their behavior, but we believe certain patterns may appear once a large number of events/sessions are analyzed. That is why we will try to engineer features about the likelyhood of certain products being close to one another in the time dimension.

Within a given session, behavioral patterns may also appear when talking about different event types, such as clicking a product that later you will put on the cart.

We want to introduce the concept of a sub-session, which is the group of events linked by being close together in the time dimension. It will be useful to create a context window for the model to use.

Within the sub-session we theoryze that the proportion of 'click' events may be greater at the start followed by an increase in 'cart' and/or 'order' events. Also we want to answer if there are products more likely to be bought at the start or at the end of the sub-session.

We would like to assess if depending on the lenght of the sub-sessions and the number of sub-sessions in a session some products may be more likely to be part of an event. This last insight also points to the relation the proportion of different event types might have with the length of a subsession.

Another valid exploration path would be to try to extract the relation within products and event types, we think that there might be products that almost never are ordered even though they are clicked often and viceversa.

### Initial Queries

- We want to answer if its possible for a product to appear in any event type other than a 'click'.

- We want to know about wether its possible to use techniques from the NLP domain like word2vec to model the input sequence of events from a session.

## Data Understanding
- **Session:** Events recorded for a single user in the period of time during which the data collection took place.
- **aid:** Represents a unique product identifier from the store. 
- **click:** Type of event performed by the user, refers to a click on the website store, has an associated product and timestamp.
- **cart:** Type of event performed by the user, represents the action of putting an item in the cart on the online shop, has an associated product and timestamp.
- **order:** Type of event performed by the user, this refers to when a sale is made, has an associated product and timestamp.
  

## Data Preparation

