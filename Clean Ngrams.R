## Code for cleaning and generating the English bigram data contained in ngrams2
setwd("~/GitHub/Whatlanguage")
library("dplyr")
twograms <- tbl_df(read.csv(file = "ngrams2.csv"))
twograms <- twograms %>%
  select(X2.gram, X...)
total <- sum(twograms$X...)
twograms <- mutate(twograms, 
                   frequency = X.../total)
write.csv(twograms, "2gram_frequency.csv")