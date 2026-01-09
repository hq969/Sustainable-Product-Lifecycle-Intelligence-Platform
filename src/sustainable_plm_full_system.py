import json
import matplotlib.pyplot as plt

GRID_INTENSITY = 0.233   # kg CO2 per kWh
ENERGY_COST = 0.12      # USD per kWh

with open("../data/product_lifecycle_data.json") as f:
    data = json.load(f)

def material_carbon(m):
    return m["mass_kg"] * m["emission_factor"]

def material_cost(m):
    return m["mass_kg"] * m["cost_per_kg"]

def supplier_esg_score(m):
    return round(
        (10 - m["emission_factor"]) * 0.4 +
        (m["recycled_percent"] / 10) * 0.3 +
        (10 if m["certified"] else 4) * 0.3, 2
    )

def total_carbon(d):
    materials = sum(material_carbon(m) for m in d["materials"])
    manufacturing = d["manufacturing_energy_kwh"] * GRID_INTENSITY
    return round(materials + manufacturing +
                 d["distribution_emissions"] +
                 d["end_of_life_emissions"], 2)

def total_cost(d):
    materials = sum(material_cost(m) for m in d["materials"])
    manufacturing = d["manufacturing_energy_kwh"] * ENERGY_COST
    return round(materials + manufacturing + d["distribution_cost"], 2)

def optimize_design(d):
    for m in d["materials"]:
        if m["material_id"] == "MAT-ABS":
            m.update({
                "name": "Bio-Polymer A1",
                "emission_factor": 1.2,
                "cost_per_kg": 2.6,
                "recycled_percent": 60,
                "certified": True
            })

baseline_carbon = total_carbon(data)
baseline_cost = total_cost(data)

optimize_design(data)

optimized_carbon = total_carbon(data)
optimized_cost = total_cost(data)

print("Baseline Carbon:", baseline_carbon)
print("Optimized Carbon:", optimized_carbon)
print("Carbon Reduction:", baseline_carbon - optimized_carbon)
print("Cost Change:", optimized_cost - baseline_cost)

plt.bar(["Baseline", "Optimized"], [baseline_carbon, optimized_carbon])
plt.title("Carbon Footprint Reduction")
plt.ylabel("kg CO2e")
plt.show()
