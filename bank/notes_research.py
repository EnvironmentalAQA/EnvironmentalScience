"""Revision notes: Research methods (spec 3.7).  Genn pp. 390-423.  Examined in both papers."""

NOTES = {
# =====================================================================
"methodology": {
    "summary": "Good decisions need good data. Every investigation follows the same logic - question, hypothesis, planned sampling, standardised technique, analysis, conclusion - and the quality of its conclusions depends on accuracy, precision, reliability, representative sampling and validity. Location, timing, size and number of samples are decided with preliminary studies.",
    "sections": [
        ("Attributes of quality", "390",
         "<table class=\"nt\"><tr><th>Term</th><th>Meaning</th></tr>"
         "<tr><td>Accuracy</td><td>How close a recorded result is to the true value</td></tr>"
         "<tr><td>Precision</td><td>The interval between possible recorded results (a mm ruler is more precise than a cm one) - a precise reading can still be inaccurate if the instrument is not calibrated</td></tr>"
         "<tr><td>Representative sample</td><td>A sub-sample that accurately reflects the complete data set</td></tr>"
         "<tr><td>Reliable method</td><td>Gives consistent, accurate results when repeated</td></tr>"
         "<tr><td>Anomalous result</td><td>Differs from others expected to be similar; repeat to see whether it is real or an error</td></tr>"
         "<tr><td>Valid study</td><td>Produces precise, accurate, reliable results on which conclusions can be based</td></tr></table>"
         "<p>Planning also covers risk management, choosing and using equipment safely, deciding what quantitative data to collect and which sampling and statistical techniques suit them.</p>"),
        ("Scientific methodology", "391",
         "<ol><li>Identify a topic of interest and find out what is already known.</li><li>Formulate a <b>hypothesis</b> and a <b>null hypothesis</b> that can be tested.</li>"
         "<li>Design the investigation: location, number, size and timing of samples; standardised technique; statistical analysis planned in advance.</li>"
         "<li>Collect data, analyse, draw conclusions (accept or reject the null hypothesis at a stated significance level).</li><li>Plan further research to fill gaps.</li></ol>"
         "<p>It is rarely possible to measure everything, so <b>sub-samples</b> estimate the whole; conclusions are only reliable if they are representative. A <b>preliminary study</b> tests the method and shows how many, how large and how often samples are needed.</p>"),
        ("Sample location", "391-392",
         "<p>Avoid bias from choosing convenient sites or sites that support the hypothesis. <b>Random sampling:</b> grid coordinates from random numbers (regular areas) or numbering all possible sites (irregular areas). <b>Systematic sampling:</b> fixed intervals, eg along a <b>line transect</b> or a <b>belt transect</b> (continuous or interrupted) across a gradient such as a shore or a path. The interval must be small enough to detect the variation (the book's graphs: 2 m intervals catch what 1 m does; 4 m misses peaks) but no smaller than necessary. <b>Stratified sampling</b> divides the area into zones sampled separately.</p>"),
        ("Sample timing", "392-393",
         "<p>If the factor changes with time, sample on several occasions to get a representative mean or to detect trends. Timescales: <b>long-term</b> (population trends, rainforest area, CO<sub>2</sub>), <b>seasonal</b> (migrants, temperature), <b>diurnal</b> (light, temperature, CO<sub>2</sub>), <b>weather-related</b> (flying insect activity, wind, minutes to weeks), other <b>short-term</b> changes (road noise through the day). The interval between samples depends on the rate of change - again found with a preliminary study.</p>"),
        ("Sample size, number and standardisation", "393",
         "<ul><li><b>Sample size:</b> larger samples are more representative where the variable is not homogeneous.</li><li><b>Number of samples:</b> depends on the scatter around the mean (standard deviation); plotting a <b>running mean</b> shows when adding samples stops changing the mean - the book's graph shows means from fewer than 50 values were unreliable. More samples also make significance easier to assess.</li>"
         "<li><b>Standardisation of techniques:</b> identical methods at every site, time and by every researcher so results are comparable; other variables controlled or monitored.</li></ul>"),
        ("Population studies: why monitor", "393",
         "<p>Ecological monitoring underpins conservation: which species are present, habitat conditions and how they change, the requirements of individual species, whether management is working, population size, distribution, survival rate and age structure - links to the ecological monitoring notes.</p>"),
    ],
    "diagrams": [
        {"type": "chart", "title": "Running mean: how many samples are enough?", "kind": "line", "x_label": "Number of samples", "y_label": "Running mean",
         "series": {"Running mean": [(5, 12), (10, 8.5), (15, 10.2), (20, 9.1), (30, 9.6), (40, 9.4), (50, 9.5), (60, 9.5), (70, 9.5)]}, "y_min": 0, "y_max": 14,
         "caption": "The mean settles after about 40-50 samples; fewer would be unreliable (Genn p. 393)."},
    ],
    "numbers": ["Precision vs accuracy: a calibrated instrument is accurate; a fine scale is precise", "Statistical significance normally p < 0.05"],
    "exam": ["Describe how to sample representatively (random / systematic) for a given scenario (Nov 2020 Q7 soil sampling; Nov 2020 Q8 trees).", "Distinguish accuracy, precision, reliability, validity; explain anomalous results.",
             "Suggest variables to standardise or control (specimen P2 Q2, June 2024 Q4).", "Interpret a running mean and justify a sample number.", "9-mark: planning decisions for valid conclusions; essay on research design (Paper 1 practice)."],
},
# =====================================================================
"sampling": {
    "summary": "Standard ecological techniques - quadrats, transects, kick sampling, Surber samplers, nets, traps, Tullgren funnels, extraction methods and mark-release-recapture - each suit particular organisms and have limitations. Abiotic factors (light, temperature, wind, humidity, water and soil properties) are measured with instruments that must be calibrated, and biotic indices turn species lists into pollution measures.",
    "sections": [
        ("Quadrats and transects", "394",
         "<p><b>Quadrats</b> (frames of known area) sample plants and sessile animals: <b>size</b> chosen from a preliminary study (species-area curve) - small for grassland, large for woodland; <b>types</b> - frame, point (pins for cover), gridded; placed randomly or along a transect. Record <b>species richness</b>, <b>frequency</b> (proportion of quadrats containing the species), <b>density</b> (individuals per unit area), <b>percentage cover</b> (estimated or by point pins) and <b>abundance scales</b> such as <b>ACFOR</b> (abundant, common, frequent, occasional, rare) - quick but subjective.</p>"),
        ("Aquatic and terrestrial invertebrate sampling", "395-400",
         "<table class=\"nt\"><tr><th>Technique</th><th>Method</th><th>Limitations</th></tr>"
         "<tr><td>Kick sampling</td><td>Disturb the stream bed for a standard time with a net held downstream</td><td>Semi-quantitative; misses burrowing and attached species; depends on effort</td></tr>"
         "<tr><td>Surber sampler</td><td>Quadrat frame with attached net gives a known area of stream bed</td><td>Only shallow, flowing water; disturbs habitat</td></tr>"
         "<tr><td>Sweep nets</td><td>Sweep vegetation a standard number of times</td><td>Catch depends on weather, time of day, sweep style; damages fragile insects</td></tr>"
         "<tr><td>Beating tray</td><td>Tap branches over a sheet</td><td>Flying insects escape; hard to standardise between trees</td></tr>"
         "<tr><td>Pitfall traps</td><td>Containers sunk level with the ground catch ground-active invertebrates; cover to exclude rain; check regularly</td><td>Catch reflects activity not density; predators eat prey in the trap; some species avoid traps</td></tr>"
         "<tr><td>Light traps</td><td>Lamp attracts night-flying insects into a box</td><td>Only species attracted to light; affected by moon and temperature; area sampled unknown</td></tr>"
         "<tr><td>Tullgren funnel</td><td>Heat and light from above drive soil invertebrates down through a sieve into preservative</td><td>Only mobile species; some die before escaping; sample size small</td></tr>"
         "<tr><td>Suction samplers</td><td>Vacuum a known area of vegetation</td><td>Misses attached species; standardising suction time</td></tr>"
         "<tr><td>Earthworm extraction</td><td>Mustard / formalin solution or electrical stimulation brings worms to the surface from a known area; hand sorting</td><td>Not all species respond; depends on soil moisture and temperature</td></tr>"
         "<tr><td>Colonisation media / artificial refuges</td><td>Reptile tins, bat boxes, nest boxes, mussel bags</td><td>Presence only; not population estimates</td></tr></table>"),
        ("Population size: mark-release-recapture (Lincoln index)", "400-402",
         "<p>Catch, mark harmlessly and release M individuals; later catch C, of which R are marked: <b>N = (M x C) / R</b>. <b>Assumptions / limitations:</b> individuals are mobile and catchable; population is closed (no births, deaths, migration during the study); marking does not affect survival or catchability; marks do not wear off; marked individuals mix freely; every individual has an equal chance of capture. <b>Simpson's index of diversity</b> D = N(N-1) / &Sigma;n(n-1) combines the number of species and their evenness (higher = more diverse for this version). <b>Identification keys</b> (dichotomous) rely on visible features that may be absent (flowers, breeding plumage) or shared between species.</p>"),
        ("Measuring abiotic factors", "407-414",
         "<table class=\"nt\"><tr><th>Factor</th><th>Method</th><th>Points to standardise</th></tr>"
         "<tr><td>Temperature (air, water, soil)</td><td>Thermometer, electronic probe, soil thermometer; data loggers for continuous records</td><td>Depth, shade, time of day; calibrate against a reference</td></tr>"
         "<tr><td>Light</td><td>Light meter (lux); light-dependent resistor loggers</td><td>Orientation of sensor, cloud, time; take readings at the same moment at all sites</td></tr>"
         "<tr><td>Humidity</td><td>Whirling hygrometer (wet and dry bulb), electronic meter</td><td>Height above ground, shelter</td></tr>"
         "<tr><td>Wind velocity</td><td>Anemometer (cup or vane)</td><td>Height, averaging period, obstacles</td></tr>"
         "<tr><td>Water: pH, dissolved oxygen, turbidity, flow, salinity</td><td>Electronic meters, colourimetry / chemical kits, Secchi disc or turbidity tube, float timing or flow meter, conductivity meter</td><td>Depth, time, distance from bank; oxygen meters need calibration and stirring</td></tr>"
         "<tr><td>Soil texture</td><td>Sieving; sedimentation in a jar (sand settles first, then silt, clay stays suspended); feel; soil triangle</td><td>Dry the sample; standard shaking</td></tr>"
         "<tr><td>Soil water content</td><td>Weigh, dry at 105 &deg;C to constant mass, reweigh: % water = loss / wet mass x 100</td><td>Drying temperature must not burn organic matter</td></tr>"
         "<tr><td>Soil organic matter</td><td>Dry sample burnt in a furnace at about 500 &deg;C: loss on ignition / dry mass x 100</td><td>Cool in a desiccator before weighing</td></tr>"
         "<tr><td>Soil pH and nutrients</td><td>pH meter or indicator kit in distilled water; colourimetric test kits for nitrate, phosphate</td><td>Sample depth, ratio of soil to water, calibration</td></tr></table>"
         "<p><b>Calibration:</b> electronic meters must be adjusted to read the same as an accurate reference; if they cannot be adjusted, record the percentage error and correct the results.</p>"),
        ("Specific practical investigations in the book", "414-419",
         "<ul><li><b>Intensity of solar power</b> at different angles and times; <b>wind velocity</b> at different heights and near obstacles; <b>heat loss</b> from containers with different insulation, surface areas and colours.</li>"
         "<li><b>Biotic indices for pollution:</b> lichens as indicators of SO<sub>2</sub> (crustose tolerant, fruticose sensitive); aquatic invertebrates with different oxygen requirements (stonefly and mayfly nymphs sensitive; tubifex and rat-tailed maggots tolerant). Advantages: integrate conditions over time, cheap, no equipment; limits: identification skill, other factors affect species, do not identify the pollutant or its concentration.</li>"
         "<li><b>Effect of pH on seed germination</b> (standardise seed type, temperature, water volume, light); <b>biomass growth</b> measured as dry mass; <b>factors affecting noise levels</b> - distance from source, acoustic insulation, barriers; <b>effect of trees on microclimate</b> (wind, humidity, light, temperature).</li></ul>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Mark-release-recapture", "nodes": [("c1", "Catch sample 1:\nmark M individuals", 0, 0), ("rel", "Release; allow\nto mix", 1, 0), ("c2", "Catch sample 2: C,\nof which R marked", 2, 0), ("n", "N = M x C / R", 3, 0)],
         "kinds": {"n": "hi"}, "edges": [("c1", "rel"), ("rel", "c2"), ("c2", "n")], "caption": "Genn pp. 401-402. Every assumption (closed population, harmless marks, equal catchability) is a possible exam question."},
    ],
    "numbers": ["Lincoln index N = MC/R", "Soil water: dry at 105 &deg;C; organic matter: ignite at about 500 &deg;C", "ACFOR abundance scale"],
    "exam": ["Complete a table of sampling activities and equipment (Nov 2020 Q1); describe a named method and its limitations.", "Calculate Lincoln index, Simpson's index, percentage water / organic matter (June 2022 Q9).",
             "Tullgren funnel method (June 2024 Q7); pitfall trap standardisation.", "Describe how an abiotic factor is measured and what must be standardised; explain calibration.", "Biotic indices: advantages and disadvantages."],
},
# =====================================================================
"stats": {
    "summary": "Statistics decide whether a difference or relationship is real. Replicates and standard deviation describe variability; significance and p-values quantify how unlikely a result is by chance; the test - Spearman's rank, chi-squared, t-test or Mann-Whitney U - is chosen to match the data and the question. Specialist technologies (imagery, DNA, sound, tracking, satellites) extend what can be monitored.",
    "sections": [
        ("Variability and the standard deviation", "420",
         "<p>Replicate readings are averaged, but a mean says nothing about spread. The <b>standard deviation</b> measures the scatter around the mean; in a normal distribution about 68% of values lie within 1 SD, 95% within 2 SD and 99.7% within 3 SD. Two means may differ, yet if their ranges overlap widely the difference may not be significant. <b>Error bars</b> (mean plus or minus 1 SD) on a graph give a quick visual check: overlapping bars suggest no significant difference. Also know mean, median and mode.</p>"),
        ("Significance and p-values", "421",
         "<p>Science never 'proves'; it estimates confidence. A result is <b>statistically significant</b> if it is unlikely to have arisen by chance - conventionally a probability (p) below 0.05 (95% confidence); p < 0.01 is stronger. The <b>null hypothesis</b> (no difference / no relationship) is rejected when p is below the chosen level. <b>Significance is not importance</b>, and a significant correlation does not prove causation: both variables may be driven by a third factor.</p>"),
        ("Choosing a statistical test", "421-423",
         "<table class=\"nt\"><tr><th>Question</th><th>Data</th><th>Test</th><th>Example hypotheses from the book</th></tr>"
         "<tr><td>Is there a correlation between two variables?</td><td>Paired values that can be ranked</td><td><b>Spearman's rank correlation coefficient</b> (r<sub>s</sub> from -1 to +1)</td><td>Crop yield rises with fertiliser; noise falls with distance from a road; earthworms decline as soil acidifies</td></tr>"
         "<tr><td>Do frequencies in categories differ from expected?</td><td>Counts in categories (not measurements)</td><td><b>Chi-squared test</b></td><td>Numbers of dormice in woodlands under different management; seeds per head in GM vs traditional wheat varieties</td></tr>"
         "<tr><td>Do two means differ?</td><td>Measured, normally distributed data</td><td><b>t-test</b></td><td>Lobster mass where collection is banned; dissolved oxygen in a polluted river; wind speed in woodland vs clearing</td></tr>"
         "<tr><td>Do two medians differ?</td><td>Counted or non-normal data, diversity indices</td><td><b>Mann-Whitney U test</b></td><td>Cars using a road after charging; biodiversity in hedges trimmed less often; bats over uncut grassland; seeds germinating at pH 5 vs 7</td></tr></table>"
         "<p>If it is uncertain whether data are normally distributed (common with small samples), use Mann-Whitney U rather than the t-test. The critical value depends on the number of pairs / samples and the significance level; compare the calculated statistic with the critical value from a table.</p>"),
        ("Specialist techniques used in ecological research", "402-407",
         "<ul><li><b>Imagery:</b> image databases of unique markings (tiger stripes, cheetah tails, whale-shark spots, dolphin fins, zebra stripes) identify individuals - territory, movements, lifespan, social groups; motion-sensitive cameras (visible by day, infrared at night); CCTV for nests with less disturbance.</li>"
         "<li><b>Marking:</b> rings, wing tags, collars; <b>DNA:</b> profiles identify individuals and gene pools; <b>eDNA</b> from shed cells detects species in water (great crested newts, invasive carp); DNA databases trace timber, ivory and fish to regional populations.</li>"
         "<li><b>Auditory:</b> bat detectors and sonograms for bats, dolphins, insects - presence, abundance, activity.</li>"
         "<li><b>Position monitoring:</b> radio, GPS and acoustic transmitters; geolocator tags (record time and light; position calculated on recapture) for small birds; <b>data recorders</b> for abiotic factors; <b>carrier systems</b> - ROVs and drones, AUVs, balloons, aircraft, satellites, animals.</li>"
         "<li><b>Satellites:</b> visible light for maps, land-use change, deforestation and flooding; infrared for vegetation density and temperature; weather sensors; radar microwaves (through cloud) for wind, sea-surface height, wave height and oil slicks; GPS for tracking.</li>"
         "<li><b>Indirect evidence:</b> nests, burrows, droppings (diet, gender, territory), feeding marks (hazel nuts opened by dormice), owl pellets, tracks, scratching posts.</li></ul>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Which statistical test?", "nodes": [("q", "What is the question?", 1, 0), ("cor", "Correlation between\ntwo variables?", 0, 1), ("diff", "Difference between\ntwo groups?", 2, 1), ("sp", "Spearman's rank", 0, 2), ("cat", "Counts in categories:\nchi-squared", 1, 2), ("mean", "Measured, normal:\nt-test (means)", 2, 2), ("mw", "Counted / not normal:\nMann-Whitney U (medians)", 3, 2)],
         "kinds": {"sp": "hi", "cat": "hi", "mean": "hi", "mw": "hi"}, "edges": [("q", "cor"), ("q", "diff"), ("cor", "sp"), ("diff", "cat"), ("diff", "mean"), ("diff", "mw")], "caption": "Based on the flow diagram, Genn p. 422."},
    ],
    "numbers": ["68% / 95% / 99.7% of values within 1 / 2 / 3 SD", "Significant if p < 0.05; strongly significant if p < 0.01", "Simpson's D = N(N-1) / sum n(n-1)"],
    "exam": ["Name the test for a scenario and justify it (Nov 2020 Q8, June 2022 Q4 net-design investigation, Nov 2021 Q9).", "Interpret p-values, error bars and standard deviations; explain correlation vs causation.",
             "Explain uses and limits of a monitoring technology (satellite radar, eDNA, geolocators).", "Complete a table matching technologies to applications."],
},
}
