df = read.csv("CS_555_Assignment_1.csv", header = FALSE)

mean = mean(df$V1)
median = median(df$V1)
sd = sd(df$V1)
quantile = quantile(df$V1)
minimum = min(df$V1)
maximum = max(df$V1)

boundaries = seq(minimum -1 , maximum, by = 1)
results <- hist(df$V1, breaks = boundaries, axes = FALSE, main =  "Histogram for Days of hospital stays", xlab = "Days of Stay", ylab = "Frequency")
x.labels <- seq(minimum - 1, maximum, by =2)
axis(1 , las = 1, at = x.labels, labels = x.labels)
axis(2, las = 1, at = results$counts, labels = results$counts )
abline(v = mean, col = "red", lwd = 2)
abline(v = median, col = "blue", lwd = 2)
text(mean + 1 , 15, "Mean", cex = 1.2, col='red')
text(median - 1 , 10, "Median", cex = 1.2, col='Blue')

boxplot(df$V1, las = 2, main = "Boxplot for days of hospital stays")