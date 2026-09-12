"""Research methods additions (examined in both papers): scientific methodology, sampling
design, Simpson's index and statistical tests.  Genn pp. 390-393, 402, 420-423."""
from gen.model import Q, P, Table, Chart, Essay

QUESTIONS = [
    # ---------------- 3.7.1 methodology ----------------
    Q("RM-16", "methodology", "3.7.1", "390-391",
      parts=[
          P("A student measured the pH of a stream with a meter that reads to 0.01 pH units but had not been calibrated. Which statement is correct? Tick <b>one</b> box.", 1,
            mcq=["The readings are precise but may not be accurate", "The readings are accurate but not precise", "The readings are both accurate and precise", "The readings are reliable because the meter is electronic"],
            ms=["The readings are precise but may not be accurate"]),
          P("Explain what is meant by an <b>anomalous result</b> and how a student should decide whether to include it.", 2,
            ms=["A result that differs from other results with which it was expected to be similar",
                "Repeat the study / measurement: if it recurs it is a 'real' result caused by another variable; if not it was an error and can be excluded"]),
          P("Explain why a preliminary study is carried out before the main investigation.", 2,
            ms=["To test the reliability of the method / equipment", "To decide the sample size, number of samples, spacing or timing needed to detect the variation without collecting unnecessary data"]),
      ]),

    Q("RM-17", "methodology", "3.7.1", "391-393",
      intro="Figure 1 shows the mean number of woodlice per pitfall trap calculated as more traps were included in the mean (a running mean).",
      figures=[Chart("line", "Number of traps used to calculate the mean", "Running mean number of woodlice per trap", {"Running mean": [(5, 12.0), (10, 8.5), (15, 10.2), (20, 9.1), (30, 9.6), (40, 9.4), (50, 9.5), (60, 9.5), (70, 9.5)]}, y_min=0, y_max=14)],
      parts=[
          P("Use Figure 1 to suggest the minimum number of traps needed to produce a reliable mean. Give a reason for your answer.", 2,
            ms=["About 40-50 traps", "Because the running mean stops changing / fluctuating with fewer than this the mean is unreliable"]),
          P("Explain why the number of samples needed depends on the degree of scatter of the results.", 2,
            ms=["Widely scattered results (large standard deviation) mean a single sample may not be representative",
                "More samples are needed so that the effect of variability is averaged out and the mean is representative / significance can be assessed"]),
          P("The student wants to compare woodlouse numbers in a woodland and in a grassland. Describe how the sampling should be standardised.", 3,
            ms=["Same type and size of pitfall trap, set for the same length of time", "Traps emptied at the same time of day / same weather conditions in both habitats",
                "Same number of traps and same method of positioning (random or systematic) in each habitat", "Other variables that could affect results (eg rainfall, temperature) monitored or controlled"]),
          P("Explain why the timing of sampling would matter if the student were investigating the activity of flying insects rather than woodlice.", 3,
            ms=["Flying insect activity changes with weather over minutes to weeks (temperature, wind) and diurnally",
                "Samples on different occasions are needed to produce a mean that represents the typical value or to identify trends",
                "The interval between samples should match the rate at which the factor changes, found from a preliminary study"]),
      ]),

    # ---------------- 3.7.2.3 statistics & specialist techniques ----------------
    Q("RM-18", "stats", "3.7.2.3", "402",
      intro="A student sampled the ground-flora of two woodlands. Table 1 shows the results for woodland A.",
      figures=[Table(["Species", "Number of individuals (n)"], [["Bluebell", "40"], ["Wood anemone", "30"], ["Dog's mercury", "20"], ["Bramble", "10"], ["Total (N)", "100"]])],
      parts=[
          P("Use the formula <i>D</i> = <i>N</i>(<i>N</i> - 1) / &Sigma;<i>n</i>(<i>n</i> - 1) to calculate Simpson's index of diversity for woodland A.", 3, calc=True, unit="",
            ms=["&Sigma;n(n - 1) = (40 x 39) + (30 x 29) + (20 x 19) + (10 x 9) = 1560 + 870 + 380 + 90 = 2900", "N(N - 1) = 100 x 99 = 9900", "D = 9900 / 2900 = 3.41 (accept 3.4)"]),
          P("Woodland B had an index of 1.6. State what this shows and give <b>one</b> limitation of using the index alone to compare the woodlands.", 2,
            ms=["Woodland A has a higher biodiversity (greater variety and more even abundance) than woodland B",
                "The index does not identify which species are present / a rare or important species may be missed; depends on identification skill and sampling method"]),
      ]),

    Q("RM-19", "stats", "3.7.2.3", "420-423",
      intro="A student measured the wind speed at 10 sites inside a woodland and at 10 sites in a nearby clearing.",
      figures=[Table(["Location", "Mean wind speed / m s^-1", "Standard deviation / m s^-1"], [["Woodland", "1.2", "0.4"], ["Clearing", "3.5", "1.1"]])],
      parts=[
          P("Name the statistical test the student should use to find out whether the difference between the means is significant. Give <b>two</b> reasons for your choice.", 3,
            ms=["t-test", "The data are measured (continuous) values and two means are being compared", "The data are (assumed to be) normally distributed"]),
          P("Explain what the student should do if it is not possible to show that the data are normally distributed.", 1,
            ms=["Use the Mann-Whitney U test instead (compares medians)"]),
          P("The test gave p = 0.02. Explain what this means.", 2,
            ms=["There is a 2% probability that the difference occurred by random chance", "As this is less than 0.05 the difference is statistically significant / the null hypothesis is rejected"]),
          P("Explain how the standard deviations in Table 1 support the conclusion that the means are different.", 2,
            ms=["The ranges of values (mean plus or minus SD) do not overlap: woodland up to 1.6 and clearing down to 2.4",
                "About 68% of values lie within one SD of each mean so the two data sets are clearly separated"]),
          P("Explain why a statistically significant result does not prove that trees cause the lower wind speed.", 2,
            ms=["Significance shows the difference is unlikely to be due to chance, not that a causal relationship exists",
                "Another variable (eg topography / aspect of the sites) could cause both; a controlled experiment or further evidence is needed"]),
      ]),

    Q("RM-20", "stats", "3.7.2.3", "422-423",
      parts=[
          P("Complete Table 1 by naming the most suitable statistical test for each hypothesis.", 4,
            table=Table(["Hypothesis", "Statistical test"],
                        [["Noise levels decrease as distance from a road increases", ""], ["Fewer cars use a road after road charging is introduced (counts on 12 days before and after)", ""],
                         ["Woodlands managed in different ways have different numbers of dormice", ""], ["Mean lobster mass is higher in areas where collection is banned", ""]], blank=True, col_widths=[10.5, 4.5]),
            ms=["Spearman's rank correlation coefficient", "Mann-Whitney U test", "Chi-squared test", "t-test"]),
          P("Explain why the chi-squared test cannot be used to compare the dissolved oxygen concentrations of two rivers.", 2,
            ms=["Chi-squared compares frequencies / counts in categories", "Dissolved oxygen is continuously variable measured data, so a t-test or Mann-Whitney U test is needed"]),
          P("Explain why a scientific investigation never 'proves' a hypothesis.", 2,
            ms=["There is always some remaining uncertainty / a probability that the result was produced by chance",
                "Statistics only give a level of confidence (eg 95%, 99%) that the result is significant"]),
          P("Describe how error bars are added to a graph of means and how they are interpreted.", 2,
            ms=["Bars drawn above and below each mean showing plus and minus one standard deviation",
                "If the bars of two means overlap a lot the difference is probably not significant; if they do not overlap it probably is"]),
      ]),
]
