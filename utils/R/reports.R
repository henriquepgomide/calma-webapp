library(tidyverse)
library(lubridate)
library(plotly)
library(chron)

data <- read_csv("~/Downloads/calmanessahora_data.csv")
glimpse(data)

data$date <- as.Date(data$date, format = "%d/%m/%Y")
data$minimum <- chron(times = data$minimum)
data$avg_time <- chron(times = data$avg_time)
data$longest <- chron(times = data$longest)

data <- 
  data %>% 
  filter(date <= as.Date("2020-05-26"))

data_g <-  
  data %>% 
  select(date, users, new_users, chats) %>% 
  gather(-date, key = "key", value = "value")

p1 <- 
  ggplot(data_g, aes(x = date, y = value, colour = key)) + 
  geom_line(size = 1.2) + 
  xlab("") + ylab("Métrica") + 
  labs(title = "Calmanessahora",
       subtitle = "Estatísticas de uso entre 11 de abril e 11 de maio") + 
  theme_minimal()

ggplotly(p1)

# Create chat by user attribute
data$chats_by_user <- data$chats / data$users
weekday <- format(data$data, "%a")
p2 <- 
  ggplot(data, aes(x = date, y = chats_by_user)) + 
  geom_line() + 
  theme_minimal() + 
  labs(title = "Calmanessahora",
       subtitle = "Taxa de atendimento de chats - chats por usuário ativo")


ggplotly(p2)
summary(data$chats_by_user, na.rm = TRUE)

p3 <- 
ggplot(data, aes(x = chats_by_user, y = users, colour = as.character(time))) + 
  geom_point()

ggplotly(p3)


p4 <- 
ggplot(data, aes(x = chats_by_user, y = users, colour = weekday)) + 
  geom_point()

ggplotly(p4)


# EDA ---------------------------------------------------------------------

# Average time of chat session
summary(data$avg_time)

# Chat volume
data %>% 
  #filter(date >= Sys.Date() - 7) %>%
  summarise(chats_sum = sum(chats),
            users_sum = sum(users),
            new_users_sum = sum(new_users),
            chats_avg_time = mean(avg_time, na.rm = TRUE), 
            chats_per_user = chats_sum / users_sum)
