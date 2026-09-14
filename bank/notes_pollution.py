"""Revision notes: Pollution (spec 3.4).  Genn pp. 236-304."""

NOTES = {
# =====================================================================
"pollutant-properties": {
    "summary": "How much harm a pollutant does depends on its properties - state, density, persistence, toxicity, reactivity, solubility, adsorption, mobility, synergism, mutagenic/carcinogenic/teratogenic action - and on environmental conditions such as temperature inversions, currents, pH and oxygen. Understanding both lets us predict where a pollutant goes and choose the control.",
    "sections": [
        ("Properties of pollutants", "236-240",
         "<table class=\"nt\"><tr><th>Property</th><th>Why it matters / examples</th></tr>"
         "<tr><td>State of matter</td><td>Solids deposit near the source (unless very fine); liquids flow and spread; gases disperse widely</td></tr>"
         "<tr><td>Energy form</td><td>Noise, heat and ionising radiation are pollutants that are energy not matter</td></tr>"
         "<tr><td>Density</td><td>Dense gases hug the ground (hydrogen cyanide at Bhopal); dense particles settle quickly; oil floats</td></tr>"
         "<tr><td>Persistence</td><td>Time before breakdown - non-persistent (sewage, pyrethroids) vs persistent (organochlorines, CFCs, heavy metals, radioisotopes with long half-lives); persistent pollutants travel far and accumulate</td></tr>"
         "<tr><td>Toxicity</td><td>Mode of action - enzyme inhibition (heavy metals, cyanide), neurotoxins (organophosphates block acetylcholinesterase), protein denaturation (acids); measured by LD50 / MDAF; some organisms are more sensitive</td></tr>"
         "<tr><td>Specificity</td><td>Range of organisms affected - Bt toxin only certain insects; organochlorines harm most animals</td></tr>"
         "<tr><td>Reactivity</td><td>Reactive pollutants may break down fast or form <b>secondary pollutants</b> (SO<sub>2</sub> to sulfuric acid, NOx and hydrocarbons to ozone and PANs)</td></tr>"
         "<tr><td>Adsorption</td><td>Sticking to clay, sediment or organic matter immobilises metals and caesium; used deliberately in activated carbon and ion exchange</td></tr>"
         "<tr><td>Solubility</td><td>Water-soluble pollutants (nitrate) disperse and leach; <b>liposoluble</b> ones (DDT, methyl mercury, PCBs) are stored in fat and <b>bioaccumulate</b> in individuals and <b>biomagnify</b> up food chains</td></tr>"
         "<tr><td>Synergism</td><td>Combined effect greater than the sum (smoke + SO<sub>2</sub>; ozone + SO<sub>2</sub>; neonicotinoids + fungicides)</td></tr>"
         "<tr><td>Mutagenic / carcinogenic / teratogenic</td><td>Damage DNA / cause cancer / cause birth defects; <b>gonadic</b> effects are inherited, <b>somatic</b> affect body cells; no safe dose so ALARA applies</td></tr>"
         "<tr><td>Mobility</td><td>How easily it moves through air, water and organisms; depends on state, solubility, adsorption</td></tr></table>"),
        ("Environmental factors affecting degradation and dispersal", "240-242",
         "<ul><li><b>Temperature</b> - faster chemical and biological breakdown when warm; <b>light</b> - photodegradation of some pesticides, but sunlight also creates photochemical smog; <b>oxygen</b> - aerobic decomposition of organic wastes, oxidation of SO<sub>2</sub>; anaerobic conditions convert mercury to methyl mercury; <b>pH</b> - controls solubility of metals (more soluble at low pH) and toxicity of ammonia; <b>adsorbent materials</b> present.</li>"
         "<li><b>Temperature inversions:</b> normally air cools with height so warm polluted air rises and disperses. An inversion - a warm layer above cool surface air, formed on clear still nights when the ground radiates heat, or in valleys, or under high pressure - traps pollutants near the ground (London 1952, Los Angeles). Sea breezes, wind and topography also govern dispersal.</li>"
         "<li><b>Water currents</b> and <b>river flow</b> dilute or concentrate; dispersal is faster in the atmosphere than in water or soil.</li></ul>"),
        ("Using properties to predict and control", "236-242",
         "<p>Non-persistent, water-soluble wastes may be safely diluted and dispersed (treated sewage into a fast river). Persistent, liposoluble or highly toxic pollutants must be contained or their use banned because dilution only spreads them into food chains. Reactive primary pollutants are controlled at source to prevent secondary pollutants. Knowledge of properties lets the likely behaviour of a new chemical be predicted from similar ones - the precautionary principle - and feeds Critical Pathway Analysis (see pollution control).</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Bioaccumulation and biomagnification of a persistent liposoluble pollutant", "nodes": [("w", "Water: 0.00005 ppm", 0, 0), ("p", "Plankton: 0.04 ppm", 1, 0), ("f", "Small fish: 0.5 ppm", 2, 0), ("b", "Large fish: 2 ppm", 3, 0), ("e", "Fish-eating bird: 25 ppm", 3, 1)],
         "kinds": {"e": "warn"}, "edges": [("w", "p"), ("p", "f"), ("f", "b"), ("b", "e")], "caption": "Illustrative DDT-type figures (Genn pp. 238-239). Each consumer eats many prey and stores the pollutant in fat, so concentration rises at each trophic level."},
        {"type": "layers", "title": "A temperature inversion traps pollutants", "side": "Height", "layers": [("Cool surface air", "Pollutants trapped below the warm layer"), ("Warm inversion layer", "Acts as a lid: rising air is no longer warmer than its surroundings"), ("Normal cooling with height", "Above the inversion air disperses as usual")],
         "caption": "Genn pp. 241-242. Forms on clear, still nights, in valleys and under high pressure - the conditions of the 1952 London smog."},
    ],
    "numbers": ["LD50 = dose killing 50% of a test population", "Bhopal 1984: dense hydrogen cyanide / methyl isocyanate cloud stayed at ground level"],
    "exam": ["Define properties and give an example pollutant for each; explain bioaccumulation vs biomagnification.", "Explain how temperature inversions form and why they matter (Nov 2021 Q5 atmosphere structure).",
             "Compare toxicity from LD50 or half-life data; explain synergism.", "9-mark and essays: how knowledge of properties reduces impacts (June 2023 essay; June 2024 essay on factors affecting dispersal and severity)."],
},
# =====================================================================
"pollution-control": {
    "summary": "Pollution control starts with predicting where a pollutant goes (Critical Pathway Analysis) and who is most exposed (Critical Group Monitoring), applies principles - polluter pays, precautionary, ALARA / BATNEEC - and chooses between preventing production, preventing release, remediating after release and switching to alternative processes. New technologies keep shifting what is achievable.",
    "sections": [
        ("Critical Pathway Analysis (CPA)", "243, 304",
         "<p>Predicts the movement of a potential pollutant to assess where and how severe pollution may be. If the pollutant would be diluted and dispersed harmlessly no action may be needed; if it would concentrate or reach sensitive sites, releases must be controlled. Mainly used for radioactive discharges. <b>Factors:</b> physical state of the effluent; meteorological conditions (wind speed and direction); river flow and ocean currents; geology and vegetation; effect of pH and oxygen on solubility; bioaccumulation and food-chain concentration; local food sources (fish, shellfish, seaweed, milk); half-lives of isotopes. Monitoring is then focused on the sites at risk and used to check the predictions.</p>"),
        ("Critical Group Monitoring (CGM)", "243, 304",
         "<p>Assesses the risk to the members of the public most exposed because of their lifestyle (eg people who eat a lot of local shellfish). If their risk is acceptably low, everyone else's is lower. It monitors <b>exposure</b> to prevent harm, not health damage after it has occurred; if the risk is unacceptable, emissions are reduced.</p>"),
        ("Emission control strategies", "243-244",
         "<ul><li><b>Control of emission location:</b> marine discharges where currents dilute and disperse; emissions downwind of urban areas; not discharging onto permeable rock above aquifers; tall chimneys.</li>"
         "<li><b>Control of emission timing:</b> avoid releasing during temperature inversions or low river flow; timed blasting; night-time bans on noisy activities.</li></ul>"),
        ("Principles of pollution control", "244-245",
         "<ul><li><b>Polluter pays principle:</b> whoever causes pollution is responsible for the damage, giving a financial incentive to prevent it when prevention costs less than the penalty - works only if enforcement is reliable and penalties high.</li>"
         "<li><b>Precautionary principle:</b> assume a waste will cause pollution until research shows it is unlikely to; ignorance of a problem is no excuse. Safer than release-and-see.</li>"
         "<li><b>Efficiency of control:</b> the cost-effectiveness curve is not linear - removing the last few per cent costs far more than the first. Zero emissions are rarely practical, so an acceptable level is set: emissions <b>As Low As Reasonably Achievable (ALARA)</b> using the <b>Best Available Technology Not Entailing Excessive Cost (BATNEEC)</b>. As cities and industries grow, original controls may no longer be sufficient.</li></ul>"),
        ("Selection of the control method", "244",
         "<table class=\"nt\"><tr><th>Approach</th><th>Examples</th></tr>"
         "<tr><td>Production prevention</td><td>Desulfurisation of fuels before combustion; low-temperature combustion to prevent NOx; smokeless fuels</td></tr>"
         "<tr><td>Prevention of release</td><td>Electrostatic precipitators, bag filters, cyclones; catalytic converters; flue-gas desulfurisation; bund walls; landfill liners</td></tr>"
         "<tr><td>Post-release remediation</td><td>Oil-spill clean-up; phytoremediation of contaminated land; liming acidified lakes</td></tr>"
         "<tr><td>Alternative processes</td><td>Electric vehicles; renewables instead of fossil fuels; pyrethroids instead of organochlorines; fuel cells</td></tr></table>"
         "<p>Prevention is generally cheaper and more complete than remediation, which rarely recovers all of a pollutant.</p>"),
        ("New technologies in pollution control", "303-304",
         "<p>The book's radioactive-waste section illustrates modern control: vitrification of high-level waste, encapsulation, engineered storage; worker monitoring with dosemeters and film badges; plus across the chapter - catalytic converters, diesel particulate filters, urea sprays for NOx, tertiary sewage treatment, bioremediation, ion exchange, activated carbon, satellite monitoring of oil slicks, eDNA and biotic indices for monitoring. Expect 'describe how a new technology reduces pollution' questions.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Critical Pathway Analysis for a coastal discharge", "nodes": [("eff", "Liquid effluent\n(state, isotopes, half-life)", 0, 1), ("cur", "Currents, dilution,\ndispersal", 1, 1), ("sed", "Adsorbed on\nsediments (pH, O2)", 2, 0), ("food", "Bioaccumulation in\nseaweed, shellfish, fish", 2, 2), ("crit", "Critical group:\npeople eating local seafood", 3, 2), ("mon", "Monitor these sites\nand people", 3, 1)],
         "kinds": {"crit": "warn", "mon": "hi"}, "edges": [("eff", "cur"), ("cur", "sed"), ("cur", "food"), ("food", "crit"), ("sed", "mon"), ("crit", "mon")],
         "caption": "Genn pp. 243 and 304. CPA predicts the pathways; CGM checks the exposure of the most-exposed group."},
        {"type": "chart", "title": "Cost of control rises steeply as emissions approach zero", "kind": "line", "x_label": "Proportion of pollution prevented / %", "y_label": "Cost / relative units",
         "series": {"Cost": [(0, 0), (20, 0.4), (40, 0.9), (60, 1.6), (80, 3.0), (90, 5.0), (95, 8.0), (99, 16.0)]}, "y_min": 0, "y_max": 18, "caption": "Why ALARA and BATNEEC set an acceptable level rather than zero (Genn p. 245)."},
    ],
    "numbers": ["ALARA: As Low As Reasonably Achievable; BATNEEC: Best Available Technology Not Entailing Excessive Cost"],
    "exam": ["Complete a table of technologies vs pollutants (June 2022 Q1, June 2024 Q1) or approaches vs examples.", "Explain CPA factors and why monitoring is focused; explain CGM.",
             "Explain polluter pays / precautionary principle and their limits.", "9-mark: evaluate principles and strategies; essays on control methods (Nov 2021) and new technologies (specimen)."],
},
# =====================================================================
"air-pollution": {
    "summary": "Smoke and smogs, acid rain gases, tropospheric ozone, carbon monoxide and hydrocarbons: each has characteristic sources, properties, effects and controls. Smoke and sulfur dioxide have been controlled successfully in developed countries; nitrogen oxides and photochemical smog from vehicles remain harder.",
    "sections": [
        ("Smoke and smoke smogs", "245-247",
         "<p><b>Smoke</b> is particulate matter from incomplete combustion of carbon-based fuels (coal, diesel, wood, wastes, crop burning). Classified by size - <b>PM10</b>, PM5, PM1 (micrometres); smaller particles stay airborne longer and penetrate deeper into the lungs. Carries toxic chemicals (fluorides, aluminium, lead, acids, phenol). <b>Effects:</b> respiratory disease, synergism with SO<sub>2</sub>, reduced light for photosynthesis, soiling of buildings, high albedo cooling the climate. <b>Smoke smogs</b> form under temperature inversions: the <b>London smog of 1952</b> killed about 12 000 people and led to the <b>Clean Air Act 1956</b> (smokeless zones, smokeless fuels, taller chimneys). <b>Industrial controls:</b> <b>electrostatic precipitators</b> (charged particles attracted to plates), <b>cyclone separators</b> (spinning gas throws particles to the wall), <b>bag filters</b>, <b>wet scrubbers</b>, more efficient combustion, diesel particulate filters, and switching to gas and electricity.</p>"),
        ("Photochemical smogs", "248-249",
         "<p>In sunny, still conditions (Los Angeles, Mexico City) NOx and unburnt hydrocarbons from vehicles react in sunlight to form <b>tropospheric ozone</b>, <b>PANs</b> (peroxyacetyl nitrates) and aldehydes - a brown haze that irritates eyes and lungs and damages plants. <b>Control:</b> catalytic converters, controlling hydrocarbons (vapour recovery at fuel stations, sealed fuel systems, better engine tuning, activated carbon canisters), reduced traffic, electric vehicles.</p>"),
        ("Acid rain", "250-252",
         "<p><b>Main gases:</b> <b>sulfur dioxide</b> (coal and oil combustion, smelting sulfide ores, volcanoes) oxidised to SO<sub>3</sub> and dissolved as sulfuric acid; <b>oxides of nitrogen</b> (high-temperature combustion in vehicles and power stations) forming nitric acid; also hydrochloric acid from burning PVC. Reactive and soluble, the gases travel hundreds of km before deposition (wet as rain, snow, fog; dry as gases and particles), so Scandinavian lakes were acidified by British and German emissions.</p>"
         "<p><b>Effects on non-living things:</b> corrosion of metals, dissolving of limestone and marble, damage to paint. <b>Effects on living organisms:</b> low pH denatures proteins in exposed cells - fish gills and eggs, root hairs, stomata; dissolves invertebrate exoskeletons; <b>indirect</b> effects through soil chemistry - leaching of calcium and magnesium (nutrient deficiency, yellowing of conifers) and mobilisation of toxic <b>aluminium</b> and lead which clog gills and damage roots; damage to leaf cuticle increasing frost and pathogen damage. <b>Severity</b> depends on bedrock: limestone and chalk neutralise acid (buffering); granite and acid soils cannot.</p>"
         "<p><b>Control of sulfur oxides:</b> <b>fuel desulfurisation</b> (coal washing, hydrodesulfurisation of oil, low-sulfur ship fuels); <b>flue-gas desulfurisation</b> - wet scrubbing with lime or limestone slurry producing gypsum, or dry injection; <b>fluidised-bed combustion</b> with limestone; switching from coal to gas or renewables. <b>Control of nitrogen oxides:</b> <b>catalytic converters</b> (platinum/rhodium reduce NOx to N<sub>2</sub>, oxidise CO and hydrocarbons; need unleaded fuel and a warm engine); lower combustion temperatures (fluidised beds, low-NOx burners, exhaust gas recirculation); <b>urea / ammonia sprays</b> (selective catalytic reduction) in power stations and lorries; liming of acidified lakes as remediation.</p>"),
        ("Tropospheric ozone", "253-254",
         "<p>A <b>secondary pollutant</b> formed when NO<sub>2</sub> is split by sunlight releasing an O atom that joins O<sub>2</sub>; hydrocarbons remove the NO that would otherwise destroy ozone, so it builds up. Effects: irritant, damages lungs, reduces crop yields and forest growth, degrades rubber and textiles, is a greenhouse gas. Control: as for photochemical smog - control NOx and hydrocarbons at source.</p>"),
        ("Carbon monoxide and hydrocarbons", "254",
         "<p><b>Carbon monoxide</b> from incomplete combustion (vehicles, faulty heaters) binds to haemoglobin more strongly than oxygen, causing headaches, reduced oxygen transport and death; controlled by catalytic converters and better combustion. <b>Hydrocarbons</b> (unburnt fuel, evaporation) - some carcinogenic (benzene), precursors of ozone; controlled by vapour recovery, converters, engine design.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Acid rain: from combustion to damage", "nodes": [("src", "Coal / oil combustion,\nsmelting, vehicles", 0, 1), ("so2", "SO2 + NOx\n(reactive, soluble)", 1, 1), ("ox", "Oxidised in air and\ndissolved in water droplets", 2, 1), ("dep", "Wet and dry deposition\nhundreds of km away", 3, 1), ("dir", "Direct: gills, roots,\nexoskeletons, stone", 3, 0), ("ind", "Indirect: Ca/Mg leached,\nAl mobilised", 3, 2)],
         "kinds": {"dir": "warn", "ind": "warn"}, "edges": [("src", "so2"), ("so2", "ox"), ("ox", "dep"), ("dep", "dir"), ("dep", "ind")], "caption": "Genn pp. 250-252. Severity depends on the bedrock's ability to neutralise acid."},
    ],
    "numbers": ["London smog 1952: about 12 000 deaths; Clean Air Act 1956", "PM10 = particles under 10 micrometres", "Catalytic converters need unleaded fuel and reach working temperature only when warm"],
    "exam": ["Explain how a particle analyser measures PM10 and why samples vary (June 2022 Q7, specimen Q8).", "Acid rain: direct and indirect harm to plants, seed germination investigation (Nov 2021 Q3).",
             "Describe control technologies for smoke, SO<sub>2</sub>, NOx (tables in June 2022 / June 2024 Q1).", "Explain why photochemical smog forms in sunny cities; tropospheric ozone chemistry.",
             "9-mark: properties of smoke and acid gases, effectiveness of controls; essay on technology and atmospheric pollution (Nov 2020)."],
},
# =====================================================================
"water-pollution": {
    "summary": "Water bodies are polluted most where dilution, oxygen and flow are lowest. Thermal pollution from cooling water lowers dissolved oxygen and alters communities; oil from tankers, pipelines, refineries and waste oil harms wildlife by toxicity, asphyxiation and loss of insulation - prevented by better tanker design and operation and cleaned up with booms, skimmers, absorbents, dispersants and bioremediation.",
    "sections": [
        ("Factors affecting water pollution", "255",
         "<p><b>Degradation</b> depends on temperature, light, oxygen and microbial activity; <b>removal rate</b> and <b>dispersal</b> depend on flow, currents, tides and volume. Water bodies most likely to be polluted: enclosed or slow-moving (lakes, estuaries, bays), low oxygen, high temperature, downstream of dense population or industry, shallow seas with restricted circulation (Baltic, Mediterranean).</p>"),
        ("Thermal pollution", "256-257",
         "<p><b>Source:</b> cooling water from power stations and industry discharged warmer than the river or sea. <b>Effects:</b> warm water holds less dissolved oxygen while raising metabolic rates and oxygen demand; changes in species composition (cold-water fish such as salmon and trout replaced by carp), earlier breeding, faster growth of algae and pathogens, thermal shock when discharge stops, altered migration. <b>Physiological changes:</b> enzyme activity, gas exchange, reproduction. <b>Control:</b> <b>cooling towers</b> (evaporation cools water before discharge or re-use), <b>cooling ponds</b>, using the heat (district heating, fish farms, greenhouses - CHP), discharging into fast-flowing or large water bodies, limits on discharge temperature.</p>"),
        ("Oil pollution: sources and effects", "258",
         "<p><b>Sources:</b> waste lubricating oil poured down drains (the largest source), ship tank washing, tanker and other ship accidents (Exxon Valdez, Torrey Canyon, MV Wakashio), refinery spills, pipeline leaks, leakage during drilling (Deepwater Horizon), natural seeps. <b>Effects:</b> <b>toxicity</b> (aromatic hydrocarbons poison organisms, especially larvae and corals); <b>asphyxiation</b> as oil coats gills, shores and sediments and blocks oxygen; <b>loss of insulation and buoyancy</b> in birds and mammals whose feathers and fur are matted, so they die of cold or drown; ingestion while preening; <b>less time to feed young</b>; food-chain effects and loss of tourism and fisheries.</p>"),
        ("Prevention of oil releases", "259-261",
         "<ul><li><b>Recycling of waste oil</b> and equipment maintenance to reduce leaks; <b>bund walls</b> around storage tanks.</li>"
         "<li><b>Improved tanker design:</b> <b>double hulls</b>, twin engines and rudders, separate ballast tanks, <b>inert gas</b> in tanks to prevent explosions.</li>"
         "<li><b>Improved tanker operation:</b> <b>load-on-top</b> and recirculation of washing water instead of discharging it, GPS and navigation systems, offshore shipping routes away from sensitive coasts, traffic separation, pilotage.</li>"
         "<li><b>Oil interceptors</b> in drains from garages and roads.</li></ul>"),
        ("Treatment of oil spills", "261-262",
         "<table class=\"nt\"><tr><th>Method</th><th>How it works / limits</th></tr>"
         "<tr><td>Inflatable booms</td><td>Floating barriers contain or divert the slick; fail in rough seas</td></tr>"
         "<tr><td>Skimmers</td><td>Recover floating oil from the surface for re-use</td></tr>"
         "<tr><td>Absorbent materials</td><td>Straw, polymers, peat soak up oil; must then be disposed of</td></tr>"
         "<tr><td>Polymerising agents</td><td>Turn oil into a solid that can be lifted</td></tr>"
         "<tr><td>Dispersants</td><td>Detergents break oil into droplets that disperse and degrade faster - but may be more toxic than the oil and spread it into the water column</td></tr>"
         "<tr><td>Steam washing</td><td>Cleans rocks but kills surviving organisms</td></tr>"
         "<tr><td>Bioremediation</td><td>Nutrients (and sometimes bacteria) added so natural microbes break the oil down; slow but low impact</td></tr></table>"),
    ],
    "diagrams": [
        {"type": "chart", "title": "Dissolved oxygen falls as water temperature rises", "kind": "line", "x_label": "Temperature / degrees C", "y_label": "Dissolved O2 / mg dm-3",
         "series": {"O2 at saturation": [(0, 14.6), (5, 12.8), (10, 11.3), (15, 10.1), (20, 9.1), (25, 8.3), (30, 7.6)]}, "y_min": 0, "y_max": 16,
         "caption": "Warm discharges lower oxygen just as organisms' oxygen demand rises (Genn pp. 256-257)."},
    ],
    "numbers": ["Waste lubricating oil is the largest source of oil pollution", "MV Wakashio (Mauritius, 2020) is the case in June 2023 Q9"],
    "exam": ["Explain effects of thermal pollution on dissolved oxygen and species; describe cooling towers.", "Sources of oil pollution and effects on birds; tanker design and operation improvements.",
             "Compare clean-up methods and their limits from a spill case study (June 2023 Q9).", "Explain why enclosed water bodies are most at risk."],
},
# =====================================================================
"pesticides": {
    "summary": "Pesticides are deliberately toxic, and their properties - toxicity, specificity, persistence, solubility, bioaccumulation and biomagnification, mobility, synergism - determine the harm to non-target species. Organochlorines, organophosphates, pyrethroids and neonicotinoids show different trade-offs, and impacts are reduced by restrictions, choice of pesticide, timing and application methods, and integrated control.",
    "sections": [
        ("Properties of pesticides that cause pollution", "262-264",
         "<ul><li><b>Toxicity:</b> measured as LD50 or the <b>MDNF</b> (maximum dose with no effect) / MDAF; some are neurotoxins (organophosphates inhibit acetylcholinesterase; neonicotinoids block acetylcholine receptors).</li>"
         "<li><b>Specificity:</b> broad-spectrum pesticides kill non-target species including pollinators and predators; specific ones (Bt, pheromones) do not.</li>"
         "<li><b>Persistence:</b> organochlorines last years; organophosphates days to weeks; pyrethroids break down in sunlight in days. Persistent pesticides travel and accumulate.</li>"
         "<li><b>Solubility:</b> water-soluble pesticides leach into water; liposoluble ones (DDT) <b>bioaccumulate</b> in fat and <b>biomagnify</b> along food chains - DDT thinned the eggshells of peregrines and sparrowhawks at the top of chains.</li>"
         "<li><b>Mobility:</b> spray drift, leaching, volatilisation, carried on soil particles and in food chains - DDT found in Antarctic penguins.</li>"
         "<li><b>Direct effects:</b> death of non-target insects, birds, fish; <b>indirect effects:</b> loss of food species, pollinators and predators (allowing pest resurgence), resistance in pests.</li></ul>"),
        ("The main pesticide groups", "264-265",
         "<table class=\"nt\"><tr><th>Group</th><th>Properties</th><th>Examples / issues</th></tr>"
         "<tr><td>Organochlorines</td><td>Very persistent, liposoluble, broad-spectrum, low vertebrate toxicity but bioaccumulate and biomagnify</td><td>DDT, dieldrin, lindane; bird of prey declines; banned in most countries</td></tr>"
         "<tr><td>Organophosphates</td><td>Non-persistent, water-soluble, very toxic to vertebrates including humans (neurotoxins)</td><td>Malathion, parathion; sheep dip; acute poisoning of farm workers</td></tr>"
         "<tr><td>Pyrethroids</td><td>Low persistence (photodegrade), low mammalian toxicity, but very toxic to fish and insects including bees</td><td>Permethrin, cypermethrin; replaced organochlorines</td></tr>"
         "<tr><td>Neonicotinoids</td><td>Systemic, water-soluble, moderately persistent; highly toxic to insects, low vertebrate toxicity (cannot cross the blood-brain barrier); sub-lethal effects on bee navigation, foraging and immunity; synergism with fungicides</td><td>Imidacloprid, acetamiprid; EU ban on outdoor use on flowering crops</td></tr></table>"),
        ("Methods of reducing pesticide pollution", "266",
         "<ul><li><b>Restrictions on use:</b> bans (organochlorines, neonicotinoids on flowering crops), licensing, maximum residue levels in food, buffer zones near water.</li>"
         "<li><b>Use of non-persistent pesticides</b> that break down before they spread; <b>use of more specific pesticides</b> (Bt toxin, hormone pesticides, pheromones).</li>"
         "<li><b>Use of systemic pesticides</b> - absorbed by the crop so only pests that eat it are affected, less spray on the surface (though neonicotinoids show the risk to pollinators via pollen).</li>"
         "<li><b>Application methods and timing:</b> spraying when crops are not in flower or at night when bees are not foraging; on still days to prevent drift; correct dose; seed coatings rather than sprays; targeted spraying with GPS.</li>"
         "<li><b>Alternatives:</b> cultural control, biological control, integrated pest management to minimise chemical use.</li></ul>"),
    ],
    "diagrams": [
        {"type": "chart", "title": "Persistence of pesticide groups in the environment (approximate half-life)", "kind": "bar", "x_label": "", "y_label": "Half-life / days",
         "series": {"Half-life": [("Pyrethroids", 5), ("Organophosphates", 20), ("Neonicotinoids", 150), ("Organochlorines (DDT)", 3000)]}, "y_min": 0, "y_max": 3500,
         "caption": "Orders of magnitude, not precise values (Genn pp. 263-265). Persistence governs how far a pesticide travels and whether it accumulates."},
    ],
    "numbers": ["DDT: persistent, liposoluble, biomagnified - eggshell thinning in peregrines", "Neonicotinoids: EU restrictions on outdoor use on flowering crops"],
    "exam": ["Explain how named properties cause impacts on non-target species (dose-response graphs, LD50).", "Compare pesticide groups; explain why systemic pesticides do not affect insects landing on crops (Nov 2021 Q6).",
             "Pesticide residues in food and MRLs (Nov 2020 Q9, 15 marks).", "9-mark: neonicotinoids and bees; methods of reducing pesticide pollution; essay on pesticide properties."],
},
# =====================================================================
"nutrient-pollution": {
    "summary": "Organic wastes deoxygenate water through microbial respiration and spread pathogens; inorganic nutrients cause eutrophication and threaten drinking water. Sewage treatment (pre-treatment, primary, secondary, sludge digestion, tertiary) controls point sources well; diffuse agricultural nitrate and phosphate are harder. Acid mine drainage and water-quality monitoring complete the topic.",
    "sections": [
        ("Cultural eutrophication (inorganic nutrients)", "267-268",
         "<p><b>Sources of nitrate:</b> leached fertiliser, manure and slurry, sewage effluent, atmospheric NOx; <b>sources of phosphate:</b> sewage (including detergents), eroded soil, manure. <b>Process:</b> nutrients stimulate algal blooms; algae shade submerged macrophytes which die; cyanobacteria release toxins; when the algae die decomposition by aerobic bacteria and night-time respiration deoxygenate the water, killing fish and invertebrates; diversity falls and pollution-tolerant species (tubifex worms, midge larvae) dominate. <b>Human health:</b> nitrate converted to nitrite in babies' stomachs causes <b>methaemoglobinaemia</b> ('blue baby syndrome'); nitrosamines are possible carcinogens. <b>Control:</b> <b>Nitrate Vulnerable Zones</b> restricting fertiliser timing and amount, low-solubility and organic fertilisers, legumes and rotation, buffer strips along rivers, manure storage, phosphate-free detergents, tertiary sewage treatment, removal of nutrient-rich sediment, aeration of lakes, biomanipulation.</p>"),
        ("Organic nutrients: sources and effects", "269",
         "<p><b>Sources:</b> sewage, farm slurry and manure, silage effluent, food processing, paper mill and tannery effluent. <b>Deoxygenation:</b> organic matter is food for aerobic bacteria whose respiration removes dissolved oxygen; a <b>sag curve</b> develops downstream of a discharge with recovery as organic matter is used up and re-aeration occurs; sewage fungus and bacterial growths coat the bed. <b>Pathogens:</b> cholera, typhoid, dysentery, polio spread by faecal contamination. <b>Inorganic nutrient release</b> from decay then causes eutrophication.</p>"),
        ("Sewage treatment", "269-273",
         "<ol><li><b>Pre-treatment:</b> screens remove litter; grit channels settle sand.</li><li><b>Primary treatment:</b> sedimentation tanks - suspended solids settle as sludge (removes most organic matter).</li>"
         "<li><b>Secondary treatment:</b> aerobic microbes digest dissolved and fine organic matter - <b>activated sludge</b> (aeration tanks with recirculated bacterial floc) or <b>trickling / percolating filter beds</b> (effluent sprinkled over stones coated with microbial film); followed by final settlement.</li>"
         "<li><b>Sludge treatment:</b> <b>anaerobic digestion</b> produces methane (biogas) for energy and a sludge used as fertiliser or landfilled; heavy metals limit use on land.</li>"
         "<li><b>Tertiary treatment</b> where needed: <b>phosphate stripping</b> with iron(III) sulfate or alum, <b>denitrification</b> in anaerobic filter beds, micro-strainers, sand filters, UV or chlorine disinfection, reed beds.</li></ol>"
         "<p><b>Collection systems:</b> combined sewers carry rain and sewage, so storm overflows discharge untreated sewage after heavy rain; separate systems avoid this but cost more.</p>"),
        ("Acid mine drainage", "273",
         "<p>Water percolating through spoil or old workings containing sulfide minerals (pyrite) is oxidised by air and bacteria to sulfuric acid, dissolving iron and other metals; the orange iron hydroxide ('ochre') coats river beds. Low pH and metals kill fish and invertebrates. <b>Control:</b> sealing and flooding mine workings to exclude oxygen, diverting water, limestone channels and treatment lagoons to raise pH and precipitate metals, constructed wetlands, covering spoil with impermeable material and vegetation.</p>"),
        ("Monitoring water pollution", "273-275",
         "<ul><li><b>Biochemical oxygen demand (BOD):</b> oxygen used by microbes in a sample over 5 days at 20 &deg;C - a measure of organic pollution; <b>chemical oxygen demand (COD)</b> uses an oxidising chemical, quicker but includes non-biodegradable matter.</li>"
         "<li><b>Coliform count</b> - bacteria indicating faecal contamination; nitrate, phosphate, dissolved oxygen, pH, turbidity and temperature meters.</li>"
         "<li><b>Biotic indices</b> (Trent Biotic Index, BMWP score): invertebrates with known pollution tolerance (mayfly and stonefly nymphs sensitive; tubifex, rat-tailed maggots tolerant) - integrate conditions over time, cheap, but need identification skill, are affected by other factors and do not identify the pollutant.</li></ul>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Sewage treatment stages", "nodes": [("pre", "Pre-treatment:\nscreens, grit", 0, 0), ("prim", "Primary:\nsedimentation", 1, 0), ("sec", "Secondary: activated\nsludge / filter beds", 2, 0), ("tert", "Tertiary: P stripping,\ndenitrification, UV", 3, 0), ("sl", "Sludge: anaerobic\ndigestion -> biogas", 1, 1), ("out", "Effluent to river", 3, 1)],
         "kinds": {"out": "hi"}, "edges": [("pre", "prim"), ("prim", "sec"), ("sec", "tert"), ("tert", "out"), ("prim", "sl"), ("sec", "sl")], "caption": "Genn pp. 269-272 (June 2022 Q10 asked for the stages in a table)."},
        {"type": "chart", "title": "Oxygen sag curve downstream of an organic discharge", "kind": "line", "x_label": "Distance downstream / km", "y_label": "Dissolved oxygen / %",
         "series": {"DO": [(0, 95), (2, 55), (5, 25), (8, 20), (12, 35), (18, 60), (25, 85), (30, 93)]}, "y_min": 0, "y_max": 100,
         "caption": "Aerobic decomposition removes oxygen; re-aeration and depletion of the waste allow recovery (Genn p. 269)."},
    ],
    "numbers": ["BOD: oxygen used over 5 days at 20 &deg;C", "Primary sedimentation removes most organic solids; tertiary treatment is expensive so used only where needed"],
    "exam": ["Complete a table of sewage treatment stages (June 2022 Q10, 15 marks); explain phosphate stripping.", "Explain eutrophication step by step and nitrate health effects.",
             "Acid mine drainage effects on pH and wildlife (June 2022 P2 Q7); harebell and nitrogen deposition (Nov 2021 Q9).", "Biotic indices vs chemical monitoring - advantages and limits.", "9-mark: evaluate control of organic vs inorganic nutrient pollution."],
},
# =====================================================================
"heavy-metals": {
    "summary": "Lead, mercury, cadmium and other heavy metals are persistent, mostly neurotoxic, and their toxicity depends on chemical form - organic (methyl) mercury and tetraethyl lead are the most dangerous because they are liposoluble and biomagnify. Control means removing them from products and effluents and storing wastes where they stay insoluble.",
    "sections": [
        ("Key properties", "275",
         "<p>Dense metals that are <b>persistent</b> (elements cannot be broken down), <b>toxic</b> at low concentrations (inhibit enzymes, damage nervous systems, kidneys and liver), often <b>liposoluble</b> in organic forms so they <b>bioaccumulate and biomagnify</b>, and whose <b>solubility rises at low pH</b> - so acid rain and acid mine drainage mobilise them, and alkaline conditions immobilise them. <b>Synergism</b> between metals increases toxicity.</p>"),
        ("Lead", "275-276",
         "<p><b>Sources:</b> historically tetraethyl lead in petrol (anti-knock), lead water pipes and solder, lead paint, lead shot and fishing weights, smelting, batteries. <b>Effects:</b> neurotoxin - reduced IQ and behavioural problems in children, anaemia, kidney damage; poisoning of swans and wildfowl that swallow shot and weights. <b>Control:</b> unleaded petrol (also needed for catalytic converters), replacement of lead pipes and use of copper / tin solder, <b>phosphoric acid dosing</b> of water so an insoluble lead phosphate lining forms in old pipes, lead-free paint, bans on lead shot over wetlands and on lead weights, filters on smelters, battery recycling. Blood lead in children has fallen by over 80% since petrol lead was removed.</p>"),
        ("Mercury", "276-277",
         "<p><b>Sources:</b> chlor-alkali plants using mercury electrodes, coal combustion, gold mining (amalgamation), batteries, thermometers, fluorescent lamps, dental amalgam, waste incineration. <b>Forms:</b> elemental liquid mercury is poorly absorbed (vapour is dangerous); inorganic compounds are moderately toxic; <b>methyl mercury</b>, made by anaerobic microbes in sediments, is liposoluble, crosses the blood-brain barrier and placenta, and biomagnifies in fish. <b>Minamata, Japan (1950s):</b> a chemical factory discharged inorganic mercury into the bay; methylated in sediments, concentrated in fish and shellfish, it caused neurological damage, paralysis and birth defects in thousands of people. <b>Control:</b> replacing mercury in electrodes, thermometers and batteries, activated carbon and ion exchange for effluents, reverse osmosis, flue-gas cleaning, safe disposal of lamps.</p>"),
        ("Cadmium and iron", "277-279",
         "<p><b>Cadmium</b> occurs with zinc ores; sources are zinc smelting, phosphate fertiliser, batteries, pigments, electroplating, sewage sludge. Effects: kidney damage, bone disease (itai-itai disease in Japan from contaminated rice), carcinogen; absorbed by crops from contaminated soil. Control: substitution, recycling of batteries, effluent treatment, limits on sludge use. <b>Iron</b> is not toxic in itself but iron-rich drainage (acid mine drainage, ochre) smothers river beds and blocks gills; controlled by treating mine water.</p>"),
        ("General control measures", "276-279",
         "<p>Removal from effluent by <b>ion exchange</b>, <b>reverse osmosis</b>, <b>activated carbon</b>, precipitation as insoluble hydroxides or sulfides at high pH; storage of wastes under <b>alkaline conditions</b> in sealed sites; <b>phytoremediation</b> of contaminated land; substitution of the metal; recycling of products; monitoring of food and water.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Minamata: how a low-toxicity discharge became a disaster", "nodes": [("d", "Inorganic mercury\ndischarged to bay", 0, 0), ("sed", "Anaerobic sediments:\nmicrobes make methyl mercury", 1, 0), ("bio", "Liposoluble: bioaccumulates\nin plankton -> fish", 2, 0), ("ppl", "People eating fish:\nneurological damage", 3, 0)],
         "kinds": {"ppl": "warn"}, "edges": [("d", "sed"), ("sed", "bio"), ("bio", "ppl")], "caption": "Genn pp. 276-277. Chemical form and food-chain concentration turned dilution into disaster."},
    ],
    "numbers": ["Blood lead in children fell over 80% after lead was removed from petrol", "Methyl mercury crosses the blood-brain barrier; inorganic mercury largely does not"],
    "exam": ["Explain why toxicity depends on chemical form (mercury); Minamata case (specimen Q7).", "Lead in petrol / pipes and control measures; calculate percentage decreases from blood-lead data.",
             "Explain why heavy metal wastes are stored at high pH; why acid drainage mobilises metals.", "Complete a table of pollutant / source / control (June 2022 Q1)."],
},
# =====================================================================
"solid-waste": {
    "summary": "Solid wastes from mining, construction, industry and homes grow with affluence. Landfill, incineration, composting and recycling each have properties, advantages and problems; hazardous and specialist wastes need encapsulation or vitrification; and good site management prevents leachate, gas and instability.",
    "sections": [
        ("Sources and properties of solid waste", "279-280",
         "<ul><li><b>Mining and construction wastes:</b> overburden, spoil, rubble - large volume, mostly inert but may be unstable or contain metals.</li>"
         "<li><b>Industrial waste:</b> may be toxic, flammable, radioactive; <b>domestic (municipal) waste:</b> paper, plastics, food, glass, metals, textiles.</li>"
         "<li><b>Properties that determine disposal:</b> toxicity, flammability, degradability, radioactivity, volume, whether mixed or separated.</li>"
         "<li><b>Waste production and affluence:</b> richer societies buy more, use packaging and disposable goods and replace rather than repair; waste per capita rises with income.</li></ul>"),
        ("Landfill", "280-282",
         "<p>Waste is tipped, compacted and covered. <b>Problems:</b> anaerobic decay releases <b>methane</b> (explosive, greenhouse gas); rain percolating through produces toxic <b>leachate</b> that can pollute groundwater and rivers; vermin, litter, smell, land take; slow decomposition. <b>Features of good management:</b> impermeable clay or polymer <b>liner</b>; leachate collection and treatment; methane collection pipes and use as fuel; daily cover; compaction; separate cells for different wastes; final capping, drainage and restoration to grassland, woodland or amenity use; monitoring boreholes. <b>Spoil heaps</b> from mining: instability (Aberfan 1966), acid drainage, dust; managed by regrading, compaction, drainage, covering with soil and vegetation; some old heaps have become valuable habitats.</p>"),
        ("Incineration", "283-284",
         "<p>Burning at high temperature reduces volume by about 90% and mass by 70%, destroys pathogens and organic toxins, and can generate electricity and heat (energy from waste). <b>Disadvantages:</b> expensive, needs fuel for wet waste, produces acid gases (HCl, SO<sub>2</sub>, NOx), heavy metals and <b>dioxins</b> if combustion is poor, toxic fly ash needing hazardous landfill, discourages recycling. <b>Features of good incinerators:</b> high temperatures (over 850 &deg;C) and rapid cooling to prevent dioxin formation, flue-gas scrubbing and filters, energy recovery, ash stored at high pH so metals stay insoluble.</p>"),
        ("Composting, recycling and waste reduction", "280, 284",
         "<p><b>Composting</b> and <b>anaerobic digestion</b> of organic waste return nutrients and (for AD) yield biogas; <b>recycling</b> saves energy and raw materials but mixed, contaminated waste is hard to separate; <b>waste minimisation</b> - reduced packaging, repair, re-use, design for disassembly - is highest in the waste hierarchy. Choice of method depends on the waste's properties, population density, land availability, energy prices and legislation (landfill tax, recycling targets).</p>"),
        ("Specialist wastes", "284-285",
         "<ul><li><b>Asbestos:</b> fibres cause asbestosis and mesothelioma; removed by licensed contractors, double-wrapped, buried in recorded specialist landfill; intact bonded asbestos may be left encapsulated.</li>"
         "<li><b>Cyanide, heavy-metal and chemical wastes:</b> neutralised, precipitated, incinerated or landfilled in hazardous sites.</li>"
         "<li><b>Encapsulation:</b> waste mixed with cement and sealed in impermeable containers; <b>vitrification:</b> waste (especially high-level radioactive) mixed with molten glass that stays stable even if it shatters.</li>"
         "<li><b>Electronic waste (WEEE):</b> toxic metals and valuable rare metals; producer-responsibility rules require collection and recycling.</li></ul>"),
    ],
    "diagrams": [
        {"type": "chart", "title": "How UK municipal waste treatment has changed (illustrative)", "kind": "bar", "x_label": "", "y_label": "% of waste", "categories": ["Landfill", "Incineration", "Recycling/composting"],
         "series": {"2000": [("Landfill", 79), ("Incineration", 9), ("Recycling/composting", 11)], "2020": [("Landfill", 14), ("Incineration", 42), ("Recycling/composting", 43)]}, "y_min": 0, "y_max": 100,
         "caption": "Landfill tax and recycling targets drove the shift (Genn pp. 280-284). Incineration with energy recovery grew fastest."},
    ],
    "numbers": ["Incineration cuts volume by ~90%; dioxins avoided above ~850 &deg;C with rapid cooling", "Aberfan 1966: spoil-heap failure"],
    "exam": ["Describe features of a well-managed landfill; explain leachate and methane problems.", "Advantages / disadvantages of incineration; why ash needs careful disposal.",
             "Specialist wastes: asbestos, encapsulation vs vitrification.", "Explain how affluence affects waste production; factors in choosing a disposal method."],
},
# =====================================================================
"noise": {
    "summary": "Noise is energy pollution measured on the logarithmic decibel scale. It harms hearing, health and behaviour in people and disturbs breeding, feeding and communication in wildlife. Aircraft, railways, roads, industry and homes each have characteristic sources controlled by design, operation and location, and measured with weighted and time-averaged scales.",
    "sections": [
        ("The decibel scale and hearing", "286",
         "<p>The dB scale is <b>logarithmic</b>: every 10 dB is a tenfold increase in sound intensity, so 90 dB is 1000 times 60 dB, and a 3 dB rise doubles intensity. Human hearing spans roughly 20 Hz to 20 kHz and is most sensitive around 1-4 kHz; the <b>dBA</b> scale weights frequencies to match the ear. Threshold of hearing 0 dB, conversation about 60 dB, damage with prolonged exposure above about 85 dB, pain around 130 dB.</p>"),
        ("Effects of noise", "287",
         "<ul><li><b>Humans:</b> hearing damage (temporary threshold shift, permanent loss, tinnitus); <b>stress-related</b> problems - raised blood pressure, sleep disturbance, poor concentration, anxiety; behavioural effects; annoyance depends on frequency, timing, pitch changes and whether the noise is expected.</li>"
         "<li><b>Other organisms:</b> masking of communication (birdsong, whale calls), abandonment of nests and feeding grounds, hearing damage and stranding of cetaceans from sonar and piling, reduced breeding success near roads and airports; some species habituate.</li></ul>"),
        ("Aircraft noise", "288-292",
         "<ul><li><b>Airport design and location:</b> away from population centres; taxiways and engine-test areas away from housing; acoustic walls and baffle mounds; land-use planning that stops housing near flight paths; grants for double glazing and insulation.</li>"
         "<li><b>Engine design:</b> <b>high-bypass-ratio turbofans</b> (more air bypasses the core so exhaust is slower and quieter), chevron nozzles, acoustic liners, hush kits on older engines.</li>"
         "<li><b>Body design:</b> fairings over undercarriage, smoother surfaces, composite materials, blended wing-body concepts.</li>"
         "<li><b>Operation:</b> steeper take-off climb, flight paths avoiding urban areas, continuous descent approaches, reduced use of reverse thrust, night curfews, <b>Chapter noise limits</b> certifying aircraft, noise charges and fines, <b>noise quota</b> counts per airport, noise monitors checking compliance.</li></ul>"),
        ("Railway, road, industrial and domestic noise", "292-294",
         "<table class=\"nt\"><tr><th>Source</th><th>Controls</th></tr>"
         "<tr><td>Railway: wheel-rail vibration, squeal on corners, brakes, pantograph turbulence</td><td>Track polishing / grinding, sound-absorbing ballast and suspension, wheel and rail lubrication on curves, composite brakes, pantograph fairings, continuous welded rail, barriers</td></tr>"
         "<tr><td>Road traffic: engine, exhaust, tyre-road, aerodynamics - affects the most people</td><td>Porous / rubber-crumb asphalt, quieter tyres, engine insulation and aerodynamics, speed limits, traffic routing and calming, acoustic fences and embankments, tree belts, double glazing, electric vehicles</td></tr>"
         "<tr><td>Industrial: compressors, pumps, stamping, pile-driving, blasting</td><td>Silencers, enclosures, pressing instead of stamping, nylon rollers, drilling instead of piling, bubble curtains around marine piling, timing of blasting, acoustic mats and curtains, remote operation, ear protection as a last resort</td></tr>"
         "<tr><td>Domestic: appliances, music, DIY, dogs</td><td>Acoustic absorbers in appliances, volume limiters, quieter appliance selection, insulation between dwellings, by-laws on hours</td></tr></table>"),
        ("Measuring noise pollution", "294-295",
         "<p>Sound-level meters give dB(A). <b>L<sub>eq</sub></b> is the equivalent continuous level over a period; <b>L<sub>10</sub></b> (level exceeded 10% of the time) is used for road traffic; airport <b>noise contours</b> (eg 57 dB L<sub>eq</sub>) map affected areas and define compensation; <b>Perceived Noise Level (PNdB)</b> and <b>effective perceived noise level (EPNdB)</b> are used for aircraft certification; measurements must standardise distance, height, weather and time.</p>"),
    ],
    "diagrams": [
        {"type": "chart", "title": "Noise level falls with distance from a point source (inverse square law)", "kind": "line", "x_label": "Distance from source / m", "y_label": "Noise level / dB",
         "series": {"Level": [(10, 90), (20, 84), (50, 76), (100, 70), (200, 64), (300, 60.5), (500, 56)]}, "y_min": 40, "y_max": 100,
         "caption": "Doubling distance reduces the level by about 6 dB (Genn pp. 288, 295; June 2024 Q4 used a similar graph)."},
    ],
    "numbers": ["10 dB = 10x intensity; 3 dB = 2x; doubling distance = -6 dB", "Hearing damage risk above ~85 dB with long exposure; 57 dB L<sub>eq</sub> contour marks airport annoyance"],
    "exam": ["Use a noise-distance graph; explain environmental factors affecting the level reaching residents (June 2024 Q4).", "Exposure time vs noise level graph (June 2023 Q8).",
             "Aircraft noise contours and airport design (Nov 2020 Q4); railway sources and controls; motorway noise (specimen Q2).", "Explain the logarithmic scale; why small dB reductions matter.", "9-mark: control by design, operation and location with named examples."],
},
# =====================================================================
"radiation": {
    "summary": "Ionising radiation is used in medicine, industry, research and nuclear power but damages DNA, causing cancers, mutations and birth defects. Risk depends on the type of radiation, half-life, dose and route of exposure. Control follows ALARA: closed sources, shielding, distance, time, monitoring, and careful management of wastes and discharges using CPA and CGM.",
    "sections": [
        ("Uses of ionising radiation", "295-296",
         "<ul><li><b>Industry:</b> thickness gauges (beta), weld and casting inspection (gamma radiography), polymer cross-linking, sterilisation of products, smoke detectors (americium), tracers for leaks, well logging in oil exploration.</li>"
         "<li><b>Healthcare:</b> X-rays, CT scans, radiotherapy (cobalt-60, linear accelerators), tracers such as technetium-99m for imaging, sterilising equipment.</li>"
         "<li><b>Scientific research:</b> radiocarbon dating, tracers in ecology and physiology.</li><li><b>Agriculture and food:</b> irradiation to kill pests and pathogens and extend shelf life; sterile insect technique.</li>"
         "<li><b>Nuclear fission and fusion</b> for electricity.</li></ul>"),
        ("Risk : benefit analysis and sources of exposure", "297-299",
         "<p>Decisions weigh benefits (cancer treatment, low-carbon electricity) against risks - hard because cancers appear years later with many possible causes, exposure data are poor, and those who benefit are often not those at risk. <b>Sources of exposure:</b> <b>radon</b> from granite and uranium-rich rock (about half of the average UK dose), cosmic radiation (higher at altitude and in aircraft), gamma rays from rocks and buildings, internal potassium-40 and carbon-14, medical procedures (the largest artificial source), occupational exposure, consumer products, nuclear industry discharges (under 1%), fallout from weapons tests and accidents (Chernobyl 1986, Fukushima 2011).</p>"),
        ("Types of radiation and half-life", "299-300",
         "<table class=\"nt\"><tr><th>Type</th><th>Nature</th><th>Penetration</th><th>Relative harm</th></tr>"
         "<tr><td>Alpha</td><td>Helium nuclei (2p 2n)</td><td>Stopped by paper / skin; a few cm of air</td><td>Very damaging if inhaled or ingested - weighting factor 20</td></tr>"
         "<tr><td>Beta</td><td>Electrons</td><td>Stopped by a few mm of aluminium</td><td>Weighting factor 1</td></tr>"
         "<tr><td>Gamma</td><td>High-energy electromagnetic</td><td>Reduced by thick lead or concrete</td><td>Weighting factor 1; external hazard</td></tr>"
         "<tr><td>Neutrons</td><td>Particles from fission</td><td>Need water / concrete</td><td>Cause activation of other materials</td></tr></table>"
         "<p><b>Half-life:</b> time for half the atoms to decay. Short half-lives (technetium-99m, 6 h) give intense but brief exposure - useful medically; long half-lives (plutonium-239, 24 000 years; caesium-137, 30 years; strontium-90, 28 years) mean wastes stay hazardous for generations. Strontium behaves like calcium (bones), iodine-131 concentrates in the thyroid, caesium like potassium in muscle.</p>"),
        ("Effects on living tissue", "301",
         "<p>Ionisation produces free radicals that break DNA and proteins. <b>Acute</b> high doses cause radiation sickness and death; <b>chronic</b> low doses raise cancer risk (leukaemia, thyroid) with no safe threshold. <b>Somatic</b> effects affect the exposed person; <b>gonadic</b> (genetic) effects are passed on; <b>teratogenic</b> effects harm the foetus. <b>Exposure</b> (external source) ends when you move away; <b>contamination</b> (material on or in the body) continues to irradiate. <b>Activation products</b> form when neutrons make stable atoms radioactive, eg reactor components.</p>"),
        ("Principles of control and strategies to reduce exposure", "302-303",
         "<ul><li><b>ALARA / BATNEEC</b>; <b>closed sources</b> (sealed so material cannot escape); <b>remote handling</b>; <b>shielding / absorbers</b> (lead, concrete, water); <b>distance</b> - intensity falls with the inverse square law; <b>limiting time</b>; protective clothing and respirators; <b>decontamination</b>; <b>potassium iodide</b> tablets to block iodine-131 uptake; dose limits for workers and public.</li>"
         "<li><b>Monitoring:</b> personal dosemeters, <b>film badges</b> (cumulative), air monitors for alpha particles, contamination monitors at exits; environmental monitoring by CPA and CGM.</li>"
         "<li><b>Units:</b> becquerel (activity), <b>gray</b> (absorbed dose, J kg<sup>-1</sup>), <b>sievert</b> (effective dose = grays x weighting factor).</li></ul>"),
        ("Waste management", "303",
         "<table class=\"nt\"><tr><th>Category</th><th>Examples</th><th>Management</th></tr>"
         "<tr><td>High-level</td><td>Spent fuel, fission products</td><td>Cooled in ponds, <b>vitrified</b> in glass in stainless steel containers, stored (Sellafield) pending deep geological disposal</td></tr>"
         "<tr><td>Intermediate-level</td><td>Fuel cladding, reactor components, filters</td><td>Encapsulated in cement in steel drums; stored</td></tr>"
         "<tr><td>Low-level solid</td><td>Clothing, equipment</td><td>Compacted, sealed, buried in engineered concrete-lined landfill (Drigg)</td></tr>"
         "<tr><td>Low-level liquid / gas</td><td>Reprocessing effluents, gases</td><td>Filtered, ion exchange, then discharged under authorisation with CPA / CGM</td></tr></table>"),
    ],
    "diagrams": [
        {"type": "chart", "title": "Radioactive decay: activity halves every half-life", "kind": "line", "x_label": "Number of half-lives", "y_label": "Activity / % of original",
         "series": {"Activity": [(0, 100), (1, 50), (2, 25), (3, 12.5), (4, 6.25), (5, 3.1), (6, 1.6)]}, "y_min": 0, "y_max": 100,
         "caption": "After 10 half-lives about 0.1% remains. Caesium-137 (30 y) takes 300 years; plutonium-239 (24 000 y) takes 240 000 (Genn p. 300)."},
    ],
    "numbers": ["Radon ~50% of average dose; nuclear industry <1%", "Alpha weighting factor 20; beta and gamma 1", "Sv = Gy x weighting factor; Cs-137 30 y, Sr-90 28 y, Pu-239 24 000 y"],
    "exam": ["Compare isotopes by half-life and radiation type to judge health risk (June 2022 Q2, June 2024 Q9 Fukushima caesium).", "Explain exposure vs contamination; somatic vs gonadic effects.",
             "Describe strategies to reduce worker exposure and how they are monitored.", "9-mark: evaluate risks and benefits of ionising radiation; waste management by category."],
},
}
