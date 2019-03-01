df = read.csv("CS_555_Assignment_2.csv", header = FALSE)

part_cal <- df$V1[1:23]
part_cal <- levels(participants)[participants]
part_cal <- as.numeric(participants)
part_cal <- participants[!is.na(participants)]

len.part = length(part_cal)
sd.part <- sd(part_cal)
mean.part <-mean(part_cal)
median.part <- median(part_cal)
  
non_part_cal <- df$V1[24:length(df$V1)]
non_part_cal <- levels(non_participants)[non_participants]
non_part_cal <- as.numeric(non_participants)
non_part_cal <- non_participants[!is.na(non_participants)]

len.non = length(non_part_cal)
sd.non = sd(non_part_cal)
mean.non = mean(non_part_cal)
median.non <- median(non_part_cal)

mean_defference <- abs(mean(part_cal) - mean(non_part_cal))

people_cal <- append(part_cal, non_part_cal, after = len.part)
participation <- append(rep(TRUE, len.part), rep(FALSE, len.non), after = length(rep(TRUE,len.part))) 

df2 <- data.frame(calorieIntake= people_cal, participation = participation)
print(df2)

################################################################################################

par(mfrow = c(1, 2))
boxplot(part_cal, main = 'Participants')
boxplot(non_part_cal, main ='Non-Participants')

##################################################

par(mfrow = c(1, 2))

hist(part_cal, main = 'Participants', xlab = 'Calorie in take', ylab = 'Number of children')
abline(v = mean.part, col = "red", lwd = 2)
abline(v = median.part, col = "blue", lwd = 2)


hist(non_part_cal, main = 'Non-Participants', xlab = 'Calorie in take', ylab = 'Number of children')
abline(v = mean.non, col = "red", lwd = 2)
abline(v = median.non, col = "blue", lwd = 2)
