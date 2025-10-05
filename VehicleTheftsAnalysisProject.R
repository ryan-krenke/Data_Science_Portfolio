# DSC640-T302
# Weeks 5/6 Assignment Kia Thefts
# Name: Krenke, Ryan
# Due Date: 7/13/25

## Load the ggplot2 package
library(ggplot2)
theme_set(theme_minimal())

## Set the working directory 
setwd('C:/Users/ryanr/dsc640/Weeks56')

## Load the carTheftsMap csv
map_df <- read.csv("C:/Users/ryanr/dsc640/Weeks56/carTheftsMap.csv")

#install various packages and run libraries
install.packages(c("maps", "dplyr", "readr", "scales"))
library(maps)
library(dplyr)
library(readr)
library(scales)
install.packages(c("maptools", "sp"))
library(sp)
#install.packages("sf")
#library(sf)

# Clean missing lat and lon coordinates
map_df <- map_df[!is.na(map_df$latitude) & !is.na(map_df$longitude), ]

# Get US state map data
us_map <- map_data("state")

#creating map plot
ggplot() +
#creates us map background
  geom_polygon(data = us_map, aes(x = long, y = lat, group = group),
               fill = "gray90", color = "white") +
#creates data points for each lat/lon 
  geom_point(data = map_df, aes(x = longitude, y = latitude, color = percentChange2019to2022),
             size = 3, alpha = 0.8) +
#color scale for percent change, midpoint 100%
  scale_color_gradient2(low = "green", mid = "white", high = "red", midpoint = 1,
                        labels = percent_format(accuracy = 1)) +
#title and color label
  labs(title = "Percent Change in Car Thefts by Police Dept (2019 to 2022)",
       color = "Change (2019–2022)") +
#clean theme without axes, ticks, or gridlines
  theme_void() +
  theme(
    legend.position = "right",
    plot.title = element_text(hjust = 0.5) #horizontal justification centered
  ) +
#keeps proper map aspect ratio
  coord_fixed(1.3) #1.3/1

install.packages("tidyverse")
library(tidyverse)
install.packages("lubridate")
library(lubridate)
install.packages("scales")
library(scales)
install.packages("tidyr")
library(tidyr)

#reading theft data for various cities into dataframe (I manually removed many cities first)
theft_df <- read.csv("C:/Users/ryanr/dsc640/Weeks56/kiaHyundaiThefts1.csv")

#create a date variable
theft_df$date <- lubridate::parse_date_time(paste(theft_df$month, theft_df$year), orders = "b Y")

#reshape the data to long format
theft_df2 <- reshape(theft_df,
                         varying = c("countKiaHyundaiThefts", "countOtherThefts"),
                         v.names = "count",
                         timevar = "theft_type",
                         times = c("Kia/Hyundai", "Other"),
                         direction = "long")
#reset rownames and sorting by city and date
rownames(theft_df2) <- NULL
theft_df2 <- theft_df2[order(theft_df2$city, theft_df2$date), ]

#keeping only 4 listed cities in the dataset
theft_df2 <- theft_df2[theft_df2$city %in% c("Chicago", "Cleveland", "Omaha", "Saint Paul"), ]
theft_df2$city <- factor(theft_df2$city, levels = c("Chicago", "Cleveland", "Omaha", "Saint Paul"))

#set date column as a date type
theft_df2$date <- as.Date(theft_df2$date)

#create group of 4 stacked area charts with ggplot
ggplot(theft_df2, aes(x = date, y = count, fill = theft_type)) +
  geom_area(alpha = 0.8, color = "black", linewidth = 0.2) + #plot area
  scale_fill_manual(values = c("Kia/Hyundai" = "steelblue", "Other" = "gray60")) +
  facet_wrap(~ city, ncol = 2, scales = "free_y") + #panel for each city, 2 columns, each own axis
  scale_x_date(date_breaks = "6 months", date_labels = "%b\n%Y") + #6 mo spacing, label mmm break yyyy
  labs(title = "Monthly Vehicle Thefts by City",
       subtitle = "Comparing Kia/Hyundai vs Other Vehicle Thefts (2019–2022)",
       x = "Date", y = "Number of Thefts", fill = "Vehicle Type") +
  theme_minimal(base_size = 13) + #minimal style, 13 font
  theme(axis.text.x = element_text(angle = 45, hjust = 1), #45 deg angle, adj right
        panel.grid.minor = element_blank()) #remove minor gridlines

#reading milwaukee theft data into df
mke_df <- read.csv("C:/Users/ryanr/dsc640/Weeks56/KiaHyundaiMilwaukeeData.csv")

#reshaping the dataframe into long version with reshape
mke_df2 <- reshape(mke_df,
                      varying = c("countKiaHyundaiThefts", "countOtherThefts"),
                      v.names = "count",
                      timevar = "type",
                      times = c("Kia/Hyundai", "Other"),
                      direction = "long")
