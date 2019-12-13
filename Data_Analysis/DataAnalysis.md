---
title: "DataAnalysis"
output: 
  html_document:
    keep_md: true
---


```r
library(tidyverse)
```

```
## ── Attaching packages ────────────────────────────────────────────────────────────────────────────────── tidyverse 1.2.1 ──
```

```
## ✔ ggplot2 3.1.1       ✔ purrr   0.3.2  
## ✔ tibble  2.1.1       ✔ dplyr   0.8.0.1
## ✔ tidyr   0.8.3       ✔ stringr 1.4.0  
## ✔ readr   1.3.1       ✔ forcats 0.4.0
```

```
## ── Conflicts ───────────────────────────────────────────────────────────────────────────────────── tidyverse_conflicts() ──
## ✖ dplyr::filter() masks stats::filter()
## ✖ dplyr::lag()    masks stats::lag()
```

```r
library(readr)
library(tidyr)
```

# Load and Clean Data 

```r
Artists<-read.csv("~/Desktop/describing_your_data/Data/Data_Sets/artandfemWiki.csv")
Athletes<- read.csv("~/Desktop/describing_your_data/Data/Data_Sets/athletesWiki.csv")
Politicians <- read.csv("~/Desktop/describing_your_data/Data/Data_Sets/politicsWiki.csv")
Scientists <- read.csv("~/Desktop/describing_your_data/Data/Data_Sets/ScientistsWiki.csv")

# Add a column to each for their group 
Artists$type<-"Artists"
Athletes$type<-"Athletes"
Politicians$type <-"Politicians"
Scientists$type<-"Scientists"

# Add a column for Athletes and Politicans, so have consistent number of variables 
Athletes$New <- "N/A"
Politicians$New <- "N/A"

# Combine into one data set 
all_data<- rbind(Artists,Athletes,Politicians,Scientists)
```

# Descriptive Statistics 

**Number of articles per group** 

Table 1. Articles per Group, broken down by articles started by the groups and those edited by them. 


```r
all_data %>%
  count(type)
```

```
## # A tibble: 4 x 2
##   type            n
##   <chr>       <int>
## 1 Artists      2521
## 2 Athletes     3052
## 3 Politicians  1213
## 4 Scientists    971
```

```r
all_data %>%
  group_by(type)%>%
  count(New)
```

```
## # A tibble: 6 x 3
## # Groups:   type [4]
##   type        New       n
##   <chr>       <chr> <int>
## 1 Artists     FALSE  2196
## 2 Artists     TRUE    325
## 3 Athletes    N/A    3052
## 4 Politicians N/A    1213
## 5 Scientists  FALSE   806
## 6 Scientists  TRUE    165
```

**Length Statistics**

```r
all_data%>%
  group_by(type)%>%
  summarise(average=mean(length), median=median(length), max=max(length), min=min(length))
```

```
## # A tibble: 4 x 5
##   type        average median    max   min
##   <chr>         <dbl>  <dbl>  <dbl> <dbl>
## 1 Artists      13525.  8562  270338   474
## 2 Athletes     12420.  6810. 234437   769
## 3 Politicians  24631. 11350  410035   346
## 4 Scientists   14603.  8612  246113   161
```

```r
library(ggridges)
```

```
## 
## Attaching package: 'ggridges'
```

```
## The following object is masked from 'package:ggplot2':
## 
##     scale_discrete_manual
```

```r
figure1<-ggplot(all_data)+
  geom_density_ridges(aes(x=log(length), y=type, fill=type), quantile_lines=TRUE, quantiles=2, show.legend=FALSE)+ 
  ggtitle("Figure 1. Length of articles, by group")+ 
  scale_fill_manual(values=c("#254181","#138d75","#a2d9ce","#72b2f5"))+
  ylab(" ")+
  xlab("log of character count")


figure2<-ggplot()+
  geom_boxplot(data=Artists, aes(x=type, y=log(length), fill=New))+
  geom_boxplot(data=Scientists, aes(x=type, y=log(length), fill=New))+
  ggtitle("Figure 2. Length of Newly Created and Edited Articles for Intervention Groups ")+
  ylab("log of character count")+
  xlab(" ")+
  scale_fill_manual(name = " ", labels = c("Existing Articles", "Newly Created"), values=c("#673990","#e7dbf2"))+
  theme_minimal()

figure1
```

```
## Picking joint bandwidth of 0.195
```

![](DataAnalysis_files/figure-html/unnamed-chunk-4-1.png)<!-- -->

```r
figure2
```

![](DataAnalysis_files/figure-html/unnamed-chunk-4-2.png)<!-- -->

```r
length_New<-all_data%>%
  group_by(type, New)%>%
  summarise(median(length), mean(length))

length_New
```

