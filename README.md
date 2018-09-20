# DS-GoodNews
Data science and analysis for the Good News project

## Good News Project
The Good News Project is a news aggregator that uses machine learning to remove clickbait news articles. In a model where ad revenue is driven by clicks, some publisher's have chosen to maximize click rate instead of providing valuable news to the reader. With the Good News Project, users get informative and worthwhile news articles without limiting their range of news sources. 

## News Sources
The sources of the news articles

## Dataset
Dataset used to analyze clickbait articles and train the classifier


Article JSON format:
```json
{
	"id" : "<id>",
	"name": "<headline>",
	"url" : "<url>",
	"timestamp" : "<date time of publication>",
	"description" : "<description>",
	"keywords" : "<keywords>",
	"summary" : "<summary>",
	"content" : "<content>",
	"clickbait" : "<binary_classification>"
}
```
Except id, all these fields can be extracted with the newspaper library given the url.

## Analysis
Analysis of the clickbait dataset

## Classifier
The classifier used to determine whether an article is clickbait or not
