bhl_16s_noS14_merge <- merge_samples(bhl_16s_noS14,“LandManagemant”)
sample_data(bhl_16s_noS14_merge)$LandManagemant <- levels(sample_data(bhl_16s_noS14)$LandManagemant)
bhl_16s_noS14_merge_re = transform_sample_counts(bhl_16s_noS14_merge, function(x) 100 * x/sum(x))
bhl_16s_noS14_merge_re_g = tax_glom(bhl_16s_noS14_merge_re, “Rank2")
otu_table(bhl_16s_noS14_merge_re_g)
BarofLM <- plot_bar(bhl_16s_noS14_merge_re_g, fill=“Rank2”) +
 ylab(“Relative Abundance of Phylum”)+
 xlab(“Land Management”)
ggsave(BarofLM, file=“~/OneDrive/Research/2018_research/BHL/Figures_R/barofLandmanagement1.pdf”, unit=“in”, width=6,height = 6)

