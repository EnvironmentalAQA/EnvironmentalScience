"""Pollution: solid wastes - domestic (landfill, incineration, recycling, composting), spoil, specialist wastes
(asbestos, cyanide, radioactive - encapsulation / vitrification) (spec 3.4.3.2.12).  Genn pp. 279-285, 303."""
from gen.model import Q, P, Table, Chart, Essay

T = "solid-waste"

QUESTIONS = [
    Q("SW-01", T, "3.4.3.2.12", "280-282",
      intro="Figure 1 shows how municipal solid waste was treated in the UK in 2000 and 2019.",
      figures=[Chart("bar", "Treatment method", "Percentage of waste / %",
                     {"2000": [("Landfill", 79), ("Incineration", 9), ("Recycling / composting", 11), ("Other", 1)],
                      "2019": [("Landfill", 14), ("Incineration", 42), ("Recycling / composting", 43), ("Other", 1)]}, y_min=0, y_max=100)],
      parts=[
          P("Describe the changes shown in Figure 1.", 2,
            ms=["Landfill fell from 79% to 14% (large decrease)", "Incineration rose from 9% to 42% and recycling / composting rose from 11% to 43% (now the largest)"]),
          P("Explain <b>three</b> environmental disadvantages of landfill that led to the change.", 3, items=3,
            ms=["Organic matter decays anaerobically releasing methane (and CO2) - greenhouse gases", "Toxic leachate may leak into groundwater / rivers from poorly managed sites",
                "Uses large areas of land; loss of habitats / farmland; contamination prevents later use", "Resource value of metals, glass, plastics is lost", "Transport noise / congestion / litter / pests / odour"]),
          P("Describe <b>four</b> features of a well-managed landfill site.", 4, items=4,
            ms=["Polymer / clay liner to prevent escape of leachate", "Collection and treatment of leachate", "Collection of methane and use as a fuel",
                "Impermeable cap (clay and polymer) when complete to stop water entering", "Regular covering with soil (pests, odour); deodorising sprays", "Perimeter fence to trap wind-blown litter",
                "Separation and recording of waste types; reactive / flammable wastes not dumped together"]),
          P("Suggest why incineration has increased more than recycling for some waste types.", 1,
            ms=["Mixed / contaminated / dirty wastes (plastics, dirty paper) are difficult and costly to separate and recycle but can be burnt with energy recovery"]),
      ]),

    Q("SW-02", T, "3.4.3.2.12", "283-284",
      parts=[
          P("Give <b>three</b> advantages of incinerating domestic waste.", 3, items=3,
            ms=["Volume of ash is much less than the original waste (less landfill)", "Heat used for district heating / electricity generation (energy recovery)",
                "No sorting / complicated management needed", "Destroys pathogens / flammable organic wastes converted to CO2 and water", "Refuse-derived fuel can replace fossil fuels (eg cement kilns)"]),
          P("Explain how each of the following features of a modern incinerator reduces pollution.", 4,
            labels=["High combustion temperature with rapid cooling of gases", "Water spray scrubber", "Removal of wet / compostable waste", "Removal of recyclable waste"],
            ms=["High temperature and rapid cooling reduce the formation of toxic dioxins (from organic wastes reacting with chlorine)",
                "Scrubber dissolves hydrogen chloride (from chlorine in PVC) which is then neutralised with alkali / limestone; also removes heavy metals for storage at high pH",
                "Wet waste needs extra fuel to burn and lowers combustion temperature; composting recovers its nutrient value",
                "Recycling conserves the resource value of metals, glass and plastics that would otherwise be lost"]),
          P("Explain why the ash from waste incinerators needs careful disposal.", 2,
            ms=["Ash may contain concentrated heavy metals / toxic residues", "Must be stored in solid form at high pH / hazardous waste landfill so the metals remain insoluble"]),
          P("State <b>one</b> reason why incineration is expensive.", 1, ms=["Fuel (natural gas) needed to burn wet / non-flammable wastes", "Cost of treating effluent gases (SO2, NOx, HCl, smoke)"]),
      ]),

    Q("SW-03", T, "3.4.3.2.12", "284-285, 303",
      intro="Table 1 shows three specialist solid wastes.",
      parts=[
          P("Complete Table 1 to show the main hazard of each waste and the disposal method used.", 6,
            table=Table(["Waste", "Main hazard", "Disposal method"], [["Asbestos", "", ""], ["Cyanide compounds", "", ""], ["High-level radioactive waste", "", ""]], blank=True, col_widths=[4, 5.5, 5.5]),
            ms=["Asbestos: fibres become airborne when it disintegrates and are inhaled, causing asbestosis (scar tissue thickens alveoli) and mesothelioma; disposal: double-wrapped in heavy-duty polythene in a specialised, recorded landfill (secure, permanent, sealed storage)",
                "Cyanide: very toxic enzyme inhibitor (aerobic respiration) if inhaled / ingested; disposal: incineration so carbon and nitrogen are separated and oxidised to CO2 and NOx (much smaller problem)",
                "High-level radioactive waste: intense ionising radiation, heat generation, long half-lives; disposal: vitrification - mixed with molten glass in sealed stainless steel containers in ventilated concrete stores"]),
          P("Explain why encapsulated asbestos in cement roof panels is not considered dangerous while it is intact.", 1,
            ms=["The fibres are bound / cannot become airborne so cannot be inhaled"]),
          P("Describe the process of encapsulation used for intermediate-level radioactive waste and wastes containing heavy metals.", 2,
            ms=["Waste is mixed with a cement slurry and poured into containers of impermeable, unreactive material", "The solid cement immobilises the waste so it cannot leak / leach out"]),
          P("Explain why vitrification is preferred to encapsulation in cement for high-level waste.", 1,
            ms=["Even if the glass shatters the waste stays encapsulated in the fragments; glass is more stable / resistant to heat and leaching over very long timescales"]),
      ]),

    Q("SW-04", T, "3.4.3.2.12", "282-283",
      intro="A coal-mine spoil heap on a hillside has been abandoned. The spoil contains shale with some iron pyrites and residual coal.",
      parts=[
          P("Explain <b>three</b> problems this spoil heap could cause and describe how each could be managed.", 6,
            ms=["Instability / landslips on the hillside, especially after heavy rain - compaction, drainage, establishing vegetation whose roots bind the spoil, regrading slopes",
                "Acid drainage from oxidation of pyrites, with toxic metals - collect and treat leachate, add lime to raise pH",
                "Spontaneous combustion of residual coal / hydrocarbons - layers of fine-grained material to reduce air flow",
                "Lack of nutrients / poor plant growth - add topsoil, sewage sludge, fertiliser", "Unattractive topography - landscaping / reshaping", "Dust / heavy metals - cover and keep at high pH"]),
          P("Explain why deep layers of soil are applied when a spoil heap containing toxic materials is restored.", 2,
            ms=["So that plant roots cannot reach the toxic layer", "Otherwise toxins could be taken up and brought to the surface / dispersed via leaf litter and food chains"]),
          P("Explain why an old steel-works spoil heap may be valuable for wildlife conservation.", 2,
            ms=["Steel slag is alkaline, producing unusual calcareous / high-pH soil conditions", "Supports uncommon plants such as cowslips / orchids that cannot compete on fertile neutral soils"]),
      ]),

    Q("SW-05", T, "3.4.3.2.12", "279-282",
      parts=[
          P("Explain how affluence and the strategies of manufacturers increase the amount of solid waste produced.", 4,
            ms=["Affluent people buy more consumer goods / trivia / disposable items and throw items away rather than repairing them",
                "Built-in obsolescence: products designed to have short lives / wear out / go out of fashion so customers upgrade",
                "Disposable products (razors, lighters, pens) that must be replaced", "Over-packaging to make products attractive; also increases wastes from manufacture and mineral extraction"]),
          P("Give <b>three</b> factors that affect the choice of disposal method for a solid waste.", 3, items=3,
            ms=["Properties of the waste: toxicity, flammability, degradability, radioactivity", "Population density (collection costs)", "Land availability for landfill",
                "Availability of recycling technology / markets", "Legislation / regulatory framework (landfill tax)", "Public willingness to recycle / environmental awareness", "Processing costs / household income"]),
          P("Explain <b>one</b> environmental advantage and <b>one</b> disadvantage of composting garden and food waste rather than sending it to landfill.", 2, labels=["Advantage", "Disadvantage"],
            ms=["Advantage: aerobic decomposition produces little methane; nutrients / organic matter returned to soil (circular economy); reduces landfill volume",
                "Disadvantage: needs separation / collection of clean organic waste; odour / pests / pathogens if poorly managed; low-value product; not suitable for mixed waste"]),
          P("Explain why mixed municipal waste is difficult to recycle.", 1,
            ms=["Many different materials are mixed together / contaminated so identification and separation are costly and the quality of recovered material is reduced"]),
      ]),
]

ESSAYS = []
