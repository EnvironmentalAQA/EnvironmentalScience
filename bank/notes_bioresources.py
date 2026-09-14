"""Revision notes: Biological resources (spec 3.5) and Sustainability (spec 3.6).  Genn pp. 306-389."""

NOTES = {
# =====================================================================
"agroecosystems": {
    "summary": "Agriculture raises food output above what the natural ecosystem would give by controlling abiotic factors (temperature, light, water, nutrients, aeration, salinity, pH, CO2, topography, wind) and biotic factors (pests, pollinators, soil biota). Each control has costs and side effects; integrated control uses the least damaging combination.",
    "sections": [
        ("The principles of agriculture", "306",
         "<p>Farmers select species suited to the environment, then modify the environment towards each species' optimum. The more the environment is modified, the higher the yield but the greater the inputs of energy and materials. Factors that affect crops and livestock are the same abiotic and biotic factors that shape natural ecosystems.</p>"),
        ("Abiotic factors and their control", "307-314",
         "<table class=\"nt\"><tr><th>Factor</th><th>Importance</th><th>Control</th></tr>"
         "<tr><td>Temperature</td><td>Enzyme activity, growth rate, frost damage, livestock stress</td><td>Greenhouses and polytunnels, cloches, mulches, windbreaks, heated housing, choosing planting dates and sites (south-facing slopes)</td></tr>"
         "<tr><td>Light</td><td>Photosynthesis; day length triggers flowering and breeding</td><td>Artificial lighting, greenhouses, planting density and orientation, pruning, shading</td></tr>"
         "<tr><td>Water</td><td>Crops: transport, turgor, photosynthesis; livestock: drinking, cooling</td><td>Irrigation (spray, drip, flood), drainage of waterlogged land, soil organic matter to hold water, drought-tolerant varieties</td></tr>"
         "<tr><td>Soil nutrients</td><td>N for proteins, P for DNA and ATP, K for enzymes; micronutrients</td><td>Inorganic fertilisers (fast, precise, but soluble, energy-intensive, leach), organic fertilisers (manure, compost, sewage sludge - slow release, improve structure, bulky); application by broadcasting, placement, foliar spray, fertigation; legumes; hydroponics</td></tr>"
         "<tr><td>Aeration</td><td>Roots and aerobic soil organisms need oxygen</td><td>Ploughing, avoiding compaction (lighter machinery, low tyre pressure), drainage, adding organic matter</td></tr>"
         "<tr><td>Salinity</td><td>Salt build-up from irrigation reduces water uptake</td><td>Drip irrigation, flushing with fresh water, drainage, salt-tolerant varieties</td></tr>"
         "<tr><td>pH</td><td>Nutrient availability, aluminium toxicity, biota</td><td>Lime to raise pH; sulfur or acidic fertiliser to lower it</td></tr>"
         "<tr><td>Carbon dioxide</td><td>Limiting factor in enclosed greenhouses</td><td>CO<sub>2</sub> enrichment from burners</td></tr>"
         "<tr><td>Topography and relief</td><td>Slope affects erosion, drainage, machinery, aspect affects temperature</td><td>Terracing, contour ploughing, land levelling</td></tr>"
         "<tr><td>Wind velocity</td><td>Physical damage, soil erosion, increased water loss, livestock chilling</td><td>Windbreaks, hedges, shelter belts</td></tr></table>"),
        ("Biotic factors: pest control", "314-319",
         "<p><b>Pest groups:</b> insects (aphids also spread viruses; locusts), nematodes, fungi (blight, rust), bacteria and viruses, weeds (competition), molluscs, mammals and birds. <b>Cultural control:</b> crop rotation breaks pest cycles, weeding, mulching, barrier crops, companion planting, timing of sowing, removal of crop residues, resistant varieties, <b>predator habitats</b> (hedgerows, beetle banks, field margins). <b>Biological control:</b> introducing predators or parasites - ladybirds and Encarsia (aphids, whitefly), Cactoblastis (prickly pear), Bt bacteria; risks if the agent attacks non-targets. <b>Pheromone traps</b> monitor or confuse mating; <b>sterile insect technique</b> (medfly). <b>GM crops</b> with Bt toxin or herbicide tolerance. <b>Chemical pesticides:</b> effective and fast but resistance, non-target impacts, residues (see pesticides); <b>hormone pesticides</b> disrupt insect development; <b>antibiotics</b> in livestock (resistance concerns). <b>Integrated pest management</b> combines monitoring, cultural and biological methods and uses chemicals only when pest numbers exceed a threshold.</p>"),
        ("Pollinators and soil biota", "320",
         "<p>Many crops (fruit, oilseed rape, beans) depend on insect pollination - hives are moved to orchards; pollinators are protected by pesticide timing and wildflower margins. <b>Soil biota</b> (bacteria, fungi, earthworms, detritivores) recycle nutrients, fix nitrogen, form mycorrhizal associations, improve structure, aeration and drainage; maintained by organic matter, reduced tillage, avoiding compaction and limiting pesticides.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Integrated pest management", "nodes": [("mon", "Monitor pest numbers\n(traps, counts)", 0, 0), ("cult", "Cultural control:\nrotation, resistant varieties,\npredator habitats", 1, 0), ("bio", "Biological control:\npredators, parasites, Bt", 2, 0), ("thr", "Above economic\nthreshold?", 1, 1), ("chem", "Targeted, specific,\nnon-persistent pesticide", 2, 1)],
         "kinds": {"chem": "warn"}, "edges": [("mon", "cult"), ("cult", "bio"), ("bio", "thr"), ("thr", "chem", "only if yes")], "caption": "Genn p. 319. Chemicals are the last resort, minimising cost, resistance and non-target damage."},
    ],
    "numbers": ["Legumes fix nitrogen through Rhizobium in root nodules", "Cactoblastis moth controlled prickly pear in Australia; Encarsia wasp controls whitefly in greenhouses"],
    "exam": ["Complete a table of agricultural terms (specimen Q1 strawberries); explain how a named abiotic factor is controlled and the side effects.", "Compare inorganic and organic fertilisers; explain hydroponics.",
             "Explain biological control examples and risks; sterile insect technique calculation (Nov 2021 Q5).", "Soil pH and crop yield investigation (specimen Q7); worldwide pesticide use trends (June 2024 Q5).", "Essays: reducing impacts of crop production (June 2023)."],
},
# =====================================================================
"food-species": {
    "summary": "Yields are raised by controlling the genetics of crops and livestock - asexual reproduction and cloning, selective and cross-breeding, artificial insemination and embryo transfer, genetic modification - and by understanding agricultural energetics: intensity, energy subsidies, energy ratios, food conversion ratios and the trophic level at which food is produced.",
    "sections": [
        ("Control of genetics: asexual reproduction", "321",
         "<p><b>Plants:</b> natural asexual reproduction (strawberry runners) and artificial propagation from cuttings or tissue culture (micropropagation) give genetically identical offspring - predictable, high survival, but no variation for improvement and fewer offspring than seed. <b>Animals - cloning:</b> nucleus from a donor cell placed in an enucleated egg, implanted in a surrogate; applications: replacing valuable animals, restocking after disease culls, multiplying elite individuals; still being developed.</p>"),
        ("Sexual reproduction: selective and cross-breeding", "322-323",
         "<p>Offspring combine genes from two parents so characteristics are unpredictable; producing a breed with desired traits and without unwanted ones takes generations. <b>Selective breeding</b> chooses parents for traits - Limousin cattle (muscle growth), Belted Galloway (milk, growth), Highland (hardy, even temper), Large White and Tamworth pigs (bacon, litters), Merino (wool), Cheviot sheep (hardy, foot-rot resistant); but breeding similar individuals risks inbreeding. <b>Cross-breeding</b> between breeds combines traits with <b>hybrid vigour</b> (heterosis) and fewer homozygous recessive problems - Zebu (heat tolerant, low milk) x Ayrshire (high milk, not heat tolerant) gives heat-tolerant high-yield cattle. <b>Artificial insemination:</b> semen from a selected male impregnates many females; frozen semen is transported and stored easily. <b>Embryo transfer:</b> FSH stimulates a selected female to release many eggs; fertilised in vitro and implanted in surrogates so she produces far more offspring.</p>"),
        ("Genetic modification (transgenics)", "323-324",
         "<p>GM transfers single genes between species, beyond what selective breeding (limited to the species' gene pool) can do. <b>Case studies:</b> <b>Roundup Ready soya</b> (glyphosate resistance gene from Agrobacterium - weeds sprayed without harming the crop); <b>Bt crops</b> (Bacillus thuringiensis toxin gene in maize, corn, cotton - kills insect pests, less spraying); <b>Golden rice</b> (daffodil and Erwinia genes make vitamin A in the grain against blindness in India and Africa); <b>omega-3 oilseed rape</b> (gene from a marine alga). <b>Advantages:</b> single traits without unwanted ones; genes from unrelated species; less pesticide; disease resistance; higher nutrition. <b>Concerns:</b> allergies; gene transfer to gut bacteria or to wild relatives and organic crops via pollen (Bt gene in wild plants killing insects); crossing into the food chain from animal-feed varieties; antibiotic-resistance marker genes; cost and seed patents disadvantaging LEDC farmers; loss of local crop diversity and seed saving; more evidence needed - so the precautionary principle has delayed adoption.</p>"),
        ("Intensive and extensive agriculture", "324-325",
         "<p><b>Intensive</b> farming uses large inputs per unit area where land is scarce - high yield per hectare but not necessarily per unit of input; <b>extensive</b> farming spreads limited inputs over a large area. The <b>law of diminishing returns</b>: each extra unit of input raises yield by less than the last, so if land is available, spreading inputs thinly gives a greater total yield. Uneven global use of inputs is partly rational (some land is more productive) and partly economic (affluent farmers can buy more).</p>"),
        ("Energy subsidies and energy ratios", "325-326",
         "<p>An <b>energy subsidy</b> is any input that aids productivity but needs energy: manufacture of nitrate fertiliser (Haber process) and pesticides, pumping irrigation water, fuel for machinery, embodied energy of equipment, grain drying, food processing and transport. Intensive systems depend on fossil-fuel subsidies. <b>Energy ratio</b> = food energy output / energy input: wheat and rice several units out per unit in; beef and milk below 1 - productive per hectare but inefficient. <b>Food conversion ratio</b> = mass of feed per unit mass gained: farmed salmon about 1.2, chicken about 2, pork 3-4, beef 6-10 - lower is better.</p>"),
        ("Control of food chain energy losses", "326-328",
         "<p><b>Autotrophs</b> capture light (photoautotrophs) or chemical energy (chemoautotrophs); <b>heterotrophs</b> depend on them. Of 100 000 units of solar energy about 4 000 are captured in photosynthesis and 1 000 stored in biomass; each trophic level loses most energy as heat in respiration, so few chains exceed four levels. Hence <b>plant food gives most food per hectare</b>; where crops cannot grow (uplands, semi-arid areas), grazing sheep and cattle with cellulose-digesting gut bacteria is best; omnivorous pigs convert food wastes; keeping livestock warm, restricting movement and choosing young fast-growing animals reduce losses.</p>"),
    ],
    "diagrams": [
        {"type": "chart", "title": "Law of diminishing returns", "kind": "line", "x_label": "Inputs / arbitrary units", "y_label": "Yield / arbitrary units",
         "series": {"Yield": [(0, 20), (1, 50), (2, 70), (3, 82), (4, 90), (5, 94)]}, "y_min": 0, "y_max": 100, "caption": "Each extra unit of input adds less yield (Genn p. 325)."},
        {"type": "flow", "title": "Energy flow through an agroecosystem (units from 100 000 of sunlight)", "nodes": [("sun", "Sunlight 100 000", 0, 0), ("lost", "Reflected, transmitted,\nwrong wavelength", 1, 1), ("cap", "Captured in\nphotosynthesis 4 000", 1, 0), ("resp", "Plant respiration\n(heat)", 2, 1), ("bio", "Crop biomass 1 000", 2, 0), ("live", "Livestock: ~10%\npasses on", 3, 0)],
         "kinds": {"bio": "hi"}, "edges": [("sun", "cap"), ("sun", "lost"), ("cap", "bio"), ("cap", "resp"), ("bio", "live")], "caption": "Genn p. 327. Eating crops directly captures more food energy per hectare than feeding them to animals."},
    ],
    "numbers": ["Energy ratios: wheat / rice several : 1; beef, milk below 1", "FCR: salmon ~1.2, chicken ~2, pork 3-4, beef 6-10", "100 000 units sun -> 4 000 captured -> 1 000 in biomass"],
    "exam": ["Compare breeding methods; explain AI and embryo transfer; hybrid vigour.", "GM case studies, advantages and concerns; Bt corn pollen investigation (June 2023 Q7, 15 marks).",
             "Calculate energy ratios and FCRs and interpret them (June 2023 Q6, Nov 2020 Q6); micropropagation (June 2022 Q6).", "Explain diminishing returns and intensive vs extensive.", "Embodied energy losses along the food chain (Nov 2021 Q10); essay on genetic manipulation (Nov 2021)."],
},
# =====================================================================
"agri-impacts": {
    "summary": "Agriculture destroys and creates habitats, introduces species, pollutes with pesticides and nutrients, releases greenhouse gases, alters the hydrological cycle and erodes soil. Social, economic and political factors - consumer choice, technology, grants, guaranteed markets, surpluses and agri-environment schemes - shape how farming is done, and a range of strategies can make it sustainable.",
    "sections": [
        ("Habitat impacts", "328-329",
         "<p>Farmland replaced forest and grassland on fertile land; even where habitat is not destroyed it is changed - <b>drainage</b> kills wetland species, <b>nutrient enrichment</b> lets grasses outcompete wildflowers, and <b>reduced biodiversity</b> follows as diverse indigenous communities are replaced by few, often non-native, species and predators and competitors are removed. Yet farming also created valuable <b>plagioclimax habitats</b>: hedgerows, hay meadows, grazed moorland and heathland, chalk grassland.</p>"),
        ("Introduced species and pollution", "329",
         "<p>Crops and livestock escape to become pests; pests arrive accidentally (potato late blight); biological control agents may eat non-targets. <b>Pesticides</b> kill non-target species and disrupt relationships; <b>nutrient pollution</b> - leached nitrate causes eutrophication, manure deoxygenates water; <b>nitrate toxicity</b> in drinking water (blue baby syndrome, possible carcinogen).</p>"),
        ("Climate change, water and soil", "330",
         "<p><b>Greenhouse gases:</b> CO<sub>2</sub> from fuel, ploughing (soil organic matter decomposition) and the <b>embodied energy</b> of fertiliser and machinery; <b>methane</b> from livestock digestion, manure and rice padi; <b>nitrous oxide</b> from manure and nitrate fertiliser. <b>Hydrological cycle:</b> irrigation depletes rivers and aquifers; erosion and compaction reduce water retention and speed runoff; evapotranspiration changes. <b>Soil erosion</b> where management is poor (see soils).</p>"),
        ("Social factors", "330-331",
         "<p>Consumer choices shape production: <b>cultural</b> (horsemeat) and <b>religious</b> (pork, beef) restrictions; <b>ethical</b> concerns; <b>local food and food miles</b>; <b>seasonal food</b> avoiding heated glasshouses and air freight; <b>free-range</b> livestock; <b>organic</b> food; <b>Fairtrade</b> guaranteeing producers an income for water, education and health.</p>"),
        ("Availability of technology", "331-332",
         "<p>Machinery, pesticides, fertilisers, improved breeds and infrastructure (transport, refrigeration, processing) are concentrated in affluent countries. <b>Survey technology</b> - GPS mapping, drones and satellites monitoring photosynthesis, biomass, soil moisture, pests and cropped area; computer <b>yield mapping</b> guides variable fertiliser application, maximising yield and minimising waste and pollution (precision agriculture).</p>"),
        ("Economic and political influences: Europe since 1945", "332-334",
         "<ol><li><b>Food aid</b> from the USA prevented post-war famine.</li><li><b>Grants</b> let farmers invest - hedgerow removal, machinery, drainage, improved livestock, liming - raising output but destroying hedgerows and wetlands.</li>"
         "<li><b>Guaranteed market:</b> governments bought surplus to hold prices at an agreed level and released stores in poor years - stability, but by the 1970s permanent <b>surpluses</b> (butter mountains, wine lakes) that could not be sold to other MEDCs, afforded by Eastern Europe or dumped on LEDCs without ruining local farmers.</li>"
         "<li><b>Reducing surpluses:</b> <b>quotas</b> (milk), <b>farm diversification</b> (tourism, cheese, ice cream), alternative crops and livestock (biofuels, pharmaceutical poppies, llamas, deer), <b>set-aside</b> payments for taking land out of production, and <b>agri-environment schemes</b> - Environmentally Sensitive Areas, Countryside Stewardship, Environmental Stewardship - paying for hedgerows (2 m no-spray margins, cutting only every two years, not in the bird breeding season), ditches, dry-stone walls, in-field trees, field margins sown with tussocky grasses, skylark plots, nectar and seed plants, stocking-density limits, woodland management and rhododendron control.</li></ol>"),
        ("Strategies to increase agricultural sustainability", "335-337",
         "<p>Only humans raise the carrying capacity of their environment; the population may reach 12 billion, so sustainable production matters more than ever. Agriculture began about 12 000 years ago in the fertile crescent, whose productivity declined - as has land in the US mid-west, parts of the UK, cleared rainforest and much of Africa - through erosion, nutrient and water loss and pest problems, answered unsustainably with fertilisers, pesticides and unrecharged groundwater. About 10% of land is cultivated and 25% grazed; little suitable land remains, and importing food can price local people out of their own land. <b>Organic agriculture</b> is not just the absence of chemicals but the positive use of natural processes for nutrients, pests and services.</p>"
         "<table class=\"nt\"><tr><th>Unsustainable feature</th><th>Sustainable strategy</th></tr>"
         "<tr><td>Reliance on chemical pesticides (resistance, non-target species, bans)</td><td>Cultural control, biological control, predator habitats, polyculture, integrated control, reduced antibiotics</td></tr>"
         "<tr><td>Non-renewable rock phosphate; fossil-fuel nitrate manufacture</td><td>Recycling organic matter, crop rotation, legumes, conservation of soil biota, less artificial fertiliser, low tillage</td></tr>"
         "<tr><td>Over-exploitation of rivers and groundwater; salinisation</td><td>Low water-use crops, reservoirs and aquifer recharge, drip irrigation, avoiding saline water</td></tr>"
         "<tr><td>Loss of soil organic matter; CO<sub>2</sub> from fuel; methane from rice and livestock</td><td>Low-tillage farming, less machinery, renewable energy, drought-tolerant rice drained earlier, ground high-carbohydrate cattle feed</td></tr>"
         "<tr><td>Loss of species providing pest control, nutrients and pollination; loss of crop wild relatives</td><td>Retain hedgerows, ditches, ponds, woodland; maintain soil biota; conserve CWR habitats; seed banks</td></tr></table>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "European agricultural policy since 1945", "nodes": [("aid", "Food aid\n(post-war shortage)", 0, 0), ("gr", "Grants: machinery,\ndrainage, hedgerow removal", 1, 0), ("gm", "Guaranteed market:\nprice support", 2, 0), ("sur", "Surpluses by\nthe 1970s", 3, 0), ("red", "Quotas, set-aside,\ndiversification", 3, 1), ("aes", "Agri-environment\nschemes", 2, 1)],
         "kinds": {"sur": "warn", "aes": "hi"}, "edges": [("aid", "gr"), ("gr", "gm"), ("gm", "sur"), ("sur", "red"), ("red", "aes")], "caption": "Genn pp. 332-334. Each policy solved the previous problem and created the next."},
    ],
    "numbers": ["About 10% of land cultivated, 25% grazed", "Population may reach 12 billion this century; agriculture began ~12 000 years ago in the fertile crescent", "Hedgerow rules in schemes: no spraying within 2 m, cut at most every 2 years, not in breeding season"],
    "exam": ["Explain how named agricultural changes affect habitats, hydrology or climate; farm income and subsidies calculation (June 2023 Q8).", "Describe ethical, quota and political influences (June 2024 Q6); explain the surplus problem and methods to reduce it.",
             "Describe features of agri-environment schemes and why they benefit wildlife.", "9-mark: strategies for sustainable agriculture; essays on crop production, livestock, food systems and climate adaptation."],
},
# =====================================================================
"fishing": {
    "summary": "Marine productivity is limited by light and nutrients, so most fish come from upwellings and shelf seas. Fishing methods differ in selectivity and habitat damage; overfishing, by-catch, ghost fishing and seabed damage are reduced by quotas, gear design, effort limits, method bans and no-take zones, guided by maximum sustainable yield estimates that are hard to obtain.",
    "sections": [
        ("Marine productivity", "338-339",
         "<p>Only a small part of the ocean is productive. <b>Light</b> penetrates about 100 m (less in turbid water), so photosynthesis by algae is confined to the <b>photic zone</b>; deeper life depends on sinking organic matter. <b>Nutrients:</b> CO<sub>2</sub> is abundant but phosphate, being poorly soluble, is often limiting; it is supplied by river runoff and <b>upwelling</b> of cold deep water where currents hit seamounts, storms mix shallow seas, or offshore winds pull surface water away (Peru, West Africa). <b>Seasonal patterns:</b> tropical oceans have light and warmth all year but low nutrients - low productivity; temperate oceans peak in spring (light rises, winter storms have mixed up nutrients), decline as nutrients are used, with a small autumn bloom; Antarctic waters bloom in the 24-hour summer light. Fresh waters are productive per area but small in total.</p>"),
        ("Fishing methods", "340-341",
         "<table class=\"nt\"><tr><th>Method</th><th>Target</th><th>Notes</th></tr>"
         "<tr><td>Demersal trawling</td><td>Seabed species: cod, haddock, plaice, shrimps, scampi</td><td>Chains and balls disturb the seabed; mixed catches, high by-catch, habitat damage</td></tr>"
         "<tr><td>Demersal long lines</td><td>Cod, haddock</td><td>Baited hooks on the bottom; less habitat damage</td></tr>"
         "<tr><td>Shellfish traps / pots</td><td>Crabs, lobsters, crayfish</td><td>Selective; lost pots ghost-fish</td></tr>"
         "<tr><td>Pelagic trawling</td><td>Mid-water shoals: herring, mackerel, bass, anchovies</td><td>Single-species shoals so low by-catch, but porpoises and dolphins caught</td></tr>"
         "<tr><td>Drift nets</td><td>Tuna, herring near the surface</td><td>Non-selective curtains catching whales, dolphins, turtles, sharks - banned or restricted</td></tr>"
         "<tr><td>Purse seining</td><td>Tuna, sardines, anchovies</td><td>Net closed under a shoal; efficient and fairly selective</td></tr>"
         "<tr><td>Pelagic long lines</td><td>Tuna, squid</td><td>Lines many km long; drown albatrosses, catch sharks and turtles</td></tr></table>"),
        ("Environmental impacts of fishing", "341-344",
         "<ul><li><b>Population decline:</b> mortality exceeds births; <b>k-selected</b> species (orange roughy, bluefin tuna, sharks, common skate, Greenland shark maturing at 100-150 years) are most vulnerable because they may be caught before breeding and recover slowly; <b>r-selected</b> herring and mackerel recover faster. As local stocks fall, fleets fish further away.</li>"
         "<li><b>By-catch:</b> unwanted catch - immature target fish, over-quota fish that must be discarded, non-commercial species; shrimp trawling by-catch can be 99% of the catch; most discards die.</li>"
         "<li><b>Ghost fishing</b> by lost gear; <b>habitat damage</b> - trawls mix aerobic and anaerobic sediment layers and destroy sea fans and deep corals, damage coral reefs and seagrass nurseries; <b>dynamite fishing</b> on reefs; <b>food-web impacts</b> on competitors, prey and predators.</li></ul>"),
        ("Methods of reducing impacts", "344-346",
         "<ul><li><b>Catch quotas</b> (total allowable catch divided among boats) - work for single-species pelagic shoals; in mixed fisheries over-quota fish are discarded dead.</li>"
         "<li><b>Gear design:</b> minimum <b>mesh size</b>; <b>square-mesh escape panels</b> (diagonal mesh closes as the net fills; square panels stay open so small fish escape); <b>turtle exclusion devices</b>; <b>acoustic deterrents</b> (pingers) for dolphins; <b>curved hooks</b>, decoys, weighted lines and night setting to protect albatrosses; <b>biodegradable</b> and radio-tracked traps against ghost fishing.</li>"
         "<li><b>Restricted fishing effort:</b> boat size and engine power, days at sea, licences, decommissioning payments.</li>"
         "<li><b>Restricted methods:</b> drift-net bans or length limits; demersal trawling banned on sensitive seabeds (Rockall Bank, Hatton Bank, Darwin Mounds).</li>"
         "<li><b>No Take Zones:</b> large (Chagos, Great Barrier Reef zones, Easter Island) and small (Lundy, Lamlash Bay) - breeding stocks recover and surplus spills over, raising catches outside; closed seasons and minimum / maximum landing sizes.</li></ul>"),
        ("Maximum sustainable yield", "348-351",
         "<p><b>MSY</b> is the largest catch that can be taken indefinitely - the population's maximum growth rate, at roughly half the carrying capacity. <b>Estimating it needs data</b> that are hard to get: fish are mobile, unevenly distributed and hidden; sampling a representative fraction of the sea is impractical. <b>Data from catches:</b> total catch, <b>catch per unit effort</b> (falling CPUE shows decline even when total catch is maintained by more effort or technology), mean size and age from scales and otoliths (falling age structure shows overfishing). <b>Data from research:</b> egg and larval surveys, trawl surveys, tagging, acoustic surveys. The Russell formula S<sub>2</sub> = S<sub>1</sub> + (A + G) - (C + M) links stock at the start and end of a year to recruitment, growth, catch and natural mortality.</p>"),
    ],
    "diagrams": [
        {"type": "chart", "title": "Seasonal productivity in a temperate ocean", "kind": "line", "x_label": "Month", "y_label": "Relative value",
         "series": {"Light": [(1, 10), (3, 40), (5, 80), (6, 100), (8, 85), (10, 40), (12, 10)], "Nutrients": [(1, 100), (3, 90), (5, 40), (6, 20), (8, 15), (10, 50), (12, 95)], "Phytoplankton": [(1, 10), (3, 30), (4, 95), (5, 60), (7, 25), (9, 45), (10, 30), (12, 10)]}, "y_min": 0, "y_max": 110,
         "caption": "Spring bloom when light rises while winter-mixed nutrients are still high; autumn storms give a second smaller bloom (Genn p. 339)."},
        {"type": "chart", "title": "Sustainable yield curve", "kind": "line", "x_label": "Population size (% of carrying capacity)", "y_label": "Annual growth = sustainable catch",
         "series": {"Growth": [(0, 0), (10, 18), (25, 38), (40, 48), (50, 50), (60, 48), (75, 38), (90, 18), (100, 0)]}, "y_min": 0, "y_max": 60,
         "caption": "Growth (and so the sustainable catch) is greatest at about half the carrying capacity - the MSY (Genn p. 348)."},
    ],
    "numbers": ["Photic zone: light to about 100 m", "Shrimp trawl by-catch up to 99%; albatrosses lay one egg every second year", "MSY at roughly half carrying capacity; Russell formula S2 = S1 + (A+G) - (C+M)"],
    "exam": ["Explain why productivity differs between upwellings, shelf seas and open ocean (Nov 2020 Q8).", "Compare fishing methods and their by-catch; explain gear modifications (June 2022 Q4).",
             "Explain vulnerability of k-selected species with data (specimen Q9, 15 marks); sustainable exploitation grades (June 2024 Q7); lobster monitoring (Nov 2021 Q7).", "Calculate S2 from the Russell formula; explain CPUE.", "9-mark: evaluate methods to reduce fishing impacts; essay on fishing impacts (June 2023)."],
},
# =====================================================================
"aquaculture": {
    "summary": "Aquaculture farms fish, shellfish and algae by controlling breeding, feeding, competition, predation, disease and abiotic conditions. It is growing fast as wild catches stagnate, but carnivorous species still depend on fishmeal, and impacts - habitat loss, pollution, disease, escapes - must be managed, ideally through polyculture, IMTA, aquaponics and closed systems.",
    "sections": [
        ("Principles and species", "352-353",
         "<p>The main species: <b>algae</b> (seaweed for food, alginates), <b>molluscs</b> (mussels, oysters - filter feeders needing no feed), <b>crustaceans</b> (shrimp, prawns), <b>fish</b> (carp, tilapia, catfish - herbivores/omnivores; salmon, trout, sea bass - carnivores). <b>Choice of species</b> depends on market value, growth rate, food conversion ratio, tolerance of crowding, ease of breeding in captivity, disease resistance and local conditions.</p>"),
        ("Control of biotic factors", "354",
         "<ul><li><b>Pests and disease:</b> high densities spread parasites (sea lice) and pathogens; controlled by vaccination, antibiotics (resistance risk), pesticides, cleaner fish (wrasse) eating lice, fallowing sites, lower densities, water treatment.</li>"
         "<li><b>Competition and predation:</b> cages exclude competitors; nets, scarers and culling deter seals, birds and otters.</li>"
         "<li><b>Nutrition:</b> formulated feed for growth; carnivores need fishmeal and oil from wild forage fish (sandeels, anchovies) - competing with wild predators such as puffins; plant-based and insect feeds are being developed.</li></ul>"),
        ("Control of abiotic factors", "355",
         "<p><b>Temperature</b> (warm water speeds growth but lowers oxygen; heated water from power stations can be used), <b>dissolved oxygen</b> (aerators, water flow), <b>water flow and quality</b> (removing wastes, salinity), <b>light</b> (photoperiod control of maturation), <b>nutrients</b> for algae and pond productivity.</p>"),
        ("Salmon aquaculture and control of limiting factors", "356",
         "<p>Hatchery breeding from selected broodstock (light and temperature control maturation; hormones induce spawning; all-female or sterile triploid stock avoids early maturation); fry reared in freshwater tanks, smolts moved to sea cages; fed pelleted feed; harvested at 2-3 years. Selective breeding raises growth rate and disease resistance.</p>"),
        ("Polyculture, IMTA, aquaponics and rice-fish systems", "357-358",
         "<p><b>Polyculture</b> stocks species using different foods and depths (Chinese carp species) so total yield rises and wastes are used; manure or fertiliser boosts pond plankton. <b>Integrated multi-trophic aquaculture</b> places seaweed and shellfish downstream of fish cages to absorb dissolved nutrients and particulate waste. <b>Aquaponics</b> combines fish tanks with hydroponic crops that clean the water. <b>Rice-fish systems</b> raise fish in flooded paddies where they eat pests and fertilise the crop. Fish have very low basal metabolic rates (no thermoregulation, water supports their weight), giving low FCRs.</p>"),
        ("Environmental impacts and how they are reduced", "359",
         "<table class=\"nt\"><tr><th>Impact</th><th>Reduction</th></tr>"
         "<tr><td>Habitat loss - mangroves cleared for shrimp ponds</td><td>Siting away from sensitive habitats, replanting, protected areas</td></tr>"
         "<tr><td>Organic waste (uneaten feed, faeces) deoxygenating water; nutrient release</td><td>Lower stocking density, sites with strong currents, IMTA, closed recirculating systems, fallowing</td></tr>"
         "<tr><td>Chemicals - pesticides, antibiotics, antifoulants</td><td>Vaccines, cleaner fish, restricted use, resistance monitoring</td></tr>"
         "<tr><td>Disease and parasites spreading to wild fish</td><td>Lower densities, fallowing, siting away from wild migration routes</td></tr>"
         "<tr><td>Escapes breeding with wild fish (gene-pool contamination)</td><td>Stronger cages, sterile triploids, land-based tanks</td></tr>"
         "<tr><td>Predator control killing seals and birds</td><td>Nets and acoustic deterrents rather than culling</td></tr>"
         "<tr><td>Fishmeal demand depleting forage fish</td><td>Herbivorous species, plant and insect feeds, filter feeders</td></tr></table>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Integrated multi-trophic aquaculture", "nodes": [("feed", "Feed", 0, 0), ("fish", "Fish cages", 1, 0), ("part", "Particulate waste", 2, 1), ("diss", "Dissolved nutrients", 2, 0), ("sea", "Seaweed absorbs\nnutrients", 3, 0), ("shell", "Mussels / sea cucumbers\nfilter particles", 3, 1)],
         "kinds": {"sea": "hi", "shell": "hi"}, "edges": [("feed", "fish"), ("fish", "diss"), ("fish", "part"), ("diss", "sea"), ("part", "shell")], "caption": "Genn p. 357. Wastes of one species become the food of the next - a circular-economy principle."},
    ],
    "numbers": ["Farmed salmon FCR about 1.2 - fish need no heat or support", "Wild catch flat since ~1990 while aquaculture output approaches it"],
    "exam": ["Explain how disease and abiotic factors are controlled (June 2024 Q8, 15 marks; Nov 2021 Q8 temperature investigation).", "Polyculture and manure in lakes (specimen Q6); shrimp farming in India (June 2023 Q9).",
             "Explain impacts and how they are reduced; escapes and gene pools.", "9-mark: can aquaculture replace fishing? Essay on reducing aquaculture impacts (Nov 2020)."],
},
# =====================================================================
"forests": {
    "summary": "Forests supply timber, fuel, food and medicines and provide atmospheric, hydrological, soil, habitat and recreation services. Traditional management (coppicing, pollarding, standards) and plantations of non-native species contrast with the deforestation driven by agriculture, mining, roads, timber, fuel and fodder, whose losses can be reduced by sustainable forest management.",
    "sections": [
        ("Forest resources", "360-362",
         "<p><b>Timber</b> needs little processing: mahogany and teak from tropical forests; oak and beech from temperate deciduous; softwoods (pine, spruce) from conifer forests for construction, paper and board. <b>Fuelwood</b> - before the industrial revolution the main energy source, still vital across the tropics; charcoal. <b>Food:</b> fruit, nuts, honey, bushmeat; wild relatives of crops. <b>Medicines</b> and other products: rubber, resins, cork, rattan, oils, dyes.</p>"),
        ("Ecosystem services", "362-364",
         "<ul><li><b>Atmospheric regulation:</b> carbon storage and sequestration; oxygen; particulates filtered.</li><li><b>Regulation of the hydrological cycle:</b> interception, infiltration, transpiration feeding rainfall, reduced flooding, steady river flow.</li>"
         "<li><b>Habitat and wildlife refuge</b> for most terrestrial species; <b>soil conservation</b> - roots bind, litter protects, organic matter builds; <b>climate moderation</b> (shade, humidity, windbreaks); <b>recreation and amenity</b> - walking, tourism, spiritual value.</li></ul>"),
        ("Traditional forest management", "364-366",
         "<p>Different species for different uses (ash for tools and furniture, oak for buildings and ships, hazel for hurdles, willow for baskets). <b>Standards</b> - trees left to grow to full size for timber; <b>coppicing</b> - cutting to a stool on a rotation (7-20 years) for poles, fuel and charcoal, keeping woodland open and diverse; <b>pollarding</b> - cutting above browsing height; coppice-with-standards combines both. <b>Cultivation of non-indigenous species:</b> fast-growing conifers (Sitka spruce, Douglas fir) and eucalyptus give high yields and predictable timber but low biodiversity, acidified soils, and less habitat value; native broadleaves grow more slowly but support far more species; mixed and native plantings are now encouraged.</p>"),
        ("Deforestation", "367-369",
         "<p><b>Causes:</b> clearance for <b>agriculture</b> (cattle ranching, soya, palm oil, subsistence), <b>mineral extraction</b>, <b>transport infrastructure</b> (roads open forests to settlers), reservoirs, <b>timber</b> harvesting (often illegal), <b>fuel</b>, <b>livestock fodder</b>, urbanisation, fire. <b>Loss of forest resources and services:</b> loss of species and genetic resources, soil erosion and fertility loss, reduced carbon storage (deforestation about 10-15% of anthropogenic CO<sub>2</sub>), <b>increased albedo</b> and changed energy balance, <b>reduced rainfall downwind</b> as transpiration falls, flooding and silted rivers, loss of indigenous peoples' livelihoods.</p>"),
        ("Sustainable forest management", "369",
         "<ul><li><b>Harvesting rates</b> no greater than regrowth; long rotations.</li><li><b>Selective logging</b> of mature trees rather than clear felling; reduced-impact logging (planned tracks, directional felling, protecting the canopy).</li>"
         "<li><b>Mixed-species and indigenous plantations</b>; natural regeneration; nurseries of native seedlings.</li><li><b>Agroforestry</b> and buffer strips; protection of watersheds and slopes.</li>"
         "<li><b>Certification</b> (Forest Stewardship Council) and the ITTO; controlling illegal logging with DNA timber tracing; community forestry and ecotourism giving local people an income from standing forest; debt-for-nature swaps and carbon payments (REDD).</li></ul>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Consequences of deforestation", "nodes": [("d", "Forest cleared", 1, 1), ("c", "CO2 released;\nsequestration lost", 0, 0), ("w", "Less transpiration:\nless rain downwind; floods", 2, 0), ("s", "Soil eroded;\nrivers silted", 0, 2), ("b", "Species and genetic\nresources lost", 2, 2), ("a", "Albedo rises;\nenergy balance changes", 1, 0)],
         "kinds": {"d": "warn"}, "edges": [("d", "c"), ("d", "w"), ("d", "s"), ("d", "b"), ("d", "a")], "caption": "Genn pp. 368-369."},
    ],
    "numbers": ["Deforestation ~10-15% of human CO<sub>2</sub> emissions", "Coppice rotations typically 7-20 years"],
    "exam": ["Explain climatic features and management of temperate forests; woodland cover in England since 1100 (Nov 2020 Q9).", "Deforestation causes by region and rates (June 2023 Q10); UK forest loss and CO<sub>2</sub> calculation (Nov 2021 Q9, 15 marks).",
             "Eucalyptus plantations and carbon sequestration; monoculture vs mixed (June 2024 Q9).", "Deforestation and insect biodiversity in fragments (specimen Q3).", "Essay: causes and consequences of deforestation and sustainable management."],
},
# =====================================================================
"dynamic-equilibria": {
    "summary": "Sustainability - meeting present needs without compromising future generations - depends on understanding the dynamic equilibria of natural systems: negative feedback that resists change, positive feedback that amplifies it, tipping points that create new equilibria, and the resistance that diversity gives. Human activities often override these mechanisms.",
    "sections": [
        ("What sustainability means", "370-371",
         "<p>The ability to maintain a lifestyle indefinitely; on a global scale the overall impact of the whole human population. The <b>Brundtland Commission (1987)</b>: 'Sustainable development meets the needs of the present generation without compromising the ability of future generations to meet their own needs.' Motivations: moral belief that it is right, or <b>enlightened self-interest</b> - protecting the environment causes fewer difficulties than not. Total impact = <b>population x per capita impact</b>; per capita impact rises with affluence and access to energy, and toxic wastes now exceed what natural processes can decontaminate. Activities sustainable at small scale (slash and burn, fishing, sewage discharge) become unsustainable when the population is too large. New activities are rarely restricted by unsustainability because the opportunity is attractive, impacts are not understood, or they occur elsewhere or later. <b>Rural</b> communities see over-exploitation quickly and tend to limit use to needs; <b>urban</b> populations draw resources from elsewhere and simply move on when one area is depleted (timber, energy, minerals, fish). Some changes can be made by individuals; others need societies or international agreement so that lifestyles are genuinely sustainable rather than slightly less damaging.</p>"),
        ("Dynamic equilibria and negative feedback", "371",
         "<p>Natural systems have developed over long periods on physical resources, renewable energy and natural processes that keep conditions stable. <b>Negative feedback</b> resists change: rising temperature increases cloud cover and albedo; higher CO<sub>2</sub> increases photosynthesis and sequestration; more evaporation gives more precipitation; density-dependent factors regulate populations homeostatically. <b>Human activities</b> ignore natural negative feedback: when soil degradation, water shortage and lost pest predators would cut yields, farmers add fertiliser, irrigation and pesticides, further damaging the natural systems that support food production.</p>"),
        ("Positive feedback and tipping points", "372",
         "<p>Throughout human evolution negative feedback dominated the climate; human activities now drive <b>positive feedback</b>: melting permafrost, ocean acidification (less CO<sub>2</sub> uptake), falling albedo, methane hydrate release, forest and peat fires, cirrus cloud formation, faster soil decomposition. <b>Tipping points</b> are rarely reached naturally because feedback restores the equilibrium, but large unusual events can overwhelm it - the possible release of methane hydrate at the end of the Permian caused climate change and mass extinction - and human activities may make natural processes self-sustaining. <b>Diverse systems</b> (coral reefs, rainforests) resist change because each species matters less and alternative pathways exist; agroecosystems focused on few species lack the detritivores, pollinators and predators that maintain stability.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Negative feedback restores equilibrium; positive feedback drives change", "nodes": [("dist", "Disturbance", 1, 0), ("neg", "Negative feedback:\nresponse opposes change", 0, 1), ("eq", "Original equilibrium\nrestored", 0, 2), ("pos", "Positive feedback:\nresponse amplifies change", 2, 1), ("tip", "Tipping point ->\nnew equilibrium", 2, 2)],
         "kinds": {"eq": "hi", "tip": "warn"}, "edges": [("dist", "neg"), ("neg", "eq"), ("dist", "pos"), ("pos", "tip")], "caption": "Genn pp. 371-372."},
    ],
    "numbers": ["Brundtland definition 1987", "Total impact = population x per capita impact"],
    "exam": ["State the Brundtland definition; explain why some activities become unsustainable as population grows.", "Classify feedback mechanisms and explain tipping points (Nov 2020 Q10).",
             "Explain why diverse systems resist change; why urban and rural attitudes differ.", "Essay: dynamic equilibria and sustainable human activities (June 2022)."],
},
# =====================================================================
"natural-systems": {
    "summary": "Natural systems run on low energy-density renewable energy at low temperatures, cycle a small number of elements so wastes become raw materials, and produce biodegradable non-toxic wastes. Human systems use non-renewable energy at high temperatures in linear flows that deplete resources, disperse minerals and create persistent toxins.",
    "sections": [
        ("Energy in natural and human systems", "373",
         "<p>All natural processes driven by solar energy - the hydrological, carbon and nitrogen cycles, atmospheric and thermohaline circulation - use <b>low energy-density</b> renewable resources. Human activities are usually powered by non-renewables; renewable-based activities have low carbon footprints. Natural processes occur at <b>low temperatures</b>: photosynthesis, decomposition and nitrogen fixation work because enzymes lower activation energies; human processes such as manufacturing, the Haber process and incineration need high temperatures and energy inputs.</p>"),
        ("Material cycles", "373-374",
         "<p>Natural processes link into <b>cycles</b> where the waste of one is the raw material of the next, using few abundant elements built into monomers and polymers (carbohydrates, proteins) - sustainable because nothing is depleted or accumulates. <b>Linear human systems</b> extract, process, use and discard: fossil fuels are used once (and often when renewables were available); minerals are dispersed or mixed into products that cannot be separated, so recovery is difficult. <b>Wastes:</b> natural wastes are non-toxic or biodegradable to raw materials for other processes; human systems build toxic metals into electronics that cannot easily be recovered and release persistent toxins (organochlorines, PCBs) that bioaccumulate and biomagnify. The book's diagram contrasts extraction, processing, manufacture, use and end-of-life in a linear system with a cycle in which design for disassembly, re-use and recycling close the loop.</p>"),
        ("Human activities should support ecosystems", "374",
         "<p>Human survival relies on ecosystem services, so activities should not damage them - the third principle of the circular economy alongside cycling materials and using renewable energy. Students should consider how the low toxicity of natural wastes and the processes that recycle them minimise environmental problems and provide sustainable supplies.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Linear human system vs natural cycle", "nodes": [("ext", "Extract\nnon-renewable resource", 0, 0), ("man", "Manufacture at\nhigh temperature", 1, 0), ("use", "Use once", 2, 0), ("disc", "Discard: dispersed,\npersistent waste", 3, 0), ("n1", "Natural process", 0, 1), ("n2", "Waste = raw material\nfor next process", 1, 1), ("n3", "Low-temperature\nenzyme reactions", 2, 1), ("n4", "Solar energy;\nnothing depleted", 3, 1)],
         "kinds": {"disc": "warn", "n4": "hi"}, "edges": [("ext", "man"), ("man", "use"), ("use", "disc"), ("n1", "n2"), ("n2", "n3"), ("n3", "n4"), ("n4", "n1")], "caption": "Genn pp. 373-374. Top row: linear; bottom row: cyclic."},
    ],
    "numbers": ["Haber process vs Rhizobium: same product (fixed nitrogen), high temperature and fossil energy vs enzymes and sunlight"],
    "exam": ["Define energy density; state natural processes driven by low energy-density resources (June 2022 Q2).", "Compare natural and human systems in a table (energy, temperature, materials, wastes).",
             "Explain how a natural process has inspired a human system (June 2024 Q10).", "9-mark / essay: copying natural systems to make human activities sustainable."],
},
# =====================================================================
"circular-economy": {
    "summary": "The circular economy applies the principles of natural systems - cycling materials, renewable energy, supporting ecosystems, diversity, connected systems, design for extended use and re-use, optimum rather than maximum production - to land use, agriculture, forestry, fisheries, energy and manufacturing. Progress is measured with ecological footprints, biocapacity, carbon footprints and the Living Planet Index, and illustrated by case studies.",
    "sections": [
        ("Principles of the circular economy", "374-376",
         "<ul><li><b>Cycling of materials</b> as in biogeochemical cycles - no depletion, no build-up of waste.</li><li><b>Energy from renewable sources</b> like almost all natural processes.</li><li><b>Human activities should support ecosystems</b> because we depend on their services.</li>"
         "<li><b>Diverse systems are more resistant to change</b> - diverse energy mixes, crops, economies.</li><li><b>Connected systems</b> where the waste of one is the resource of another (industrial symbiosis).</li>"
         "<li><b>Design of products for extended use</b>, repair, re-use, refurbishment, disassembly and recycling; separation of biological and technical materials.</li><li><b>Optimum rather than maximum production</b> - sustainable yields rather than short-term maxima.</li><li><b>Use of new technologies</b> that copy natural processes.</li></ul>"),
        ("Applications", "376-379",
         "<ul><li><b>Agriculture:</b> natural processes for nutrients and pests, soil biota, integrated systems, agroforestry.</li><li><b>Forestry:</b> mixed-species and native forests, selective logging, long rotations, use of all timber products.</li>"
         "<li><b>Fishery management:</b> selective methods, quotas at MSY, no-take zones, IMTA aquaculture.</li><li><b>Diverse systems</b> and <b>initiatives</b>: EU targets on packaging, batteries, WEEE and landfill; producer responsibility; deposit schemes.</li>"
         "<li><b>Conservation of biodiversity</b> as the foundation of ecosystem services; <b>energy</b> - renewables, storage, efficiency; <b>design of manufactured appliances</b> for repair and recycling, leasing rather than owning; urban design with green infrastructure and permeable surfaces.</li></ul>"),
        ("Measuring sustainability", "379-380",
         "<table class=\"nt\"><tr><th>Measure</th><th>Meaning</th></tr>"
         "<tr><td>Biocapacity</td><td>The area's capacity to produce renewable resources and absorb wastes</td></tr>"
         "<tr><td>Ecological footprint</td><td>The productive area needed to supply a population's resources and absorb its wastes; humanity's footprint now exceeds the Earth's biocapacity by about 70% (about 1.7 Earths)</td></tr>"
         "<tr><td>Global hectare (gha)</td><td>A hectare of world-average productivity - the unit for both; UK footprint about 4 gha per person against about 1.7 gha available per person worldwide</td></tr>"
         "<tr><td>Earth Overshoot Day</td><td>The date by which the year's regenerative capacity has been used - now around August, earlier each year</td></tr>"
         "<tr><td>Carbon footprint</td><td>Greenhouse-gas emissions caused by a person, product or activity</td></tr>"
         "<tr><td>Living Planet Index</td><td>Population trends of thousands of vertebrate species - down by more than half since 1970</td></tr></table>"),
        ("Case studies", "380-389",
         "<ul><li><b>Ol Pejeta, Kenya:</b> conservancy combining wildlife (rhinos, elephants managed with corridors and tracking; drones against poaching) with cattle ranching, ecotourism, community links and employment.</li>"
         "<li><b>Eigg, Scotland:</b> community-owned island with its own renewable grid (wind, hydro, solar with battery storage and a demand cap), local food and tourism.</li>"
         "<li><b>Rio Bravo Conservation and Management Area, Belize:</b> rainforest reserve funded by charities and companies; sustainable selective logging of large mahogany with restricted machinery, planned track routes, use of smaller branches, tree nurseries, control of illegal logging, community projects and ecotourism.</li>"
         "<li><b>Kalundborg, Denmark:</b> industrial symbiosis - power-station waste heat warms the town and fish farm, gypsum from flue-gas desulfurisation makes plasterboard, fly ash makes cement, refinery gas fuels the power station, yeast from insulin production feeds pigs.</li>"
         "<li><b>EU initiatives</b> and DC micro-grids; urban examples of docks and lagoons redeveloped with habitat.</li></ul>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Kalundborg industrial symbiosis",
         "nodes": [("ref", "Oil refinery:\nsurplus gas", 0, 0), ("ps", "Coal power station", 1, 1), ("pharma", "Insulin plant\n(steam from power station)", 2, 0), ("pigs", "Yeast waste ->\npig feed", 3, 0), ("heat", "Waste heat -> town\nheating and fish farm", 0, 2), ("gyp", "Gypsum from FGD ->\nplasterboard factory", 1, 2), ("ash", "Fly ash ->\ncement works", 2, 2)],
         "kinds": {"ps": "hi"}, "edges": [("ref", "ps", "fuel"), ("ps", "pharma", "steam"), ("pharma", "pigs"), ("ps", "heat"), ("ps", "gyp"), ("ps", "ash")],
         "caption": "Genn p. 388. A connected system: each link cuts waste, energy use and raw-material demand."},
    ],
    "numbers": ["Humanity uses about 1.7 Earths; UK footprint ~4 gha per person vs ~1.7 gha available", "Living Planet Index down more than half since 1970", "Earth Overshoot Day now around August"],
    "exam": ["Interpret biocapacity vs footprint graphs (June 2022 Q10); define gha, Overshoot Day, LPI.", "Explain how a named case study applies circular principles.",
             "Explain recycling and design for re-use (June 2024 Q10).", "9-mark: apply circular principles to three sectors; essays on the circular economy and sustainable lifestyles (specimen)."],
},
}
