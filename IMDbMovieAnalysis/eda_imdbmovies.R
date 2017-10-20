rm(list = ls())

#Laoding some important libraries for graphical visualisation
library(ggplot2)
library(dplyr)
library(plotly)
library(data.table)
library(gridExtra)
library(magrittr)
library(formattable)

#Setting working directory
setwd("C:/Users/Bala Vineeth/Desktop/movie_metadata")
getwd()

#Reading and loading the data set located on a local computer
movie_table <- read.csv("movie_metadata.csv",header=T,stringsAsFactors = F)
attach(movie_table)

#Giving details of the movie present in the Dataset
str(movie_table)
dim(movie_table)

#Correlaion between the variables 
numericColumns <- sapply(movie_table, is.numeric)
corMatrix<-cor(movie_table[,numericColumns])
corMatrix

#Calculating Average IMDb rating by year relationship
#temp <- movie_table %>% select(imdb_score,title_year)
#temp <- temp %>% group_by(title_year)%>% summarise(score=mean(imdb_score))
#temp <- na.omit(temp)
#p <- plot_ly(temp, x = title_year, y = score, name = "Avg Score by Year")
#p %>%
#  add_trace(y = fitted(loess(score ~ as.numeric(title_year))), x = title_year) %>%
#  layout(title = "Year and Score", showlegend = FALSE) %>%
#  dplyr::filter(score == max(score)) %>%
#  layout(annotations = list(x = title_year, y = score, text = "Peak", showarrow = T))


#IMDb scores vs Content type
imdbscore_content <- movie_table %>% select(imdb_score,content_rating)
imdbscore_content <- na.omit(imdbscore_content)
plot_ly(imdbscore_content, x = imdb_score, color = content_rating, type = "box")


#p <- ggplot(data = movie_table, aes(x = as.numeric(title_year), y = imdb_score)) +
#  geom_point(aes(text = paste("Clarity:", clarity))) +
#  geom_smooth(aes(colour = cut, fill = cut)) + facet_wrap(~ cut)

#ggplotly(p)

