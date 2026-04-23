# starting with dplyr

# access dplyr package
library(dplyr)

dplyr::filter()
stats::filter()

# information about star wars dataset
??starwars

dim(starwars) # 87 14 variables

str(starwars) # structure, first  columns

# first and last observation
head(starwars) # 6 first lines
tail(starwars) # 6 last lines

# dbl - decimal number 
# NA - missing values 

filter() # choose rows that meet logical criteria
slice() # select rows by position
arrange() 
select() #  move columns to new position

# select observations ("cases")
starwars |> filter(skin_color == "light", eye_color == "brown") # professor version
starwars[starwars$skin_color == "light" & starwars$eye_color == "brown", ] # my version

# let's consider their height
starwars |>
  filter(skin_color == "light", eye_color == "brown") |>
  select(height)


mutate() # transformation of one set of observations
starwars |> mutate(height_m = height/100)

starwars |> summarise(height = mean(height, na.rm = TRUE)) # collapses data into row
summary(starwars) # not as helpful in this context, provides a set of basic descriptive stats to each column

# mean of mass and mean of height in each combo of species and sex
starwars |>
  group_by(species, sex) |> # stratification
  select(height, mass) |>
  summarise( 
    height = mean(height, na.rm = TRUE),
    mass = mean(mass, na.rm = TRUE)
  )

# representations of subsets of observations