```
## # A tibble: 6 x 4
## # Groups:   type [4]
##   type        New   `median(length)` `mean(length)`
##   <chr>       <chr>            <dbl>          <dbl>
## 1 Artists     FALSE            9338          14647.
## 2 Artists     TRUE             4946           5946.
## 3 Athletes    N/A              6810.         12420.
## 4 Politicians N/A             11350          24631.
## 5 Scientists  FALSE            9613          16091.
## 6 Scientists  TRUE             4848           7333.
```

**Wikilinks Statistics** 


```r
Artists_Net<-read.csv("~/Desktop/describing_your_data/Data/Wikilinks_Networks/ArtistsNet.csv")
Athletes_Net<- read.csv("~/Desktop/describing_your_data/Data/Wikilinks_Networks/AthletesNet.csv")
Politicians_Net<- read.csv("~/Desktop/describing_your_data/Data/Wikilinks_Networks/PoliticiansNet.csv")
Scientists_Net<- read.csv("~/Desktop/describing_your_data/Data/Wikilinks_Networks/ScientistsNet.csv")

Artists_Neta<-Artists_Net %>%
  group_by(Source)%>%
  summarise(num_of_links=n_distinct(Destination)) 

Athletes_Neta<-Athletes_Net %>%
  group_by(Source)%>%
  summarise(num_of_links=n_distinct(Destination))

Politicians_Neta<- Politicians_Net %>%
  group_by(Source)%>%
  summarise(num_of_links=n_distinct(Destination))
  
Scientists_Neta<- Scientists_Net %>%
  group_by(Source)%>%
  summarise(num_of_links=n_distinct(Destination))


mean(Artists_Neta$num_of_links)
```

```
## [1] 72.98282
```

```r
mean(Athletes_Neta$num_of_links)
```

```
## [1] 142.2551
```

```r
mean(Politicians_Neta$num_of_links)
```

```
## [1] 271.4734
```

```r
mean(Scientists_Neta$num_of_links)
```

```
## [1] 101.0643
```

```r
median(Artists_Neta$num_of_links)
```

```
## [1] 33
```

```r
median(Athletes_Neta$num_of_links)
```

```
## [1] 80
```

```r
median(Politicians_Neta$num_of_links)
```

```
## [1] 157
```

```r
median(Scientists_Neta$num_of_links)
```

```
## [1] 45
```

```r
colnames(Artists_Neta)[colnames(Artists_Neta) == 'Source'] <- 'title'
colnames(Athletes_Neta)[colnames(Athletes_Neta) == 'Source'] <- 'title'
colnames(Politicians_Neta)[colnames(Politicians_Neta) == 'Source'] <- 'title'
colnames(Scientists_Neta)[colnames(Scientists_Neta) == 'Source'] <- 'title'

all_nets <- rbind(Artists_Neta, Athletes_Neta, Politicians_Neta, Scientists_Neta)
all_data_net<- merge(all_data, all_nets, by="title")

figure3<-ggplot(all_data_net, aes(x=length, y=num_of_links, color=type))+
  geom_point()+
  geom_smooth(aes(method="lm", se=FALSE))+
  scale_color_manual(values=c("#254181","#138d75","#a2d9ce","#72b2f5"))+
  ggtitle("Figure 3. Relationship of Wikilinks and length, per group ")+
  xlab("Character count")+
  ylab("Count of Wikilinks")+
  theme_minimal()
```

```
## Warning: Ignoring unknown aesthetics: method, se
```

```r
figure3
```

```
## `geom_smooth()` using method = 'gam' and formula 'y ~ s(x, bs = "cs")'
```

![](DataAnalysis_files/figure-html/unnamed-chunk-5-1.png)<!-- -->

**Infobox Statistics** 

```r
infobox_report<-all_data%>%
  group_by(type)%>%
  summarise(total=length(infobox),no_info=length(infobox)-length(unique(infobox)))

infobox_report
```

```
## # A tibble: 4 x 3
##   type        total no_info
##   <chr>       <int>   <int>
## 1 Artists      2521     942
## 2 Athletes     3052     389
## 3 Politicians  1213     105
## 4 Scientists    971     296
```

```r
infobox_report_long<-gather(infobox_report, Info, N, total:no_info, factor_key=TRUE)
infobox_report_long
```

```
## # A tibble: 8 x 3
##   type        Info        N
##   <chr>       <fct>   <int>
## 1 Artists     total    2521
## 2 Athletes    total    3052
## 3 Politicians total    1213
## 4 Scientists  total     971
## 5 Artists     no_info   942
## 6 Athletes    no_info   389
## 7 Politicians no_info   105
## 8 Scientists  no_info   296
```

