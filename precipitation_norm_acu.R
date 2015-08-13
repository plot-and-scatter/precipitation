setwd("~/Dropbox/dev/plot-and-scatter/R_precipitation") ##Set working directory
data<- read.csv("precipitation_data.csv", header = TRUE) ## Open file, and set as 'data'

yr2010<-data[1:12,] ##Subset for 2010
annual_mean10<-sapply(yr2010[,2:73], mean) ## Calculate annual mean for each station's actual and normal precipitation.

yr2011<-data[13:24,] ##Subset for 2011
annual_mean11<-sapply(yr2011[,2:73], mean) ## Calculate annual mean for each station's actual and normal precipitation.

yr2012<-data[25:36,] ##Subset for 2012
annual_mean12<-sapply(yr2012[,2:73], mean) ## Calculate annual mean for each station's actual and normal precipitation.

yr2013<-data[37:48,] ##Subset for 2012
annual_mean13<-sapply(yr2013[,2:73], mean) ## Calculate annual mean for each station's actual and normal precipitation.

yr2014<-data[49:60,] ##Subset for 2012
annual_mean14<-sapply(yr2014[,2:73], mean) ## Calculate annual mean for each station's actual and normal precipitation.

yrmean.data<- data.frame(annual_mean10, annual_mean11, annual_mean12, annual_mean13, annual_mean14) #create a new data frame with annual means
yrmean.dec<-print(yrmean.data, digits=4) # print new data frame with only 2 decimals. 
##Note this creates a new data frame but doesn't print the data frame in 2 decimals. Must print separately.
write.table(yrmean.dec, file = "annual_means.csv", sep = ",", col.names = NA) ## write data frame to csv file


