"""Biological resources: forest resources - importance, productivity vs biodiversity, deforestation, sustainable management (spec 3.5.3).
Genn pp. 360-369 (and 50-56 for woodland / rainforest)."""
from gen.model import Q, P, Table, Chart, Essay

T = "forests"

QUESTIONS = [
    Q("FOR-01", T, "3.5.3.1", "360-364",
      parts=[
          P("Describe the resources obtained from forests. Give <b>one</b> example for each category.", 5,
            labels=["Timber", "Fuel", "Food", "Fibres", "Medicines"],
            ms=["Timber: building construction, furniture, tools, telegraph poles, concrete shuttering (oak, beech, mahogany, teak, conifer softwood)", "Fuel: fuelwood and charcoal - still the main energy source for most people in LEDCs",
                "Food: fruit, nuts, bushmeat, livestock fodder; crops of forest origin (coffee, cacao, bananas, Brazil nuts); pigs and chickens were forest animals", "Fibres: paper (wood pulp cellulose), cotton, viscose / rayon",
                "Medicines: quinine (cinchona), taxol (yew), aspirin (willow); most species not yet researched"]),
          P("Explain why forests are an important carbon reservoir and how they can be used to counteract climate change.", 3,
            ms=["Wood is mainly cellulose which is hard to digest, so carbon stored in wood has a long residence time; total forest carbon (vegetation plus soil) is about double that in the atmosphere",
                "Growing trees sequester CO2 by photosynthesis and release oxygen; forest soils hold more carbon than the trees (especially boreal)", "Planting / protecting forests removes CO2 and reduces the enhanced greenhouse effect"]),
          P("Explain how forests regulate the hydrological cycle and local climate.", 2,
            ms=["Highest transpiration of any ecosystem increases downwind rainfall; interception increases evaporation; deep organic soils retain water and delay runoff so river flow is more even and flooding reduced",
                "Low albedo absorbs sunlight; heat stored and released at night reduces day-night temperature extremes; canopy microclimate: lower light, wind, higher humidity"]),
      ]),

    Q("FOR-02", T, "3.5.3.2", "365-367",
      intro="Table 1 compares an indigenous mixed broadleaf woodland with a Sitka spruce plantation of the same area in Scotland.",
      figures=[Table(["Feature", "Mixed indigenous woodland", "Sitka spruce plantation"], [["Tree species", "12", "1"], ["Age structure", "All ages, dead wood present", "All planted in the same year"], ["Planting density", "Natural, variable", "Close, 2 m spacing"], ["Timber yield / m^3 ha^-1 yr^-1", "4", "16"], ["Bird species", "38", "9"], ["Ground flora species", "60", "4"]])],
      parts=[
          P("Use Table 1 to explain why the plantation has a much higher timber yield but far lower biodiversity.", 6,
            ms=["Non-indigenous species (Sitka spruce from North America) chosen for fast growth and pest resistance; indigenous wildlife's needs for food, pollination, seed dispersal and habitat are not met",
                "Single species: easy planting, thinning and felling over large areas; but each tree species supports its own community so few species overall",
                "Close planting makes trees compete for light so they grow tall and straight (good timber) but shades out ground flora and the species that depend on them",
                "Simple age structure: uniform size makes management easy but gives little variety of light, temperature, wind; no old trees or dead wood for invertebrates and woodpeckers",
                "Mixed woodland: varied niches, stratification, dead wood, indigenous trees each with their own dependent species"]),
          P("Explain why commercial plantations are felled before the trees reach full size.", 2,
            ms=["Trees are felled when income will be greatest - approaching full size when the growth rate starts to decline", "Continuing to grow them ties up land and capital for little extra timber; natural forests keep old and dead trees"]),
          P("Explain why there is little demand today for coppiced or pollarded wood.", 2,
            ms=["Industrial society replaced species-specific uses (baskets, fencing, charcoal, tool handles) with large-scale uses: chipboard, plywood, pulp", "Wood fuel replaced by fossil fuels / electricity; so traditional management declined and woods became uniform"]),
      ]),

    Q("FOR-03", T, "3.5.3.3", "367-368",
      intro="Figure 1 shows the area of forest lost each year in three regions between 1990 and 2020.",
      figures=[Chart("line", "Year", "Forest loss / million ha per year", {"South America": [(1990, 5.1), (2000, 5.5), (2010, 3.7), (2020, 2.6)], "Africa": [(1990, 3.3), (2000, 3.4), (2010, 3.4), (2020, 3.9)], "Europe": [(1990, -0.8), (2000, -0.9), (2010, -0.6), (2020, -0.3)]}, y_min=-2, y_max=7)],
      parts=[
          P("Describe the trends shown in Figure 1.", 3,
            ms=["South America: high loss (5.1-5.5 Mha yr^-1) falling by about half by 2020", "Africa: loss steady at about 3.4 then rising to 3.9 by 2020 - now the highest", "Europe: negative values - forest area increasing (afforestation exceeds loss), though the gain is shrinking"]),
          P("Explain the main causes of forest loss in South America and Africa.", 4,
            ms=["South America: clearance for commercial cash crops (sugar cane, soya) and cattle ranching for export; HEP reservoirs; roads improving access; mining",
                "Africa: growing rural populations clearing land for subsistence farming; fuelwood and charcoal collection above regrowth (charcoal wastes much of the wood's energy); fodder cutting in dry areas",
                "Both: hardwood timber (teak, mahogany) from clear-felled mixed forest often not replanted; urban expansion"]),
          P("Explain why roads and railways cause more forest loss than the area they occupy.", 2,
            ms=["They create barriers fragmenting wildlife populations", "Improved access makes it easier to remove timber and farm produce, so clearance spreads along them"]),
          P("Explain why softwood from Scandinavia and Canada is generally produced more sustainably than tropical hardwood.", 1,
            ms=["Conifers grow quickly so plantations are replanted after harvest and yield a saleable crop within decades; slow-growing hardwoods (teak, mahogany) take too long for commercial plantations so they are taken from natural forest that is clear-felled and not replanted"]),
      ]),

    Q("FOR-04", T, "3.5.3.3", "368-369",
      parts=[
          P("Explain the effects of deforestation on soil.", 4,
            ms=["Less dead organic matter / leaf litter so less humus and slower soil formation; fewer nutrients returned", "Loss of canopy and litter exposes soil to rain splash and wind",
                "Decomposing roots no longer bind soil so erosion, gullying and landslides increase (especially on slopes)", "Reduced organic matter and biota lower infiltration and water retention"]),
          P("Explain how deforestation affects hydrology and climate.", 4,
            ms=["Reduced interception and transpiration so less water returned to the atmosphere and less rainfall downwind", "Increased runoff: more flooding after rain, lower flows in dry periods; sedimentation of rivers",
                "Increased albedo of cleared land (reflects more sunlight)", "Reduced carbon sequestration and loss of the carbon reservoir (CO2 released by burning / decay) contributing to climate change"]),
          P("Give <b>two</b> ecological impacts of deforestation other than the direct loss of species.", 2, items=2,
            ms=["Fragmentation of remaining forest into isolated patches with non-viable populations / edge effects", "Loss of inter-species relationships (pollinators, seed dispersers) causing further declines", "Loss of genetic resources / potential medicines before they are discovered"]),
      ]),

    Q("FOR-05", T, "3.5.3.3", "369, 386-387",
      intro="The Rio Bravo Conservation and Management Area in Belize exploits mahogany under a sustainable management plan while conserving a rainforest of over 200 tree, 400 bird and 70 mammal species.",
      parts=[
          P("Describe <b>five</b> features of the timber harvesting at Rio Bravo that make it sustainable.", 5, items=5,
            ms=["Harvest rate below the maximum sustainable yield; only economically valuable species (mahogany) selectively logged, not clear-felled", "Trees felled only where other mahoganies stand upwind so seeds recolonise the clearing; large seed trees and small trees left to grow",
                "Buffer zones with no harvesting or machinery near rivers / wetlands", "Restricted machinery and planned track routes re-used to avoid damaging roots of retained / rare / fruit trees", "Each felled tree tagged and tracked to the retailer for FSC accreditation; rangers control illegal logging; tree nurseries replant over-exploited and ecologically important species"]),
          P("Explain why involving local communities is essential to the success of the reserve.", 3,
            ms=["The reserve removed traditional uses (fuelwood, timber, farming clearings, hunting, medicines) so people would otherwise resent / ignore it", "Employment as rangers, forestry and tourism workers; ecotourists use local restaurants, produce and souvenirs; offcuts given to local carvers",
                "Benefits give the community an incentive to protect the forest; carbon sequestration payments from companies fund management"]),
          P("Explain why selective logging is better for wildlife than clear-felling, and give <b>one</b> disadvantage.", 2,
            ms=["Removing individual trees leaves small clearings so remaining populations survive nearby and the forest structure / microclimate is kept; timber resource used over a longer period",
                "Disadvantage: more labour-intensive and expensive; more tracks needed per tree"]),
      ]),

    Q("FOR-06", T, "3.5.3", "360-369",
      parts=[
          P("Which of the following features of a plantation would most increase its wildlife value? Tick one box.", 1,
            mcq=["Close planting of a single non-indigenous species", "Mixed indigenous species with a mixed age structure", "Clear-felling on a 40-year rotation", "Removal of dead wood"], ms=["B"]),
          P("Describe <b>four</b> features of sustainably managed forests and explain how each benefits biodiversity or productivity.", 4, items=4,
            ms=["Harvesting no faster than the MSY - resource never depleted", "Mixed species plantations - more food choices, relationships and niches", "Indigenous species - support indigenous insects, birds",
                "Mixed age structure - varied light, temperature, wind so more species; continuous cover and yield", "Selective logging - small clearings, less disturbance, long-term timber benefit", "Retention of dead wood, buffer zones, corridors"]),
      ]),
]

ESSAYS = [
    Essay("ESS-P2-FORESTS", 2,
          "Discuss the causes and consequences of deforestation and evaluate the extent to which forests can be exploited sustainably.",
          "3.5.3, 3.1.2.3.4", "50-57, 360-369, 386-387",
          ["Importance: resources (timber, fuel, food, fibres, medicines) and ecosystem services (atmospheric regulation, carbon store, hydrological regulation, climate, soil conservation, habitat, recreation)",
           "Causes: agriculture (subsistence and cash crops), mineral extraction, reservoirs, urbanisation, transport, unsustainable timber, fuel and fodder exploitation above MSY; trends by region",
           "Consequences: loss of resources, biodiversity and species, fragmentation; hydrological changes; soil impacts; climate impacts (albedo, carbon, rainfall)",
           "Productivity vs biodiversity: non-indigenous species, monocultures, close planting, simple age structure, clear-felling",
           "Sustainable management: MSY harvest rates, mixed indigenous species, mixed age structure, selective logging, traditional coppicing / pollarding, FSC certification, community involvement, protected areas, debt-for-nature, afforestation programmes (China); Rio Bravo case study",
           "Evaluation: economics of slow-growing hardwoods, enforcement, demand from MEDCs, ITTO failures; judgement"]),
]
