#####here is how pairwise anosim work 
pairwise.anosim <- function(x,factors, sim.function = ‘vegdist’, sim.method = ‘bray’, p.adjust.m =‘bonferroni’)
{

 co = combn(unique(as.character(factors)),2)
 pairs = c()
 F.Model =c()
 R = c()
 p.value = c()
 
 for(elem in 1:ncol(co)){
   if(sim.function == ‘daisy’){
     library(cluster); x1 = daisy(x[factors %in% c(co[1,elem],co[2,elem]),],metric=sim.method)
   } else{x1 = vegdist(x[factors %in% c(co[1,elem],co[2,elem]),],method=sim.method)}
   
   ad = anosim(x1 ,factors[factors %in% c(co[1,elem],co[2,elem])] , permutations=999);
   pairs = c(pairs,paste(co[1,elem],‘vs’,co[2,elem]));
   
   R = c(R,unlist(ad[5]));
   p.value = c(p.value,unlist(ad[2]))
 }
 p.adjusted = p.adjust(p.value,method=p.adjust.m)
 sig = c(rep(‘’,length(p.adjusted)))
 sig[p.adjusted <= 0.05] <-‘.’
 sig[p.adjusted <= 0.01] <-‘*’
 sig[p.adjusted <= 0.001] <-‘**’
 sig[p.adjusted <= 0.0001] <-‘***’
 
 pairw.res = data.frame(pairs,R,p.value,p.adjusted,sig)
 print(“Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1”)
 return(pairw.res)
}
