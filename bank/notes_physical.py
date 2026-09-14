"""Revision notes: The physical environment (spec 3.2).  Genn pp. 86-169.
Each section is (heading, printed pages, html).  Diagram specs are drawn by gen/diagrams.py."""

NOTES = {
# =====================================================================
"atm-energy": {
    "summary": "The atmosphere is a thin layer of gases held by gravity. It supplies the elements life is built from, filters solar radiation, keeps the surface warm by delaying the escape of infrared, and moves heat and water around the planet. Its composition is a dynamic equilibrium that human activities can disturb.",
    "sections": [
        ("Composition of the atmosphere", "86",
         "<p>Dry air is about <b>78% nitrogen</b>, <b>21% oxygen</b>, <b>0.9% argon and other rare gases</b>, <b>0.04% carbon dioxide</b> and tiny traces of ozone (0.000007%) and other gases; water vapour varies from place to place. The composition is in <b>dynamic equilibrium</b>: processes that add gases (respiration, combustion, volcanoes, denitrification) are balanced by processes that remove them (photosynthesis, dissolving in the oceans, nitrogen fixation), so the average stays constant while concentrations fluctuate around a mean.</p>"
         "<ul><li><b>Daily CO<sub>2</sub> fluctuation:</b> lower in the day (photosynthesis exceeds respiration), higher at night.</li>"
         "<li><b>Annual CO<sub>2</sub> fluctuation:</b> falls through the northern-hemisphere growing season (spring-summer) and rises in autumn-winter when leaf fall stops photosynthesis but decomposition and respiration continue. The northern hemisphere has more land and vegetation, so the global cycle follows its seasons. Expect a question asking you to describe and explain this saw-tooth graph.</li></ul>"),
        ("How the atmosphere supports life", "87",
         "<ul><li><b>Gases for natural processes:</b> carbon, hydrogen, oxygen and nitrogen are extracted as N<sub>2</sub>, O<sub>2</sub>, CO<sub>2</sub> and H<sub>2</sub>O to build carbohydrates, lipids and proteins (proteins also need nitrogen).</li>"
         "<li><b>Absorption of electromagnetic radiation:</b> the upper atmosphere stops most of the damaging radiation of the 'solar wind'; in the stratosphere monatomic (O), diatomic (O<sub>2</sub>) and triatomic (O<sub>3</sub>, ozone) oxygen form a dispersed <b>ozone layer</b> that absorbs ultraviolet light in a dynamic equilibrium of reactions that make and destroy ozone.</li>"
         "<li><b>Delaying the escape of infrared energy:</b> visible light is absorbed by the surface, converted to heat and re-emitted as infrared; naturally occurring gases absorb this, warm up, and (a) emit infrared back to the surface and (b) reduce heat loss by conduction from land and sea. Without this the surface would be 33 &deg;C colder.</li>"
         "<li><b>Heat distribution:</b> most solar energy is absorbed at the surface in the tropics; warm winds (eg the south-westerlies bringing Caribbean heat to the UK) and ocean currents (the North Atlantic Conveyor) carry heat to higher latitudes, which is why the UK is milder than places at the same latitude.</li>"
         "<li><b>Transport of water vapour:</b> winds carry evaporated water to regions that would otherwise be dry.</li>"
         "<li><b>Atmospheric pressure:</b> controls how easily water molecules evaporate; at much lower pressure there would be no liquid water on Earth.</li>"
         "<li><b>Gases for human exploitation:</b> nitrogen, oxygen, carbon dioxide and the inert gases argon, neon, krypton and xenon are extracted industrially.</li></ul>"),
        ("Structure of the atmosphere", "88",
         "<p>Altitude changes composition and physical conditions, producing layers. The <b>troposphere</b> (surface to about 10-15 km, containing about 80% of the gas and all weather) and the <b>stratosphere</b> above it (containing the ozone layer) are the layers affected by human activity; the mesosphere lies above. Temperature falls with height in the troposphere, rises through the stratosphere because ozone absorbs UV there, then falls again in the mesosphere - this <b>thermal stratification</b> is a favourite 'draw the line on the graph' question.</p>"),
        ("Energy processes in the atmosphere", "88",
         "<p>Energy arriving from the Sun and energy leaving to space are generally in dynamic equilibrium. Incoming radiation is mainly <b>ultraviolet, visible light and near infrared</b> (short wavelengths); outgoing radiation is mainly <b>long-wave (far) infrared</b>. This energy drives climate, ocean currents and the hydrological cycle and therefore the distribution of species, so any human activity that changes energy movement can affect all of them.</p>"
         "<p><b>The energy budget</b> (percentages of incoming solar radiation): about 30% is reflected - 25% by clouds, dust and the atmosphere and 5% by the surface (the <b>planetary albedo</b>); about 20% is absorbed by the atmosphere and 50% by the surface. The surface emits far more infrared than it received from the Sun because greenhouse gases absorb it and re-radiate most of it back (about 95 units absorbed, 85 re-emitted downwards in the book's figure), while only about 70 units finally escape to space - matching the 70% of sunlight absorbed.</p>"
         "<table class=\"nt\"><tr><th>Wavelength</th><th>What happens to it</th></tr>"
         "<tr><td>Ultraviolet</td><td>Short wavelength; absorbed in the stratosphere by O, O<sub>2</sub> and O<sub>3</sub>; energy converted to chemical energy in the reactions; little reaches the surface</td></tr>"
         "<tr><td>Visible light</td><td>Passes through the atmosphere easily; absorbed by the surface and converted to heat, or absorbed by chlorophyll in photosynthesis</td></tr>"
         "<tr><td>Infrared</td><td>Emitted by the warm surface; absorbed by greenhouse gases (CO<sub>2</sub>, water vapour, methane) and converted to heat; re-emitted in all directions</td></tr></table>"),
        ("Why atmospheric processes are hard to predict", "86-87",
         "<p>Human actions trigger sequences: changing one process changes others as a direct result. Much about atmospheric processes is still not understood, so the impact of a specific activity cannot be predicted accurately - the basis of the <b>precautionary principle</b> and a common evaluation point in 9-mark answers.</p>"),
    ],
    "diagrams": [
        {"type": "layers", "title": "Thermal stratification of the atmosphere (bottom = surface)", "side": "Altitude",
         "layers": [("Troposphere", "0-~12 km; ~80% of gas; weather; temperature falls with height"), ("Stratosphere", "~12-50 km; ozone layer; temperature rises (UV absorbed)"),
                    ("Mesosphere", "50-85 km; temperature falls again"), ("Thermosphere", "above 85 km; very thin; absorbs solar wind")],
         "caption": "Based on the structure diagram, Genn p. 88. Only the troposphere and stratosphere are significantly affected by human activities."},
        {"type": "flow", "title": "The energy budget: what happens to 100 units of incoming solar radiation",
         "nodes": [("sun", "Incoming solar\nradiation 100", 0, 1), ("ref", "Reflected 30\n(clouds/dust 25, surface 5)", 1, 0), ("atm", "Absorbed by\natmosphere 20", 1, 1), ("surf", "Absorbed by\nsurface 50", 1, 2),
                   ("ghg", "Infrared absorbed by\ngreenhouse gases", 2, 2), ("back", "Re-emitted to\nsurface", 2, 1), ("space", "Infrared to\nspace 70", 3, 1)],
         "kinds": {"sun": "hi", "space": "hi"},
         "edges": [("sun", "ref"), ("sun", "atm"), ("sun", "surf"), ("surf", "ghg", "IR"), ("ghg", "back"), ("back", "surf"), ("ghg", "space"), ("atm", "space")],
         "caption": "Numbers are percentages of incoming solar energy (Genn p. 88). Absorbed (70) = emitted to space (70): dynamic equilibrium."},
    ],
    "numbers": ["N<sub>2</sub> 78%, O<sub>2</sub> 21%, Ar 0.9%, CO<sub>2</sub> 0.04%", "Planetary albedo about 30%", "Natural greenhouse effect warms the surface by 33 &deg;C", "Troposphere holds about 80% of the atmosphere's gas; 99.9% is below the stratopause"],
    "exam": ["Describe and explain the annual CO<sub>2</sub> graph (photosynthesis vs respiration, northern-hemisphere seasons).", "Draw the temperature-altitude line and name the layers; explain why the stratosphere warms with height.",
             "Explain each wavelength's fate (UV / visible / IR) - usually 6 marks, 2 per wavelength.", "Calculate albedo or the energy retained from a budget table.",
             "'Explain why the UK is warmer than Moscow' - winds plus the North Atlantic Conveyor.", "9-mark: how human activities alter energy processes in the troposphere and stratosphere and why the consequences are hard to predict (links to climate change and ozone)."],
},
# =====================================================================
"climate-change": {
    "summary": "Human activities are raising the concentration of gases that absorb infrared, enhancing the natural greenhouse effect. The consequences run through the cryosphere, oceans, weather, ecosystems and human systems, are hard to monitor and predict, and are being tackled by emission control, carbon storage, geoengineering, adaptation and international agreements with only partial success.",
    "sections": [
        ("The natural and enhanced greenhouse effects", "89",
         "<p>Visible light passes through the atmosphere and warms the surface; the surface emits infrared which <b>greenhouse gases</b> - any gas better at absorbing infrared than the atmospheric average, chiefly water vapour and CO<sub>2</sub> - absorb, warming the troposphere. Human activities increase the concentration of natural greenhouse gases and add new ones, causing the <b>enhanced greenhouse effect</b>: anthropogenic global climate change.</p>"
         "<table class=\"nt\"><tr><th>Gas</th><th>Main anthropogenic sources</th><th>Notes</th></tr>"
         "<tr><td>Carbon dioxide</td><td>Fossil fuel combustion, deforestation, cement</td><td>Most important by volume; long residence time</td></tr>"
         "<tr><td>Methane</td><td>Livestock (ruminant digestion), rice padi fields, landfill, leaks from gas and coal mines, melting permafrost</td><td>About 25 times the warming effect of CO<sub>2</sub> per molecule but shorter residence time</td></tr>"
         "<tr><td>Nitrous oxide (N<sub>2</sub>O)</td><td>Fertilised soils, livestock waste, combustion</td><td>Very high GWP, long-lived</td></tr>"
         "<tr><td>CFCs / HFCs</td><td>Refrigerants, aerosols, foams (ODS replacements)</td><td>Entirely synthetic; thousands of times CO<sub>2</sub>'s GWP</td></tr>"
         "<tr><td>Tropospheric ozone</td><td>Photochemical reactions of vehicle emissions</td><td>Secondary pollutant</td></tr></table>"
         "<p>Know the difference between <b>global warming potential</b> (warming per molecule relative to CO<sub>2</sub>) and <b>residence time</b> (how long it stays in the atmosphere): a gas with a high GWP but short residence time may matter less over a century.</p>"),
        ("Evidence: ice cores and other proxies", "90, 101-102",
         "<p>Direct temperature records only cover about 150 years, so <b>proxy data</b> reconstruct the past: air bubbles in <b>ice cores</b> give past CO<sub>2</sub> and methane, oxygen-18 : oxygen-16 ratios give temperature, tree rings, pollen, coral growth and magnesium : calcium in calcite add detail. Ice cores show CO<sub>2</sub> and temperature moving together over hundreds of thousands of years, with CO<sub>2</sub> now far above any pre-industrial level (about 280 ppm before industrialisation, over 410 ppm now).</p>"),
        ("Consequences: ecological changes", "90-92",
         "<ul><li>Changes in the <b>distribution of species</b> as climate zones shift polewards and uphill; species that cannot move (mountain tops, islands) face extinction.</li>"
         "<li>Changes in <b>timing</b> (phenology): earlier flowering, breeding and migration, which can break inter-species relationships such as caterpillar emergence and bird nesting.</li>"
         "<li>Case example in the book: UK bats extending their range and activity with milder winters; coral bleaching where sea temperatures rise.</li></ul>"),
        ("Consequences: changes in climatic processes", "93",
         "<ul><li><b>Wind patterns:</b> more energy means changed circulation - shifting jet streams, more intense storms and tropical cyclones in some regions, fewer in others (the book notes possibly fewer typhoons reaching Japan).</li>"
         "<li><b>Rainfall:</b> warmer air holds more water vapour; some regions get heavier rain and floods, others longer droughts as rain belts move.</li></ul>"),
        ("Consequences: the cryosphere", "94-96",
         "<p>Categories of ice: <b>ice sheets</b> (Antarctica, Greenland), <b>ice caps and ice fields</b>, <b>glaciers</b>, <b>ice shelves</b> (floating extensions of land ice), <b>sea ice</b> and <b>permafrost</b>. Melting <b>land ice</b> raises sea level; melting <b>sea ice</b> does not directly, but reduces albedo. Loss of <b>ice shelves</b> removes the barrier holding back glaciers so land ice flows faster into the sea. <b>Snow- and ice-fed rivers</b> (Ganges, Indus, Andes) lose their summer flow as glaciers shrink, threatening water and food supplies for hundreds of millions.</p>"),
        ("Consequences: ocean currents", "96-98",
         "<p>The <b>North Atlantic Conveyor</b> (part of the global thermohaline circulation) carries warm surface water north-east to Europe; the water cools, becomes denser and sinks, driving the circulation. Fresh water from melting Greenland ice and more rain could reduce salinity and density and weaken the sinking, cooling north-west Europe even as the planet warms. <b>El Ni&ntilde;o</b>: normally equatorial winds push warm Pacific water westwards and cold nutrient-rich water upwells off Peru; in El Ni&ntilde;o years the winds weaken, warm water flows back east, upwelling stops, the anchovy fishery collapses and weather patterns change worldwide. Climate change may make El Ni&ntilde;o events more frequent or intense.</p>"),
        ("Consequences for people", "99-100",
         "<ul><li><b>Sea level rise</b> from thermal expansion and melting land ice: flooding of low-lying land and cities, saltwater incursion into aquifers, loss of coastal habitats.</li>"
         "<li><b>Health:</b> spread of vector-borne diseases (malaria, dengue) into new areas, heat stress.</li><li><b>Water supplies:</b> drought, loss of glacier-fed flow.</li>"
         "<li><b>Food supplies:</b> changed growing seasons, drought, pests; some high-latitude areas may gain.</li><li><b>Infrastructure:</b> flooding, storm damage, landslides after heavy rain, melting permafrost undermining roads and buildings.</li></ul>"),
        ("Why monitoring and prediction are difficult", "100-102",
         "<ul><li><b>Time scales and spatial scales</b> - changes occur over decades and vary regionally.</li><li><b>Interconnected systems</b> - one change alters others (eg cloud cover both reflects sunlight and traps heat).</li>"
         "<li><b>Natural fluctuations</b> - solar output cycles, volcanic eruptions, Milankovitch orbital cycles mask or mimic the human signal.</li><li><b>Time delay between cause and effect</b> - oceans absorb heat slowly, so today's emissions produce warming decades later.</li>"
         "<li><b>Data collection</b> - historic data are patchy; proxies are indirect; satellites now measure temperature, ice, sea level and ocean currents (Argo floats); <b>computer models</b> depend on the assumptions and resolution used.</li></ul>"),
        ("Feedback mechanisms and tipping points", "103-104",
         "<p><b>Negative feedback</b> resists change: warming increases evaporation and cloud cover, raising albedo; more CO<sub>2</sub> stimulates photosynthesis. <b>Positive feedback</b> amplifies it: melting ice lowers albedo; thawing permafrost releases methane; warmer oceans hold less CO<sub>2</sub> and may release methane hydrates; drought causes forest and peat fires; faster decomposition releases CO<sub>2</sub>; cirrus cloud formation. A <b>tipping point</b> is reached when positive feedback makes change self-sustaining and the system moves to a new equilibrium - eg complete loss of Arctic summer ice or collapse of the Amazon rainforest - which is why delay is dangerous.</p>"),
        ("Control of global climate change", "105-106",
         "<ul><li><b>Reducing emissions:</b> energy conservation in transport, buildings and industry; renewables and nuclear replacing fossil fuels; capturing landfill methane; changed livestock diets; reduced deforestation.</li>"
         "<li><b>Carbon storage:</b> afforestation and conserving forests, peat bogs and soil organic matter (carbon sequestration); <b>carbon capture and storage</b> from power stations.</li>"
         "<li><b>Geoengineering:</b> increasing albedo (white roofs, reflective aerosols, solar shades), ocean fertilisation with iron to boost plankton - largely untested with possibly unpredictable side effects.</li>"
         "<li><b>International agreements:</b> Kyoto Protocol (binding targets for developed countries), Paris Agreement (all countries, but targets are self-set and non-binding); carbon trading and carbon taxes.</li></ul>"),
        ("Adapting to climate change", "106-108",
         "<p>Because some change is now unavoidable: <b>flood control</b> (barriers, embankments), <b>coastal erosion control</b>, <b>managed retreat</b> (abandoning low-value land to the sea), <b>urban drainage control</b> with permeable surfaces, green roofs and sustainable drainage, <b>river flow management</b> (storage, floodplains), raised and floating buildings, drought-tolerant crops, changed infrastructure design. Adaptation reduces impacts but not the cause.</p>"),
        ("Evaluating success", "105-107",
         "<p>CO<sub>2</sub> keeps rising and global temperature is about 1 &deg;C above pre-industrial; emissions are falling in some developed countries but rising in developing economies. Difficulties: fossil fuels underpin economies, lifestyle change is needed, cost, time lags hide the benefit of action, political disagreement, and developing countries' right to develop. Compare with the Montreal Protocol's success on ozone: that was a substitution problem with few producers; this is systemic.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Positive and negative feedback in the climate system",
         "nodes": [("warm", "Warming", 1, 1), ("ice", "Ice melts:\nalbedo falls", 0, 0), ("perm", "Permafrost thaws:\nmethane released", 2, 0), ("cloud", "More evaporation:\nmore cloud, albedo rises", 0, 2), ("photo", "More CO2:\nmore photosynthesis", 2, 2)],
         "kinds": {"warm": "hi", "ice": "warn", "perm": "warn"},
         "edges": [("warm", "ice"), ("ice", "warm", "+"), ("warm", "perm"), ("perm", "warm", "+"), ("warm", "cloud"), ("cloud", "warm", "-"), ("warm", "photo"), ("photo", "warm", "-")],
         "caption": "Top row: positive feedback (amplifies). Bottom row: negative feedback (resists). Genn pp. 103-104."},
        {"type": "chart", "title": "Atmospheric CO2 since 1750 (ppm) - the shape you should be able to sketch", "kind": "line", "x_label": "Year", "y_label": "CO2 / ppm",
         "series": {"CO2": [(1750, 280), (1850, 285), (1900, 296), (1950, 311), (1970, 326), (1990, 354), (2000, 369), (2010, 390), (2020, 413)]}, "y_min": 250, "y_max": 430,
         "caption": "Pre-industrial about 280 ppm; over 410 ppm today. Values from ice cores and Mauna Loa (Genn pp. 89-90, 101)."},
    ],
    "numbers": ["Pre-industrial CO<sub>2</sub> about 280 ppm; over 410 ppm now", "Global temperature up about 1 &deg;C since pre-industrial times", "Natural greenhouse effect: 33 &deg;C of warming", "Methane: about 25x CO<sub>2</sub> per molecule; CFCs thousands of times"],
    "exam": ["Complete a table of greenhouse gases (sources, GWP, residence time).", "Explain proxy data and why historic data are limited; interpret an ice-core graph.",
             "El Ni&ntilde;o mechanism and its effect on the Peruvian anchovy catch (June 2023 Q10, 15 marks).", "Distinguish land ice / sea ice / ice shelves and their effects on sea level.",
             "Classify feedback mechanisms as positive or negative; explain tipping points.", "9-mark: evaluate control strategies, or compare with ozone; monitoring difficulties.", "Essays: strategies for reducing climate change; agriculture adapting to it (Paper 2)."],
},
# =====================================================================
"ozone": {
    "summary": "Stratospheric ozone absorbs ultraviolet light. CFCs and related gases release chlorine and bromine that catalyse its destruction, thinning the ozone layer and producing the Antarctic 'hole'. The Montreal Protocol phased out the gases and the layer is slowly recovering - the clearest example of a global environmental problem tackled successfully.",
    "sections": [
        ("Importance of stratospheric ozone", "108",
         "<p>Monatomic, diatomic and triatomic oxygen in the stratosphere absorb UV light. UV splits O<sub>2</sub> into two reactive O atoms; O joins O<sub>2</sub> to make O<sub>3</sub>; UV splits O<sub>3</sub> back into O<sub>2</sub> and O. This dynamic equilibrium converts UV energy into heat (warming the stratosphere) so little UV reaches the surface. UV is <b>mutagenic</b>: it causes skin cancer, cataracts and immune suppression in people, damages phytoplankton and crops, degrades materials.</p>"),
        ("CFCs and the Rowland-Molina hypothesis", "109",
         "<p><b>Chlorofluorocarbons</b> were ideal industrial gases: very stable, non-toxic, non-flammable, easily liquefied - used in aerosol propellants, refrigerants, foam blowing, solvents. Their stability means they persist for decades and are carried up into the stratosphere. There, UV breaks off a <b>chlorine atom</b> which reacts with ozone (Cl + O<sub>3</sub> &rarr; ClO + O<sub>2</sub>); ClO then reacts with O to regenerate Cl (ClO + O &rarr; Cl + O<sub>2</sub>). Chlorine is a <b>catalyst</b>, so one atom destroys thousands of ozone molecules before it is finally removed. Rowland and Molina proposed this in <b>1974</b>; halons (bromine) and HCFCs behave similarly.</p>"),
        ("Measuring ozone", "110",
         "<p>Ozone is measured in <b>Dobson units</b> (thickness the ozone column would have at surface pressure). <b>Ground-based</b> Dobson spectrophotometers compare UV at wavelengths absorbed and not absorbed by ozone; <b>satellites</b> (eg TOMS) map ozone globally from above; balloons and aircraft measure ClO directly, confirming the mechanism. Ozone varies naturally with season, latitude and the solar cycle, so long data series are needed to detect a trend.</p>"),
        ("Ozone depletion over Antarctica", "111",
         "<p>The 'hole' forms each southern spring (September-October). In the winter polar vortex, temperatures fall low enough for <b>polar stratospheric clouds</b> of ice crystals to form; reactions on their surfaces convert stable chlorine compounds into reactive forms. When sunlight returns in spring, rapid ozone destruction occurs. Depletion is worse over the Antarctic than the Arctic because the vortex is colder and more stable. Global ozone loss overall has been limited to about 4%.</p>"),
        ("Restoration: the Montreal Protocol", "111-113",
         "<p>Agreed in <b>1987</b> and strengthened since: phased out production of CFCs, halons and later HCFCs; nearly every country signed; legally binding targets; a fund to help developing countries; trade bans on ODSs with non-signatories. <b>Alternatives:</b> HCFCs (transitional, less damaging), HFCs (no chlorine but strong greenhouse gases), hydrocarbons such as propane/butane in aerosols and fridges, pump-action sprays, changed foam-blowing methods; recovery and destruction of CFCs from old fridges.</p>"
         "<p><b>Evidence of success:</b> atmospheric CFC concentrations are falling, the hole has stopped growing and is beginning to shrink, UV at the surface is no longer rising. <b>Why it worked:</b> a clear, frightening consequence (skin cancer); few producers and products; alternatives existed and were cheap; binding targets; global agreement. <b>Limits:</b> CFCs persist for decades so full recovery is expected around 2060-2070; some ODSs (methyl bromide, some HCFCs) still in use; illegal production reported; HFC replacements add to global warming.</p>"),
        ("Ozone as a model of the scientific method", "108-113",
         "<p>The book uses ozone to illustrate how environmental problems are investigated: observation of a problem (Antarctic measurements), hypothesis (Rowland-Molina), data collection and analysis (Dobson units, satellites, ClO detection), proposed solutions, enactment (Montreal), and monitoring of the outcome. Learn this sequence for 'compare with climate change' essays.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "How chlorine from CFCs catalyses ozone destruction",
         "nodes": [("cfc", "CFC molecule\nreaches stratosphere", 0, 0), ("uv", "UV light breaks\noff Cl atom", 1, 0), ("cl", "Cl", 2, 0), ("o3", "Cl + O3 -> ClO + O2", 3, 0), ("clo", "ClO + O -> Cl + O2", 3, 1), ("again", "Cl free again:\ncycle repeats thousands of times", 2, 1)],
         "kinds": {"cl": "hi", "again": "warn"},
         "edges": [("cfc", "uv"), ("uv", "cl"), ("cl", "o3"), ("o3", "clo"), ("clo", "again"), ("again", "cl")],
         "caption": "The Rowland-Molina mechanism, Genn p. 109. Chlorine is regenerated, so it acts as a catalyst."},
    ],
    "numbers": ["Rowland-Molina hypothesis 1974; Montreal Protocol 1987", "Ozone measured in Dobson units", "Global ozone loss limited to about 4%; Antarctic hole each September-October", "Recovery expected around 2060-2070"],
    "exam": ["Explain the properties of CFCs that made them useful and dangerous (stability, persistence, chlorine).", "Describe the chlorine catalytic cycle - equations are worth learning.",
             "Explain why depletion is worst over Antarctica in spring.", "Evaluate the Montreal Protocol and explain why it succeeded where climate agreements struggle (June 2024 Q10, 15 marks; Nov 2021 Q2).",
             "Interpret graphs of ozone concentration vs ODS emissions and explain the time lag."],
},
# =====================================================================
"hydro-cycle": {
    "summary": "Water cycles between oceans, atmosphere, land and living organisms, with residence times from days (atmosphere) to millennia (deep groundwater). Human activities change flows and stores; rivers and aquifers are over-exploited in many regions with serious environmental and political consequences.",
    "sections": [
        ("The natural hydrological cycle", "115",
         "<p><b>Reservoirs</b> (stores) and their approximate share of the Earth's water: oceans about 97%; ice caps and glaciers about 2%; groundwater under 1%; lakes, rivers, soil moisture, atmosphere and living organisms tiny fractions - yet these small stores are the ones people use. <b>Processes</b> (transfers): evaporation, transpiration, condensation, precipitation, interception by vegetation, infiltration into soil, percolation into rock, surface runoff, throughflow, groundwater flow, and abstraction by people. Energy from the Sun drives evaporation; gravity drives flow.</p>"
         "<p><b>Residence time</b> = volume of the reservoir / rate of flow through it: about 9 days for the atmosphere, weeks to years for rivers and lakes, centuries to thousands of years for deep aquifers and ice sheets. A short residence time means a reservoir responds quickly to change; a long one means pollution or over-abstraction takes a long time to reverse.</p>"),
        ("Human impacts on the cycle", "116",
         "<ul><li><b>Deforestation:</b> less interception and transpiration, more runoff, faster river flow and flooding, less infiltration so lower groundwater recharge, less rainfall downwind.</li>"
         "<li><b>Agriculture:</b> irrigation abstraction, drainage of wetlands, soil compaction increasing runoff, changed evapotranspiration.</li>"
         "<li><b>Urban development:</b> impermeable surfaces cut infiltration and speed runoff (flash floods), storm drains bypass natural storage; abstraction for supply.</li>"
         "<li><b>Global climate change:</b> altered rainfall patterns, more evaporation, loss of glacier stores, sea-level rise causing saltwater incursion.</li></ul>"),
        ("Rivers and reservoirs", "117-118",
         "<p>Reservoirs store surplus water for dry periods, but <b>environmental effects</b> include flooded habitats and settlements, changed flow regime downstream (less flooding of floodplains and wetlands, altered temperature and oxygen), trapped sediment starving deltas and coasts, barriers to migrating fish, methane from drowned vegetation, and evaporation losses. <b>Over-exploited rivers:</b> the Colorado no longer reaches the sea in most years; the Nile, Tigris-Euphrates (Turkey / Iraq / Syria) and Jordan are sources of international conflict because upstream dams and abstraction reduce downstream flow; the Aral Sea shrank after Soviet irrigation diverted its inflow rivers.</p>"),
        ("Aquifers", "119-121",
         "<p><b>Features:</b> a permeable rock (chalk, sandstone, limestone) that stores water; recharged by infiltration in the <b>recharge zone</b>; an <b>unconfined aquifer</b> has a water table open to the surface; a <b>confined aquifer</b> lies between impermeable layers and may be under pressure (artesian). <b>Unsustainable exploitation:</b> when abstraction exceeds recharge the water table falls, wells dry, rivers and wetlands fed by springs decline, land subsides (Mexico City) and in coastal aquifers seawater flows in (<b>saltwater incursion</b>). Fossil aquifers (Ogallala, USA; Saharan aquifers) receive almost no recharge so use is mining. Sustainable management: matching abstraction to recharge, artificial recharge, controlling pollution of recharge zones.</p>"),
    ],
    "diagrams": [
        {"type": "cycle", "title": "The hydrological cycle", "centre": "Sun's energy\n+ gravity",
         "nodes": ["Oceans (97%)", "Evaporation", "Atmosphere\n(~9 days)", "Precipitation", "Land: interception,\ninfiltration, runoff", "Rivers, lakes,\ngroundwater"],
         "caption": "Genn p. 115. Transpiration from plants also feeds the atmosphere; groundwater flow and rivers return water to the oceans."},
    ],
    "numbers": ["Oceans ~97% of water, ice ~2%, groundwater <1%", "Atmospheric residence time about 9 days; deep aquifers thousands of years", "Residence time = volume / flow"],
    "exam": ["Calculate transfers or residence time from a table of volumes and flows (June 2023 Q7).", "Explain how deforestation / urbanisation change river flow.",
             "Explain the features of aquifers and the consequences of over-abstraction (saltwater incursion, subsidence).", "Interpret a water-table graph and suggest short- and long-term causes of trends (specimen P2 Q4).", "Water-budget calculations for a lake such as the Dead Sea (Nov 2020 Q10)."],
},
# =====================================================================
"hydro-management": {
    "summary": "Growing demand means exploiting new sources (rainwater, rivers, reservoirs, barrages, desalination, new aquifers), managing supplies sustainably (recharge, regulation reservoirs, transfers, afforestation), conserving water, and treating water to the quality each use needs.",
    "sections": [
        ("Exploitation of new sources of water", "122-124",
         "<ul><li><b>Rainwater collection:</b> from roofs into tanks; important in cities where supply cannot meet demand (India) and rural areas with no mains; reduces urban flooding; water is often cleaner than rivers.</li>"
         "<li><b>Rivers:</b> most convenient - long, accessible; usefulness depends on total annual discharge, flow fluctuations, natural contaminants and human pollutants (waste from upstream communities).</li>"
         "<li><b>Reservoirs:</b> store surplus for shortage. <b>Site selection factors:</b> topography (narrow exit from a large deep basin so a small dam holds a large volume); impermeable, strong bedrock without faults or seismic activity; large catchment with regular high rainfall and low evaporation; catchment land use with low pollution risk (pesticides, industry) and low soil erosion (sedimentation reduces capacity); vegetation in the flooded area decays anaerobically releasing methane; access for workers and materials; distance to the area of demand; value of land lost - urban areas and nature reserves protected, farmland less so; a loss-benefit analysis that differs between countries.</li>"
         "<li><b>Estuary barrages:</b> dam across an estuary creating a freshwater reservoir - fewer land-use conflicts but destroys inter-tidal habitat, obstructs shipping, and receives pollution from the whole catchment.</li>"
         "<li><b>Seawater / desalination:</b> reverse osmosis or distillation; very energy-intensive and expensive, so only where freshwater is inadequate (Middle East).</li></ul>"),
        ("Sustainable management of water", "124-125",
         "<ul><li><b>Artificial recharge of aquifers:</b> surplus wet-season water pumped underground or spread in lagoons to infiltrate, maintaining supplies for dry-season abstraction.</li>"
         "<li><b>River-regulation reservoirs:</b> store flood peaks and release water in droughts, evening out flows made more extreme by deforestation and urbanisation.</li>"
         "<li><b>Inter-basin transfers:</b> canals and pipes from surplus to deficit areas - China, Russia, Australia, Wales to England; costly, and can cause conflict between regions.</li>"
         "<li><b>Unexploited aquifers:</b> newly discovered in North Africa and northern Kenya.</li><li><b>Afforestation:</b> trees reduce erosion and slow runoff, reducing floods and maintaining dry-season flow.</li></ul>"),
        ("Water conservation", "125-126",
         "<ul><li><b>Low-volume uses:</b> low-water washing machines and dishwashers, dual-flush toilets, tap timers, low-flow shower heads; <b>xeriscaping</b> with drought-adapted plants; <b>drip irrigation</b> delivering water to roots with less evaporation than sprays.</li>"
         "<li><b>Recycled water:</b> grey water from baths and showers re-used for toilets and gardens.</li><li><b>Pollution control</b> so contaminated sources can be re-used (sewage treatment, mine drainage control, buffer strips).</li>"
         "<li><b>Reduced wastage:</b> about 20% of UK public supply is lost from leaking pipes - repairs and maintenance; <b>water meters</b> charge by volume so there is an incentive to save.</li></ul>"),
        ("Water treatment", "126-127",
         "<p>Treatment matches the source quality to the <b>quality required by the use</b>: potable supply needs no pathogens, acceptable toxins, and water that looks, smells and tastes good; spray irrigation needs low turbidity and low heavy metals; power-station cooling needs no gross solids; industrial boilers need no dissolved minerals (soft water) to avoid scale.</p>"
         "<table class=\"nt\"><tr><th>Process</th><th>What it does</th></tr>"
         "<tr><td>Screens</td><td>Metal grills remove vegetation and litter</td></tr><tr><td>Sedimentation</td><td>Static water lets silt settle</td></tr>"
         "<tr><td>Aeration</td><td>Air bubbles or sprays raise dissolved oxygen, remove hydrogen sulfide smell, oxidise dissolved metals so they become insoluble</td></tr>"
         "<tr><td>Flocculation / coagulation</td><td>Clay particles repel each other electrostatically and will not settle; alum (aluminium sulfate) or polyelectrolytes neutralise the charge so they clump and settle in the clarifier</td></tr>"
         "<tr><td>Filtration</td><td>Slow sand / gravel filters remove remaining solids and bacteria</td></tr><tr><td>Activated carbon</td><td>Adsorbs organic chemicals, pesticides, tastes</td></tr>"
         "<tr><td>Sterilisation</td><td>Chlorine (persists in pipes), ozone or UV kill pathogens</td></tr><tr><td>pH adjustment / fluoridation</td><td>Lime or sodium hydroxide; fluoride in some areas</td></tr>"
         "<tr><td>Ion exchange / reverse osmosis</td><td>Remove dissolved salts and metals where needed (desalination, boiler water)</td></tr></table>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Stages in a water treatment works", "nodes": [("s", "Screens", 0, 0), ("sed", "Sedimentation", 1, 0), ("aer", "Aeration", 2, 0), ("floc", "Flocculation +\nclarification", 3, 0), ("filt", "Filtration\n(sand/gravel)", 3, 1), ("carb", "Activated\ncarbon", 2, 1), ("ster", "Sterilisation\n(Cl2 / O3 / UV)", 1, 1), ("out", "pH adjustment ->\nservice reservoir", 0, 1)],
         "kinds": {"out": "hi"}, "edges": [("s", "sed"), ("sed", "aer"), ("aer", "floc"), ("floc", "filt"), ("filt", "carb"), ("carb", "ster"), ("ster", "out")],
         "caption": "Genn p. 127. Not every works uses every stage - it depends on the source and the intended use."},
    ],
    "numbers": ["About 20% of UK public supply lost through leaks", "Desalination only where seawater is available and freshwater inadequate"],
    "exam": ["Complete a table of treatment processes vs contaminants (Nov 2021 Q1) or uses vs quality requirements.", "Explain why clay needs flocculation; purpose of aeration; sterilisation options.",
             "Factors in reservoir site selection - a classic 9-mark evaluate.", "Explain metering, drip irrigation, grey water; calculate % reductions.", "Water resource management case study (India, Nov 2021 Q6); essays on meeting demand sustainably (June 2022)."],
},
# =====================================================================
"minerals": {
    "summary": "Metals and other minerals are concentrated by igneous, hydrothermal, sedimentary, metamorphic and biological processes. Whether a deposit is worth mining depends on purity, cost and technology. Exploration, extraction and processing have large impacts that can be reduced, and future supplies depend on lower-grade ores, new technologies and recycling.",
    "sections": [
        ("Uses of mineral resources", "130-131",
         "<p>Metals (iron/steel for construction and transport, copper for electrical wiring, aluminium, titanium as white pigment, cadmium in batteries, rare earths in electronics, platinum-group catalysts) and non-metals (limestone for cement, sand and gravel, china clay, salt, phosphate rock for fertiliser). Demand grows with population and affluence; the book's table of uses is worth a look.</p>"),
        ("Formation of mineral deposits", "132-134",
         "<ul><li><b>Igneous processes:</b> as magma cools, minerals crystallise at different temperatures (<b>fractional crystallisation</b>) and dense minerals settle, concentrating them in layers of the batholith.</li>"
         "<li><b>Hydrothermal deposition:</b> superheated water from cooling magma dissolves metals and carries them into cracks in surrounding rock; as it cools, minerals crystallise in veins, arranged in sequence outward from the batholith (tin, copper, lead, zinc...).</li>"
         "<li><b>Metamorphic processes:</b> heat and pressure recrystallise rocks and concentrate minerals.</li>"
         "<li><b>Sedimentary processes:</b> weathering and erosion; transport in solution or by rivers; <b>alluvial deposits</b> (placer gold, tin) where dense particles settle as flow slows; <b>evaporites</b> (salt, gypsum, potash) where seas dried out; <b>chemical precipitation</b> (banded iron formations); <b>biological sediments</b> (limestone and chalk from shells, coal from vegetation, phosphate from guano and bones).</li></ul>"),
        ("Reserves, resources and stock", "135-136",
         "<p>The <b>stock (resource base)</b> is all of a mineral in the crust; the <b>resource</b> is the part that may become exploitable; <b>reserves</b> are what can be exploited economically now with existing technology. Reserves grow when prices rise, technology improves or new deposits are found, and shrink as mining proceeds. Mineral reserves are categorised by confidence (proven, probable, possible). <b>Lasky's principle:</b> as ore grade falls arithmetically the amount available rises geometrically - vast quantities exist at low grade. The <b>cut-off ore grade (COOG)</b> is the lowest grade worth mining; it falls as prices rise or extraction costs fall.</p>"),
        ("Exploration", "137",
         "<ul><li><b>Remote sensing:</b> satellite and aircraft <b>infrared spectroscopy</b> detects surface minerals by their reflectance; <b>gravimetry</b> detects dense ore bodies; <b>magnetometry</b> detects magnetic ores (magnetite, some cobalt and tungsten ores); <b>seismic surveys</b> use shock waves and geophones to map rock structure; <b>resistivity</b> measures how well rocks conduct electricity (sedimentary rocks with water conduct better than igneous).</li>"
         "<li><b>Trial drilling and chemical analysis</b> confirm composition and purity - expensive, so used last, targeted by the surveys.</li></ul>"),
        ("Factors affecting the viability of exploitation", "138-139",
         "<p><b>Ore purity</b> (grade), <b>chemical form</b> (some compounds need much more energy to process), <b>overburden and hydrology</b> (depth of waste rock, need to pump water), <b>depth</b> (open-cast vs underground), <b>economic viability</b> (market price vs costs of extraction, processing and transport), <b>transport costs</b> (bulk ore to smelter or port), <b>political factors</b>, <b>land availability</b> and environmental restrictions. Market economics: prices fluctuate, so a marginal mine may open and close.</p>"),
        ("Environmental impacts of mining", "139-142",
         "<ul><li><b>Land take</b> and <b>habitat loss</b>; <b>loss of amenity</b> and landscape.</li><li><b>Dust</b> from blasting, vehicles and spoil - silicosis, smothering vegetation; controlled by water sprays, covering lorries.</li>"
         "<li><b>Noise</b> from blasting and machinery - timing, baffle mounds.</li><li><b>Turbid drainage water</b> and toxic leachates (acid mine drainage from sulfide ores) - settlement lagoons, treatment.</li>"
         "<li><b>Spoil disposal:</b> unstable heaps (Aberfan), leaching; regrading, compaction, vegetation.</li><li><b>Subsidence</b> over underground workings.</li>"
         "<li><b>Mine site restoration:</b> landscaping, replacing topsoil, planting, creating lakes and nature reserves, urban development on stable sites; restoration planned before mining begins.</li></ul>"),
        ("Future mineral supplies", "143-147",
         "<ul><li><b>Better exploration:</b> higher-resolution multispectral satellites, portable field analysers (XRF), cheaper trial drilling.</li>"
         "<li><b>Deeper mining and larger open-cast mines</b> as machinery improves.</li>"
         "<li><b>Exploiting low-grade deposits at low energy cost:</b> <b>bioleaching</b> - acidophilic bacteria oxidise sulfide ores releasing copper and other metals into solution; <b>phytomining</b> - hyperaccumulator plants concentrate nickel etc, harvested and burnt; <b>iron displacement</b> of copper from solution; bacterial adsorption of rare earths; <b>polymer adsorption</b> of uranium from seawater.</li>"
         "<li><b>New sources:</b> <b>polymetallic nodules</b> and metal-rich sediments on the deep-sea bed (environmental and legal issues), Antarctica (currently protected by treaty), rare earth deposits.</li>"
         "<li><b>Recycling and design:</b> recycling saves energy (aluminium about 95%) but is limited by dispersal, alloys and mixed products; <b>Cradle to Cradle design</b> plans products for disassembly and material recovery; longer product lifetimes; substitution of scarce metals.</li></ul>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "Stock, resource and reserve", "nodes": [("stock", "Stock / resource base:\nall of the mineral in the crust", 0, 0), ("res", "Resource:\ncould become exploitable", 1, 0), ("rsv", "Reserve:\nexploitable now", 2, 0), ("price", "Higher price,\nbetter technology", 1, 1), ("mine", "Mining\nuses it up", 3, 1)],
         "kinds": {"rsv": "hi"}, "edges": [("stock", "res", "discovery"), ("res", "rsv", "COOG falls"), ("price", "rsv"), ("rsv", "mine")],
         "caption": "Genn pp. 135-136. Reserves are not fixed: they move with price, technology and exploration."},
    ],
    "numbers": ["Recycling aluminium saves about 95% of the energy of primary production", "Bioleaching: copper from ores too low-grade to smelt"],
    "exam": ["Complete a table of exploration techniques (June 2023 Q2); explain why trial drilling comes last.", "Explain hydrothermal ore formation from a batholith cross-section (specimen Q3).",
             "Copper ore grade vs cumulative mass graph - Lasky's principle and COOG (Nov 2021 Q4).", "Evaluate impacts of a proposed mine and restoration options.", "9-mark: strategies to secure future metal supplies; essay on managing mineral resources (June 2022)."],
},
# =====================================================================
"biogeochem": {
    "summary": "Carbon, nitrogen and phosphorus cycle between living organisms, the atmosphere, water and rock. Each cycle is a dynamic equilibrium of biological and physical processes that human activities have disturbed - combustion, deforestation, the Haber process, fertilisers, sewage, mining - and each disturbance can be reduced by managing those activities.",
    "sections": [
        ("The carbon cycle", "148-149",
         "<p><b>Stores:</b> atmosphere (CO<sub>2</sub>, methane), biosphere (living organisms, dead organic matter, soil), hydrosphere (dissolved CO<sub>2</sub> and hydrogen carbonate), lithosphere (fossil fuels, carbonate rocks - by far the largest). <b>Processes:</b> <b>photosynthesis</b> removes CO<sub>2</sub>; <b>respiration</b> (aerobic releases CO<sub>2</sub>; anaerobic releases methane) and <b>combustion</b> return it; carbon passes along <b>food webs</b>; <b>decomposition</b> releases it from dead matter; <b>dissolving</b> in the oceans and <b>sedimentation / fossilisation</b> lock it into rocks and fossil fuels over millions of years; volcanic activity and weathering return it slowly.</p>"),
        ("Human impacts on the carbon cycle", "150-151",
         "<ul><li><b>Changes in photosynthesis:</b> deforestation and land-use change reduce uptake; more CO<sub>2</sub> may increase it (negative feedback).</li>"
         "<li><b>Changes in aerobic respiration / decomposition:</b> ploughing and draining soils and peat bogs aerate them, speeding decomposition; warming speeds it too.</li>"
         "<li><b>Changes in anaerobic respiration:</b> rice padi fields, landfill sites and livestock create new anaerobic environments releasing methane.</li>"
         "<li><b>Combustion</b> of fossil fuels and biomass moves carbon from long-term stores to the atmosphere far faster than natural sedimentation removes it; <b>methane leaks</b> from gas fields, coal mines and pipelines.</li>"
         "<li><b>Carbonic acid in the sea:</b> more dissolved CO<sub>2</sub> lowers pH - ocean acidification harms corals and shell-builders and reduces the sea's capacity to absorb more.</li>"
         "<li><b>Biomass movements:</b> timber and food trade moves carbon between regions.</li></ul>"),
        ("Sustainable management of the carbon cycle", "151-152",
         "<ul><li>Replacing fossil fuels with renewables and nuclear; energy conservation.</li><li><b>Conservation of biomass carbon stores:</b> protecting forests and peat bogs; afforestation matched to deforestation and timber use; increasing soil organic matter by low tillage, mulching and organic fertiliser.</li>"
         "<li><b>Carbon capture and storage (CCS):</b> CO<sub>2</sub> separated from power-station exhaust and pumped into depleted oil and gas fields or saline aquifers - possible but expensive and unproven at scale.</li><li>Capturing landfill and mine methane as fuel.</li></ul>"),
        ("The nitrogen cycle", "152-154",
         "<p>Nitrogen gas (78% of the air) is unreactive, so life depends on <b>fixation</b>: <b>Rhizobium</b> bacteria in legume root nodules and free-living soil bacteria (Azotobacter) convert N<sub>2</sub> to ammonium; lightning and the <b>Haber process</b> fix it industrially. <b>Nitrification</b> by aerobic bacteria (Nitrosomonas, Nitrobacter) converts ammonium to nitrite then nitrate, which roots absorb (<b>root absorption</b>) to make proteins that pass along <b>food chains</b>. <b>Ammonification</b> (decomposition of dead matter and wastes) returns ammonium; <b>denitrification</b> by anaerobic bacteria in waterlogged soil converts nitrate back to N<sub>2</sub>; <b>leaching</b> washes soluble nitrate into water.</p>"),
        ("Human impacts on the nitrogen cycle and their control", "154-155",
         "<ul><li>The <b>Haber process</b> has roughly doubled global fixation; nitrate fertiliser leaches into water (eutrophication, nitrate in drinking water) and denitrifies to <b>nitrous oxide</b>, a greenhouse gas.</li>"
         "<li><b>Legume cultivation</b> increases fixation; <b>drainage</b> increases nitrification and reduces denitrification; <b>combustion</b> at high temperature produces NOx (acid rain, smog); <b>sewage</b> and livestock waste add ammonium and nitrate.</li>"
         "<li><b>Control:</b> more efficient / lower-temperature combustion and catalytic converters or urea sprays for NOx; biological fixation (legumes, rotation) instead of manufactured fertiliser; <b>management of biological wastes</b> (manure as fertiliser, sewage treatment with denitrification); avoiding eutrophication with organic and slow-release fertilisers, correct timing and buffer strips; <b>management of soil processes</b> - avoiding waterlogging or compaction, maintaining soil biota.</li></ul>"),
        ("The phosphorus cycle", "156-157",
         "<p>Phosphorus has no significant atmospheric store, so the cycle is slow. Phosphate is released from rock by <b>weathering</b> (mountain building exposes new rock), absorbed by roots, passed along food chains, returned by <b>decomposition</b> and eventually lost to <b>sedimentation</b> in the oceans, where it is only returned over geological time by uplift. Phosphate is poorly soluble, so it is often the limiting nutrient in fresh and sea water. <b>Human impacts:</b> mining of phosphate rock (a non-renewable resource - Morocco holds most reserves) for fertiliser and detergents; phosphate in sewage and eroded soil causes eutrophication; deforestation and erosion move phosphate to the sea faster. <b>Control:</b> recycling manure and sewage sludge, phosphate stripping in sewage works, erosion control, reduced use.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "The carbon cycle",
         "nodes": [("co2", "Atmospheric CO2", 1, 0), ("comb", "Combustion", 0, 1), ("photo", "Photosynthesis", 2, 1), ("foss", "Fossil fuels and\ncarbonate rock", 0, 2), ("dec", "Decomposition and\nrespiration", 1, 2), ("pl", "Plants and\nfood webs", 2, 2), ("dom", "Dead organic matter\nand soil", 1, 3)],
         "kinds": {"co2": "hi"},
         "edges": [("co2", "photo"), ("photo", "pl"), ("pl", "dom", "death"), ("dom", "dec"), ("dec", "co2"), ("dom", "foss", "fossilisation"), ("foss", "comb"), ("comb", "co2")],
         "caption": "Genn pp. 148-149. Dissolving in the oceans and sedimentation also remove carbon; volcanoes and weathering return it."},
        {"type": "flow", "title": "The nitrogen cycle",
         "nodes": [("n2", "N2 in atmosphere", 1, 0), ("fix", "Fixation: Rhizobium,\nlightning, Haber process", 0, 1), ("den", "Denitrification\n(anaerobic bacteria)", 2, 1), ("amm", "Ammonium", 0, 2), ("nit", "Nitrification\n(aerobic bacteria)", 1, 2), ("no3", "Nitrate in soil\n(leaches to water)", 2, 2), ("ammf", "Ammonification", 0, 3), ("dead", "Dead matter\nand wastes", 1, 3), ("pl", "Roots -> proteins\n-> food chains", 2, 3)],
         "kinds": {"n2": "hi"},
         "edges": [("n2", "fix"), ("fix", "amm"), ("amm", "nit"), ("nit", "no3"), ("no3", "pl", "absorption"), ("pl", "dead"), ("dead", "ammf"), ("ammf", "amm"), ("no3", "den"), ("den", "n2")],
         "caption": "Genn pp. 152-154. Leaching removes nitrate to water; denitrification in waterlogged soil returns N2 to the air."},
    ],
    "numbers": ["Haber process has roughly doubled global nitrogen fixation", "Atmosphere 78% N<sub>2</sub>; carbonate rock is the largest carbon store", "Standard-form calculation practice: atmospheric carbon about 750 Gt = 7.5 x 10<sup>11</sup> t"],
    "exam": ["Label or complete a cycle diagram / table of processes (June 2023 Q1 phosphorus).", "Calculate atmospheric carbon in standard form from reservoir data (June 2022 Q3).",
             "Explain how each human activity changes a named process (6 marks, 2 per activity).", "Measuring nitrate / carbon in samples (colourimetry, biomass sampling - Nov 2020 Q8, June 2024 Q5).", "9-mark: how humans altered the carbon and nitrogen cycles and strategies to counteract this."],
},
# =====================================================================
"soils": {
    "summary": "Soil fertility depends on mineral particles, organic matter, water, air and organisms. Soil forms slowly and is lost quickly when vegetation is removed, slopes are ploughed or structure is destroyed; erosion reduces productivity, silts rivers and adds dust to the air. Good management keeps soil covered, structured and rich in organic matter.",
    "sections": [
        ("Soil fertility: what a fertile soil provides", "158-161",
         "<ul><li><b>Mineral nutrients</b> from weathered rock and decomposed organic matter; held on clay and humus by <b>cation exchange</b> (nutrient retention) and released to roots.</li>"
         "<li><b>Water:</b> <b>gravitational water</b> drains away; <b>capillary water</b> is held in small pores and available to plants (<b>field capacity</b> is what remains after drainage); <b>hygroscopic water</b> is bound too tightly to be used. Clay holds more water than sand but much of it is unavailable; loams are best.</li>"
         "<li><b>Air content:</b> roots and aerobic organisms need oxygen; waterlogging causes anaerobic conditions and denitrification.</li>"
         "<li><b>Dead organic matter and humus:</b> release nutrients on decomposition, hold water and nutrients, bind particles into crumbs, darken the soil (warms faster), food for soil biota.</li>"
         "<li><b>Soil biota:</b> bacteria and fungi decompose and fix nitrogen; mycorrhizae increase phosphate uptake; earthworms mix, aerate and drain the soil; detritivores fragment litter.</li>"
         "<li><b>Soil texture:</b> the proportions of sand (2-0.06 mm), silt and clay (below 0.002 mm), read from the <b>soil triangle</b>; controls drainage, aeration, water retention, nutrient retention, root penetration and ease of cultivation. <b>Soil structure:</b> how particles aggregate into peds; crumb structure is ideal.</li>"
         "<li><b>pH:</b> affects nutrient availability and biota; lime raises pH, sulfur lowers it.</li></ul>"),
        ("Soil erosion: processes", "162",
         "<p><b>Wind erosion</b> removes dry, fine, bare soil (dust bowls, loess); <b>water erosion</b> by raindrop impact (splash), sheet wash, rill and gully formation on slopes, and bank erosion. Erosion is a natural process; the problem is <b>accelerated erosion</b> when the rate of loss exceeds the rate of formation.</p>"),
        ("Causes of accelerated erosion", "163-164",
         "<ul><li><b>Vegetation removal</b> (deforestation, overgrazing, burning) exposes soil to rain and wind and removes root binding and organic matter input.</li>"
         "<li><b>Ploughing vulnerable soils</b> - light sandy or peaty soils, dry regions, ploughing up and down slopes creating channels; leaving fields bare over winter.</li>"
         "<li><b>Reduced soil biota</b> and organic matter (pesticides, monoculture, artificial fertiliser) weakens structure.</li><li><b>Soil compaction</b> by machinery and livestock reduces infiltration so more water runs off.</li>"
         "<li><b>Cultivating steep slopes</b> without terracing.</li></ul>"),
        ("Effects of accelerated erosion", "164",
         "<ul><li><b>Reduced productivity</b> - loss of the fertile topsoil, nutrients and water-holding capacity; desertification.</li><li><b>Sedimentation</b> of rivers and reservoirs - reduced flow and capacity, flooding, turbidity harming aquatic life, blocked irrigation channels.</li>"
         "<li><b>Increased atmospheric particulates</b> - dust storms, health effects, changed albedo.</li><li>Nutrient and pesticide pollution of water carried on soil particles.</li></ul>"),
        ("Methods of reducing erosion", "164-166",
         "<ul><li><b>Long-term crops</b> and perennials that keep the soil covered; cover crops over winter; <b>reduced / zero tillage</b>.</li>"
         "<li><b>Contour ploughing</b> across the slope so furrows hold water; <b>terracing</b> steep slopes; <b>strip cropping</b> alternating crops that hold soil.</li>"
         "<li><b>Windbreaks</b> and shelter belts of trees or hedges reduce wind speed; <b>mulching</b> protects the surface and adds organic matter; <b>increasing organic matter</b> with manure, compost and crop residues improves structure.</li>"
         "<li>Controlled grazing to prevent overgrazing; keeping heavy machinery off wet soils; maintaining drainage and liming where needed.</li></ul>"),
        ("The Universal Soil Loss Equation", "167-169",
         "<p><b>A = R x K x L x S x C x P</b>: A = annual soil loss; <b>R</b> = rainfall erosivity (intensity and amount); <b>K</b> = soil erodibility (texture, structure, organic matter); <b>L</b> = slope length; <b>S</b> = slope gradient (often combined as LS); <b>C</b> = cropping / vegetation cover factor (bare soil 1, dense forest near 0); <b>P</b> = erosion-control practice factor (1 for none; contour ploughing, strip cropping and terracing reduce it). The equation shows that the manageable factors are C and P - keep the soil covered and use conservation practices - because R, K, L and S are fixed by climate, soil and landscape. Be ready to calculate A from given values and to explain the effect of changing one factor.</p>"),
    ],
    "diagrams": [
        {"type": "flow", "title": "USLE: which factors can a farmer change?", "nodes": [("R", "R rainfall\nerosivity", 0, 0), ("K", "K soil\nerodibility", 1, 0), ("LS", "L, S slope length\nand gradient", 2, 0), ("A", "A = soil loss\nper year", 1, 1), ("C", "C crop cover\n(0 forest - 1 bare)", 0, 2), ("P", "P practices: contour\nploughing, terraces", 2, 2)],
         "kinds": {"A": "hi", "C": "warn", "P": "warn"}, "edges": [("R", "A"), ("K", "A"), ("LS", "A"), ("C", "A"), ("P", "A")],
         "caption": "Genn pp. 167-169. Shaded factors are the ones management changes; the others are set by climate, soil and topography."},
    ],
    "numbers": ["Sand 2-0.06 mm, silt 0.06-0.002 mm, clay < 0.002 mm", "USLE: A = R K L S C P", "Field capacity = water held after gravitational drainage"],
    "exam": ["Use the soil triangle to classify samples (June 2023 Q3); calculate water and organic matter content from wet / dry / ignited masses (June 2022 Q9).", "Explain how named agricultural practices increase erosion (Nov 2021 Q7); slope and land-use data (June 2023 Q4, June 2024 Q3).",
             "USLE calculations and reasoning (specimen Q9, June 2024 Q3).", "Describe how soil organisms increase fertility; Tullgren funnel method (June 2024 Q7).", "Essay: soil management and environmental damage at local, regional and global scales (Nov 2020)."],
},
}
