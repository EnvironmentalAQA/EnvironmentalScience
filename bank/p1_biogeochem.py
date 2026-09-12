"""Physical environment: biogeochemical cycles - carbon, nitrogen, phosphorus (spec 3.2.4).  Genn pp. 148-157."""
from gen.model import Q, P, Table, Chart, Essay

T = "biogeochem"

QUESTIONS = [
    Q("BGC-01", T, "3.2.4.2", "148-149",
      intro="Table 1 shows the mass of carbon in the main reservoirs of the carbon cycle.",
      figures=[Table(["Reservoir", "Mass of carbon / billion tonnes"], [["Atmosphere (CO_2)", "700"], ["Living organisms", "470"], ["Dead organic matter (soil)", "3 700"], ["Surface ocean waters", "500"], ["Deep ocean (dissolved)", "35 000"], ["Fossil fuels", "10 000"], ["Sedimentary carbonate rocks", "20 000 000"]])],
      parts=[
          P("Express the mass of carbon in the atmosphere in standard form, in tonnes.", 1, calc=True, unit="tonnes", ms=["7 x 10^11 tonnes"]),
          P("Calculate the percentage increase in atmospheric carbon that would result from burning 10% of the fossil fuel reservoir, assuming all the carbon remained in the atmosphere.", 2, calc=True, unit="%",
            ms=["10% of 10 000 = 1000 billion tonnes", "1000 / 700 x 100 = 143% (accept 142.9)"]),
          P("Explain why the sedimentary carbonate rocks, although by far the largest reservoir, have little effect on atmospheric CO<sub>2</sub> concentrations.", 2,
            ms=["Carbon is transferred into and out of rocks extremely slowly (fossilisation / sedimentation, weathering, volcanic release)", "Residence time is millions of years so the flux to the atmosphere is tiny compared with respiration / photosynthesis / combustion"]),
          P("Describe how carbon moves from the atmosphere into sedimentary carbonate rocks.", 3,
            ms=["CO2 dissolves in the sea (forming carbonic acid / hydrogen carbonate ions) and is absorbed by phytoplankton through photosynthesis",
                "Organisms such as molluscs, corals and planktonic organisms build calcium carbonate shells / exoskeletons", "When they die the shells sink and sediment on the seabed, becoming limestone / chalk over long periods"]),
          P("Explain why aerobic respiration returns carbon to the atmosphere as CO<sub>2</sub> but anaerobic respiration returns it mainly as methane.", 2,
            ms=["Aerobic respiration uses oxygen to break down organic compounds completely to CO2 (and water), releasing much more energy",
                "Without oxygen, anaerobic organisms only partly break down organic compounds, releasing carbon as methane (CH4), which is later oxidised to CO2 in the atmosphere"]),
      ]),

    Q("BGC-02", T, "3.2.4.2", "150-151",
      parts=[
          P("Explain how each of the following human activities changes the amount of carbon in the atmosphere.", 6,
            labels=["Ploughing farmland", "Draining marshland / peat bogs", "Toxic pollution of the sea"],
            ms=["Ploughing: increases the oxygen supply to soil decomposers so aerobic decomposition of dead organic matter is faster; carbon in the soil DOM store falls and atmospheric CO2 rises",
                "Draining: waterlogged anaerobic conditions preserved dead organic matter (peat) and produced methane slowly; drainage makes the soil aerobic so stored carbon is rapidly decomposed to CO2 (though methane release stops)",
                "Marine pollution: kills phytoplankton so less dissolved CO2 is absorbed by photosynthesis and less carbon sinks to sediments in dead plankton; less CO2 then dissolves from the atmosphere to replace it, so atmospheric CO2 rises"]),
          P("Give <b>three</b> anaerobic environments created by human activities that release methane.", 3, items=3,
            ms=["Rice paddy fields", "Landfill sites", "Anaerobic sediments in reservoirs", "Livestock intestines (cattle)", "Manure / slurry stores"]),
          P("Explain how rising atmospheric CO<sub>2</sub> causes ocean acidification.", 1,
            ms=["More CO2 dissolves in the sea, forming carbonic acid which dissociates into hydrogen carbonate and hydrogen ions; more H+ lowers the pH"]),
      ]),

    Q("BGC-03", T, "3.2.4.2", "151-152",
      parts=[
          P("Explain why planting a new forest only sequesters carbon for a limited period, and how the storage can be extended.", 3,
            ms=["Trees absorb CO2 by photosynthesis and store carbon in wood as they grow", "Once mature there is no further net storage (photosynthesis balanced by respiration / decomposition), though the standing forest remains a reservoir",
                "Harvesting the timber and keeping it as wood (eg house construction) then replanting produces additional storage as the new trees grow"]),
          P("Compare pre-combustion and post-combustion methods of carbon capture.", 4,
            ms=["Pre-combustion: the fuel is modified before use so no CO2 is released when burnt - eg gasification of coal to hydrogen and CO2 (CO2 stored, hydrogen distributed); oxy-fuel combustion in pure oxygen giving only CO2 and water vapour which is condensed out",
                "Advantage: capture at a large central facility; suits small dispersed sources (vehicles) that cannot capture CO2",
                "Post-combustion: CO2 removed from exhaust gases by solvents, membrane filtration, adsorption / desorption, cryogenic separation, graphene",
                "Disadvantage: only about 20% of flue gas is CO2 so separation is costly / energy-intensive; none fully developed"]),
          P("Describe <b>two</b> ways captured CO<sub>2</sub> can be stored and give <b>one</b> concern about long-term storage.", 3,
            ms=["Injected into depleted oil / gas fields or saline aquifers", "Injected into oil reservoirs to provide pressure for secondary oil recovery", "Reaction with fractured basalt to form solid carbonate minerals",
                "Concern: leakage back to the atmosphere / monitoring over centuries; limited suitable geology; cost"]),
      ]),

    Q("BGC-04", T, "3.2.4.3", "152-154",
      intro="Figure 1 shows a simplified nitrogen cycle with some processes labelled 1 to 6.",
      figures=[Table(["Number", "Process description"], [["1", "Nitrogen gas converted to ammonium ions by Rhizobium in root nodules"], ["2", "Ammonium ions oxidised to nitrite then nitrate by Nitrosomonas and Nitrobacter"],
                     ["3", "Nitrates reduced to nitrogen gas by Pseudomonas in anaerobic soil"], ["4", "Amino groups in dead organic matter released as ammonium ions by decomposers"], ["5", "Nitrogen and oxygen react during lightning to form NOx"], ["6", "Nitrates washed out of soil into rivers"]], caption="Figure 1")],
      parts=[
          P("Name processes 1 to 6.", 3, ms=["1 nitrogen fixation; 2 nitrification", "3 denitrification; 4 ammonification", "5 ionisation; 6 leaching (3 marks for all six, 2 for four or five, 1 for two or three)"]),
          P("Explain why draining a waterlogged field increases the nitrate available to crops.", 3,
            ms=["Drainage makes the soil aerobic", "Aerobic nitrifying bacteria (and nitrogen fixers) increase so more ammonium is converted to nitrate",
                "Anaerobic denitrifying bacteria decline so less nitrate is lost as nitrogen gas"]),
          P("Explain why nitrogen is described as a resource that is 'not very abundant' for living organisms even though the atmosphere is 78% nitrogen.", 2,
            ms=["Nitrogen gas is very unreactive so most organisms cannot use it directly", "Only nitrogen fixation (bacteria, lightning, Haber process) converts it to usable ammonium / nitrate; the cycle recycles a small usable amount"]),
          P("Explain why growing legumes such as clover in a crop rotation reduces the need for artificial fertiliser.", 2,
            ms=["Rhizobium bacteria in their root nodules fix atmospheric nitrogen into ammonium / proteins", "When the plants die / are ploughed in, decomposition and nitrification release nitrates for the following crop"]),
      ]),

    Q("BGC-05", T, "3.2.4.3", "154-155",
      intro="Table 1 shows global reactive nitrogen fixed each year by natural processes and by human activities.",
      figures=[Table(["Source", "Nitrogen fixed / million tonnes per year"], [["Biological fixation (natural ecosystems)", "110"], ["Lightning", "5"], ["Haber process (fertiliser manufacture)", "120"], ["Cultivation of legume crops", "60"], ["Combustion (NOx)", "30"]])],
      parts=[
          P("Use Table 1 to calculate the percentage of total nitrogen fixation that is caused by human activities.", 2, calc=True, unit="%", ms=["Human = 120 + 60 + 30 = 210; total = 325", "210 / 325 x 100 = 64.6% (accept 65%)"]),
          P("Describe the Haber process and explain why it is unsustainable compared with biological nitrogen fixation.", 3,
            ms=["Nitrogen and hydrogen react to form ammonia over an iron catalyst at high temperature and pressure; ammonia then converted to nitrates for fertiliser",
                "Uses large amounts of energy from fossil fuels (also the hydrogen source), releasing CO2 and NOx", "Biological fixation by bacteria occurs at low temperature using solar energy captured by plants (enzymes lower activation energy)"]),
          P("Describe <b>three</b> consequences of the increased movement of nitrogen compounds caused by human activities.", 3, items=3,
            ms=["Eutrophication of water bodies by leached nitrates / sewage", "Photochemical smogs and tropospheric ozone from NOx", "Acid rain (nitric acid)", "Nitrous oxide as a greenhouse gas", "NOx toxicity / respiratory disease", "Nitrate in drinking water (methaemoglobinaemia)"]),
          P("Explain how composting or anaerobic digestion of biological wastes produces a better fertiliser than raw waste.", 2,
            ms=["Carbon is lost as CO2 (composting) or CH4 (digestion) so the C:N ratio improves / more nitrogen-rich", "Bulk and odour reduced, pathogens killed, easier to apply; digestion also yields biogas"]),
      ]),

    Q("BGC-06", T, "3.2.4.4", "156-157",
      parts=[
          P("Explain why phosphorus is more likely than nitrogen to be a limiting factor on biological productivity.", 3,
            ms=["There is no gaseous / atmospheric reservoir of phosphorus (no equivalent of nitrogen fixation)", "Most phosphorus compounds have low solubility so little is available in soil water",
                "Phosphorus lost to marine sediments only returns through very slow processes: mountain building (uplift) and weathering of rocks"]),
          P("Explain how mycorrhizal fungi increase phosphate uptake by plants.", 2,
            ms=["Fungal hyphae form a symbiotic relationship with plant roots and spread through a large volume of soil", "Greatly increasing the surface area for absorbing (poorly mobile) phosphate ions, passed to the plant in exchange for carbohydrates"]),
          P("Describe how human activities have altered the phosphorus cycle.", 3,
            ms=["Mining of calcium phosphate rock (and past mining of guano deposits, eg Peru, Nauru, now largely exhausted)", "Treated to make more soluble ammonium phosphate fertilisers, mobilising phosphorus into the environment",
                "Fertiliser runoff / eroded soil / sewage effluent carry phosphates into water bodies causing eutrophication (with nitrates); harvesting removes phosphorus from farmland"]),
          P("Explain <b>two</b> strategies for the sustainable management of phosphorus supplies.", 2,
            ms=["Use biological wastes (manure, sewage sludge, compost) as fertiliser to return phosphates rather than mining rock", "Breed crops that absorb phosphate more efficiently",
                "Maintain conditions for mycorrhizal fungi (less tillage, fewer fungicides, organic matter)", "Recover phosphate from sewage effluent by iron(III) sulfate precipitation; reduce soil erosion"]),
      ]),

    Q("BGC-07", T, "3.2.4", "148-157",
      parts=[
          P("Describe how human activities have altered the natural equilibria of the carbon and nitrogen cycles, and evaluate the strategies that could counteract these changes.", 9, level=True,
            ms=["Carbon: combustion of fossil fuels and biomass moving carbon from long-term stores to the atmosphere; deforestation reducing photosynthesis; ploughing / drainage increasing aerobic decomposition; new anaerobic environments (paddies, landfill, reservoirs, livestock) releasing methane; marine pollution reducing phytoplankton; consequences: rising CO2 and CH4, climate change, ocean acidification, reduced soil organic matter",
                "Nitrogen: Haber process doubling fixation; legume cultivation; drainage increasing nitrification and reducing denitrification; combustion NOx; sewage and fertiliser leaching; consequences: eutrophication, smogs, acid rain, N2O warming, NOx toxicity",
                "Counter-strategies carbon: renewables / nuclear replacing fossil fuels, energy conservation, afforestation matched to deforestation and timber use, conserving peat bogs and forests, increasing soil organic matter (low tillage, mulching), CCS (pre / post combustion, storage)",
                "Counter-strategies nitrogen: reduced combustion, catalytic converters / urea sprays, biological fixation instead of Haber, legumes and crop rotation, management of biological wastes as fertiliser, low-solubility fertilisers, timing, buffer strips, low tillage, nitrate vulnerable zones",
                "Evaluation: some strategies well established and cheap (rotation, buffer strips), others expensive or unproven (CCS); scale of fossil fuel dependence; feedback and time lags; link to circular economy and low-temperature natural processes; judgement"]),
          P("State what is meant by the <b>residence time</b> of a substance in a reservoir.", 1, ms=["The average time an atom / molecule remains in the reservoir before being transferred out (volume / transfer rate)"]),
      ]),

    Q("BGC-08", T, "3.2.4.2", "148-151",
      intro="A student measured the mass of carbon stored per hectare in three land uses in the same region.",
      figures=[Table(["Land use", "Carbon in vegetation / t ha^-1", "Carbon in soil dead organic matter / t ha^-1"], [["Mature woodland", "120", "95"], ["Permanent pasture", "3", "80"], ["Arable (ploughed annually)", "2", "45"]])],
      parts=[
          P("Calculate the total carbon lost per hectare when mature woodland is converted to arable farmland.", 1, calc=True, unit="t ha^-1", ms=["(120 + 95) - (2 + 45) = 168 t ha^-1"]),
          P("Explain why the soil carbon in arable land is so much lower than in pasture, even though the vegetation carbon is similar.", 2,
            ms=["Annual ploughing aerates the soil so aerobic decomposers break down dead organic matter faster, releasing CO2", "Harvest removes biomass so less dead organic matter is returned; pasture roots and litter constantly add organic matter"]),
          P("Suggest <b>two</b> ways the arable farmer could increase soil carbon storage.", 2, items=2,
            ms=["Low / zero tillage", "Adding manure, compost or mulch", "Growing cover crops / leaving crop residues", "Converting to long-term grass or tree crops in rotation"]),
      ]),
]

ESSAYS = []