```r
figure4<-ggplot(data=infobox_report_long)+
  geom_col(aes(x=type,y=N, fill=Info), position="dodge", show.legend=TRUE)+
  scale_fill_manual(values=c("#673990", "#d2b4de"), labels=c("Total Articles", "No InfoBox"))+
  ggtitle("Figure 4. Proportion of Articles Without Infoboxes within each group")+
  ylab("Number of Articles")+
  xlab(" ")+
  theme_minimal()
      
figure4
```

![](DataAnalysis_files/figure-html/unnamed-chunk-6-1.png)<!-- -->


**Average number of editors**

```r
editors<-all_data%>%
  group_by(type) %>%
  summarise(average=mean(editorcount), median=median(editorcount), max=max(editorcount), min=min(editorcount))

editors
```

```
## # A tibble: 4 x 5
##   type        average median   max   min
##   <chr>         <dbl>  <dbl> <dbl> <dbl>
## 1 Artists        99.7     30  3137     2
## 2 Athletes       81.4     43  2037     1
## 3 Politicians   214.      78  3419     1
## 4 Scientists    116.      23  2325     1
```

**Average number of pageviewss**

```r
pageviews<-all_data%>%
  group_by(type) %>%
  summarise(average=mean(aveviews), median=median(aveviews), max=max(aveviews), min=min(aveviews))
```

**Pageview and Editor Plots** 

```r
figure5<-ggplot(data=all_data) +
  geom_boxplot(aes(x=type, y=log(aveviews), fill=type), show.legend=FALSE)+
  scale_fill_manual(values=c("#254181","#138d75","#a2d9ce","#72b2f5"))+
  theme_minimal()+
  xlab("")+
  ylab("Count of daily pageviews, logarithmic scale")+
  ggtitle("Figure 5. Median Daily Page Views by Group")


figure6<-ggplot(data=all_data)+
  geom_boxplot(aes(x=type, y=log(editorcount), fill=type), show.legend=FALSE)+
  theme_minimal()+
  scale_fill_manual(values=c("#254181","#138d75","#a2d9ce","#72b2f5"))+
  xlab("")+
  ylab("Editor count, logarithmic scale")+
  ggtitle("Figure 6. Median Editors by Group")

figure5
```

![](DataAnalysis_files/figure-html/unnamed-chunk-9-1.png)<!-- -->

```r
figure6
```

![](DataAnalysis_files/figure-html/unnamed-chunk-9-2.png)<!-- -->

**Pageviews and Editor Count for New and Existing Articles**

```r
figure7<-ggplot()+
  geom_boxplot(data=Artists, aes(x=type, y=log(aveviews), fill=New))+
  geom_boxplot(data=Scientists, aes(x=type, y=log(aveviews), fill=New))+
  ggtitle("Figure 7. Pageviews of Newly Created and Edited Articles \n for Intervention Groups ")+
  ylab("log of pageviews")+
  xlab(" ")+
  scale_fill_manual(name = " ", labels = c("Existing Articles", "Newly Created"), values=c("#673990","#e7dbf2"))+
  theme_minimal()


figure8<- ggplot()+
  geom_boxplot(data=Artists, aes(x=type, y=log(editorcount), fill=New))+
  geom_boxplot(data=Scientists, aes(x=type, y=log(editorcount), fill=New))+
  ggtitle("Figure 8. Editor Count of Newly Created and Edited Articles \n for Intervention Groups ")+
  ylab("log of editor count")+
  xlab(" ")+
  scale_fill_manual(name = " ", labels = c("Existing Articles", "Newly Created"), values=c("#673990","#e7dbf2"))+
  theme_minimal()

figure7
```

![](DataAnalysis_files/figure-html/unnamed-chunk-10-1.png)<!-- -->

```r
figure8
```

![](DataAnalysis_files/figure-html/unnamed-chunk-10-2.png)<!-- -->

```r
figure9<-ggplot(all_data)+
  geom_point(aes(x=editorcount, y=length, col=type))+
  geom_smooth(aes(x=editorcount, y=length, col=type, method="lm", se=FALSE))+
  scale_color_manual(values=c("#254181","#138d75","#a2d9ce","#72b2f5"))+
  theme_minimal()+
  ylab("length of article")+
  xlab("editorcount")+
  ggtitle("Figure 9. Relationship between number of editors and length of article")
```

```
## Warning: Ignoring unknown aesthetics: method, se
```

```r
figure9
```

```
## `geom_smooth()` using method = 'gam' and formula 'y ~ s(x, bs = "cs")'
```

![](DataAnalysis_files/figure-html/unnamed-chunk-10-3.png)<!-- -->



