clear
set more off
cap log close
cd /Users/jsusser
use atlas.dta
*summarizes Data
sum kfr_pooled_p25 [aw = count_pooled]
sum kfr_pooled_p25 if state == 55 [aw = count_pooled ]            


*Regression: predicts kfr_pooled_p25 based off other variables
*Coef is how much each affects it. How much each kfr_pooled_p25 goes up eachtime the other variable goes up
reg kfr_pooled_p25 kfr_white_p25 poor_share2000 singleparent_share2000, robust
gen yvar = kfr_pooled_p25

sum yvar
gen y_std = (yvar - r(mean))/r(sd)
gen xvar = count_pooled
sum xvar
gen x_std = (xvar - r(mean))/r(sd)
reg y_std x_std , robust
twoway (scatter yvar xvar) (lfit yvar xvar)