#creating df of summed data
yearly_totals <- aggregate(count ~ year + type, data = mke_df2, FUN = sum)

#creating pie chart of totals for 2019
ggplot(subset(yearly_totals, year == 2019), aes(x = "", y = count, fill = type)) +
  geom_bar(stat = "identity", width = 1, color = "white") + #identity uses count
  coord_polar(theta = "y") + #creates pie chart
  scale_fill_manual(values = c("Kia/Hyundai" = "steelblue", "Other" = "gray60")) +
  labs(title = "Milwaukee Thefts – 2019", fill = "Vehicle Type") +
  theme_void() +
  theme(plot.title = element_text(hjust = 0.5), #centered title
        aspect.ratio = 1) #square

#creating pie chart of totals for 2020
ggplot(subset(yearly_totals, year == 2020), aes(x = "", y = count, fill = type)) +
  geom_bar(stat = "identity", width = 1, color = "white") +
  coord_polar(theta = "y") +
  scale_fill_manual(values = c("Kia/Hyundai" = "steelblue", "Other" = "gray60")) +
  labs(title = "Milwaukee Thefts – 2020", fill = "Vehicle Type") +
  theme_void() +
  theme(plot.title = element_text(hjust = 0.5),
        aspect.ratio = 1)

#creating pie chart of totals for 2021
ggplot(subset(yearly_totals, year == 2021), aes(x = "", y = count, fill = type)) +
  geom_bar(stat = "identity", width = 1, color = "white") +
  coord_polar(theta = "y") +
  scale_fill_manual(values = c("Kia/Hyundai" = "steelblue", "Other" = "gray60")) +
  labs(title = "Milwaukee Thefts – 2021", fill = "Vehicle Type") +
  theme_void() +
  theme(plot.title = element_text(hjust = 0.5),
        aspect.ratio = 1)

#creating pie chart of totals for 2022
ggplot(subset(yearly_totals, year == 2022), aes(x = "", y = count, fill = type)) +
  geom_bar(stat = "identity", width = 1, color = "white") +
  coord_polar(theta = "y") +
  scale_fill_manual(values = c("Kia/Hyundai" = "steelblue", "Other" = "gray60")) +
  labs(title = "Milwaukee Thefts – 2022", fill = "Vehicle Type") +
  theme_void() +
  theme(plot.title = element_text(hjust = 0.5),
        aspect.ratio = 1)

# Summarize totals by car type
total_kia <- sum(mke_df$countKiaH)
total_other <- sum(mke_df$countOthe)

#creating dataframe with the totals
mke_totals <- data.frame(
  type = c("Kia/Hyundai", "Other"),
  count = c(total_kia, total_other))

#create donut chart
ggplot(mke_totals, aes(x = 2, y = count, fill = type)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar(theta = "y") +
  xlim(1.0, 2.5) + #creates hole along with x=2 above
  scale_fill_manual(values = c("Kia/Hyundai" = "steelblue", "Other" = "gray60")) +
  labs(title = "Share of Total Vehicle Thefts in Milwaukee (2019–2022)",
       fill = "Vehicle Type") +
  theme_void() +
  theme(legend.position = "right")

library(lubridate)

#combine month and year into a date column
mke_df$date <- parse_date_time(paste(mke_df$month, mke_df$year), orders = "b Y")
mke_df$date <- as.Date(mke_df$date) #changing to date type

#create area plot with date and percent data
ggplot(mke_df, aes(x = date, y = percentKiaHyundai)) +
  geom_area(fill = "steelblue", alpha = 0.7) +
  scale_y_continuous(labels = scales::percent_format(accuracy = 1)) #proportions to percentages nearest whole +
  labs(title = "Kia/Hyundai Theft Share Over Time in Milwaukee",
       subtitle = "Percent of total vehicle thefts (2019–2022)",
       x = "Date", y = "Percent Kia/Hyundai") +
  theme_minimal(base_size = 13) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

#combine month and year into a date column
mke_df2$date <- parse_date_time(paste(mke_df2$month, mke_df2$year), orders = "b Y")
mke_df2$date <- as.Date(mke_df2$date) #changing to date type

#create stacked bar chart
ggplot(mke_df2, aes(x = date, y = count, fill = type)) +
  geom_bar(stat = "identity", position = "stack", color = "black") +
  scale_fill_manual(values = c("Kia/Hyundai" = "royalblue", "Other" = "gray60")) +
  labs(title = "Monthly Vehicle Thefts in Milwaukee",
       x = "Date", y = "Number of Thefts", fill = "Vehicle Type") +
  scale_x_date(date_breaks = "3 months", date_labels = "%b\n%Y") +
  theme_minimal(base_size = 13) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
