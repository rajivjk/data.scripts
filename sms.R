require(graphics) 
rm(list=ls())
library(ggplot2)
library(scales)
library(reshape)



#get the rawfile from github
#Step 1: create a tempfile call it "datafile"
#Step 2: download the file
#Step 3: read the file into a R dataframe

datafile <- tempfile()
download.file('https://raw.github.com/rajivjk/data.scripts/master/sms.csv', destfile=datafile,method='curl')
data <- read.csv(datafile,header=FALSE)


#the raw data doesn't have headers, so lets add that.
#names(data) <- c("sender", "receiver", "num.texts")



