# DS-GoodNews
Data science and analysis for the Good News project

## Good News Project
The Good News Project is a news aggregator that uses machine learning to remove clickbait news articles. In a model where ad revenue is driven by clicks, some publisher's have chosen to maximize click rate instead of providing valuable news to the reader. With the Good News Project, users get informative and worthwhile news articles without limiting their range of news sources. 

## News Sources
The sources of the news articles

## Dataset
Dataset used to analyze clickbait articles and train the classifier

### JSON format
Article JSON format:<br />
{<br />
	"id" : "<id>",<br />
	"name": "<headline>",<br />
	"url" : "<url>",<br />
	"timestamp" : "<date time of publication>",<br />
	"description" : "<description>",<br />
	"keywords" : "<keywords>",<br />
	"summary" : "<summary>",<br />
	"content" : "<content>"<br />
}<br />
Except id, all these fields can be extracted with the newspaper library given the url.

## Analysis
Analysis of the clickbait dataset

## Classifier
The classifier used to determine whether an article is clickbait or not
