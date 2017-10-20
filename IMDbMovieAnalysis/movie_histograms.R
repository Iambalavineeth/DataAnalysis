rm(list = ls())

library(ggplot2)
library(dplyr)
library(GGally)
library(memisc)
library(gridExtra)
library(ellipse)

#Setting working directory
setwd("C:/Users/Bala Vineeth/Desktop/movie_metadata")
getwd()

#Reading and loading the data set located on a local computer
movie_table <- read.csv("movie_metadata.csv",header=T,stringsAsFactors = F)
attach(movie_table)

#Histogram - imdb_score vs count
ggplot(data=movie_table,aes(x = imdb_score))+geom_histogram(binwidth=0.1)

#Histogram - title_year vs count
ggplot(data=movie_table,aes(x = title_year))+geom_histogram(binwidth = 1)